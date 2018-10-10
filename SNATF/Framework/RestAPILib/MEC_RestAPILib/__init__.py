
import sys
sys.path.insert(0,'/home/test/SNATF/TestRepository/Variables')
import variables
from MEC_RestAPILib.rest_utils import REST
import MEC_ControllerConfig

rest_session = REST(user=variables.ODL_RESTCONF_USER, password=variables.ODL_RESTCONF_PASSWORD,
                                                    content_type=MEC_ControllerConfig.CONTENT_TYPE)
#rest_session = REST(user='', password='',
#                    content_type=ControllerConfig.CONTENT_TYPE)


