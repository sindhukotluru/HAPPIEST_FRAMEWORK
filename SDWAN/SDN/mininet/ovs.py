import re
from SDN.core.interface.cli_interface import SSHConnection
from SDN import config

Debug = True


def dlog(log):
    if Debug :
        print log


# TBD : The resp attribute will need to be flushed as it will hold the output of the previous command output
class ovs(object):

    _OVS_OFCTL_COMMAND = "ovs-ofctl"

    def __init__(self,**kwargs):
        self.rc = SSHConnection(IP=kwargs["IP"], username=kwargs["username"], password=kwargs["password"])
        self.rc.connect()

    def addflows(self,**kwargs):
        self.parameters= "add-flow "
        self.interface, self.priority, self.protocol, self.protocol_type, self.input_port, self.action = (kwargs["interface"], kwargs["priority"], kwargs['protocol'],
                                                                           kwargs["protocolType"], kwargs["input_port"], kwargs["action"])
        if self.interface:
            self.parameters += "%s " % self.interface

        if self.priority:
            self.parameters += "priority=%d" % self.priority

        if self.protocol:
            self.parameters += ",%s" % self.protocol

        if self.protocol_type:
            self.parameters += " %s " % self.protocol_type

        if self.input_port:
            self.parameters += ",in_port=%d" % self.input_port

        if self.action:
            self.parameters += ",actions=%s" % self.action

        self.CMD = "%s %s" % (self._OVS_OFCTL_COMMAND, self.parameters)
        print("Flow Configured on %s : %s" %("SWITCH",self.CMD))
        return True if self.rc.execute_command(self.CMD) else False


    def dumpflows(self,**kwargs):
        self.parameters= " dump-flows "
        self.protocol, self.protocol_type, self.interface = (kwargs["protocol"], kwargs["protocolType"],
                                                             kwargs['interface'])
        if self.protocol:
            self.parameters += "-O %s " % self.protocol

        if self.interface:
            self.parameters += " %s " % self.interface

        if self.protocol_type:
            self.parameters += " %s " % self.protocol_type

        dlog( self.parameters)
        self.CMD = "sudo %s %s" % (self._OVS_OFCTL_COMMAND, self.parameters)
        #self.CMD = "%s %s" % (self._OVS_OFCTL_COMMAND, self.parameters)
        return True if self.rc.execute_command(self.CMD) else False

       # TBD: This needs to be moved to the system utils module
    def ifconfig(self,**kwargs):
        self.CMD = "ifconfig %s"
        self.parameters = " "
        if kwargs.get('InterfaceList') is True :
            self.parameters += "| grep Link| awk '{print $1}'"
            
        dlog(self.CMD%(self.parameters))
        return [True, self.rc.resp] if self.rc.execute_command(self.CMD%(self.parameters)) else False

    def version(self):
        #self.CMD = "sudo %s %s"%(self._OVS_OFCTL_COMMAND, "--version")
        self.CMD = "%s %s" % (self._OVS_OFCTL_COMMAND, "--version")
        regexp = r'\(Open vSwitch\).(\d+\.\d+\.\d+)'
        status = self.rc.execute_command(self.CMD)
        #print(self.rc.resp)
        if status:
            match = re.search(regexp, self.rc.resp)
            if match:
                return match.groups()[0]

    def add_group_flows(self,flows_input):
        self.pattern = 'add-group -O OpenFlow13'

        bucket_frame = ''
        inputs = flows_input.copy()
        for key, value in inputs.items():
            if key is 'bridge':
                self.pattern += " %s " % value
            elif key is 'group':
                self.pattern += "group_id=%s" % (value)
            elif key is 'type':
                self.pattern += ",%s=%s," % (key,value)
            elif key is 'buckets':
                for bucket in value:
                    bucket = 'bucket=%s,'%bucket
                    bucket_frame += bucket
        self.pattern += bucket_frame.rstrip(',')
        #print pattern
        self.CMD = "%s %s" % (self._OVS_OFCTL_COMMAND, self.pattern)
        print self.CMD
        print("Flow Configured on %s : %s" % ("SWITCH", self.CMD))
        return True if self.rc.execute_command(self.CMD) else False

    def validate_flows(self, manage_type, br_name, input, ovs_protocol="-O OpenFlow13"):
        """
        This method is to validate the flows created using ovs-ofctl dump-flows cli
        :return: True if it validates the flows properly else False
        """
        search = ""
        if input.has_key("id"): del input["id"]
        if input.has_key("order"): del input["order"]
        self.CMD = self._OVS_OFCTL_COMMAND + " group-flows %s %s" % (ovs_protocol, br_name)
        if self.rc.execute_command(self.CMD, "#"):
            group_flows = self.rc.resp
            print group_flows
            if len(input) == 0:
                search = None
            input_list = group_flows.splitlines()
            if len(input_list) == 1 and "OFPST_FLOW reply" in input_list[0]:search = None
            else:
                for key, value in input.items():
                    pattern = key + "=" + str(value)
                    if key is "dl_type":
                        if value is "2048":
                            pattern = ',ip,'

                    return_list = self.get_match_flow(pattern=pattern, input_list=input_list)
                    if len(return_list) > 1:
                        return_list = self.get_match_flow(pattern=pattern, input_list=return_list)
                    else:
                        search = None if len(return_list) == 0 else True
                        input_list = return_list
                        continue
            if manage_type is not "delete" and search is not None:
                return True
            elif manage_type is "delete" and search is None:
                return True

    def get_flows(self, **kwargs):

        self.parameters = " dump-flows "
        self.protocol, self.protocol_type, self.interface = (kwargs["protocol"], kwargs["protocolType"],
                                                             kwargs['interface'])
        if self.protocol:
            self.parameters += "-O %s " % self.protocol

        if self.interface:
            self.parameters += " %s " % self.interface

        if self.protocol_type:
            self.parameters += " %s " % self.protocol_type

        #dlog(self.parameters)
        self.CMD = "sudo %s %s" % (self._OVS_OFCTL_COMMAND, self.parameters)
        #self.CMD = "%s %s" % (self._OVS_OFCTL_COMMAND, self.parameters)


        flow_records = []
        #print "\nself.CMD = ", self.CMD
        #print "\nself.rc.execute_command(self.CMD) = ", self.rc.execute_command(self.CMD)

        if self.rc.execute_command(self.CMD):
           #print "\nself.rc.resp = ", self.rc.resp
           for line in self.rc.resp.split("\r\n"):
               line = line.strip()
               if line.startswith("cookie"):
                   flow_info = {}
                   for flow_param in line.split(", "):
                       param, value = flow_param.split("=", 1)
                       flow_info[param] = value
                   flow_records.append(flow_info)
        else:
            print "\nInvalid Command: ", self.CMD
        return flow_records

    def _check_iperf_server(self,**kwargs):
        import time
        ip = kwargs['ServerIP']

        self.clientobject = SSHConnection(IP=self.client,
                                          username=self.client_username,
                                          password=self.client_password,
                                          port=5001
                                          )
        self.clientobject.connect()

        self.cmd= 'iperf -c %s'%(ip)

        clientrun = 1
        string = "/sec"
        Resp = ""
        ser_Resp = ""
        ## Checking for the Client and Server response for req-string.
        while string not in Resp and string not in ser_Resp:
            if clientrun :
                result = self.clientobject.execute_command(self.cmd )
                self.rc.execute_command("\n")## To update the server response.
                print result
                clientrun = 0
            time.sleep(0.5)
            Resp = self.clientobject.rc.rc.before
            ## TBD:rc object is cascaded a bit more !!
            ser_Resp = self.rc.rc.rc.before
        self.rc.rc.rc.sendcontrol('c') ## Gently terminate the server connection
        del self.clientobject
        print Resp
        return result

    def iperf_client(self,**kwargs):

        ##import socket
        import os

        self.serverIP = kwargs['serverip']

        self.cmd=  'iperf %s'
        self.server_cmd = 'iperf -s'
        self.parameters = ""
        """
        ##source = kwargs['source']
        dlog('Checking for any iperf sessions running:')
        if os.system('killall -9 iperf') :
            dlog("Killing the existing instance")
        else:
            dlog("No instances found.")
        """
        if kwargs.has_key('client'):
            self.client = kwargs['client']
        if kwargs.has_key('client_username'):
            self.client_username = kwargs['client_username']
        if kwargs.has_key('client_password'):
            self.client_password = kwargs['client_password']

        if kwargs.has_key('timeout'):
            self.timeout = kwargs['timeout']
        if kwargs.has_key('connectiontype'):
            self.connectiontype = kwargs['connectiontype']
            self.parameters = "-u "

            ##self.parameters += " -c %s"%(self.client)

        self.rc.execute_command(self.server_cmd)
        ##self.rc.execute_command(self.cmd%(self.parameters))
        return self._check_iperf_server(ServerIP= self.serverIP)




        

