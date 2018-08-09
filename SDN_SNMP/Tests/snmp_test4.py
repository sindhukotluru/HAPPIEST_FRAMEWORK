import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
import re  

oid   = '1.3.6.1.2.1.2.2.1.7'
up = []
down = []

## Performing GET-BULK operation on interface status
print('Performing GET-BULK operation on interface status')
code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET-BULK')
utf8string = output.encode("utf-8")
print(utf8string)

b = re.findall(r"^(1.3.6.1.2.1.2.2.1.7.[0-9]+) (=)+ ([0-9]+)",utf8string,re.M)
for i in range(0,len(b)) :
    if b[i][2] == '1':
       up.append((b[i][0].split("."))[-1])
       up_interfaces = " ".join(up)
    else : 
       down.append((b[i][0].split("."))[-1])
       down_interfaces = " ".join(down)

print("The interfaces with idx {0} are in UP state.".format(up_interfaces))
print("The interfaces with idx {0} are in DOWN state.".format(down_interfaces))

if len(up) or len(down) > 0 :
   print("Success")

