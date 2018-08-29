'''
Created on May 9, 2018

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
from gre_test import gre_test
from dia_test import dia_test
from mpls_test import mpls_test
from driversetup import *
# driver = webdriver.Firefox(executable_path = 'E:\Old Desktop Backup\geckodriver-v0.19.1-win64\geckodriver.exe')

log_in()
 
if dia_test():
    print "DIA TEST SUCCESSFUL"
else:
    print "DIA TEST FAILED"

if gre_test():
    print "GRE TEST SUCCESSFUL"
else:
    print "GRE TEST FAILED"
    
if mpls_test():
    print "MPLS TEST SUCCESSFUL"
else:
    print "MPLS TEST FAILED"

close_webdriver()

    
