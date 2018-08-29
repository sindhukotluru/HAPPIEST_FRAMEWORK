from bitstring import ConstBitStream
from collections import OrderedDict


class HEADER(object):

    _VERSION_FIELD = "version"
    _TYPE_FIELD = "type"
    _PACKET_LENGTH_FIELD = "packet length"
    _ROUTER_ID_FIELD = "router id"
    _AREA_ID_FIELD = "area id"
    _CHECKSUM_FIELD = "checksum"
    _AUTH_TYPE_FIELD = "auth type"
    _AUTH_FIELD = "authentication"

    def __init__(self, packet_data):
        self._field_size = OrderedDict([(self._VERSION_FIELD, 8),
                                       (self._TYPE_FIELD, 8),
                                       (self._PACKET_LENGTH_FIELD, 16),
                                       (self._ROUTER_ID_FIELD, 32),
                                       (self._AREA_ID_FIELD, 32),
                                       (self._CHECKSUM_FIELD, 16),
                                       (self._AUTH_TYPE_FIELD, 16),
                                       (self._AUTH_FIELD, 32)])

        self._field_values = dict.fromkeys(self._field_size.keys(), None)
        self._packet_data = packet_data

    def get_field_size(self):

        return [size for size in self._field_size.itervalues()]

    def parse_field_values(self):
        data = ConstBitStream(filename=self._packet_data)
        self._field_values = dict(zip(self._field_size.keys(), data.readlist(self.get_field_size())))

    def get_all_field_value(self):
        return self._field_values

    def set_version(self, value):
        self._field_values[self._VERSION_FIELD] = value

    @property
    def version(self):
        return self._field_values[self._VERSION_FIELD].hex

    @property
    def type(self):
        return self._field_values[self._TYPE_FIELD].hex

    @property
    def packet_length(self):
        return self._field_values[self._PACKET_LENGTH_FIELD].hex

    @property
    def router_id(self):
        return self._field_values[self._ROUTER_ID_FIELD].hex

    @property
    def area_id(self):
        return self._field_values[self._AREA_ID_FIELD].hex

    @property
    def checksum(self):
        return self._field_values[self._CHECKSUM_FIELD].hex

    @property
    def auth_type(self):
        return self._field_values[self._AUTH_TYPE_FIELD].hex

    @property
    def authentication(self):
        return self._field_values[self._AUTH_FIELD].hex


class HELLO_PACKET(object):
    pass


class LLS_DATA_BLOCK(object):
    pass

