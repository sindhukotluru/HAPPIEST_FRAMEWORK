from Supporting_Libs import variables
from Supporting_Libs.rest_utils import REST
from Config import ControllerConfig

rest_session = REST(user=variables.ODL_RESTCONF_USER, password=variables.ODL_RESTCONF_PASSWORD,
                                                    content_type=ControllerConfig.OF_CONTENT_TYPE)
#rest_session = REST(user='', password='',
#                    content_type=ControllerConfig.CONTENT_TYPE)


