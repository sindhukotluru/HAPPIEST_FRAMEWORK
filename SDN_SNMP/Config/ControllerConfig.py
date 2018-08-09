#
#This Configuration file is to handle the CONTROLLER related input/information
#

# Controller level info
CONTROLLER_TYPE = "ODL"
#ODL_PATH = "/home/test/ODL/karaf-0.8.2/bin"
ODL_PATH = "sudo /home/test/oxygen/karaf-0.8.2/bin"
ODL = {"IP":"192.168.203.7","PORT":"6653",\
           "USER":"test","PASSWORD":"test123"}
ONOS = {"IP":"192.168.203.44","PORT":"6653",\
           "USER":"test","PASSWORD":"test123"}
CONTROLLER_PROFILE = {"ODL":ODL,"ONOS":ONOS}
if CONTROLLER_TYPE is not None: CONTROLLER_INFO = CONTROLLER_PROFILE[CONTROLLER_TYPE].copy()

# REST Configuration parameters
CONTROLLER_RESTCONF_INFO = {'RESTCONF_USER':'admin','RESTCONF_PASSWORD':'admin','RESTCONFPORT':8181}

# Openflow interface info
OF_PLUGINS = ['odl-restconf','odl-l2switch-all', 'odl-openflowplugin-flow-services', 'odl-openflowplugin-drop-test', 'odl-mdsal-all', 'odl-openflowplugin-southbound']
NODE_ID = 'openflow:218538505255758'
OF_API = '/opendaylight-inventory:nodes/node/%s/flow-node-inventory:table/'%NODE_ID
OF_REST_CON = '/restconf/config'
OF_CONTENT_TYPE = r'application/json'
#CONTENT_TYPE = r'application/yang.data+json'

# SNMP Interface info
SNMP_PLUGINS = ['odl-restconf', 'odl-snmp-plugin', 'odl-dlux-core', 'odl-dluxapps-applications']
#SNMP_PLUGINS = ['odl-restconf', 'odl-mdsal-all', 'odl-snmp-plugin']
SNMP_API = "http://{0}:{1}/restconf/operations/snmp:".format(CONTROLLER_INFO['IP'],CONTROLLER_RESTCONF_INFO['RESTCONFPORT'])
SNMP_INPUT = {"input": {"ip-address": "<DUT>","oid" : "<OID>","community" : "<COMMUNITY>","get-type" : "<GET-OPTION>"}} 
      #This is the template for GET operations and for SET "get-type" will be replaced by "value" field during usage phase
