import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
import re  
import time

oid   = '1.3.6.1.2.1.25.1.2.0'

## Get the system up time
code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')
up_time = re.search(r'(.*) = (.*)',output,flags = re.DOTALL).group(2) 
print("The System UP Time is " + up_time)
