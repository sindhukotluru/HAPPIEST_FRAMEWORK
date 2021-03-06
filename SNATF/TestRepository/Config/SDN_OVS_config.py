import os

ROOT_DIR = r'/root/'
GEN_LOG = True

LOG_PATH = '/var/log/automation/SDNC_LOGS'

# Topology Configuration parameters
HOST1 = {'IP':"192.168.203.27","USER":"mininet","PASSWORD":"mininet","PORT_CONFIG":{'iface1':'eth1','iface1_ip':'15.15.15.1/24'}}
#HOST1 = {'IP':"192.168.203.31","USER":"test","PASSWORD":"test123","PORT_CONFIG":{'iface1':'ens8','iface1_ip':'15.15.15.1/24'}}
HOST2 = {'IP':"192.168.203.28","USER":"mininet","PASSWORD":"mininet","PORT_CONFIG":{'iface1':'eth1','iface1_ip':'15.15.15.2/24'}}
#SWITCH = {'IP':"10.16.86.119","USER":"test","PASSWORD":"test123",'ROOT_PSWD':'test123'}
#SWITCH = {'IP':"192.168.1.10","USER":"test","PASSWORD":"test123",'ROOT_PSWD':'test123'}
#SWITCH = {'IP':"192.168.203.32","USER":"test","PASSWORD":"test123",'ROOT_PSWD':'test123'}
SWITCH = {'IP':"192.168.203.4","USER":"test","PASSWORD":"test123",'ROOT_PSWD':'test123'}

source = "h3"
dest = "h4"
MININET = False

OVS_BRIDGE_CONF = {"NAME":"test","PORTS":{'vnet1': '0000:00:04.0', 'vnet3': '0000:00:05.0'}}          #in case of DPDK presence

###############   Input for Traffic Generator ###############
Ethernet = {'dst':"'21:43:65:87:09:02'", 'src':"'12:34:56:78:90:01'"}
Vlan = {"vlan_id":'555'}
Arp = {'src_ip':HOST1["PORT_CONFIG"]["iface1_ip"].split('/')[0],'dst_ip':HOST2["PORT_CONFIG"]["iface1_ip"].split('/')[0],'op_code':'1'}
ICMPv4 = {'type':8,'code':0}
IP = {'src_ip': '33.33.33.1','dst_ip':HOST2["PORT_CONFIG"]["iface1_ip"].split('/')[0]}
#IP = {'src_ip': '100.100.100.2','dst_ip':'1.2.2.12'}

pkt_count = 10  # should not be string type
interval = 0.5  # should not be string type

###############   MEC INPUT  #################
MEC_URL = 'http://'+SWITCH['IP']+':8081/'
Login_input = {"login":{"username":"abc","password":"xyz"}}
Reset_input = {"reset":{"action":"reset"}}
#Service_Selection_input = {"services":{"type1":"firewall","type2":"dns","type3":"telemetry"}}
Service_Selection_input = {"services":{"type1":"Ip-Tables","type2":"DNS-MASq","type3":"Telemetry"}}
Service_Config_input1 ={"config":{"vlan":[{"id":5,"telemetry":[{"selected":True}],"firewall":[{"src_ip":"100.100.100.2","dest_ip":"1.2.2.12","protocol":"icmp"}],"fwS":True,"dnsS":True,"dns":[{"url":"trello.com"}]}],"action":"add"}}
Service_Config_input2 ={"config":{"vlan":[{"id":8,"telemetry":[{"selected":True}],"firewall":[{"src_ip":"200.200.200.3","dest_ip":"2.2.2.21","protocol":"icmp"}],"fwS":True,"dnsS":True,"dns":[{"url":"google.com"}]}],"action":"add"}}
Service_Ovs_Ports = {5:[179,180],8:[181,182]}


