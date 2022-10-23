from my_app.utils.config import appConfig

#load app configfile 
APP_INI = "appConfig.ini"
APP_CONFIG = appConfig(APP_INI)

if APP_CONFIG.parser is not None:
	PARAMATER_A = APP_CONFIG.get("my_section","parameter_a")
    PARAMATER_B = APP_CONFIG.get("my_section","parameter_b")