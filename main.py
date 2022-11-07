from my_app.utils.config import appConfig

#load app configfile 
APP_INI = "appConfig.ini"
APP_CONFIG = appConfig(APP_INI).parser

#methods to read values
PARAM_A = APP_CONFIG.get("section","param_a")
PARAM_B = APP_CONFIG.getboolean("section","param_b")
PARAM_C = APP_CONFIG.getint("section","param_c")
PARAM_D = APP_CONFIG.getfloat("section","param_d")

