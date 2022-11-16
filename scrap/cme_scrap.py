from logic.functions import clean_scraping_values
from scrap.interface_scraping import Scraping
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from log.logger import Log
import json


class Cme(Scraping):
    def __init__(self) -> None:
        super().__init__(Log())
        self.logger = Log().getLogger(__name__)

    def get_response_by_url(self, url: str) -> dict:
        try:
            req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
            webpage = urlopen(req, timeout=10).read()
            html_content = soup(webpage, "html.parser")
            response = json.loads(html_content.text)
            return response

        except Exception as e:
            self.logger.error(f'Se produjo un error en el response de: "{url}" error: "{e}"')

    def get_data_from_pages(self) -> dict[str, str]:
        """
        Retorno los valores extraidos del Scraping de CME

        :return: dict[str, str]
        """
        try:
            for name, url in self.cme_pages.items():

                response = self.get_response_by_url(url)
                value_to_insert = []

                for i in range(6):
                    if (i == 0) and (response['quotes'][i]['last'] != '-'):
                        cme_last = response['quotes'][i]['last']
                        cme_last_value = clean_scraping_values('cme', cme_last)

                        value_to_insert.append(cme_last_value)

                    else:
                        cme_priorSettle = response['quotes'][i]['priorSettle']
                        cme_priorSettle_value = clean_scraping_values('cme', cme_priorSettle)

                        value_to_insert.append(cme_priorSettle_value)

                self.cme_pages[name] = value_to_insert
                print(f'Se extrajeron correctamente los valores de: "{name}" -> "{value_to_insert}"')
                self.logger.info(f'Se extrajeron correctamente los valores de: "{name}" -> "{value_to_insert}"')

            return self.cme_pages

        except Exception as e:
            print(f'=========== ERROR No se pudo extraer datos: "{e}" ===============')
            self.logger.error(f'No se pudo extraer datos de error: "{e}"')
