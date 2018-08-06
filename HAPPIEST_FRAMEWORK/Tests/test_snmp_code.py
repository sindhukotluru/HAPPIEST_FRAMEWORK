import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Supporting_Libs import snmp_utils
import time

#code, text = snmp_utils.perform_odl_snmp_operation(IP='192.168.203.3',OID='1.3.6.1.2.1.1',COMMUNITY='private',GETTYPE='GET-BULK')
code, text = snmp_utils.perform_odl_snmp_operation(IP='192.168.203.3',OID='1.3.6.1.2.1.1.5.0',COMMUNITY='private',VALUE='TeStMaChAiNe')
code, text = snmp_utils.perform_odl_snmp_operation(IP='192.168.203.3',OID='1.3.6.1.2.1.1.5.0',COMMUNITY='private',GETTYPE='GET')
#print code
print text
#code, text = snmp_utils.perform_odl_snmp_operation(IP='192.168.203.3',OID='1.3.6.1.2.1.1',COMMUNITY='test',GETTYPE='GET-BULK')
#print code
#print text
