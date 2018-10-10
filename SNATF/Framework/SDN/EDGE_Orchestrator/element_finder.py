'''
Created on May 4, 2018

@author: Debiprasanna.M
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from ovsconnect import fn
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(executable_path = 'E:\Old Desktop Backup\geckodriver-v0.19.1-win64\geckodriver.exe')

def element_finder():
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
    time.sleep(2)

    driver.find_element_by_link_text("Statistics").click()
    time.sleep(2)
    #wait(driver, 5).until(method, message)
    driver.find_element_by_link_text("Flow Entries").click()
    time.sleep(4)
    global flw_ent1,flw_ent2,flw_ent3,flw_ent4,pr_ty1,pr_ty2
    flw_ent1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]").text
    flw_ent2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[4]").text
    flw_ent3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[3]").text
    flw_ent4=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[4]").text
    pr_ty1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[2]").text
    pr_ty2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[2]").text
    
    print flw_ent1,flw_ent2,flw_ent3,flw_ent4,pr_ty1,pr_ty2
    return flw_ent1,flw_ent2,flw_ent3,flw_ent4,pr_ty1,pr_ty2
    driver.close()
#element_finder()