'''
Created on May 10, 2018

@author: Debiprasanna.M
'''
from ovsconnect import fn
import time
import paramiko    
onn=fn("ovs-ofctl dump-ports S1 4 \n")
print onn