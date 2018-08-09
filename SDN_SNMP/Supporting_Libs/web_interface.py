from selenium import webdriver
from Supporting_Libs.common_types import BrowserType
from Config import config

class WebInterface(object):

    def __init__(self, browser):
        if browser == BrowserType.FIREFOX:
            profile = webdriver.FirefoxProfile()
            self._driver = webdriver.Firefox(firefox_profile=profile)
            self._driver.manage().window().maximize()

        if browser == BrowserType.CHROME:
            #self._driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            self.option = webdriver.ChromeOptions()
            self.option.add_argument("--start-maximized")
            self._driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, chrome_options=self.option)





    @property
    def driver(self):
        return self._driver
