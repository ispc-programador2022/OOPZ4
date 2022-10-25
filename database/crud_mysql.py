from configparser import ConfigParser
from log.logger import Log
import pymysql

# GLOBAL VALUES
config = ConfigParser()
config.read('config.ini')
HOST = config['database']['host']
USER = config['database']['user']
PASSWORD = config['database']['password']
DB = config['database']['db']
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