from logic.functions import clean_scraping_values
from scrap.interface_scraping import Scraping
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from log.logger import Log
import json


class Bloomberg(Scraping):
    def __init__(self) -> None:
        super().__init__(Log())
        self.logger = Log().getLogger(__name__)

    def get_response_by_url(self, url: str) -> dict:
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            html_content = soup(webpage, "html.parser")
            response = json.loads(html_content.text)
            return response

        except Exception as e:
            self.logger.error(f'Se produjo un error en el response de: "{url}" error: "{e}"')

    def get_data_from_pages(self) -> list[str]:
        """
        Retorno los valores extraidos del Scraping de BLOOMBERG

        :return: list[str]
        """
        try:
            data_list = []
            for name, url in self.bloomberg_pages.items():

                response = self.get_response_by_url(url)

                for i in range(2):
                    bloomberg_price = response["fieldDataCollection"][i]['price']
                    bloomberg_change_day = response["fieldDataCollection"][i]['priceChange1Day']

                    bloomberg_price_value = clean_scraping_values('bloomberg', bloomberg_price)
                    bloomberg_change_day_value = clean_scraping_values('bloomberg', bloomberg_change_day)

                    data_list.append(bloomberg_price_value)
                    data_list.append(bloomberg_change_day_value)

                bloomberg_list = data_list[:4] if len(data_list) < 5 else data_list[4:]

                print(f'Se extrajeron correctamente los valores de: "{name}" -> "{bloomberg_list}"')
                self.logger.info(f'Se extrajeron correctamente los valores de: "{name}" -> "{bloomberg_list}"')

            print('====================== Finalizado el Scraping de datos ======================')

            return data_list

        except Exception as e:
            print(f'=========== ERROR No se pudo extraer datos: "{e}" ===============')
            self.logger.error(f'No se pudo extraer datos, error: "{e}"')
