from pathlib import Path
from .utils import Log,Config

#logger can be used from anywhere in package
APP_ROOT = Path(__file__).parent.resolve()

LOGGER = Log(APP_ROOT.stem).logger
LOGGER.addHandler(Log.console_handler())

INI_FILE = APP_ROOT.joinpath("conf.ini")
CONFIG = Config(INI_FILE).parser