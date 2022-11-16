from pymongo import MongoClient
import pandas as pd
from configparser import ConfigParser
from log.logger import Log

# GLOBAL VALUES
config = ConfigParser()
config.read('config.ini')
CONN_STRING = config['Mongo']['connection_string']
logger = Log().getLogger(__name__)

def connect():
    client = MongoClient(CONN_STRING)