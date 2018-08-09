import sys
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
from Supporting_Libs import Karaf     
import re  
import time


### Start the ODL controller by Karaf Clean ###
odl_connection = Karaf.Karaf(IP=ControllerConfig.ODL["IP"],username=ControllerConfig.ODL["USER"],password=ControllerConfig.ODL["PASSWORD"]) 
odl_connection.start_karaf(clean=True)

### Install SNMP plugins in the ODL controller ###
odl_connection.configure_plugins(config_flag='install',plugins=ControllerConfig.SNMP_PLUGINS)


### Verify installed SNMP plugins in the ODL controller ###
odl_connection.verify_installed_plugins(plugins=ControllerConfig.SNMP_PLUGINS)
