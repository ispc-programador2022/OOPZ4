from database.crud_mysql import post_data_to_database, get_data_from_database
from log.logger import Log
import datetime

# GLOBAL VALUES
DOLLAR = 'dollar'
CME = 'cme'
BLOOMBERG = 'bloomberg'
logger = Log().getLogger(__name__)


def clean_scraping_values(scrap: str, value):
    """
    Retorno el valor limpio de un numero decimal en formato de String dado el scraping que se hizo.

    :param scrap: str
    :param value: str
    :return: str
    """
    try:
        if scrap == 'dollar':
            clear_val = round(float(value), 2)
            value = str(clear_val).replace(',', '.')
            return value

        elif scrap == 'rofex':
            value = value.text.strip().split("\n")[1]
            return value

        elif scrap == 'bloomberg':
            value = round(value, 2)
            return value

        elif scrap == 'cme':
            return value

    except Exception as e:
        print(f'Ocurrio un error en la limpieza del valor: "{e}"')


def post_scrapings_to_database(scrap_dollar: list[str], scrap_cme: dict[str, str],
                               scrap_bloomberg: list[str]) -> None:
    """
    Mando los 3 scrapings a la base de datos

    :param scrap_dollar: list[str]
    :param scrap_cme: dict[str, str]
    :param scrap_bloomberg: list[str]
    """
    try:
        post_data_to_database(DOLLAR, scrap_dollar)
        post_data_to_database(CME, scrap_cme)
        if scrap_bloomberg is not None:
            post_data_to_database(BLOOMBERG, scrap_bloomberg)

        logger.info(f'Se guardaron "[POST]" correctamente los datos de la base: ["{DOLLAR}", "{CME}", "{BLOOMBERG}"]')

    except Exception as e:
        logger.error(f'Ocurrio un error en el POST a la base de datos, error: "{e}"')


def get_str_time_now() -> str:
    """ Retorno el momento cuando que se ejecuta el script en formato de String

    :return: list[str]
    """
    return str(datetime.datetime.now())


def get_scrapings_from_database() -> (list[tuple], list[float], list[tuple]):
    """
    Extraigo los 3 scrapings de la base de datos

    :return: list[tuple], list[float], list[tuple]
    """
    try:
        dollar_db = get_data_from_database(DOLLAR)
        cme_db = get_data_from_database(CME)
        bloomberg_db = get_data_from_database(BLOOMBERG)

        logger.info(f'Se extrajo "[GET]" correctamente los datos de la base: ["{DOLLAR}", "{CME}", "{BLOOMBERG}"]')

        return dollar_db, cme_db, bloomberg_db

    except Exception as e:
        logger.error(f'Ocurrio un error en el GET a la base de datos, error: "{e}"')


def scraping_to_list(dollar_db: list[tuple], cme_db: list[tuple], bloomberg_db: list[tuple]) -> list[str]:
    """
    Retorno una lista con el horario de extraccion y los 3 scrapings en el siguiente orden:
        * Data_scraping: [time, dollar, bloomberg, cme]

    :param dollar_db: list[tuple]
    :param cme_db: list[float]
    :param bloomberg_db: list[tuple]
    :return: data_scraping: list[str]
    """
    time_now = get_str_time_now()

    scraping_list = [time_now]
    for element in dollar_db[0]:
        scraping_list.append(str(element))
    for element in cme_db:
        for sub_element in element:
            scraping_list.append(str(sub_element))

    # Transformo los typos de datos a string
    data_scraping = [str(element) for element in scraping_list]

    return scraping_list


def get_scrapings_list_values() -> list[str]:
    """
    Retorno los scrapings de la base de datos en una lista de Strings.

    :return: list[str]
    """
    try:
        # Extraigo los datos de la base
        dollar_db, cme_db, bloomberg_db = get_scrapings_from_database()

        # Appendeo los 3 scrapings en uno solo
        data_scraping = scraping_to_list(dollar_db, cme_db, bloomberg_db)

        return data_scraping

    except Exception as e:
        logger.error(f'Error en el retorno de los scrapings de la base de datos, error: "{e}"')
