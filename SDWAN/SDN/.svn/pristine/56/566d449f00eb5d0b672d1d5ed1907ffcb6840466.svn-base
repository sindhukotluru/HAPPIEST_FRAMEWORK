from selenium.webdriver.common.by import By
from SDN.core.utils.common_types import BrowserType
import time

class BasePage(object):

    _SECTION_XPATH = "//a[.='{0}']"

    def __init__(self, gui_driver):

        self.gui_driver = gui_driver

    def browse_url(self, url):
        self.gui_driver.driver.get(url)
        time.sleep(2)

    def navigate_to_section(self, name):
        elem = self.gui_driver.driver.find_element_by_xpath(self._SECTION_XPATH.format(name))
        elem.click()










