import unittest
import sys
import json
sys.path.append('/home/test/AUTOMATION/HAPPIEST_FRAMEWORK')
from Config import config,ControllerConfig,MEC_REST_INPUT
from Config import OvsConf
from Supporting_Libs.ovs import ovs
from Supporting_Libs import rest_session


class test_MEC_REST_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ovs_obj = ovs(IP=config.SWITCH['IP'], username= config.SWITCH['USER'],
                           password= config.SWITCH['PASSWORD'])
        URL = MEC_REST_INPUT.MEC_URL+'login'
#        rest_session.send_post_request(url=URL, data=json.dumps(MEC_REST_INPUT.Login_input))
        rest_session.send_post_request(url=URL, data=MEC_REST_INPUT.Login_input)
        if rest_session.response_code is not 200: assert False

    unittest.skip("Test to be Skipped")
    def test_1_MEC_SERVICE_ENABLE_Test(self):
        """
        Enable the desired service(s)
        using REST ipnut
        """
        global data, URL
        URL = MEC_REST_INPUT.MEC_URL+'serviceList'
        rest_session.send_post_request(url=URL, data=MEC_REST_INPUT.Reset_input)
        if rest_session.response_code is not 200: assert False
        URL = MEC_REST_INPUT.MEC_URL+'saveList'
        data = MEC_REST_INPUT.make_input(MEC_REST_INPUT.Service_Selection_input,['firewall','dns','telemetry'])
#        data = MEC_REST_INPUT.make_input(MEC_REST_INPUT.Service_Config_input,['firewall','telemetry'])
        rest_session.send_post_request(url=URL, data=data)
        if rest_session.response_code is not 200: assert False 

    unittest.skip("Test to be Skipped")
    def test_2_MEC_VALIDATE_ENABLED_SERVICE_via_REST_Test(self):
        """
        Validate the enabled service conf
        using REST calls
        """
        rest_session.send_get_request(url=URL)
        return_data = rest_session.response_as_text    
        if ((cmp(data,return_data) !=0) or (rest_session.response_code != 200)):assert False 
         
    



if __name__== "__main__":
    unittest.main()
