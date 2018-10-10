import sys
sys.path.insert(0,'/home/test/SNATF/TestRepository/Variables')
import variables
from RestAPILib.rest_utils import REST
import ControllerConfig

rest_session = REST(user=variables.ODL_RESTCONF_USER, password=variables.ODL_RESTCONF_PASSWORD,
                                                    content_type=ControllerConfig.OF_CONTENT_TYPE)
#rest_session = REST(user='', password='',
#                    content_type=ControllerConfig.CONTENT_TYPE)


