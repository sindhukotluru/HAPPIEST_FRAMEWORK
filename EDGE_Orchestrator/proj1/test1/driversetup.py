'''
Created on May 9, 2018

@author: Debiprasanna.M
'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path = 'E:\Old Desktop Backup\geckodriver-v0.19.1-win64\geckodriver.exe')

global driver
 
def get_webdriver():
    return webdriver.Firefox(executable_path = 'E:\Old Desktop Backup\geckodriver-v0.19.1-win64\geckodriver.exe')

driver = get_webdriver()

def log_in():
    driver.get("http://10.16.82.170:8000/odlctrl")
    assert "Login" in driver.title
    elem = driver.find_element_by_name("userName")
    elem.clear()
    elem.send_keys("admin")
    time.sleep(2)
    elem1 = driver.find_element_by_name("password")
    elem1.clear()
    elem1.send_keys("hmwano123")
    time.sleep(2)
    elem1.send_keys(Keys.RETURN)
    
#log_in()
def close_webdriver():
    driver.close()