from logic.decorator import singleton
import logging


@singleton
class Log:
    def __init__(self) -> None:
        LOG_FILENAME = 'log/LOG.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S')

    @staticmethod
    def getLogger(route: str) -> logging:
        return logging.getLogger(route)