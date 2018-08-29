'''
Created on May 8, 2018

@author: Debiprasanna.M
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from ovsconnect import fn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driversetup import driver
# driver = webdriver.Firefox(executable_path = 'E:\Old Desktop Backup\geckodriver-v0.19.1-win64\geckodriver.exe')

def add_all_flows():
#     driver = webdriver.Firefox(executable_path = 'E:\Old Desktop Backup\geckodriver-v0.19.1-win64\geckodriver.exe')
#     driver.get("http://10.16.82.170:8000/odlctrl")
#     assert "Login" in driver.title
#     elem = driver.find_element_by_name("userName")
#     elem.clear()
#     elem.send_keys("admin")
#     time.sleep(2)
#     elem1 = driver.find_element_by_name("password")
#     elem1.clear()
#     elem1.send_keys("hmwano123")
#     time.sleep(2)
#     elem1.send_keys(Keys.RETURN)
    driver.get("http://10.16.82.170:8000/odlctrl/index")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Configuration")))
    driver.find_element_by_link_text("Configuration").click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "EDGE Device")))
    driver.find_element_by_link_text("EDGE Device").click()
    wait.until(EC.element_to_be_clickable((By.ID, "add_config_rule")))
    driver.find_element_by_id("add_config_rule").click()
    time.sleep(3)
    
    select_fr = Select(driver.find_element_by_id("ethernet_type"))
    time.sleep(2)
    select_fr.select_by_index(3)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div//div//input[@id='source_ip']")))
    source_ip = driver.find_element_by_xpath("//div//div//input[@id='source_ip']")
    time.sleep(1)
    source_ip.click()
    time.sleep(1)
    driver.execute_script("document.getElementById('source_ip').value='10.10.10.1';")
    time.sleep(2)
    driver.find_element_by_id("source_ip_mask").send_keys("32")
    time.sleep(2)
    select_ingress = Select(driver.find_element_by_id("in_port"))
    time.sleep(2)
    select_ingress.select_by_index(1)
    time.sleep(2)
    radio1 = driver.find_element_by_xpath("//div//label//input[@value='4']")
    radio1.click()
    time.sleep(2)
    driver.find_element_by_id("save_flow_btn").click()
    time.sleep(3)
    driver.find_element_by_id("add_config_rule").click()
    time.sleep(3)
    select_fr = Select(driver.find_element_by_id("ethernet_type"))
    time.sleep(2)
    select_fr.select_by_index(3)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div//div//input[@id='source_ip']")))
    source_ip = driver.find_element_by_xpath("//div//div//input[@id='source_ip']")
    time.sleep(1)
    source_ip.click()
    time.sleep(1)
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
    driver.find_element_by_id("add_config_rule").click()
    time.sleep(3)
    select_fr = Select(driver.find_element_by_id("ethernet_type"))
    time.sleep(2)
    select_fr.select_by_index(3)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div//div//input[@id='source_ip']")))
    source_ip = driver.find_element_by_xpath("//div//div//input[@id='source_ip']")
    time.sleep(1)
    source_ip.click()
    time.sleep(1)
    driver.execute_script("document.getElementById('source_ip').value='10.10.10.3';")
    time.sleep(2)
    driver.find_element_by_id("source_ip_mask").send_keys("32")
    time.sleep(2)
    select_ingress = Select(driver.find_element_by_id("in_port"))
    time.sleep(2)
    select_ingress.select_by_index(1)
    time.sleep(2)
    radio1 = driver.find_element_by_xpath("//div//label//input[@value='3']")
    radio1.click()
    time.sleep(2)
    driver.find_element_by_id("save_flow_btn").click()
    time.sleep(2)
    
    ing_port1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]").text#value 1
    print ing_port1
    ing_port2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]").text#value 1
    print ing_port2
    ing_port3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[1]").text#value 1
    print ing_port3
    egr_port1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]").text#value 2
    print egr_port1
    egr_port2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]").text#value 4
    print egr_port2
    egr_port3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[2]").text#value 3
    print egr_port3
    
    if driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[4]"):
        if driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[4]"):
            if driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[4]"):
                print "Flow add success"
    else:
        print "flow add Unsuccess"
    
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Statistics")))
    driver.find_element_by_link_text("Statistics").click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Flow Entries")))
    driver.find_element_by_link_text("Flow Entries").click()
    time.sleep(4)
    print "-------------------------------------------------------------------"
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/table/tbody/tr[6]/td[3]")))
    flw_ent1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[6]/td[3]").text#value--------1
    flw_ent2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[5]/td[4]").text#value--------1
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/table/tbody/tr[6]/td[4]")))
    flw_ent3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[6]/td[4]").text
    flw_ent4=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[5]/td[3]").text
    pr_ty1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[6]/td[2]").text
    pr_ty2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[5]/td[2]").text
    print flw_ent1,flw_ent2,flw_ent3,flw_ent4,pr_ty1,pr_ty2
    #second flow
    flw_ent1_1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[3]").text#value--------1
    flw_ent2_1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[4]").text#value--------1
    flw_ent3_1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[4]").text
    flw_ent4_1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[3]").text
    pr_ty1_1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[2]").text
    pr_ty2_1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[2]").text
    print flw_ent1_1,flw_ent2_1,flw_ent3_1,flw_ent4_1,pr_ty1_1,pr_ty2_1
    #third flow
    flw_ent1_2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]").text#value--------1
    flw_ent2_2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[4]").text#value--------1
    flw_ent3_2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[4]").text
    flw_ent4_2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[3]").text
    pr_ty1_2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[2]").text
    pr_ty2_2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[1]/td[2]").text
    print flw_ent1_2,flw_ent2_2,flw_ent3_2,flw_ent4_2,pr_ty1_2,pr_ty2_2
    
    if ing_port1==flw_ent1 and egr_port2==flw_ent4:
        if ing_port1==flw_ent2 and egr_port2==flw_ent3:
            if ing_port2==flw_ent1_1 and egr_port1==flw_ent4_1:
                if ing_port2==flw_ent2_1 and egr_port1==flw_ent3_1:
                    if ing_port3==flw_ent1_2 and egr_port3==flw_ent4_2:
                        if ing_port3==flw_ent2_2 and egr_port3==flw_ent3_2:
                            print "flow entry matched on UI"
    else:
        print "not matched"
        
    switch_flow_table = fn()
    
    print switch_flow_table
    
    if pr_ty1 and pr_ty2 in switch_flow_table:
        if pr_ty1_1 and pr_ty2_1 in switch_flow_table:
            if pr_ty1_2 and pr_ty2_2 in switch_flow_table:
                print "Flow Entry Verified in OVS-Switch"
    else:
        print "failed"
        
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Tests")))
    driver.find_element_by_link_text("Tests").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[1]/input")))  
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[1]/input").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[2]/input")))
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[2]/input").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[3]/input")))
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/label[3]/input").click()
    driver.find_element_by_xpath("//*[@id='start-btn']").click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Tests")))
    driver.find_element_by_link_text("Tests").click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Statistics")))
    driver.find_element_by_link_text("Statistics").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div[2]/div/ul/li[2]/ul/li[1]/a")))
    driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/ul/li[2]/ul/li[1]/a").click()
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]")))
    tx_pkts=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[3]").text
    rx_pkts=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/table/tbody/tr[4]/td[2]").text
    print "the tx count on switchport is", tx_pkts
    print "the rx count on switchport is", rx_pkts
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div[2]/div/ul/li[5]/a")))
    driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/ul/li[5]/a").click()
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stop-btn']")))
    driver.find_element_by_xpath("//*[@id='stop-btn']").click()
    
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Configuration")))
    time.sleep(2)
    driver.find_element_by_link_text("Configuration").click()
    time.sleep(2)
    if driver.find_element_by_link_text("EDGE Device"):
        driver.find_element_by_link_text("EDGE Device").click()
        print "Found"
    else:
        print "not found"
    
    if wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i"))):
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i").click()
        time.sleep(3)
        if wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i"))):
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i").click()
            time.sleep(3)
            if wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i"))):
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/table/tbody/tr/td[10]/a[2]/i").click()
                time.sleep(3)
        print "Flow deletion successful"
    else:
        print "Flow deletion unsuccessful"

    assert "No results found." not in driver.page_source
    #driver.close()
    
#add_all_flows()