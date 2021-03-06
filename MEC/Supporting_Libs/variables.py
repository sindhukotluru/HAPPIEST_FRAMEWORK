"""
Definitions of common variables for the system test robot suites of the
OpenDaylight project.

Authors: Baohua Yang@IBM, Denghui Huang@IBM
Edited: Many times by many people
"""

# VM Environment defaults
DEFAULT_LINUX_PROMPT = '>'
DEFAULT_USER = 'jenkins'
DEFAULT_TIMEOUT = '30s'

# ODL system variables
ODL_SYSTEM_IP = '10.22.20.77'  # Override if ODL is not running locally to pybot
ODL_SYSTEM_IP_1 = '10.22.20.77'  # Override if ODL is not running locally to pybot
ODL_SYSTEM_IP_LIST = ['ODL_SYSTEM_1_IP', 'ODL_SYSTEM_2_IP', 'ODL_SYSTEM_3_IP']
ODL_SYSTEM_USER = DEFAULT_USER
ODL_SYSTEM_PASSWORD = ''  # empty means use public key authentication
ODL_SYSTEM_PROMPT = DEFAULT_LINUX_PROMPT

# "Tools" system variables (mininet etc).
TOOLS_SYSTEM_IP = '192.168.1.107'  # Override if tools are not run locally to pybot
TOOLS_SYSTEM_2_IP= '192.168.1.106' 
TOOLS_SYSTEM_USER = 'mininet' 
TOOLS_SYSTEM_PASSWORD = 'mininet'  # empty means use public key authentication
TOOLS_SYSTEM_PROMPT = 'mininet@mininet-vm:~$' 
TOOLS_MININET_PROMPT = 'mininet>'

# KARAF Variables
KARAF_SHELL_PORT = '8101'
ESCAPE_CHARACTER = '\x1B'
KARAF_DETAILED_PROMPT = '@' + ESCAPE_CHARACTER + '[0m' + ESCAPE_CHARACTER + '[34mroot' + ESCAPE_CHARACTER + '[0m>'
KARAF_USER = 'karaf'
KARAF_PASSWORD = 'karaf'
KARAF_PROMPT = 'opendaylight-user'

# Logging levels
DEFAULT_ODL_LOG_LEVEL = 'INFO'
DEFAULT_BGPCEP_LOG_LEVEL = DEFAULT_ODL_LOG_LEVEL
DEFAULT_PROTOCOL_LOG_LEVEL = DEFAULT_BGPCEP_LOG_LEVEL
BGPCEP_LOG_LEVEL = DEFAULT_BGPCEP_LOG_LEVEL
PROTOCOL_LOG_LEVEL = BGPCEP_LOG_LEVEL

# BGP variables
ODL_BGP_PORT = '1790'
BGP_TOOL_PORT = '17900'

# Restconf variables
ODL_RESTCONF_USER = 'admin'
ODL_RESTCONF_PASSWORD = 'admin'

# Netconf variables
ODL_NETCONF_CONFIG_PORT = '1830'
ODL_NETCONF_MDSAL_PORT = '2830'
ODL_NETCONF_USER = 'admin'
ODL_NETCONF_PASSWORD = 'admin'
ODL_NETCONF_PROMPT = ']]>]]>'
ODL_NETCONF_NAMESPACE = 'urn:ietf:params:xml:ns:netconf:base:1.0'

# OpenFlow variables
ODL_OF_PLUGIN = 'lithium'

# VTN Coordinator Variables
VTNC = '127.0.0.1'
VTNCPORT = '8083'
VTNC_PREFIX = 'http://' + VTNC + ':' + VTNCPORT
VTNC_HEADERS = {'Content-Type': 'application/json',
                'username': 'admin', 'password': 'adminpass'}

VTNWEBAPI = '/vtn-webapi'
# controllers URL
CTRLS_CREATE = 'controllers.json'
CTRLS = 'controllers'
SW = 'switches'

# vtn URL
VTNS_CREATE = 'vtns.json'
VTNS = 'vtns'

# vbridge URL
VBRS_CREATE = 'vbridges.json'
VBRS = 'vbridges'

# interfaces URL
VBRIFS_CREATE = '(config)interfaces.json'
VBRIFS = 'interfaces'

# portmap URL
PORTMAP_CREATE = 'portmap.json'

# vlanmap URL
VLANMAP_CREATE = 'vlanmaps.json'

