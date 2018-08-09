import sys
import json
sys.path.append('/home/test/AUTOMATION/HAPPIEST_FRAMEWORK')
from Supporting_Libs import rest_session

data = {"login":{"username":"abc","password":"xyz"}}
#url = 'http://10.16.86.74:8081/login'
url = 'http://192.168.43.180:8081/login'

rest_session.send_post_request(url=url, data=json.dumps(data))

print ">>>>>>>> %s    \n>>>>>>>%s "%(rest_session.response_code, rest_session.response_as_text)
