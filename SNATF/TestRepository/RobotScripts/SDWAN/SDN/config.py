import os

ROOT_DIR = r'/root/'

# Topology Configuration parameters
CLIENT_IP = "192.168.203.3"
CLIENT_USER = "test"
CLIENT_PASSWORD = "test123"

HOST1_IP = "192.168.203.27"
HOST1_USER = "root"
HOST1_PASSWORD = "mininet"

HOST2_IP = "192.168.203.28"
HOST2_USER = "root"
HOST1_PASSWORD = "mininet"

SWITCH_IP = "192.168.203.4"
#SWITCH_USER = "execution"
#SWITCH_PASSWORD = "test123"

SWITCH_USER = "test"
SWITCH_PASSWORD = "test123"


CONTROLLER_IP = "192.168.203.44"

#WEB_SERVER = '10.18.33.165'
WEB_SERVER = '192.168.203.3'
#WEB_SERVER = '192.168.122.22'

# REST Configuration parameters
ODL_RESTCONF_USER = 'admin'
ODL_RESTCONF_PASSWORD = 'admin'
RESTCONFPORT = '8181'

REST_CON = '/restconf/config'
CONFIG_FLOW_API = '/opendaylight-inventory:nodes/node/1/flow-node-inventory:table/1/flow/'
CONFIG_FLOW_API = '/opendaylight-inventory:nodes/node/1/flow-node-inventory:table/'

BASE_PAGE_URL = 'http://{0}:8080/SDWAN/mainPage4.html'.format(WEB_SERVER)

#CHROME_DRIVER_PATH = r'/home/osboxes/Downloads/E_R&D/SDN/browser_drivers/chromedriver'
#FIREFOX_PROFILE_DIR = r'/home/osboxes/Downloads/E_R&D/SDN/browser_profile/firefox'
#CHROME_DRIVER_PATH = ROOT_DIR + os.path.sep + r'/root/SDN/browser_drivers/posix/chromedriver_x64'
CHROME_DRIVER_PATH = r'/home/test/repo_12_04_17/SDN/browser_drivers/posix/chromedriver_x64'
FIREFOX_PROFILE_DIR = r'/home/test/repo_12_04_17/SDN/browser_drivers/ff/firefox'
#FIREFOX_PROFILE_DIR = ROOT_DIR + os.path.sep + r'SDN\browser_profile\firefox'
