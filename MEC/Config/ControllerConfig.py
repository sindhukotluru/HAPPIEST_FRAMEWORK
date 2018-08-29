#
#This Configuration file is to handle the CONTROLLER related input/information
#
CONTROLLER_TYPE = "ODL"

ODL = {"IP":"192.168.203.62","PORT":"6653",\
           "USER":"administrator","PASSWORD":"rootroot"}
ONOS = {"IP":"192.168.203.62","PORT":"6653",\
           "USER":"administrator","PASSWORD":"rootroot"}
CONTROLLER_PROFILE = {"ODL":ODL,"ONOS":ONOS}

if CONTROLLER_TYPE is not None: CONTROLLER_INFO = CONTROLLER_PROFILE[CONTROLLER_TYPE].copy()

ODL_PATH = "/home/administrator/ODL/distribution-karaf-0.4.2-Beryllium-SR2/bin"
ODL_PLUGINS = ['odl-restconf-all', 'odl-l2switch-switch', 'odl-openflowplugin-all', 'odl-dlux-all',
               'odl-openflowplugin-flow-services-ui', 'odl-l2switch-hosttracker', 'odl-mdsal-apidocs',
               'odl-dlux-core webconsole', 'odl-ovsdb-southbound-impl-ui']

# REST Configuration parameters
CONTROLLER_RESTCONF_INFO = {'RESTCONF_USER':'admin','RESTCONF_PASSWORD':'admin','RESTCONFPORT':8181}

#CONTENT_TYPE = r'application/yang.data+json'
CONTENT_TYPE = r'application/json'
REST_CON = '/restconf/config'
#REST_CON = '/restconf/config'
NODE_ID = 'openflow:108748501158208'
CONFIG_FLOW_API = '/opendaylight-inventory:nodes/node/%s/flow-node-inventory:table/'%NODE_ID