# ports URL
PORTS = 'ports/detail.json'

# flowlist URL
FLOWLISTS_CREATE = 'flowlists.json'

# flowlistentry_URL
FLOWLISTENTRIES_CREATE = 'flowlistentries.json'
FLOWLISTS = 'flowlists'

# flowfilter_URL
FLOWFILTERS_CREATE = 'flowfilters.json'
FLOWFILTERENTRIES_CREATE = 'flowfilterentries.json'
FLOWFILTERS = 'flowfilters/in'
FLOWFILTERS_UPDATE = 'flowfilterentries'

# Rest Base Paths
REST_CON = '/restconf/config'
REST_OPER = '/restconf/operational'

# Common APIs
CONFIG_NODES_API = REST_CON+'/opendaylight-inventory:nodes'
OPERATIONAL_NODES_API = REST_OPER+'/opendaylight-inventory:nodes/'
OPERATIONAL_NODES_NETVIRT = '/restconf/operational/network-topology:network-topology/topology/netvirt:1'
OPERATIONAL_TOPO_API = '/restconf/operational/network-topology:' \
                       'network-topology'
CONFIG_TOPO_API = '/restconf/config/network-topology:network-topology'
CONTROLLER_CONFIG_MOUNT = ('/restconf/config/network-topology:'
                           'network-topology/topology'
                           '/topology-netconf/node/'
                           'controller-config/yang-ext:mount')
CONFIG_API = '/restconf/config'
OPERATIONAL_API = '/restconf/operational'
MODULES_API = '/restconf/modules'

# VPN APIs
VPN_INST_API = REST_CON + '/l3vpn:vpn-instances/'
OPERATIONAL_VPN_INST_API = REST_OPER + '/l3vpn:vpn-instances/'
IETF_INTF_API = REST_CON + '/ietf-interfaces:interfaces/'
OPERATIONAL_IETF_INTF_STATE_API = REST_OPER + '/ietf-interfaces:interfaces-state/'
VPN_INTF_API = REST_CON + '/l3vpn:vpn-interfaces/'
OPERATIONAL_VPN_INTF_API = REST_OPER + '/l3vpn:vpn-interfaces/'
OPERATIONAL_FIB_ENTRIES = REST_OPER + '/odl-fib:fibEntries/'
OPERATIONAL_FIB_ENTRIES_VRF_TABLE = REST_OPER + '/odl-fib:fibEntries/vrfTables/'

# NEMO Variables
PREDEFINE_ROLE_URI = '/restconf/config/nemo-user:user-roles'
PREDEFINE_NODE_URI = '/restconf/config/nemo-object:node-definitions'
PREDEFINE_CONNECTION_URI = '/restconf/config/nemo-object:connection-definitions'
REGISTER_TENANT_URI = '/restconf/operations/nemo-intent:register-user'
STRUCTURE_INTENT_URI = '/restconf/operations/nemo-intent:structure-style-nemo-update'
GET_INTENTS_URI = '/retconf/config/intent:intents'

# TOKEN
AUTH_TOKEN_API = '/oauth2/token'
REVOKE_TOKEN_API = '/oauth2/revoke'

# Base Mininet Mac address. DPID of mininet switches will be derived from this.
BASE_MAC_1 = '00:4b:00:00:00:00'
# Base IP of mininet hosts
BASE_IP_1 = '75.75.0.0'

# Vlan Custom Topology Path and File
CREATE_VLAN_TOPOLOGY_FILE = "vlan_vtn_test.py"
CREATE_VLAN_TOPOLOGY_FILE_PATH = "MininetTopo/" +\
                                 CREATE_VLAN_TOPOLOGY_FILE

# Mininet Custom Topology Path and File
CREATE_FULLYMESH_TOPOLOGY_FILE = "create_fullymesh.py"
CREATE_FULLYMESH_TOPOLOGY_FILE_PATH = "libraries/MininetTopo/" +\
                                      CREATE_FULLYMESH_TOPOLOGY_FILE

# Mininet Custom Topology Path and File for Path Policy
CREATE_PATHPOLICY_TOPOLOGY_FILE = "topo-3sw-2host_multipath.py"
CREATE_PATHPOLICY_TOPOLOGY_FILE_PATH = "MininetTopo/" +\
                                       CREATE_PATHPOLICY_TOPOLOGY_FILE

