import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
import re  

## Set the System Description MIB, which is READ-ONLY    
print("Set the value to MIB, which has only READ-ONLY rights")

value = 'Ubuntu'
oid   = '1.3.6.1.2.1.1.1.0'

code , output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,VALUE=value)
m = re.search('Not writable',output)
if m:
  print(output)
