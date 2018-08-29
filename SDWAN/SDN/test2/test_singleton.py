import unittest

from temp.singleton import Session

from odl.util.rest_utils import REST


class TestSession(unittest.TestCase):

    def test_session_singleton(self):
        s1 = Session()
        s2 = Session()

        print s1
        print s2

    def test_rest_singleton(self):
        rest1 = REST()
        rest1.create_session(user="admin", password="admin")
        rest2 = REST()

        print rest1.session
        print rest2.session
