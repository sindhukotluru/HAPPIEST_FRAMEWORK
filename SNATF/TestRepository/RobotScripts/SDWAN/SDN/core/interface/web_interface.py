from selenium import webdriver
from SDN.core.utils.common_types import BrowserType
from SDN import config

class WebInterface(object):

    def __init__(self, browser):
        if browser == BrowserType.FIREFOX:
            profile = webdriver.FirefoxProfile()
            self._driver = webdriver.Firefox(firefox_profile=profile)

        if browser == BrowserType.CHROME:
            self._driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)

    @property
    def driver(self):
        return self._driver
