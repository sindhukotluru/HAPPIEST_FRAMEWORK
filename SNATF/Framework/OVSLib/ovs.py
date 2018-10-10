import sys
sys.path.insert(0,'/home/test/SNATF/Framework/CliLib')
import re
import time
import pdb
from cli_interface import SSHConnection
from OVSLib.flow_utils import FlowManagement
import OvsConf
import config
import ControllerConfig
from log_generate import fill_getLogger
from robot.api.deco import keyword

Debug = True


def dlog(log):
    if Debug:
        print log


# TBD : The resp attribute will need to be flushed as it will hold the output of the previous command output
class ovs(SSHConnection):
    _OVS_OFCTL_COMMAND = "ovs-ofctl"
    _OVS_VSCTL_COMMAND = "ovs-vsctl"
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, *args, **kwargs):
        super(ovs,self).__init__(*args,**kwargs)
        self.IP = kwargs['IP']
        self.usr = kwargs['username']
        self.pwd = kwargs['password']
        self.connect()
        logger_name = __name__.split('.')[-1]
        self.log_handler = fill_getLogger(logger_name)
        self.log_handler.writeInfolog("************* SSH to OVS SWITCH %s *************" % self.IP)

    def disconnect_ovs(self):
        self.disconnect()

    def ovs_execute_command(self,cmd,exp_out=None,prompt='#'):
        result = self.execute_command(cmd=cmd,exp_out=exp_out,prompt=prompt)
        self.resp = self.resp
        return result

    def get_ovs_dpid(self,brname):
        """
        To fetch the datapathid of Switch and convert into decimal
        """
        self.dpid = 0
        cmd = self._OVS_VSCTL_COMMAND+' get bridge {0} datapath-id'.format(brname)
        if self.ovs_execute_command(cmd=cmd,prompt='#'):
            self.dpid = self.resp
        return self.dpid

    def is_ovs_alive(self):
        """
        This small method to check whether ovs is running or not
        :return: True is ove is alive
        """
        #Code yet to be added
        return True

    def update_ovs_ports_id(self,br_name):
        """
        To return the ovs-port ids
        """
        ports_ids = []
        self.ovs_execute_command(cmd='ovs-ofctl show {0}'.format(br_name))
        cmd_out = self.resp
        for port in config.OVS_BRIDGE_CONF["PORTS"]:
            reg_obj = re.search('(\d+)\(%s\): addr:'%port,cmd_out)
            if reg_obj: ports_ids.extend(reg_obj.group(1)) 
         
    def create_validate_bridge(self, br_name, cntrlr, topo = None,dpdk = None):
        """
        Date: 15/06/2017  Author: Sirish
        This is to configure the bridge with controll and ensure
        the bridge & controller details are listed properly under vsctl
        br_name is bridge name & cntrlr is a list with ip & port number
        """
        regex = regex1 = None
        result = self.validate_bridge_conf(br_name=br_name, cntrlr=cntrlr, topo=topo)
        if result is False:
            self.log_handler.writeInfolog("Unable to find ovs bridge %s, lets configure" %br_name)
            self.ovs_execute_command("ovs-vsctl del-br %s"%br_name)
            self.CMD = "%s add-br %s" %(self._OVS_VSCTL_COMMAND, br_name)
            if dpdk == True:
                self.CMD = self.CMD+" -- set bridge {0} datapath_type=netdev".format(br_name)
            result1 = self.ovs_execute_command(self.CMD)
            dpid = hex(int(ControllerConfig.NODE_ID.split(':')[1])).split('x')[1]
            if len(dpid) < 16:
               dpid = '0'*(16-len(dpid))+dpid 
            self.ovs_execute_command("ovs-vsctl set bridge {0} other-config:datapath-id={1}".format(br_name,dpid))
            self.CMD = "%s set-controller %s tcp:%s:%s" %(self._OVS_VSCTL_COMMAND,br_name,cntrlr[0],cntrlr[1])
            result2 = self.ovs_execute_command(self.CMD)
            time.sleep(10)
            result = self.validate_bridge_conf(br_name=br_name, cntrlr=cntrlr, topo=topo)
            if result is False:
                self.log_handler.writeErrorlog("Something wrong with OVS bridge & controller config")
        if result is True:
            self.log_handler.writeInfolog("Bridge and Controller configured properly")
        return result

    def validate_bridge_conf(self, br_name, cntrlr, topo):
        """
        Date: 15/06/2017  Author: Sirish
        To ensure the bridge config against the given inputs
        """
        result = False
        regex = None
        time.sleep(15)
        self.CMD = "%s show" % self._OVS_VSCTL_COMMAND
        if self.ovs_execute_command(cmd=self.CMD,prompt='#'):
            command_output = self.resp
            regex = 'Bridge\s+\"?%s\"?'%br_name
            if re.search(regex, command_output):
                regex = 'Contr.*\"tcp:%s:%s\"' %(cntrlr[0],cntrlr[1])
                if topo is not None:
                    regex = 'Contr.*\"tcp:%s:66\d+\"' %(cntrlr[0])
                if re.search(regex, command_output) and re.search('is_connected: true', command_output):
                    result = True
        return result

    def addports_validate(self, br_name, ports,topo=None, dpdk=None):
        """
         This method is to add ports to the desired bridge
        :param br_name:
        :param ports: list of ports
        :param dpdk: to differentiate b/w ovs & ovdk
        :return: True if ports added to bridge properly
        """
        result = False
        i = 0
        if topo is None:
            for port in ports:
                self.ovs_execute_command("ifconfig %s"%port)
                out = self.resp
                if re.search('Device not found',out) and dpdk == None:
                    self.log_handler.writeInfolog("Provided ports are not avialable, moving to next port...\n")
                    continue
                else:
                    self.ovs_execute_command("ifconfig %s up"%port)
                    self.CMD = "%s port-to-br %s" % (self._OVS_VSCTL_COMMAND,port)
                    temp = self.ovs_execute_command(self.CMD)
                    cmd_output = self.resp
                    cmd_out = cmd_output.splitlines()
                    if temp and re.search('no port named', self.resp) and br_name not in cmd_out:
                        self.CMD = "%s add-port %s %s -- set Interface %s ofport_request=%s" \
                                   %(self._OVS_VSCTL_COMMAND,br_name,port,port,OvsConf.ports[i])
                        if dpdk == True:
                            self.CMD += " type=dpdk options:dpdk-devargs={0}".format(ports[port])
                        i += 1
                        temp = self.ovs_execute_command(self.CMD)
                        if temp:
                            self.log_handler.writeInfolog("%s\nPort %s is added to bridge %s successfully\n"
                                                          %(self.resp,port,br_name))
                            result = True
                        else:
                            self.log_handler.writeErrorlog("Unable to add port %s to bridge %s"%(port,br_name))
                    elif br_name in cmd_out:
                        self.log_handler.writeInfolog("Port %s is already part of the bridge %s" % (port, br_name))
                        result = True
                        continue
                    else:
                        self.log_handler.writeErrorlog("Operation is not permitted as port %s is already part "
                                                                            "of another bridge %s" %(port,cmd_out[1]))
                        continue
        else:
            result = True
        if result is True:
            time.sleep(5)
            self.ovs_execute_command("ovs-ofctl del-flows %s"%br_name)
        return result

    def manage_flows(self, manage_type, br_name,flow_inputs,ovs_protocol = "", controller=None):
        """
         This method is to manage OVS flows like add,modify,del & validate
         return True on the successful execution
        """
        manage_type = str(manage_type)
        cli = msg = pattern = action = ""
        result = cmd_result = False
        if flow_inputs is None or 'Null' in flow_inputs:
            flow_inputs = {}
        inputs = flow_inputs.copy()
        self.ovs_execute_command("ovs-ofctl dump-flows %s"%br_name, prompt="#")
        if controller is 'ODL':flowutils = FlowManagement()
        #Below block is to construct the pattern to install flow using ovs cli
        if inputs is not None and controller is None:
            if inputs.has_key("id"): del inputs["id"]
            if inputs.has_key("order"): del inputs["order"]
            for key,value in inputs.items():
                if key is 'protocol':pattern += "%s,"%value
                elif key is 'actions' and manage_type is "delete":
                    continue
            pattern += action
        #Preparing cli/restinput against the desired action, add/delete
        if manage_type == "add" or manage_type == "alter":
            if controller is 'ODL':
                msg = "ADDED by %s" % controller
                inputs["max_length"] = "100"
            else:
                cli = " add-flow " if manage_type is "add" else " mod-flow "

        elif manage_type == "delete":
            if controller is not None:
                flow_attrs=None if len(flow_inputs)==0 else flow_inputs
                msg = "DELETED by %s" % controller
            else:
                cli = "del-flows --strict" if (len(inputs) != 0) else "del-flows "
        
        #Execute cli/restcall to perform desired action, add/delete flow
        if controller is 'ODL':
            final_input = flow_attrs if manage_type == 'delete' else inputs
            cmd_result=flowutils.configure_flows(option=manage_type,flow_attrs=final_input)
            if manage_type == 'add':del inputs["max_length"]
        else:
            self.CMD = self._OVS_OFCTL_COMMAND + " %s %s %s %s" % (cli, ovs_protocol, br_name, pattern)
            cmd_result = self.ovs_execute_command(self.CMD,prompt="#")

        if cmd_result:
            #pdb.set_trace()
            if self.validate_flows(manage_type=manage_type,br_name=br_name, input=inputs):
                self.log_handler.writeInfolog("Flow is %s successfully and verified the same in dump-flows"%msg)
                result = True
        if result is False: self.log_handler.writeErrorlog("Failed to %s the Flow, Check manually...!!!"%manage_type)
        return result


    def validate_flows(self, manage_type, br_name, input, ovs_protocol=""):
        """
        This method is to validate the flows created using ovs-ofctl dump-flows cli
        :return: True if it validates the flows properly else False
        """
        search = pattern = ""
        return_list = []
        if manage_type == 'delete': input['None']='None'
        if input.has_key("id"): del input["id"]
        if input.has_key("order"): del input["order"]
        self.CMD = self._OVS_OFCTL_COMMAND + " dump-flows %s %s" % (ovs_protocol, br_name)
        if self.ovs_execute_command(self.CMD, "#"):
            dump_flows = self.resp
            input_list = dump_flows.splitlines()
            flows_list = dup_flow_list = []
            for entry in input_list:
                if re.search('^\scookie=.*table.*',entry):
                    flows_list.append(entry)
            dup_flow_list = flows_list
            if len(input) == 0 and len(flows_list) == 0:
                search = None
            else:
                for key, value in input.items():
                    if key == 'dl_type':
                        continue
                    if key == ("nw_src" or "nw_dst") and input['dl_type'] == ("2048" or "0x0800"):
                        pattern = ',ip,'
                    elif key == 'nw_proto':
                        if str(value) == '6':
                            pattern = 'tcp'
                        elif str(value) == '17':
                            pattern = 'udp'
                        elif str(value) == '1' and input['dl_type'] == ("2048" or "0x0800"):
                            pattern = 'icmp'
                    elif key == 'tcp_dst':
                        pattern = 'tp_dst'+'='+str(value)
                    else:
                        pattern = key + "=" + str(value)
                    if 'None' not in pattern:return_list = self.get_match_flow(pattern=pattern, input_list=flows_list)
                    if len(return_list) == 0:
                        search = None
                        if manage_type == 'delete':
                            flows_list = return_list
                            continue
                        else: break
                    else: flows_list = return_list
                if len(return_list) > 1 and manage_type != "delete":search = None
                if len(flows_list) == len(return_list) and manage_type == 'delete':search = None
            if manage_type != "delete" and search is not None:
                return True
            elif manage_type == "delete" and search is None:
                return True

    def get_match_flow(self,pattern,input_list):
        """
        Supportive method to get the matched flow list out of dump flows list
        :return: list of matched flows to the input pattern
        """
        temp = []
        pattern = re.sub(r'(actions=.*,?)(\d+)', r'\1output:\2', pattern)
        for entry in input_list:
            if pattern not in entry:
                temp.append(entry)
                if len(input_list)==1:return []
        diff_list = list(set(input_list)-set(temp))
        if len(diff_list) > 0:
            return diff_list
        else:
            return input_list


    def version(self):
        # self.CMD = "sudo %s %s"%(self._OVS_OFCTL_COMMAND, "--version")
        self.CMD = "%s %s" % (self._OVS_OFCTL_COMMAND, "--version")
        regexp = r'\(Open vSwitch\).(\d+\.\d+\.\d+)'
        status = self.execute_command(self.CMD)
        # print(self.resp)
        if status:
            match = re.search(regexp, self.resp)
            if match:
                return match.groups()[0]

