import sys
import unittest
sys.path.append('/home/test/automation/All_repo/SDNC-FUNC/HAPPIEST_FRAMEWORK')
from Config import ControllerConfig
from Config import variables       
from Supporting_Libs import snmp_utils
from Supporting_Libs import Karaf      
import re  
import time
import logging

class test_SNMP_ODL_FUNC_Test(unittest.TestCase):

   logging.basicConfig(filename='SNMP_ODL_TEST-' + str(time.strftime("%Y%m%d-%H%M%S")) + '.log',level=logging.INFO,format='%(message)s')

   unittest.skip("Test to be Skipped")
   def test_1_snmp_set(self):

        logging.info("\nSNMP TEST 1::\n")  

        value = 'Controller'
        oid   = '1.3.6.1.2.1.1.5.0'

         ## Set the system name 
        snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,VALUE=value)

         ## Get the system name
        code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')

         ## Verify the SNMP set
        match = re.search(value, output)
        if match :
             logging.info("The provided system name ' {0} ' is successfully set in the server".format(match.group(0)))   
             return True
        else : 
             logging.info("The provided system name is not in the server")   
             assert False    


   unittest.skip("Test to be Skipped")
   def test_2_snmp_get(self):
 
        logging.info("\nSNMP TEST 2::\n")  

        oid   = '1.3.6.1.2.1.25.1.2.0'

        ## Get the system up time
        code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')
        up_time = re.search(r'(.*) = (.*)',output,flags = re.DOTALL).group(2) 
        if up_time:
            logging.info("The System UP Time is " + up_time)
            return True
        else :
            assert False


   unittest.skip("Test to be Skipped")
   def test_3_snmp_read_only_mib(self):

       logging.info("\nSNMP TEST 3::\n")  
       ## Set the System Description MIB, which is READ-ONLY    
       logging.info("Set the value to MIB, which has only READ-ONLY rights")

       value = 'Ubuntu'
       oid   = '1.3.6.1.2.1.1.1.0'

       code , output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,VALUE=value)
       result = re.search('Not writable',output)
       logging.info(output)

       if result :
          return True
       else :
         assert False

   unittest.skip("Test to be Skipped")
   def test_4_snmp_get_bulk(self):
       
       logging.info("\nSNMP TEST 4::\n")  
       oid   = '1.3.6.1.2.1.2.2.1.7'
       up = []
       down = []

       ## Performing GET-BULK operation on interface status
       logging.info('Performing GET-BULK operation on interface status')
       code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET-BULK')
       utf8string = output.encode("utf-8")
       logging.info(utf8string)

       b = re.findall(r"^(1.3.6.1.2.1.2.2.1.7.[0-9]+) (=)+ ([0-9]+)",utf8string,re.M)
       for i in range(0,len(b)) :
             if b[i][2] == '1':
               up.append((b[i][0].split("."))[-1])
               up_interfaces = " ".join(up)
             else : 
               down.append((b[i][0].split("."))[-1])
               down_interfaces = " ".join(down)

       logging.info("The interfaces with idx {0} are in UP state.".format(up_interfaces))
       logging.info("The interfaces with idx {0} are in DOWN state.".format(down_interfaces))

       if len(up) or len(down) > 0 :
          return True     
       else :
          assert False



   unittest.skip("Test to be Skipped")
   def test_5_snmp_get_next(self):

       logging.info("\nSNMP TEST 5::\n")  
       oid   = '1.3.6.1.2.1.1'

       ## Perform GET-NEXT operation
       logging.info("GET-NEXT operation is performed for the OID " + oid)
       code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET-NEXT')
       logging.info(output)

       result = re.search("ERROR MESSAGE",output)

       if result :
         assert False
       else :
         return True

   unittest.skip("Test to be Skipped")
   def test_6_snmp_get_walk(self):

       logging.info("\nSNMP TEST 6::\n")  
       oid = '1.3.6.1.2.1.3.1.1.2'

       ## Perform SNMP WALK operation
       logging.info("**** Perform SNMP WALK operation ****\n")
       code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET-WALK')
       logging.info(output)

       result = re.search("ERROR MESSAGE",output)

       if result :
         assert False
       else :
         return True

   unittest.skip("Test to be Skipped")
   def test_7_snmp_access_unavailable_mibs(self):

       logging.info("\nSNMP TEST 7::\n")  
       oid   = '1.3.6.1.2.1.4.21'

       ## Accessing the MIB , which has no access rights

       logging.info("********* Accessing the MIB , which has no access rights *********")

       code, output = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid,COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')
       result = re.search("noSuchInstance", output)

       if result :
          logging.info(output)
          return True
       else :
          logging.info("The test does not returns error on accessing the mib which is not available")
          assert False

   unittest.skip("Test to be Skipped")
   def test_8_snmp_multiple_get(self):

       logging.info("\nSNMP TEST 8::\n")  
       oid   = ['1.3.6.1.2.1.1.4.0', '1.3.6.1.2.1.1.3.0', '1.3.6.1.2.1.1.6.0']
       output = []

       ## Get the value of System Contact, System UP time, System location
       for i in range(0, len(oid)) :
           code,value = snmp_utils.perform_odl_snmp_operation(IP=variables.SNMP_server_ip,OID=oid[i],COMMUNITY=variables.SNMP_COMMUNITY,GETTYPE='GET')
           output.append((value.encode("utf-8")).split("=")[-1])
 
       logging.info("System Contact person :" + output[0])
       logging.info("System UP Time   :" + output[1])
       logging.info("System Location  :" + output[2])
 
       if len(output) == 3 :
          return True
       else :
          assert False
 

if __name__== "__main__":
    unittest.main()
