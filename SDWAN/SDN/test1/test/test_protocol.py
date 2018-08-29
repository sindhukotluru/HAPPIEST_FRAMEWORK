import unittest
from pprint import pprint

from odl.util.protocol.ospf import HEADER


class TestProtocol(unittest.TestCase):

    def test_ospf_header(self):

        obj_header = HEADER(r'C:\Users\Karthik.prakash\PycharmProjects\SDN\test\data\ospf_packets\header.bin')
        print obj_header.get_field_size()
        obj_header.parse_field_values()
        print obj_header.version
        print obj_header.type
        print obj_header.area_id
        print obj_header.auth_type
        print obj_header.checksum
        print obj_header.router_id
        pprint(obj_header.get_all_field_value())
