'''
Created on May 3, 2018

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
driver = webdriver.Firefox(executable_path = '/home/test/geckodriver')

def gre_test():
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
    driver.find_element_by_link_text("Configuration").click()
    time.sleep(3)
    driver.find_element_by_link_text("EDGE Device").click()
    time.sleep(3)
    driver.find_element_by_id("add_config_rule").click()
    time.sleep(3)
    select_fr = Select(driver.find_element_by_id("ethernet_type"))
    time.sleep(2)
    select_fr.select_by_index(3)
    time.sleep(5)
    source_ip = driver.find_element_by_xpath("//div//div//input[@id='source_ip']")
    time.sleep(3)
    source_ip.click()
    time.sleep(2)
    driver.execute_script("document.getElementById('source_ip').value='10.10.10.2';")
    time.sleep(2)
    driver.find_element_by_id("source_ip_mask").send_keys("32")
    time.sleep(2)
    select_ingress = Select(driver.find_element_by_id("in_port"))
    time.sleep(2)
    select_ingress.select_by_index(1)
    time.sleep(2)
    radio1 = driver.find_element_by_xpath("//div//label//input[@value='2']")
    radio1.click()
    time.sleep(2)
    driver.find_element_by_id("save_flow_btn").click()
    time.sleep(2)
    
    ing_port=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[1]").text
    egr_port=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[2]").text
    
    if driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[4]"):
        print "Flow add success"
    else:
        print "Unsuccess"
    
    driver.find_element_by_link_text("Statistics").click()
    time.sleep(2)
    driver.find_element_by_link_text("Flow Entries").click()
    time.sleep(4)
    
    flw_ent1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]").text
    time.sleep(4)
    flw_ent2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[4]").text
    flw_ent3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[3]").text
    flw_ent4=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[4]").text
    pr_ty1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[2]").text
    pr_ty2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[2]").text
    
    if ing_port==flw_ent1 and egr_port==flw_ent4:
        if ing_port==flw_ent2 and egr_port==flw_ent3:
            print "flow entry matched on UI"
    else:
        print "not matched"
        
    switch_flow_table = fn()
    
    #print switch_flow_table
    
    if pr_ty1 and pr_ty2 in switch_flow_table:
        print "Flow Entry Verified in OVS-Switch"
    else:
        print "failed"
    time.sleep(2)
    driver.find_element_by_link_text("Tests").click()
    time.sleep(2)  
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[3]/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='start-btn']").click()
    time.sleep(10)
    driver.find_element_by_link_text("Tests").click()
    time.sleep(2)
    driver.find_element_by_link_text("Statistics").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/ul/li[2]/ul/li[1]/a").click()
    time.sleep(2)
    tx_pkts=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]").text
    rx_pkts=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[2]").text
    print "the tx count on switchport is", tx_pkts
    print "the rx count on switchport is", rx_pkts
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/ul/li[5]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='stop-btn']").click()
    time.sleep(2)
    driver.find_element_by_link_text("Configuration").click()
    time.sleep(3)
    driver.find_element_by_link_text("EDGE Device").click()
    time.sleep(1)
    if driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i").click():
        print "Flow deletion successful"
    else:
        print "Flow deletion unsuccessful"
    assert "No results found." not in driver.page_source
    driver.close()
    
gre_test()
