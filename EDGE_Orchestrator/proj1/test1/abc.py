'''
Created on Apr 27, 2018

@author: Debiprasanna.M
'''
from ovsconnect import fn

switch_flow_table = fn()
print switch_flow_table
if "49" and "18" in switch_flow_table:
    print "Flow Entry Verified in OVS-Switch"
else:
    print "failed"