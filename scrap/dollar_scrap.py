from logic.functions import clean_scraping_values
from scrap.interface_scraping import Scraping
from bs4 import BeautifulSoup
from log.logger import Log
import requests


class Dollar(Scraping):
    def __init__(self) -> None:
        super().__init__(Log())
        self.logger = Log().getLogger(__name__)

    def get_response_by_url(self, url: str) -> BeautifulSoup:
        try:
            res = requests.get(url)
            response = BeautifulSoup(res.content, 'html.parser')
            return response
        except Exception as e:
            self.logger.error(f'Se produjo un error en el response de: "{url}" error: "{e}"')

    def get_data_from_pages(self) -> list[str]:
        """
        Retorno los valores extraidos del Scraping de BANCO NACION, ROFEX

        :return: list[str]
        """
        try:
            data_list = []
            print('===================== Iniciando el Scraping de datos =====================')
            for name, url in self.dollar_pages.items():

                response = self.get_response_by_url(url)

                if name == 'banco_nacion':
                    td = response.find('div', id='divisas').find('tbody').find_all('td')[2].text
                    banco_nacion_value = clean_scraping_values('dollar', td)
                    data_list.append(banco_nacion_value)

                else:
                    rofex_list = []
                    for td in response.find('div', {'class': 'table-responsive'}).find('tbody').find_all('tr'):
                        matbarofex_value = clean_scraping_values('rofex', td)
                        rofex_list.append(matbarofex_value)

                    data_list.extend(rofex_list[0:5])

                dollar_list = data_list[:1] if len(data_list) == 1 else data_list[1:]

                print(f'Se extrajeron correctamente los valores de: "{name}" -> "{dollar_list}"')
                self.logger.info(f'Se extrajeron correctamente los valores de: "{name}" -> "{dollar_list}"')

            return data_list

        except Exception as e:
            print(f'=========== ERROR No se pudo extraer datos: "{e}" ===============')
            self.logger.error(f'No se pudo extraer datos, error: "{e}"')

