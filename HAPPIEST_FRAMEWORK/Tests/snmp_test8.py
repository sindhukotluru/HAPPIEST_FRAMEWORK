import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
import re  

oid   = ['1.3.6.1.2.1.1.4.0', '1.3.6.1.2.1.1.3.0', '1.3.6.1.2.1.1.6.0']
output = []

## Get the value of System Contact, System UP time, System location
for i in range(0, len(oid)) :
   code,value = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid[i],COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')
   output.append((value.encode("utf-8")).split("=")[-1])
 
print("System Contact person :" + output[0])
print("System UP Time   :" + output[1])
print("System Location  :" + output[2])
