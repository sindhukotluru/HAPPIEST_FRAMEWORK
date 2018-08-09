import ast,json
from requests import Session


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class REST(object):

    __metaclass__ = Singleton

    def __init__(self, user='', password='', content_type=r'application/yang.data+json'):
        self._session = None
        self._response = None
        self.response_code = None
        self.response_as_json = None
        self.response_as_text = None
        self._create_session(user=user, password=password, content_type=content_type)

    def _create_session(self, user, password, content_type):
        self._session = Session()
        self._session.auth = (user, password)
        self._session.headers["Content-Type"] = content_type
#        print("REQUEST HEADER = ", self._session.headers)

    def send_get_request(self, url):
        self._response = self._session.get(url)
        self.response_code = self._response.status_code
        #self.response_as_text = ast.literal_eval(self._response.text)
        #self.response_as_text = json.loads(self._response.text)
        self.response_as_text = self._response.text

    def send_post_request(self, url, data):
        #if type(data) != str:
        #data = json.dumps(data)
        self._response = self._session.post(url=url, data=data)
        self.response_code = self._response.status_code
        self.response_as_text = self._response.text

    def send_put_request(self, url, data):
        self._response = self._session.put(url=url, data=data)
        self.response_code = self._response.status_code
        self.response_as_text = self._response.text

    def send_delete_request(self, url):

        self._response = self._session.delete(url=url)
        self.response_code = self._response.status_code
        self.response_as_text = self._response.text

    @property
    def session(self):
        return self._session






