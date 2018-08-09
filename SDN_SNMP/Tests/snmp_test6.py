import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
import re  


oid = '1.3.6.1.2.1.3.1.1.2'

## Perform SNMP WALK operation
print("**** Perform SNMP WALK operation ****\n")
code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET-WALK')
print(output)
