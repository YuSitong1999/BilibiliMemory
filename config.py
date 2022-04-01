import configparser

config = configparser.ConfigParser()
is_config_exist = False
default_config = {'output': 'output', 'tmppath': '.'}


def try_load_config() -> bool:
    global config, is_config_exist
    config_list = config.read('config.ini')
    is_config_exist = len(config_list) > 0
    return is_config_exist


def get_config(key: str) -> str:
    global config, is_config_exist
    return config.get('main', key) if is_config_exist else default_config[key.lower()]
