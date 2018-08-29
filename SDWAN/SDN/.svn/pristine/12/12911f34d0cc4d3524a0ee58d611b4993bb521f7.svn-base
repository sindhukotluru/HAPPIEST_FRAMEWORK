import unittest
from pprint import pprint

from SDN.odl.interface.restconf import variables
from SDN import config

from SDN.odl.interface.restconf.vpn_instance import APPLY_LABEL
from SDN.odl.interface.restconf.vpn_instance import IPV4_FAMILY
from SDN.odl.interface.restconf.vpn_instance import VPN_INSTANCE


#from restconf.interface import SDN_INTERFACE

class TestVPNInstance(unittest.TestCase):

    def setUp(self):
        self.vpn_inst = VPN_INSTANCE()
        #self.vpn_inst.set_rest_url(value="http://{0}:{1}{2}".format(variables.ODL_SYSTEM_IP_1, variables.RESTCONFPORT,
        #                                                            variables.VPN_INST_API))
        self.vpn_inst.set_rest_url(value="http://{0}:{1}{2}".format(config.CONTROLLER_IP, config.RESTCONFPORT,
                                                                    variables.VPN_INST_API))

        #self.sdn_interface = SDN_INTERFACE()

    @unittest.skip("Default Value test skipped")
    def test_get_default_values(self):

        print("\n{0}".format(VPN_INSTANCE.__name__))
        pprint(self.vpn_inst.get_template(default=True))
        pprint(self.vpn_inst.get_json(default=True))

        print("\n{0}:{1}".format(VPN_INSTANCE.__name__, IPV4_FAMILY.__name__))
        pprint(self.vpn_inst.ipv4_family.get_template(default=True))
        pprint(self.vpn_inst.ipv4_family.get_json(default=True))

        print("\n{0}:{1}:{2}".format(VPN_INSTANCE.__name__, IPV4_FAMILY.__name__, APPLY_LABEL.__name__))
        pprint(self.vpn_inst.ipv4_family.apply_label.get_template(default=True))
        pprint(self.vpn_inst.ipv4_family.apply_label.get_json(default=True))

    def test_set_vpninstance_attributes(self):

        try:
            exp_description_value = "Test VPN Instance 1"
            exp_vpn_inst_name = "testVpn1"
            exp_route_distinguisher_value = "100:1"
            exp_export_route_policy_value = "300:1"
            exp_import_route_policy_value = "200:1"
            exp_apply_label_per_route_value = "true"

            self.vpn_inst.set_description(exp_description_value)
            self.vpn_inst.set_vpn_instance_name(exp_vpn_inst_name)
            self.vpn_inst.ipv4_family.set_export_route_policy(value=exp_export_route_policy_value)
            self.vpn_inst.ipv4_family.set_import_route_policy(exp_import_route_policy_value)
            self.vpn_inst.ipv4_family.set_route_distinguisher(exp_route_distinguisher_value)
            self.vpn_inst.ipv4_family.apply_label.set_apply_label_per_route(exp_apply_label_per_route_value)

            print("Create VPN Instance")
            status, message = self.vpn_inst.create_vpn_instance()
            print("Status = ", status)
            print("Message = ", message)
            self.assertEqual(status, 204)

            print("\nGet all VPN Instances")
            status, message = self.vpn_inst.get_vpn_instance()
            print("Status = ", status)
            print("Message = ", message)
            self.assertEqual(status, 200)
        finally:
            print("Delete created VPN Instance")
            status, message = self.vpn_inst.delete_vpn_instance()
            print("Status = ", status)
            print("Message = ", message)
            self.assertEqual(status, 200)






