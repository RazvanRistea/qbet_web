import configparser
import urllib.parse
from allure_commons.types import LinkType
from definitions import CONFIG_PATH
import posixpath


class ConfigManager:

    @staticmethod
    def getConfig(section, option):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        return config[section][option]


