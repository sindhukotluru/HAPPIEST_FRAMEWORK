import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
import re  

value = raw_input("Provide the System name :")
oid   = '1.3.6.1.2.1.1.5.0'

## Set the system name 
snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,VALUE=value)

## Get the system name
code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')

## Verify the SNMP set
match = re.search(value, output)
if match :
     print("The provided system name ' {0} ' is successfully set in the server".format(match.group(0)))   
else : 
     print("The test returns failure on setting the system name")
