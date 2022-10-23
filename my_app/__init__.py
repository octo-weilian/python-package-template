from pathlib import Path
from .utils.logger import appLogger

#logger can be used from anywhere in package
APP_NAME = Path(__file__).parent.resolve().stem
LOGGER = appLogger(APP_NAME).logger
LOGGER.addHandler(appLogger.console_handler())

RLOGGER = appLogger(f"R_{APP_NAME}").logger
RLOGGER.addHandler(appLogger.console_handler("\r"))