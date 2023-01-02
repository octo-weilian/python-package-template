from configparser import ConfigParser
from pathlib import Path
import logging
from logging import StreamHandler,FileHandler
from logging.handlers import RotatingFileHandler
import sys

FORMAT  = '%(asctime)s %(funcName)s [%(levelname)s] - %(message)s'
FORMAT_TS = '%d-%b %H:%M:%S'
FORMATTER = logging.Formatter(fmt =FORMAT,datefmt=FORMAT_TS)

class Config:
    def __init__(self, ini_file):
        self.ini_file = ini_file
        self.parser = self.read_config()
    
    def read_config(self):
        if Path(self.ini_file).is_file() and Path(self.ini_file).exists():
            parser = ConfigParser()
            parser.read(self.ini_file)
            return parser
        else:
            raise FileNotFoundError(f"{self.ini_file} does not exists.")

    def save_config(self,section,values):
        options = [option for option,_ in self.parser.items(section)]
        for i in range(len(options)):
            self.parser.set(section, options[i], str(values[i]))

        with open(self.ini_file, 'w+') as dst:
            self.parser.write(dst)
            
class Log:
    def __init__(self,name):
        self.logger_name = name
        self.logger = self.get_logger()
        
    @staticmethod
    def console_handler(terminator=None):
        handler = StreamHandler(sys.stdout)
        if terminator:
            handler.terminator = terminator
        handler.setFormatter(FORMATTER)
        return handler
        
    @staticmethod
    def file_handler(log_file):
        handler = RotatingFileHandler(log_file,maxBytes=1e3,backupCount=1,mode='w+')
        handler.setFormatter(FORMATTER)
        return handler

    def get_logger(self):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        return logger