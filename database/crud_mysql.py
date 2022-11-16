from configparser import ConfigParser
from log.logger import Log
import pymysql

# GLOBAL VALUES
config = ConfigParser()
config.read('config.ini')
HOST = config['Database']['host']
USER = config['Database']['user']
PASSWORD = config['Database']['password']
DB = config['Database']['db']
logger = Log().getLogger(__name__)


def get(query: str):
    try:
        conexion = pymysql.connect(host=HOST,
                                   user=USER,
                                   password=PASSWORD,
                                   db=DB)
        print(f'========= Correcta conexion a: "{DB}" =========')
        logger.info(f'Correcta conexion a la base de datos: "{DB}"')

        try:
            with conexion.cursor() as cursor:
                logger.info(f'\nQuery enviada: "{query}"\n')
                print(f'Se envia la query: {query}')
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            conexion.close()
            print(f'========= Conexion cerrada a: "{DB}" =========')
            logger.info(f'Conexion cerrada a: "{DB}"')

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        logger.info(f'Correcta conexion a la base de datos: "{DB}"')


def post(query: str):
    try:
        conexion = pymysql.connect(host=HOST,
                                   user=USER,
                                   password=PASSWORD,
                                   db=DB)
        print(f'========= Correcta conexion a: "{DB}" =========')
        logger.info(f'Correcta conexion a la base de datos: "{DB}"')

        try:
            with conexion.cursor() as cursor:
                logger.info(f'\nQuery enviada: "{query}"\n')
                print(f'Se envia la query: {query}')
                cursor.execute(query)
            conexion.commit()
            logger.info(f'Cambios enviados a la bd')
        finally:
            conexion.close()
            print(f'========= Conexion cerrada a: "{DB}" =========')
            logger.info(f'Conexion cerrada a: "{DB}"')

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        logger.info(f'Correcta conexion a la base de datos: "{DB}"')


def post_data_to_database(scrap: str, scrap_value) -> None:
    if scrap == 'dollar':
        query = """INSERT INTO dolar_cotizaciones
                                     (dolar_nacion, M_ArUSD, M1_ArUSD, M2_ArUSD, M3_ArUSD, M4_ArUSD) 
                                     VALUES (?, ?, ?, ?, ?, ?)"""
        post(query)

        data_tuple = (
            float(scrap_value[0]), float(scrap_value[1]), float(scrap_value[2]), float(scrap_value[3]),
            float(scrap_value[4]),
            float(scrap_value[5]))

    elif scrap == 'cme':

        for name, value in scrap_value.items():
            if (name == 'cme_cotizaciones_dated_brent') or (name == 'cme_cotizaciones_ice_brent') or (
                    name == 'cme_cotizaciones_wti'):
                query = """INSERT INTO {} (M_USD_bbl, M1_USD_bbl, M2_USD_bbl, M3_USD_bbl, M4_USD_bbl,M5_USD_bbl) 
                VALUES (?, ?, ?, ?, ?, ?)""".format(name)

            else:
                query = """INSERT INTO {} (M_USD_Gal, M1_USD_Gal, M2_USD_Gal, M3_USD_Gal, M4_USD_Gal,M5_USD_Gal) 
                VALUES (?, ?, ?, ?, ?, ?)""".format(name)

            post(query)

            data_tuple = (float(value[0]), float(value[1]), float(value[2]),
                          float(value[3]), float(value[4]), float(value[5]))


    elif scrap == 'bloomberg':

        query = """INSERT INTO bloomberg_cotizaciones (WTI_NYMEX_M1_USD_bbl_price, 
        WTI_NYMEX_M1_USD_bbl_change, BRENT_NYMEX_M2_USD_bbl_price, BRENT_NYMEX_M2_USD_bbl_change,
        RBOB87_M1_cpg_price, RBOB87_M1_cpg_change, Heating_Oil_M1_cpg_price,Heating_Oil_M1_cpg_change) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

        post(query)

        data_tuple = (float(scrap_value[0]), float(scrap_value[1]), float(scrap_value[2]), float(scrap_value[3]),
                      float(scrap_value[4]), float(scrap_value[5]), float(scrap_value[6]), float(scrap_value[7]))


def get_data_from_database(scrap: str) -> list:
    if scrap == 'dollar':
        query = """SELECT dolar_nacion, M_ArUSD, M1_ArUSD, M2_ArUSD, M3_ArUSD, M4_ArUSD 
                                    FROM dolar_cotizaciones ORDER BY id DESC LIMIT 1"""
        dollar_list = list(get(query))
        return dollar_list

    elif scrap == 'cme':
        all_data = []

        list_table_names = ['cme_cotizaciones_dated_brent', 'cme_cotizaciones_ice_brent', 'cme_cotizaciones_wti',
                            'cme_cotizaciones_cme_rbob87', 'cme_cotizaciones_ho', 'cme_cotizaciones_jet54_usgc',
                            'cme_cotizaciones_fo_ny', 'cme_cotizaciones_propane_opis',
                            'cme_cotizaciones_butane_opis',
                            'cme_cotizaciones_naphtha_cif_nwe']

        for count, table_name in enumerate(list_table_names):
            if count < 3:
                query = """SELECT M_USD_bbl, M1_USD_bbl, M2_USD_bbl, M3_USD_bbl, 
                M4_USD_bbl, M5_USD_bbl FROM {} ORDER BY id DESC LIMIT 1""" \
                    .format(table_name)
                totalRows = get(query)
                [all_data.append(x) for x in totalRows]
            else:
                query = """SELECT M_USD_Gal, M1_USD_Gal, M2_USD_Gal, M3_USD_Gal, M4_USD_Gal,
                                                         M5_USD_Gal FROM {} ORDER BY id DESC LIMIT 1""" \
                    .format(table_name)
                totalRows = get(query)
                [all_data.append(x) for x in totalRows]

        return all_data

    elif scrap == 'bloomberg':

        query = """SELECT WTI_NYMEX_M1_USD_bbl_price, WTI_NYMEX_M1_USD_bbl_change, 
                                                BRENT_NYMEX_M2_USD_bbl_price, BRENT_NYMEX_M2_USD_bbl_change,
                                                RBOB87_M1_cpg_price, RBOB87_M1_cpg_change, 
                                                Heating_Oil_M1_cpg_price, Heating_Oil_M1_cpg_change 
                                                FROM {} ORDER BY id DESC LIMIT 1""".format('bloomberg_cotizaciones')

        bloomberg_list = get(query)

        return bloomberg_list
