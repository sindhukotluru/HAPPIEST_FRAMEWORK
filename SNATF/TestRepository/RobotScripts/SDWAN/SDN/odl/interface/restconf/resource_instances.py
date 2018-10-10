from SDN.odl.interface.restconf.api.vpn_interfaces import *
from SDN.odl.interface.restconf.api.vpn_instances import *
from SDN.odl.interface.restconf.api.interfaces import *


class INSTANCES(object):

    def __init__(self):

        self.interface = INTERFACE()
        self.vpn_instance = VPN_INSTANCE()
        self.vpn_interface = VPN_INTERFACE()
        self.dict_resource_instances = {'VPN_INSTANCE': self.vpn_instance,
                                        'VPN_INTERFACE': self.vpn_interface,
                                        'INTERFACE': self.interface}

    def get_resource_instance(self, resource_name):
        return self.dict_resource_instances[resource_name]

