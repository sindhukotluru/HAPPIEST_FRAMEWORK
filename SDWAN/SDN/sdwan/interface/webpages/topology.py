import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from SDN.sdwan.interface.webpages.base import BasePage

class Topology(BasePage):

    SECTION_NAME = 'Topology'
    RELOAD_BUTTON = (By.XPATH, "//button[@id='reload_Button']")
    #RELOAD_BUTTON = (By.CSS_SELECTOR, '#reload_Button')

    def navigate_to_topology_section(self):
        self.navigate_to_section(name=Topology.SECTION_NAME)
        self.gui_driver.driver.maximize_window()
        #self.zoom_in_topology_view()
        time.sleep(2)

    def reload_topology_view(self):
        #elem = self.gui_driver.driver.find_element_by_xpath(self.RELOAD_BUTTON_XPATH)
        elem = WebDriverWait(self.gui_driver.driver, 10).until(EC.presence_of_element_located(self.RELOAD_BUTTON))
        elem.click()


    def zoom_in_topology_view(self):
        #elem = self.gui_driver.driver.find_element_by_tag_name("html")
        #elem.send_keys(Keys.chord(Keys.CONTROL, Keys.SUBTRACT))
        self.gui_driver.driver.execute_script("document.body.style.zoom='90 %'")

