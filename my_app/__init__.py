from pathlib import Path
from .utils.logger import appLogger

#logger can be used from anywhere in package
APP_ROOT = Path(__file__).parent.resolve()
LOGGER = appLogger(APP_ROOT.stem).logger
LOGGER.addHandler(appLogger.console_handler())

RLOGGER = appLogger(f"R_{APP_ROOT.stem}").logger
RLOGGER.addHandler(appLogger.console_handler("\r"))