GBP_REGEP_API = "/restconf/operations/endpoint:register-endpoint"
GBP_UNREGEP_API = "/restconf/operations/endpoint:unregister-endpoint"
GBP_TENANTS_API = "/restconf/config/policy:tenants"
GBP_TUNNELS_API = "/restconf/config/opendaylight-inventory:nodes"

# LISP Flow Mapping variables
LFM_RPC_API = "/restconf/operations/odl-mappingservice"
LFM_RPC_API_LI = "/restconf/operations/lfm-mapping-database"
LFM_SB_RPC_API = "/restconf/operations/odl-lisp-sb"

# Neutron
NEUTRON_NB_API = '/controller/nb/v2/neutron'

# Other global variables
# TODO: Move these to more apropriate sections.
PORT = '8080'
RESTPORT = '8282'
RESTCONFPORT = '8181'
OVSDBPORT = '6640'
CONTAINER = 'default'
PREFIX = 'http://' + ODL_SYSTEM_IP + ':' + PORT  # TODO: determine where this is used; create a better named variable
USER = 'admin'  # TODO: who is using this?  Can we make it more specific? (e.g.  RESTCONF_USER)
PWD = 'admin'
PASSWORD = 'EMPTY'
AUTH = [u'admin', u'admin']
SCOPE = 'sdn'
HEADERS = {'Content-Type': 'application/json'}
HEADERS_YANG_JSON = {'Content-Type': 'application/yang.data+json'}
HEADERS_XML = {'Content-Type': 'application/xml'}
ACCEPT_XML = {'Accept': 'application/xml'}
ACCEPT_JSON = {'Accept': 'application/json'}
ACCEPT_EMPTY = {}  # Json should be default, but no-output RPC cannot have Accept header.
ODL_CONTROLLER_SESSION = None
TOPO_TREE_LEVEL = 2
TOPO_TREE_DEPTH = 3
TOPO_TREE_FANOUT = 2
KEYFILE_PASS = 'any'
SSH_KEY = 'id_rsa'
CONTROLLER_STOP_TIMEOUT = 120  # Max number of seconds test will wait for a controller to stop
TOPOLOGY_URL = 'network-topology:network-topology/topology'
SEND_ACCEPT_XML_HEADERS = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}
USER_HOME = '/home/osboxes/'

# Test deadlines global control
ENABLE_GLOBAL_TEST_DEADLINES = True

# Deprecated old variables, to be removed once all tests that need them are
# updated to use the new names.
CONTROLLER = ODL_SYSTEM_IP
CONTROLLERS = ['ODL_SYSTEM_1_IP', 'ODL_SYSTEM_2_IP', 'ODL_SYSTEM_3_IP']
CONTROLLER_PASSWORD = ODL_SYSTEM_PASSWORD
CONTROLLER_PROMPT = ODL_SYSTEM_PROMPT

# Centinel Variables
SET_CONFIGURATION_URI = '/restconf/operations/configuration:set-centinel-configurations'
GET_CONFIGURATION_URI = '/restconf/operational/configuration:configurationRecord/'
STREAMRECORD_CONFIG = '/restconf/config/stream:streamRecord'
SET_STREAMRECORD = '/restconf/operations/stream:set-stream'
ALERTFIELDCONTENTRULERECORD = '/restconf/config/alertrule:alertFieldContentRuleRecord/'
SET_ALERTFIELDCONTENTRULERECORD = '/restconf/operations/alertrule:set-alert-field-content-rule'
ALERTFIELDVALUERULERECORD = '/restconf/config/alertrule:alertFieldValueRuleRecord'
SET_ALERTFIELDVALUERULERECORD = '/restconf/operations/alertrule:set-alert-field-value-rule'
ALERTMESSAGECOUNTRULERECORD = '/restconf/config/alertrule:alertMessageCountRuleRecord/'
SET_ALERTMESSAGECOUNTRULERECORD = '/restconf/operations/alertrule:set-alert-message-count-rule'
GET_DASHBOARDRECORD = '/restconf/operational/dashboardrule:dashboardRecord/'
SET_DASHBOARDRECORD = '/restconf/operations/dashboardrule:set-dashboard'
DELETE_DASHBOARDRECORD = '/restconf/operations/dashboardrule:delete-dashboard'
SET_SUBSCRIBEUSER = '/restconf/operations/subscribe:subscribe-user'
SUBSCRIPTION = '/restconf/config/subscribe:subscription/'
