import os

ROOT_DIR = r'/root/'
GEN_LOG = True

LOG_PATH = '/var/log/automation/SDNC_LOGS'

# Topology Configuration parameters
CLIENT_IP = "192.168.1.52"
CLIENT_USER = "test"
CLIENT_PASSWORD = "test123"

HOST1_IP = "192.168.203.27"
HOST1_USER = "mininet"
HOST1_PASSWORD = "mininet"

HOST2_IP = "192.168.203.28"
HOST2_USER = "mininet"
HOST2_PASSWORD = "mininet"

source = "h3"
dest = "h4"

SWITCH_IP = "192.168.203.4"

SWITCH_USER = "test"
SWITCH_PASSWORD = "test123"
SWITCH_ROOT_PSWD = "test123"

OVS_BRIDGE = "s1"
MININET = False
#OVS_BRIDGE_PORTS = ['vnet1','vnet3']
OVS_BRIDGE_PORTS = {'vnet5': '0000:00:04.0', 'vnet7': '0000:00:05.0'}          #in case of DPDK presence

HOST1_PORTS = ['eth1']
HOST2_PORTS = ['eth1']

HOST1_IPs = ['15.15.15.1/24']
HOST2_IPs = ['15.15.15.2/24']

CONTROLLER_TYPE = "ODL"
CONTROLLER_IP = "192.168.203.62"
CONTROLLER_PORT = '6653'
CONTROLLER_USER = 'administrator'
CONTROLLER_PASSWORD = 'rootroot'

ODL_PATH = "/home/administrator/ODL/distribution-karaf-0.4.2-Beryllium-SR2/bin"
ODL_PLUGINS = ['odl-restconf-all', 'odl-l2switch-switch', 'odl-openflowplugin-all', 'odl-dlux-all',
               'odl-openflowplugin-flow-services-ui', 'odl-l2switch-hosttracker', 'odl-mdsal-apidocs',
               'odl-dlux-core webconsole', 'odl-ovsdb-southbound-impl-ui']
RESTCONFPORT = 8181
#WEB_SERVER = '10.18.33.165'
WEB_SERVER = '10.22.20.203'
#WEB_SERVER = '192.168.122.22'

# REST Configuration parameters
ODL_RESTCONF_USER = 'admin'
ODL_RESTCONF_PASSWORD = 'admin'
#RESTCONFPORT = '8181'

REST_CON = '/restconf/config'
NODE_ID = 'openflow:72674121520714'
#openflow:72674121520714
#CONFIG_FLOW_API = '/opendaylight-inventory:nodes/node/1/flow-node-inventory:table/1/flow/'
CONFIG_FLOW_API = '/opendaylight-inventory:nodes/node/%s/flow-node-inventory:table/'%NODE_ID

BASE_PAGE_URL = 'http://{0}:8080/SDWAN/mainPage4.html'.format(WEB_SERVER)

#CHROME_DRIVER_PATH = r'/home/osboxes/Downloads/E_R&D/SDN/browser_drivers/chromedriver'
#FIREFOX_PROFILE_DIR = r'/home/osboxes/Downloads/E_R&D/SDN/browser_profile/firefox'
#CHROME_DRIVER_PATH = ROOT_DIR + os.path.sep + r'/root/SDN/browser_drivers/posix/chromedriver_x64'
CHROME_DRIVER_PATH = r'/home/test/vivek_repo/SDN/browser_drivers/posix/chromedriver_x64'
FIREFOX_PROFILE_DIR = r'/home/test/vivek_repo/SDN/browser_drivers/ff/firefox'
#FIREFOX_PROFILE_DIR = ROOT_DIR + os.path.sep + r'SDN\browser_profile\firefox'


###############   Input for Traffic Generator ###############
Ethernet = {'dst':"'21:43:65:87:09:02'", 'src':"'12:34:56:78:90:01'"}
Vlan = {"vlan_id":'555'}
Arp = {'src_ip':HOST1_IPs[0].split('/')[0],'dst_ip':HOST2_IPs[0].split('/')[0],'op_code':'1'}
ICMPv4 = {'type':8,'code':0}
IP = {'src_ip': '33.33.33.1','dst_ip':HOST2_IPs[0].split('/')[0]}

pkt_count = 10  # should not be string type
interval = 0.5  # should not be string type
