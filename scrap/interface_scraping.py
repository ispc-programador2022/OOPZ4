from configparser import ConfigParser
from log.logger import Log
from abc import ABCMeta, abstractmethod


class Scraping(object):
    __metaclass__ = ABCMeta

    def __init__(self, log=Log()):
        self.logger = log.getLogger(__name__)

        config = ConfigParser()
        config.read('config.ini')

        self.dollar_pages = {
            'banco_nacion': config['Dollar']['banco_nacion'],
            'rofex':        config['Dollar']['rofex']
        }

        self.cme_pages = {
            'cme_cotizaciones_dated_brent':     config['Cme']['cme_cotizaciones_dated_brent'],
            'cme_cotizaciones_ice_brent':       config['Cme']['cme_cotizaciones_ice_brent'],
            'cme_cotizaciones_wti':             config['Cme']['cme_cotizaciones_wti'],
            'cme_cotizaciones_cme_rbob87':      config['Cme']['cme_cotizaciones_cme_rbob87'],
            'cme_cotizaciones_ho':              config['Cme']['cme_cotizaciones_ho'],
            'cme_cotizaciones_jet54_usgc':      config['Cme']['cme_cotizaciones_jet54_usgc'],
            'cme_cotizaciones_fo_ny':           config['Cme']['cme_cotizaciones_fo_ny'],
            'cme_cotizaciones_propane_opis':    config['Cme']['cme_cotizaciones_propane_opis'],
            'cme_cotizaciones_butane_opis':     config['Cme']['cme_cotizaciones_butane_opis'],
            'cme_cotizaciones_naphtha_cif_nwe': config['Cme']['cme_cotizaciones_naphtha_cif_nwe'],
        }

        self.bloomberg_pages = {
            'bloomberg_1': config['Bloomberg']['bloomberg_1'],
            'bloomberg_2': config['Bloomberg']['bloomberg_2']
        }

    @abstractmethod
    def get_response_by_url(self, url): pass

    @abstractmethod
    def get_data_from_pages(self): pass

