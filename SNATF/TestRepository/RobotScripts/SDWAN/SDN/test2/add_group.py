import re
from SDN.core.interface.cli_interface import SSHConnection
from SDN import config


buckets = ['mod_dl_src=00:00:00:92:11:11,mod_dl_dst=00:00:00:91:22:22,output:2',
           'mod_dl_src=00:00:00:91:11:11,mod_dl_dst=00:00:00:92:22:22,output:1',
           'mod_dl_src=00:00:00:93:11:11,mod_dl_dst=00:00:00:93:22:22,output:1']

flows_input = {'bridge': 'br', 'group': 'id', 'type': 'all','buckets':buckets}


class ovs(object):

    _OVS_OFCTL_COMMAND = "ovs-ofctl add-group "

    #def __init__(self,**kwargs):
    #    self.rc = SSHConnection(IP=kwargs["IP"], username=kwargs["username"], password=kwargs["password"])
    #    self.rc.connect()

    def add_group_flows(self, flows_input):
        pattern = ''
        bucket_frame = ''
        inputs = flows_input.copy()
        for key, value in inputs.items():
            if key is 'bridge':
                pattern += "%s " % value
            elif key is 'group':
                pattern += "group_id=%s" % (value)
            elif key is 'type':
                pattern += ",%s=%s," % (key,value)
            elif key is 'buckets':
                for bucket in buckets:
                    bucket = 'bucket=%s,'%bucket
                    bucket_frame += bucket
        pattern += bucket_frame.rstrip(',')
        #print pattern
        pattern = self._OVS_OFCTL_COMMAND + pattern
        print pattern





obj = ovs()
obj.add_group_flows(flows_input)






