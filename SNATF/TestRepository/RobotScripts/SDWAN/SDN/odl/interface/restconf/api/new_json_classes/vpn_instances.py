from copy import deepcopy
import json
from SDN.odl.interface.restconf import rest_session



class MVPN(object):

    _MVPN_FIELD = "mvpn"
    _SEND_COMMUNITY_FIELD = "send-community"
    _ADVERTISEMENT_INTERVAL_FIELD = "advertisement-interval"
    _WEIGHT_FIELD = "weight"
    _MAXIMUM_PREFIX_FIELD = "maximum-prefix"
    _NEXT_HOP_SELF_FIELD = "next-hop-self"
    _SPLIT_UPDATE_GROUP_FIELD = "split-update-group"
    _ROUTE_REFLECTOR_CLIENT_FIELD = "route-reflector-client"
    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _NEXT_HOP_UNCHANGED_FIELD = "next-hop-unchanged"
    _DETECTION_FIELD = "detection"
    _PREFIX_LIST_FIELD = "prefix-list"
    _ALLOWAS_IN_FIELD = "allowas-in"
    _SOO_FIELD = "soo"
    _ACTIVE_FIELD = "active"
    _SOFT_RECONFIGURATION_FIELD = "soft-reconfiguration"

    def __init__(self):
        self._template = {}
        self._template[self._SEND_COMMUNITY_FIELD] = None
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._MAXIMUM_PREFIX_FIELD] = None
        self._template[self._NEXT_HOP_SELF_FIELD] = None
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = None
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = None
        self._template[self._REMOVE_PRIVATE_AS_FIELD] = None
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = None
        self._template[self._DETECTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._ALLOWAS_IN_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._template[self._SOFT_RECONFIGURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._remove_private_as = REMOVE_PRIVATE_AS()
        self._detection = DETECTION()
        self._prefix_list = PREFIX_LIST()

    @property
    def remove_private_as(self):
        return self._remove_private_as

    @property
    def detection(self):
        return self._detection

    @property
    def prefix_list(self):
        return self._prefix_list

    def set_send_community(self, value):
        self._template[self._SEND_COMMUNITY_FIELD] = value

    def set_advertisement_interval(self, value):
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_maximum_prefix(self, value):
        self._template[self._MAXIMUM_PREFIX_FIELD] = value

    def set_next_hop_self(self, value):
        self._template[self._NEXT_HOP_SELF_FIELD] = value

    def set_split_update_group(self, value):
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = value

    def set_route_reflector_client(self, value):
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = value

    def set_next_hop_unchanged(self, value):
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = value

    def set_allowas_in(self, value):
        self._template[self._ALLOWAS_IN_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

    def set_soft_reconfiguration(self, value):
        self._template[self._SOFT_RECONFIGURATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template(default=default)
            self._default_template[self._DETECTION_FIELD] = self.detection.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            return self._default_template
        else:
            self._template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template()
            self._template[self._DETECTION_FIELD] = self.detection.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        remove_private_as_payload = self.remove_private_as.get_payload()
        if remove_private_as_payload:
            payload[self._REMOVE_PRIVATE_AS_FIELD] = remove_private_as_payload
        detection_payload = self.detection.get_payload()
        if detection_payload:
            payload[self._DETECTION_FIELD] = detection_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_mvpn(self):
        
        payload = {self._MVPN_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_mvpn(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_mvpn(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ENTITY(object):

    _ENTITY_FIELD = "entity"
    _OWNER_FIELD = "owner"
    _ID_FIELD = "id"
    _CANDIDATE_FIELD = "candidate"

    def __init__(self):
        self._template = {}
        self._template[self._OWNER_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._template[self._CANDIDATE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._candidate = CANDIDATE()

    @property
    def candidate(self):
        return self._candidate

    def set_owner(self, value):
        self._template[self._OWNER_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._CANDIDATE_FIELD] = self.candidate.get_template(default=default)
            return self._default_template
        else:
            self._template[self._CANDIDATE_FIELD] = self.candidate.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        candidate_payload = self.candidate.get_payload()
        if candidate_payload:
            payload[self._CANDIDATE_FIELD] = candidate_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_entity(self):
        
        payload = {self._ENTITY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_entity(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_entity(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class DETECTION(object):

    _DETECTION_FIELD = "detection"
    _THRESHOLD_FIELD = "threshold"
    _ENABLE_FIELD = "enable"

    def __init__(self):
        self._template = {}
        self._template[self._THRESHOLD_FIELD] = None
        self._template[self._ENABLE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_threshold(self, value):
        self._template[self._THRESHOLD_FIELD] = value

    def set_enable(self, value):
        self._template[self._ENABLE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_detection(self):
        
        payload = {self._DETECTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_detection(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_detection(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIX(object):

    _PREFIX_FIELD = "prefix"
    _PREFIX_FILTER_FIELD = "prefix-filter"
    _SEQ_NR_FIELD = "seq-nr"

    def __init__(self):
        self._template = {}
        self._template[self._PREFIX_FILTER_FIELD] = None
        self._template[self._SEQ_NR_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefix_filter = PREFIX_FILTER()

    @property
    def prefix_filter(self):
        return self._prefix_filter

    def set_seq_nr(self, value):
        self._template[self._SEQ_NR_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIX_FILTER_FIELD] = self.prefix_filter.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIX_FILTER_FIELD] = self.prefix_filter.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefix_filter_payload = self.prefix_filter.get_payload()
        if prefix_filter_payload:
            payload[self._PREFIX_FILTER_FIELD] = prefix_filter_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_prefix(self):
        
        payload = {self._PREFIX_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_prefix(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_prefix(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class DEFAULT_ORIGINATE(object):

    _DEFAULT_ORIGINATE_FIELD = "default-originate"
    _ENABLE_FIELD = "enable"

    def __init__(self):
        self._template = {}
        self._template[self._ENABLE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_enable(self, value):
        self._template[self._ENABLE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_default_originate(self):
        
        payload = {self._DEFAULT_ORIGINATE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_default_originate(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_default_originate(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class RTFILTER(object):

    _RTFILTER_FIELD = "rtfilter"
    _UNICAST_FIELD = "unicast"

    def __init__(self):
        self._template = {}
        self._template[self._UNICAST_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._unicast = UNICAST()

    @property
    def unicast(self):
        return self._unicast

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._UNICAST_FIELD] = self.unicast.get_template(default=default)
            return self._default_template
        else:
            self._template[self._UNICAST_FIELD] = self.unicast.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        unicast_payload = self.unicast.get_payload()
        if unicast_payload:
            payload[self._UNICAST_FIELD] = unicast_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_rtfilter(self):
        
        payload = {self._RTFILTER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_rtfilter(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_rtfilter(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PEER_ADDRESS_TYPE(object):

    _PEER_ADDRESS_TYPE_FIELD = "peer-address-type"
    _IP_HOST_ADDRESS_FIELD = "ip-host-address"
    _PREFIX_FIELD = "prefix"
    _IP_ADDRESS_FIELD = "ip-address"

    def __init__(self):
        self._template = {}
        self._template[self._IP_HOST_ADDRESS_FIELD] = None
        self._template[self._PREFIX_FIELD] = None
        self._template[self._IP_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefix = PREFIX()

    @property
    def prefix(self):
        return self._prefix

    def set_ip_host_address(self, value):
        self._template[self._IP_HOST_ADDRESS_FIELD] = value

    def set_ip_address(self, value):
        self._template[self._IP_ADDRESS_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIX_FIELD] = self.prefix.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIX_FIELD] = self.prefix.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefix_payload = self.prefix.get_payload()
        if prefix_payload:
            payload[self._PREFIX_FIELD] = prefix_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_peer_address_type(self):
        
        payload = {self._PEER_ADDRESS_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_peer_address_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_peer_address_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MDT(object):

    _MDT_FIELD = "mdt"
    _SEND_COMMUNITY_FIELD = "send-community"
    _ADVERTISEMENT_INTERVAL_FIELD = "advertisement-interval"
    _WEIGHT_FIELD = "weight"
    _MAXIMUM_PREFIX_FIELD = "maximum-prefix"
    _NEXT_HOP_SELF_FIELD = "next-hop-self"
    _SPLIT_UPDATE_GROUP_FIELD = "split-update-group"
    _ROUTE_REFLECTOR_CLIENT_FIELD = "route-reflector-client"
    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _NEXT_HOP_UNCHANGED_FIELD = "next-hop-unchanged"
    _DETECTION_FIELD = "detection"
    _PREFIX_LIST_FIELD = "prefix-list"
    _ALLOWAS_IN_FIELD = "allowas-in"
    _SOO_FIELD = "soo"
    _ACTIVE_FIELD = "active"
    _SOFT_RECONFIGURATION_FIELD = "soft-reconfiguration"

    def __init__(self):
        self._template = {}
        self._template[self._SEND_COMMUNITY_FIELD] = None
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._MAXIMUM_PREFIX_FIELD] = None
        self._template[self._NEXT_HOP_SELF_FIELD] = None
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = None
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = None
        self._template[self._REMOVE_PRIVATE_AS_FIELD] = None
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = None
        self._template[self._DETECTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._ALLOWAS_IN_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._template[self._SOFT_RECONFIGURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._remove_private_as = REMOVE_PRIVATE_AS()
        self._detection = DETECTION()
        self._prefix_list = PREFIX_LIST()

    @property
    def remove_private_as(self):
        return self._remove_private_as

    @property
    def detection(self):
        return self._detection

    @property
    def prefix_list(self):
        return self._prefix_list

    def set_send_community(self, value):
        self._template[self._SEND_COMMUNITY_FIELD] = value

    def set_advertisement_interval(self, value):
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_maximum_prefix(self, value):
        self._template[self._MAXIMUM_PREFIX_FIELD] = value

    def set_next_hop_self(self, value):
        self._template[self._NEXT_HOP_SELF_FIELD] = value

    def set_split_update_group(self, value):
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = value

    def set_route_reflector_client(self, value):
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = value

    def set_next_hop_unchanged(self, value):
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = value

    def set_allowas_in(self, value):
        self._template[self._ALLOWAS_IN_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

    def set_soft_reconfiguration(self, value):
        self._template[self._SOFT_RECONFIGURATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template(default=default)
            self._default_template[self._DETECTION_FIELD] = self.detection.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            return self._default_template
        else:
            self._template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template()
            self._template[self._DETECTION_FIELD] = self.detection.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        remove_private_as_payload = self.remove_private_as.get_payload()
        if remove_private_as_payload:
            payload[self._REMOVE_PRIVATE_AS_FIELD] = remove_private_as_payload
        detection_payload = self.detection.get_payload()
        if detection_payload:
            payload[self._DETECTION_FIELD] = detection_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_mdt(self):
        
        payload = {self._MDT_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_mdt(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_mdt(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ACTION_CHOICE(object):

    _ACTION_CHOICE_FIELD = "action-choice"
    _SET_DL_DST_ACTION_FIELD = "set-dl-dst-action"
    _OUTPUT_ACTION_FIELD = "output-action"
    _SET_NW_DST_ACTION_FIELD = "set-nw-dst-action"
    _PUSH_VLAN_ACTION_FIELD = "push-vlan-action"
    _SET_TP_DST_ACTION_FIELD = "set-tp-dst-action"
    _SET_FIELD_ACTION_FIELD = "set-field-action"
    _SET_DL_SRC_ACTION_FIELD = "set-dl-src-action"
    _PUSH_MPLS_ACTION_FIELD = "push-mpls-action"
    _SET_TP_SRC_ACTION_FIELD = "set-tp-src-action"
    _SET_NW_SRC_ACTION_FIELD = "set-nw-src-action"
    _POP_MPLS_ACTION_FIELD = "pop-mpls-action"
    _ENQUEUE_ACTION_FIELD = "enqueue-action"
    _GROUP_ACTION_FIELD = "group-action"
    _SET_QUEUE_ACTION_FIELD = "set-queue-action"
    _SET_NW_TTL_ACTION_FIELD = "set-nw-ttl-action"
    _SET_VLAN_PCP_ACTION_FIELD = "set-vlan-pcp-action"
    _SET_VLAN_VID_ACTION_FIELD = "set-vlan-vid-action"
    _PUSH_PBB_ACTION_FIELD = "push-pbb-action"
    _SET_MPLS_TTL_ACTION_FIELD = "set-mpls-ttl-action"
    _SET_NW_TOS_ACTION_FIELD = "set-nw-tos-action"

    def __init__(self):
        self._template = {}
        self._template[self._SET_DL_DST_ACTION_FIELD] = None
        self._template[self._OUTPUT_ACTION_FIELD] = None
        self._template[self._SET_NW_DST_ACTION_FIELD] = None
        self._template[self._PUSH_VLAN_ACTION_FIELD] = None
        self._template[self._SET_TP_DST_ACTION_FIELD] = None
        self._template[self._SET_FIELD_ACTION_FIELD] = None
        self._template[self._SET_DL_SRC_ACTION_FIELD] = None
        self._template[self._PUSH_MPLS_ACTION_FIELD] = None
        self._template[self._SET_TP_SRC_ACTION_FIELD] = None
        self._template[self._SET_NW_SRC_ACTION_FIELD] = None
        self._template[self._POP_MPLS_ACTION_FIELD] = None
        self._template[self._ENQUEUE_ACTION_FIELD] = None
        self._template[self._GROUP_ACTION_FIELD] = None
        self._template[self._SET_QUEUE_ACTION_FIELD] = None
        self._template[self._SET_NW_TTL_ACTION_FIELD] = None
        self._template[self._SET_VLAN_PCP_ACTION_FIELD] = None
        self._template[self._SET_VLAN_VID_ACTION_FIELD] = None
        self._template[self._PUSH_PBB_ACTION_FIELD] = None
        self._template[self._SET_MPLS_TTL_ACTION_FIELD] = None
        self._template[self._SET_NW_TOS_ACTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_set_dl_dst_action(self, value):
        self._template[self._SET_DL_DST_ACTION_FIELD] = value

    def set_output_action(self, value):
        self._template[self._OUTPUT_ACTION_FIELD] = value

    def set_set_nw_dst_action(self, value):
        self._template[self._SET_NW_DST_ACTION_FIELD] = value

    def set_push_vlan_action(self, value):
        self._template[self._PUSH_VLAN_ACTION_FIELD] = value

    def set_set_tp_dst_action(self, value):
        self._template[self._SET_TP_DST_ACTION_FIELD] = value

    def set_set_field_action(self, value):
        self._template[self._SET_FIELD_ACTION_FIELD] = value

    def set_set_dl_src_action(self, value):
        self._template[self._SET_DL_SRC_ACTION_FIELD] = value

    def set_push_mpls_action(self, value):
        self._template[self._PUSH_MPLS_ACTION_FIELD] = value

    def set_set_tp_src_action(self, value):
        self._template[self._SET_TP_SRC_ACTION_FIELD] = value

    def set_set_nw_src_action(self, value):
        self._template[self._SET_NW_SRC_ACTION_FIELD] = value

    def set_pop_mpls_action(self, value):
        self._template[self._POP_MPLS_ACTION_FIELD] = value

    def set_enqueue_action(self, value):
        self._template[self._ENQUEUE_ACTION_FIELD] = value

    def set_group_action(self, value):
        self._template[self._GROUP_ACTION_FIELD] = value

    def set_set_queue_action(self, value):
        self._template[self._SET_QUEUE_ACTION_FIELD] = value

    def set_set_nw_ttl_action(self, value):
        self._template[self._SET_NW_TTL_ACTION_FIELD] = value

    def set_set_vlan_pcp_action(self, value):
        self._template[self._SET_VLAN_PCP_ACTION_FIELD] = value

    def set_set_vlan_vid_action(self, value):
        self._template[self._SET_VLAN_VID_ACTION_FIELD] = value

    def set_push_pbb_action(self, value):
        self._template[self._PUSH_PBB_ACTION_FIELD] = value

    def set_set_mpls_ttl_action(self, value):
        self._template[self._SET_MPLS_TTL_ACTION_FIELD] = value

    def set_set_nw_tos_action(self, value):
        self._template[self._SET_NW_TOS_ACTION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_action_choice(self):
        
        payload = {self._ACTION_CHOICE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_action_choice(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_action_choice(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class STATISTICS(object):

    _STATISTICS_FIELD = "statistics"
    _PREFIX_HIT_COUNT_FIELD = "prefix-hit-count"

    def __init__(self):
        self._template = {}
        self._template[self._PREFIX_HIT_COUNT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_prefix_hit_count(self, value):
        self._template[self._PREFIX_HIT_COUNT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_statistics(self):
        
        payload = {self._STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BGP_NEIGHBOR_STATE(object):

    _BGP_NEIGHBOR_STATE_FIELD = "bgp-neighbor-state"
    _ADMINSTATUS_FIELD = "adminStatus"
    _IN_LASTUPDATETIME_FIELD = "in-lastupdatetime"

    def __init__(self):
        self._template = {}
        self._template[self._ADMINSTATUS_FIELD] = None
        self._template[self._IN_LASTUPDATETIME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_adminstatus(self, value):
        self._template[self._ADMINSTATUS_FIELD] = value

    def set_in_lastupdatetime(self, value):
        self._template[self._IN_LASTUPDATETIME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_neighbor_state(self):
        
        payload = {self._BGP_NEIGHBOR_STATE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_neighbor_state(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_neighbor_state(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class CANDIDATE(object):

    _CANDIDATE_FIELD = "candidate"
    _NAME_FIELD = "name"

    def __init__(self):
        self._template = {}
        self._template[self._NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_candidate(self):
        
        payload = {self._CANDIDATE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_candidate(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_candidate(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ENTITY_TYPE(object):

    _ENTITY_TYPE_FIELD = "entity-type"
    _TYPE_FIELD = "type"
    _ENTITY_FIELD = "entity"

    def __init__(self):
        self._template = {}
        self._template[self._TYPE_FIELD] = None
        self._template[self._ENTITY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._entity = ENTITY()

    @property
    def entity(self):
        return self._entity

    def set_type(self, value):
        self._template[self._TYPE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ENTITY_FIELD] = self.entity.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ENTITY_FIELD] = self.entity.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        entity_payload = self.entity.get_payload()
        if entity_payload:
            payload[self._ENTITY_FIELD] = entity_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_entity_type(self):
        
        payload = {self._ENTITY_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_entity_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_entity_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class REMOVE_PRIVATE_AS(object):

    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _REMOVE_PRIVATE_AS_NUMBER_FIELD = "remove-private-as-number"
    _REPLACE_WITH_LOCAL_AS_FIELD = "replace-with-local-as"

    def __init__(self):
        self._template = {}
        self._template[self._REMOVE_PRIVATE_AS_NUMBER_FIELD] = None
        self._template[self._REPLACE_WITH_LOCAL_AS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_remove_private_as_number(self, value):
        self._template[self._REMOVE_PRIVATE_AS_NUMBER_FIELD] = value

    def set_replace_with_local_as(self, value):
        self._template[self._REPLACE_WITH_LOCAL_AS_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_remove_private_as(self):
        
        payload = {self._REMOVE_PRIVATE_AS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_remove_private_as(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_remove_private_as(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIXES(object):

    _PREFIXES_FIELD = "prefixes"
    _PREFIX_FIELD = "prefix"

    def __init__(self):
        self._template = {}
        self._template[self._PREFIX_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefix = PREFIX()

    @property
    def prefix(self):
        return self._prefix

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIX_FIELD] = self.prefix.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIX_FIELD] = self.prefix.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefix_payload = self.prefix.get_payload()
        if prefix_payload:
            payload[self._PREFIX_FIELD] = prefix_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_prefixes(self):
        
        payload = {self._PREFIXES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_prefixes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_prefixes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IPV6_FAMILY(object):

    _IPV6_FAMILY_FIELD = "ipv6-family"
    _L3VPNVRFPIPE_FIELD = "l3vpnVrfPipe"
    _TRAFFIC_STATISTICS_FIELD = "traffic-statistics"
    _VPNTARGETS_FIELD = "vpnTargets"
    _VPN_FRR_FIELD = "vpn-frr"
    _TUNNEL_POLICY_FIELD = "tunnel-policy"
    _IMPORTRIBS_FIELD = "importRibs"
    _EXPORT_ROUTE_POLICY_FIELD = "export-route-policy"
    _PREFIX_LIMIT_FIELD = "prefix-limit"
    _ROUTING_TABLE_LIMIT_FIELD = "routing-table-limit"
    _APPLY_LABEL_FIELD = "apply-label"
    _IMPORT_ROUTE_POLICY_FIELD = "import-route-policy"
    _L3VPNTTLMODE_FIELD = "l3vpnTtlMode"
    _ROUTE_DISTINGUISHER_FIELD = "route-distinguisher"

    def __init__(self):
        self._template = {}
        self._template[self._L3VPNVRFPIPE_FIELD] = None
        self._template[self._TRAFFIC_STATISTICS_FIELD] = None
        self._template[self._VPNTARGETS_FIELD] = None
        self._template[self._VPN_FRR_FIELD] = None
        self._template[self._TUNNEL_POLICY_FIELD] = None
        self._template[self._IMPORTRIBS_FIELD] = None
        self._template[self._EXPORT_ROUTE_POLICY_FIELD] = None
        self._template[self._PREFIX_LIMIT_FIELD] = None
        self._template[self._ROUTING_TABLE_LIMIT_FIELD] = None
        self._template[self._APPLY_LABEL_FIELD] = None
        self._template[self._IMPORT_ROUTE_POLICY_FIELD] = None
        self._template[self._L3VPNTTLMODE_FIELD] = None
        self._template[self._ROUTE_DISTINGUISHER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._l3vpnvrfpipe = L3VPNVRFPIPE()
        self._vpntargets = VPNTARGETS()
        self._importribs = IMPORTRIBS()
        self._prefix_limit = PREFIX_LIMIT()
        self._routing_table_limit = ROUTING_TABLE_LIMIT()
        self._apply_label = APPLY_LABEL()
        self._l3vpnttlmode = L3VPNTTLMODE()

    @property
    def l3vpnvrfpipe(self):
        return self._l3vpnvrfpipe

    @property
    def vpntargets(self):
        return self._vpntargets

    @property
    def importribs(self):
        return self._importribs

    @property
    def prefix_limit(self):
        return self._prefix_limit

    @property
    def routing_table_limit(self):
        return self._routing_table_limit

    @property
    def apply_label(self):
        return self._apply_label

    @property
    def l3vpnttlmode(self):
        return self._l3vpnttlmode

    def set_traffic_statistics(self, value):
        self._template[self._TRAFFIC_STATISTICS_FIELD] = value

    def set_vpn_frr(self, value):
        self._template[self._VPN_FRR_FIELD] = value

    def set_tunnel_policy(self, value):
        self._template[self._TUNNEL_POLICY_FIELD] = value

    def set_export_route_policy(self, value):
        self._template[self._EXPORT_ROUTE_POLICY_FIELD] = value

    def set_import_route_policy(self, value):
        self._template[self._IMPORT_ROUTE_POLICY_FIELD] = value

    def set_route_distinguisher(self, value):
        self._template[self._ROUTE_DISTINGUISHER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._L3VPNVRFPIPE_FIELD] = self.l3vpnvrfpipe.get_template(default=default)
            self._default_template[self._VPNTARGETS_FIELD] = self.vpntargets.get_template(default=default)
            self._default_template[self._IMPORTRIBS_FIELD] = self.importribs.get_template(default=default)
            self._default_template[self._PREFIX_LIMIT_FIELD] = self.prefix_limit.get_template(default=default)
            self._default_template[self._ROUTING_TABLE_LIMIT_FIELD] = self.routing_table_limit.get_template(default=default)
            self._default_template[self._APPLY_LABEL_FIELD] = self.apply_label.get_template(default=default)
            self._default_template[self._L3VPNTTLMODE_FIELD] = self.l3vpnttlmode.get_template(default=default)
            return self._default_template
        else:
            self._template[self._L3VPNVRFPIPE_FIELD] = self.l3vpnvrfpipe.get_template()
            self._template[self._VPNTARGETS_FIELD] = self.vpntargets.get_template()
            self._template[self._IMPORTRIBS_FIELD] = self.importribs.get_template()
            self._template[self._PREFIX_LIMIT_FIELD] = self.prefix_limit.get_template()
            self._template[self._ROUTING_TABLE_LIMIT_FIELD] = self.routing_table_limit.get_template()
            self._template[self._APPLY_LABEL_FIELD] = self.apply_label.get_template()
            self._template[self._L3VPNTTLMODE_FIELD] = self.l3vpnttlmode.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        l3vpnvrfpipe_payload = self.l3vpnvrfpipe.get_payload()
        if l3vpnvrfpipe_payload:
            payload[self._L3VPNVRFPIPE_FIELD] = l3vpnvrfpipe_payload
        vpntargets_payload = self.vpntargets.get_payload()
        if vpntargets_payload:
            payload[self._VPNTARGETS_FIELD] = vpntargets_payload
        importribs_payload = self.importribs.get_payload()
        if importribs_payload:
            payload[self._IMPORTRIBS_FIELD] = importribs_payload
        prefix_limit_payload = self.prefix_limit.get_payload()
        if prefix_limit_payload:
            payload[self._PREFIX_LIMIT_FIELD] = prefix_limit_payload
        routing_table_limit_payload = self.routing_table_limit.get_payload()
        if routing_table_limit_payload:
            payload[self._ROUTING_TABLE_LIMIT_FIELD] = routing_table_limit_payload
        apply_label_payload = self.apply_label.get_payload()
        if apply_label_payload:
            payload[self._APPLY_LABEL_FIELD] = apply_label_payload
        l3vpnttlmode_payload = self.l3vpnttlmode.get_payload()
        if l3vpnttlmode_payload:
            payload[self._L3VPNTTLMODE_FIELD] = l3vpnttlmode_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ipv6_family(self):
        
        payload = {self._IPV6_FAMILY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ipv6_family(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ipv6_family(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIX_LIST(object):

    _PREFIX_LIST_FIELD = "prefix-list"
    _PREFIXES_FIELD = "prefixes"
    _PREFIX_LIST_NAME_FIELD = "prefix-list-name"

    def __init__(self):
        self._template = {}
        self._template[self._PREFIXES_FIELD] = None
        self._template[self._PREFIX_LIST_NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefixes = PREFIXES()

    @property
    def prefixes(self):
        return self._prefixes

    def set_prefix_list_name(self, value):
        self._template[self._PREFIX_LIST_NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIXES_FIELD] = self.prefixes.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIXES_FIELD] = self.prefixes.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefixes_payload = self.prefixes.get_payload()
        if prefixes_payload:
            payload[self._PREFIXES_FIELD] = prefixes_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_prefix_list(self):
        
        payload = {self._PREFIX_LIST_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_prefix_list(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_prefix_list(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IPV4(object):

    _IPV4_FIELD = "ipv4"
    _MVPN_FIELD = "mvpn"
    _UNICAST_FIELD = "unicast"
    _MULTICAST_FIELD = "multicast"
    _MDT_FIELD = "mdt"

    def __init__(self):
        self._template = {}
        self._template[self._MVPN_FIELD] = None
        self._template[self._UNICAST_FIELD] = None
        self._template[self._MULTICAST_FIELD] = None
        self._template[self._MDT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._mvpn = MVPN()
        self._unicast = UNICAST()
        self._multicast = MULTICAST()
        self._mdt = MDT()

    @property
    def mvpn(self):
        return self._mvpn

    @property
    def unicast(self):
        return self._unicast

    @property
    def multicast(self):
        return self._multicast

    @property
    def mdt(self):
        return self._mdt

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MVPN_FIELD] = self.mvpn.get_template(default=default)
            self._default_template[self._UNICAST_FIELD] = self.unicast.get_template(default=default)
            self._default_template[self._MULTICAST_FIELD] = self.multicast.get_template(default=default)
            self._default_template[self._MDT_FIELD] = self.mdt.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MVPN_FIELD] = self.mvpn.get_template()
            self._template[self._UNICAST_FIELD] = self.unicast.get_template()
            self._template[self._MULTICAST_FIELD] = self.multicast.get_template()
            self._template[self._MDT_FIELD] = self.mdt.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        mvpn_payload = self.mvpn.get_payload()
        if mvpn_payload:
            payload[self._MVPN_FIELD] = mvpn_payload
        unicast_payload = self.unicast.get_payload()
        if unicast_payload:
            payload[self._UNICAST_FIELD] = unicast_payload
        multicast_payload = self.multicast.get_payload()
        if multicast_payload:
            payload[self._MULTICAST_FIELD] = multicast_payload
        mdt_payload = self.mdt.get_payload()
        if mdt_payload:
            payload[self._MDT_FIELD] = mdt_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ipv4(self):
        
        payload = {self._IPV4_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ipv4(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ipv4(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IPV6(object):

    _IPV6_FIELD = "ipv6"
    _MVPN_FIELD = "mvpn"
    _UNICAST_FIELD = "unicast"
    _MULTICAST_FIELD = "multicast"

    def __init__(self):
        self._template = {}
        self._template[self._MVPN_FIELD] = None
        self._template[self._UNICAST_FIELD] = None
        self._template[self._MULTICAST_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._mvpn = MVPN()
        self._unicast = UNICAST()
        self._multicast = MULTICAST()

    @property
    def mvpn(self):
        return self._mvpn

    @property
    def unicast(self):
        return self._unicast

    @property
    def multicast(self):
        return self._multicast

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MVPN_FIELD] = self.mvpn.get_template(default=default)
            self._default_template[self._UNICAST_FIELD] = self.unicast.get_template(default=default)
            self._default_template[self._MULTICAST_FIELD] = self.multicast.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MVPN_FIELD] = self.mvpn.get_template()
            self._template[self._UNICAST_FIELD] = self.unicast.get_template()
            self._template[self._MULTICAST_FIELD] = self.multicast.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        mvpn_payload = self.mvpn.get_payload()
        if mvpn_payload:
            payload[self._MVPN_FIELD] = mvpn_payload
        unicast_payload = self.unicast.get_payload()
        if unicast_payload:
            payload[self._UNICAST_FIELD] = unicast_payload
        multicast_payload = self.multicast.get_payload()
        if multicast_payload:
            payload[self._MULTICAST_FIELD] = multicast_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ipv6(self):
        
        payload = {self._IPV6_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ipv6(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ipv6(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPN_INSTANCE(object):

    _VPN_INSTANCE_FIELD = "vpn-instance"
    _IPV4_FAMILY_FIELD = "ipv4-family"
    _DESCRIPTION_FIELD = "description"
    _ODL_L3VPN_ROUTE_ENTRY_ID_FIELD = "odl-l3vpn:route-entry-id"
    _ODL_L3VPN_VPN_ID_FIELD = "odl-l3vpn:vpn-id"
    _VPN_ID_FIELD = "vpn-id"
    _IPV6_FAMILY_FIELD = "ipv6-family"
    _VPN_INSTANCE_NAME_FIELD = "vpn-instance-name"

    def __init__(self):
        self._template = {}
        self._template[self._IPV4_FAMILY_FIELD] = None
        self._template[self._DESCRIPTION_FIELD] = None
        self._template[self._ODL_L3VPN_ROUTE_ENTRY_ID_FIELD] = None
        self._template[self._ODL_L3VPN_VPN_ID_FIELD] = None
        self._template[self._VPN_ID_FIELD] = None
        self._template[self._IPV6_FAMILY_FIELD] = None
        self._template[self._VPN_INSTANCE_NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ipv4_family = IPV4_FAMILY()
        self._ipv6_family = IPV6_FAMILY()

    @property
    def ipv4_family(self):
        return self._ipv4_family

    @property
    def ipv6_family(self):
        return self._ipv6_family

    def set_description(self, value):
        self._template[self._DESCRIPTION_FIELD] = value

    def set_odl_l3vpn_route_entry_id(self, value):
        self._template[self._ODL_L3VPN_ROUTE_ENTRY_ID_FIELD] = value

    def set_odl_l3vpn_vpn_id(self, value):
        self._template[self._ODL_L3VPN_VPN_ID_FIELD] = value

    def set_vpn_id(self, value):
        self._template[self._VPN_ID_FIELD] = value

    def set_vpn_instance_name(self, value):
        self._template[self._VPN_INSTANCE_NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._IPV4_FAMILY_FIELD] = self.ipv4_family.get_template(default=default)
            self._default_template[self._IPV6_FAMILY_FIELD] = self.ipv6_family.get_template(default=default)
            return self._default_template
        else:
            self._template[self._IPV4_FAMILY_FIELD] = self.ipv4_family.get_template()
            self._template[self._IPV6_FAMILY_FIELD] = self.ipv6_family.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ipv4_family_payload = self.ipv4_family.get_payload()
        if ipv4_family_payload:
            payload[self._IPV4_FAMILY_FIELD] = ipv4_family_payload
        ipv6_family_payload = self.ipv6_family.get_payload()
        if ipv6_family_payload:
            payload[self._IPV6_FAMILY_FIELD] = ipv6_family_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpn_instance(self):
        
        payload = {self._VPN_INSTANCE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpn_instance(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpn_instance(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class APPLY_LABEL(object):

    _APPLY_LABEL_FIELD = "apply-label"
    _APPLY_LABEL_MODE_FIELD = "apply-label-mode"

    def __init__(self):
        self._template = {}
        self._template[self._APPLY_LABEL_MODE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._apply_label_mode = APPLY_LABEL_MODE()

    @property
    def apply_label_mode(self):
        return self._apply_label_mode

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._APPLY_LABEL_MODE_FIELD] = self.apply_label_mode.get_template(default=default)
            return self._default_template
        else:
            self._template[self._APPLY_LABEL_MODE_FIELD] = self.apply_label_mode.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        apply_label_mode_payload = self.apply_label_mode.get_payload()
        if apply_label_mode_payload:
            payload[self._APPLY_LABEL_MODE_FIELD] = apply_label_mode_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_apply_label(self):
        
        payload = {self._APPLY_LABEL_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_apply_label(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_apply_label(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class L2VPN(object):

    _L2VPN_FIELD = "l2vpn"
    _VPLS_FIELD = "vpls"
    _EVPN_FIELD = "evpn"

    def __init__(self):
        self._template = {}
        self._template[self._VPLS_FIELD] = None
        self._template[self._EVPN_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._vpls = VPLS()
        self._evpn = EVPN()

    @property
    def vpls(self):
        return self._vpls

    @property
    def evpn(self):
        return self._evpn

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._VPLS_FIELD] = self.vpls.get_template(default=default)
            self._default_template[self._EVPN_FIELD] = self.evpn.get_template(default=default)
            return self._default_template
        else:
            self._template[self._VPLS_FIELD] = self.vpls.get_template()
            self._template[self._EVPN_FIELD] = self.evpn.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        vpls_payload = self.vpls.get_payload()
        if vpls_payload:
            payload[self._VPLS_FIELD] = vpls_payload
        evpn_payload = self.evpn.get_payload()
        if evpn_payload:
            payload[self._EVPN_FIELD] = evpn_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_l2vpn(self):
        
        payload = {self._L2VPN_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_l2vpn(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_l2vpn(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IPV4_FAMILY(object):

    _IPV4_FAMILY_FIELD = "ipv4-family"
    _L3VPNVRFPIPE_FIELD = "l3vpnVrfPipe"
    _TRAFFIC_STATISTICS_FIELD = "traffic-statistics"
    _VPNTARGETS_FIELD = "vpnTargets"
    _VPN_FRR_FIELD = "vpn-frr"
    _TUNNEL_POLICY_FIELD = "tunnel-policy"
    _IMPORTRIBS_FIELD = "importRibs"
    _EXPORT_ROUTE_POLICY_FIELD = "export-route-policy"
    _PREFIX_LIMIT_FIELD = "prefix-limit"
    _ROUTING_TABLE_LIMIT_FIELD = "routing-table-limit"
    _APPLY_LABEL_FIELD = "apply-label"
    _IMPORT_ROUTE_POLICY_FIELD = "import-route-policy"
    _L3VPNTTLMODE_FIELD = "l3vpnTtlMode"
    _ROUTE_DISTINGUISHER_FIELD = "route-distinguisher"

    def __init__(self):
        self._template = {}
        self._template[self._L3VPNVRFPIPE_FIELD] = None
        self._template[self._TRAFFIC_STATISTICS_FIELD] = None
        self._template[self._VPNTARGETS_FIELD] = None
        self._template[self._VPN_FRR_FIELD] = None
        self._template[self._TUNNEL_POLICY_FIELD] = None
        self._template[self._IMPORTRIBS_FIELD] = None
        self._template[self._EXPORT_ROUTE_POLICY_FIELD] = None
        self._template[self._PREFIX_LIMIT_FIELD] = None
        self._template[self._ROUTING_TABLE_LIMIT_FIELD] = None
        self._template[self._APPLY_LABEL_FIELD] = None
        self._template[self._IMPORT_ROUTE_POLICY_FIELD] = None
        self._template[self._L3VPNTTLMODE_FIELD] = None
        self._template[self._ROUTE_DISTINGUISHER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._l3vpnvrfpipe = L3VPNVRFPIPE()
        self._vpntargets = VPNTARGETS()
        self._importribs = IMPORTRIBS()
        self._prefix_limit = PREFIX_LIMIT()
        self._routing_table_limit = ROUTING_TABLE_LIMIT()
        self._apply_label = APPLY_LABEL()
        self._l3vpnttlmode = L3VPNTTLMODE()

    @property
    def l3vpnvrfpipe(self):
        return self._l3vpnvrfpipe

    @property
    def vpntargets(self):
        return self._vpntargets

    @property
    def importribs(self):
        return self._importribs

    @property
    def prefix_limit(self):
        return self._prefix_limit

    @property
    def routing_table_limit(self):
        return self._routing_table_limit

    @property
    def apply_label(self):
        return self._apply_label

    @property
    def l3vpnttlmode(self):
        return self._l3vpnttlmode

    def set_traffic_statistics(self, value):
        self._template[self._TRAFFIC_STATISTICS_FIELD] = value

    def set_vpn_frr(self, value):
        self._template[self._VPN_FRR_FIELD] = value

    def set_tunnel_policy(self, value):
        self._template[self._TUNNEL_POLICY_FIELD] = value

    def set_export_route_policy(self, value):
        self._template[self._EXPORT_ROUTE_POLICY_FIELD] = value

    def set_import_route_policy(self, value):
        self._template[self._IMPORT_ROUTE_POLICY_FIELD] = value

    def set_route_distinguisher(self, value):
        self._template[self._ROUTE_DISTINGUISHER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._L3VPNVRFPIPE_FIELD] = self.l3vpnvrfpipe.get_template(default=default)
            self._default_template[self._VPNTARGETS_FIELD] = self.vpntargets.get_template(default=default)
            self._default_template[self._IMPORTRIBS_FIELD] = self.importribs.get_template(default=default)
            self._default_template[self._PREFIX_LIMIT_FIELD] = self.prefix_limit.get_template(default=default)
            self._default_template[self._ROUTING_TABLE_LIMIT_FIELD] = self.routing_table_limit.get_template(default=default)
            self._default_template[self._APPLY_LABEL_FIELD] = self.apply_label.get_template(default=default)
            self._default_template[self._L3VPNTTLMODE_FIELD] = self.l3vpnttlmode.get_template(default=default)
            return self._default_template
        else:
            self._template[self._L3VPNVRFPIPE_FIELD] = self.l3vpnvrfpipe.get_template()
            self._template[self._VPNTARGETS_FIELD] = self.vpntargets.get_template()
            self._template[self._IMPORTRIBS_FIELD] = self.importribs.get_template()
            self._template[self._PREFIX_LIMIT_FIELD] = self.prefix_limit.get_template()
            self._template[self._ROUTING_TABLE_LIMIT_FIELD] = self.routing_table_limit.get_template()
            self._template[self._APPLY_LABEL_FIELD] = self.apply_label.get_template()
            self._template[self._L3VPNTTLMODE_FIELD] = self.l3vpnttlmode.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        l3vpnvrfpipe_payload = self.l3vpnvrfpipe.get_payload()
        if l3vpnvrfpipe_payload:
            payload[self._L3VPNVRFPIPE_FIELD] = l3vpnvrfpipe_payload
        vpntargets_payload = self.vpntargets.get_payload()
        if vpntargets_payload:
            payload[self._VPNTARGETS_FIELD] = vpntargets_payload
        importribs_payload = self.importribs.get_payload()
        if importribs_payload:
            payload[self._IMPORTRIBS_FIELD] = importribs_payload
        prefix_limit_payload = self.prefix_limit.get_payload()
        if prefix_limit_payload:
            payload[self._PREFIX_LIMIT_FIELD] = prefix_limit_payload
        routing_table_limit_payload = self.routing_table_limit.get_payload()
        if routing_table_limit_payload:
            payload[self._ROUTING_TABLE_LIMIT_FIELD] = routing_table_limit_payload
        apply_label_payload = self.apply_label.get_payload()
        if apply_label_payload:
            payload[self._APPLY_LABEL_FIELD] = apply_label_payload
        l3vpnttlmode_payload = self.l3vpnttlmode.get_payload()
        if l3vpnttlmode_payload:
            payload[self._L3VPNTTLMODE_FIELD] = l3vpnttlmode_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ipv4_family(self):
        
        payload = {self._IPV4_FAMILY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ipv4_family(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ipv4_family(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ADJACENCY(object):

    _ADJACENCY_FIELD = "adjacency"
    _NEXTHOPID_FIELD = "nextHopId"
    _ODL_L3VPN_NEXTHOPID_FIELD = "odl-l3vpn:nextHopId"
    _ODL_L3VPN_IP_ADDRESS_FIELD = "odl-l3vpn:ip_address"
    _MAC_ADDRESS_FIELD = "mac_address"
    _ODL_L3VPN_LABEL_FIELD = "odl-l3vpn:label"
    _LABEL_FIELD = "label"
    _IP_ADDRESS_FIELD = "ip_address"
    _ODL_L3VPN_MAC_ADDRESS_FIELD = "odl-l3vpn:mac_address"

    def __init__(self):
        self._template = {}
        self._template[self._NEXTHOPID_FIELD] = None
        self._template[self._ODL_L3VPN_NEXTHOPID_FIELD] = None
        self._template[self._ODL_L3VPN_IP_ADDRESS_FIELD] = None
        self._template[self._MAC_ADDRESS_FIELD] = None
        self._template[self._ODL_L3VPN_LABEL_FIELD] = None
        self._template[self._LABEL_FIELD] = None
        self._template[self._IP_ADDRESS_FIELD] = None
        self._template[self._ODL_L3VPN_MAC_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_nexthopid(self, value):
        self._template[self._NEXTHOPID_FIELD] = value

    def set_odl_l3vpn_nexthopid(self, value):
        self._template[self._ODL_L3VPN_NEXTHOPID_FIELD] = value

    def set_odl_l3vpn_ip_address(self, value):
        self._template[self._ODL_L3VPN_IP_ADDRESS_FIELD] = value

    def set_mac_address(self, value):
        self._template[self._MAC_ADDRESS_FIELD] = value

    def set_odl_l3vpn_label(self, value):
        self._template[self._ODL_L3VPN_LABEL_FIELD] = value

    def set_label(self, value):
        self._template[self._LABEL_FIELD] = value

    def set_ip_address(self, value):
        self._template[self._IP_ADDRESS_FIELD] = value

    def set_odl_l3vpn_mac_address(self, value):
        self._template[self._ODL_L3VPN_MAC_ADDRESS_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_adjacency(self):
        
        payload = {self._ADJACENCY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_adjacency(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_adjacency(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPNTARGETS(object):

    _VPNTARGETS_FIELD = "vpnTargets"
    _VPNTARGET_FIELD = "vpnTarget"

    def __init__(self):
        self._template = {}
        self._template[self._VPNTARGET_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._vpntarget = VPNTARGET()

    @property
    def vpntarget(self):
        return self._vpntarget

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._VPNTARGET_FIELD] = self.vpntarget.get_template(default=default)
            return self._default_template
        else:
            self._template[self._VPNTARGET_FIELD] = self.vpntarget.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        vpntarget_payload = self.vpntarget.get_payload()
        if vpntarget_payload:
            payload[self._VPNTARGET_FIELD] = vpntarget_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpntargets(self):
        
        payload = {self._VPNTARGETS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpntargets(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpntargets(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPNV6(object):

    _VPNV6_FIELD = "vpnv6"
    _UNICAST_FIELD = "unicast"
    _MULTICAST_FIELD = "multicast"

    def __init__(self):
        self._template = {}
        self._template[self._UNICAST_FIELD] = None
        self._template[self._MULTICAST_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._unicast = UNICAST()
        self._multicast = MULTICAST()

    @property
    def unicast(self):
        return self._unicast

    @property
    def multicast(self):
        return self._multicast

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._UNICAST_FIELD] = self.unicast.get_template(default=default)
            self._default_template[self._MULTICAST_FIELD] = self.multicast.get_template(default=default)
            return self._default_template
        else:
            self._template[self._UNICAST_FIELD] = self.unicast.get_template()
            self._template[self._MULTICAST_FIELD] = self.multicast.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        unicast_payload = self.unicast.get_payload()
        if unicast_payload:
            payload[self._UNICAST_FIELD] = unicast_payload
        multicast_payload = self.multicast.get_payload()
        if multicast_payload:
            payload[self._MULTICAST_FIELD] = multicast_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpnv6(self):
        
        payload = {self._VPNV6_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpnv6(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpnv6(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPNV4(object):

    _VPNV4_FIELD = "vpnv4"
    _UNICAST_FIELD = "unicast"
    _MULTICAST_FIELD = "multicast"

    def __init__(self):
        self._template = {}
        self._template[self._UNICAST_FIELD] = None
        self._template[self._MULTICAST_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._unicast = UNICAST()
        self._multicast = MULTICAST()

    @property
    def unicast(self):
        return self._unicast

    @property
    def multicast(self):
        return self._multicast

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._UNICAST_FIELD] = self.unicast.get_template(default=default)
            self._default_template[self._MULTICAST_FIELD] = self.multicast.get_template(default=default)
            return self._default_template
        else:
            self._template[self._UNICAST_FIELD] = self.unicast.get_template()
            self._template[self._MULTICAST_FIELD] = self.multicast.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        unicast_payload = self.unicast.get_payload()
        if unicast_payload:
            payload[self._UNICAST_FIELD] = unicast_payload
        multicast_payload = self.multicast.get_payload()
        if multicast_payload:
            payload[self._MULTICAST_FIELD] = multicast_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpnv4(self):
        
        payload = {self._VPNV4_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpnv4(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpnv4(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BGP_NEIGHBOR_STATISTICS(object):

    _BGP_NEIGHBOR_STATISTICS_FIELD = "bgp-neighbor-statistics"
    _NR_OUT_UPDATES_FIELD = "nr-out-updates"
    _NR_IN_UPDATES_FIELD = "nr-in-updates"

    def __init__(self):
        self._template = {}
        self._template[self._NR_OUT_UPDATES_FIELD] = None
        self._template[self._NR_IN_UPDATES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_nr_out_updates(self, value):
        self._template[self._NR_OUT_UPDATES_FIELD] = value

    def set_nr_in_updates(self, value):
        self._template[self._NR_IN_UPDATES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_neighbor_statistics(self):
        
        payload = {self._BGP_NEIGHBOR_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_neighbor_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_neighbor_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ROUTING_TABLE_LIMIT(object):

    _ROUTING_TABLE_LIMIT_FIELD = "routing-table-limit"
    _ROUTING_TABLE_LIMIT_ACTION_FIELD = "routing-table-limit-action"
    _ROUTING_TABLE_LIMIT_NUMBER_FIELD = "routing-table-limit-number"

    def __init__(self):
        self._template = {}
        self._template[self._ROUTING_TABLE_LIMIT_ACTION_FIELD] = None
        self._template[self._ROUTING_TABLE_LIMIT_NUMBER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._routing_table_limit_action = ROUTING_TABLE_LIMIT_ACTION()

    @property
    def routing_table_limit_action(self):
        return self._routing_table_limit_action

    def set_routing_table_limit_number(self, value):
        self._template[self._ROUTING_TABLE_LIMIT_NUMBER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ROUTING_TABLE_LIMIT_ACTION_FIELD] = self.routing_table_limit_action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ROUTING_TABLE_LIMIT_ACTION_FIELD] = self.routing_table_limit_action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        routing_table_limit_action_payload = self.routing_table_limit_action.get_payload()
        if routing_table_limit_action_payload:
            payload[self._ROUTING_TABLE_LIMIT_ACTION_FIELD] = routing_table_limit_action_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_routing_table_limit(self):
        
        payload = {self._ROUTING_TABLE_LIMIT_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_routing_table_limit(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_routing_table_limit(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IMPORTRIBS(object):

    _IMPORTRIBS_FIELD = "importRibs"
    _BGP_VALID_ROUTE_FIELD = "bgp-valid-route"
    _PROCESSID_FIELD = "processId"
    _PROTOCOL_FIELD = "protocol"
    _POLICYNAME_FIELD = "policyName"

    def __init__(self):
        self._template = {}
        self._template[self._BGP_VALID_ROUTE_FIELD] = None
        self._template[self._PROCESSID_FIELD] = None
        self._template[self._PROTOCOL_FIELD] = None
        self._template[self._POLICYNAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_bgp_valid_route(self, value):
        self._template[self._BGP_VALID_ROUTE_FIELD] = value

    def set_processid(self, value):
        self._template[self._PROCESSID_FIELD] = value

    def set_protocol(self, value):
        self._template[self._PROTOCOL_FIELD] = value

    def set_policyname(self, value):
        self._template[self._POLICYNAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_importribs(self):
        
        payload = {self._IMPORTRIBS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_importribs(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_importribs(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIX_LIMIT(object):

    _PREFIX_LIMIT_FIELD = "prefix-limit"
    _PREFIX_LIMIT_ACTION_FIELD = "prefix-limit-action"
    _PREFIX_LIMIT_NUMBER_FIELD = "prefix-limit-number"

    def __init__(self):
        self._template = {}
        self._template[self._PREFIX_LIMIT_ACTION_FIELD] = None
        self._template[self._PREFIX_LIMIT_NUMBER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefix_limit_action = PREFIX_LIMIT_ACTION()

    @property
    def prefix_limit_action(self):
        return self._prefix_limit_action

    def set_prefix_limit_number(self, value):
        self._template[self._PREFIX_LIMIT_NUMBER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIX_LIMIT_ACTION_FIELD] = self.prefix_limit_action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIX_LIMIT_ACTION_FIELD] = self.prefix_limit_action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefix_limit_action_payload = self.prefix_limit_action.get_payload()
        if prefix_limit_action_payload:
            payload[self._PREFIX_LIMIT_ACTION_FIELD] = prefix_limit_action_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_prefix_limit(self):
        
        payload = {self._PREFIX_LIMIT_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_prefix_limit(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_prefix_limit(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ROUTING_TABLE_LIMIT_ACTION(object):

    _ROUTING_TABLE_LIMIT_ACTION_FIELD = "routing-table-limit-action"
    _ALERT_PERCENT_VALUE_FIELD = "alert-percent-value"
    _SIMPLE_ALERT_FIELD = "simple-alert"

    def __init__(self):
        self._template = {}
        self._template[self._ALERT_PERCENT_VALUE_FIELD] = None
        self._template[self._SIMPLE_ALERT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_alert_percent_value(self, value):
        self._template[self._ALERT_PERCENT_VALUE_FIELD] = value

    def set_simple_alert(self, value):
        self._template[self._SIMPLE_ALERT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_routing_table_limit_action(self):
        
        payload = {self._ROUTING_TABLE_LIMIT_ACTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_routing_table_limit_action(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_routing_table_limit_action(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class EVPN(object):

    _EVPN_FIELD = "evpn"
    _SEND_COMMUNITY_FIELD = "send-community"
    _ADVERTISEMENT_INTERVAL_FIELD = "advertisement-interval"
    _WEIGHT_FIELD = "weight"
    _MAXIMUM_PREFIX_FIELD = "maximum-prefix"
    _NEXT_HOP_SELF_FIELD = "next-hop-self"
    _SPLIT_UPDATE_GROUP_FIELD = "split-update-group"
    _ROUTE_REFLECTOR_CLIENT_FIELD = "route-reflector-client"
    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _NEXT_HOP_UNCHANGED_FIELD = "next-hop-unchanged"
    _DETECTION_FIELD = "detection"
    _PREFIX_LIST_FIELD = "prefix-list"
    _ALLOWAS_IN_FIELD = "allowas-in"
    _SOO_FIELD = "soo"
    _ACTIVE_FIELD = "active"
    _SOFT_RECONFIGURATION_FIELD = "soft-reconfiguration"

    def __init__(self):
        self._template = {}
        self._template[self._SEND_COMMUNITY_FIELD] = None
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._MAXIMUM_PREFIX_FIELD] = None
        self._template[self._NEXT_HOP_SELF_FIELD] = None
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = None
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = None
        self._template[self._REMOVE_PRIVATE_AS_FIELD] = None
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = None
        self._template[self._DETECTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._ALLOWAS_IN_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._template[self._SOFT_RECONFIGURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._remove_private_as = REMOVE_PRIVATE_AS()
        self._detection = DETECTION()
        self._prefix_list = PREFIX_LIST()

    @property
    def remove_private_as(self):
        return self._remove_private_as

    @property
    def detection(self):
        return self._detection

    @property
    def prefix_list(self):
        return self._prefix_list

    def set_send_community(self, value):
        self._template[self._SEND_COMMUNITY_FIELD] = value

    def set_advertisement_interval(self, value):
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_maximum_prefix(self, value):
        self._template[self._MAXIMUM_PREFIX_FIELD] = value

    def set_next_hop_self(self, value):
        self._template[self._NEXT_HOP_SELF_FIELD] = value

    def set_split_update_group(self, value):
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = value

    def set_route_reflector_client(self, value):
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = value

    def set_next_hop_unchanged(self, value):
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = value

    def set_allowas_in(self, value):
        self._template[self._ALLOWAS_IN_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

    def set_soft_reconfiguration(self, value):
        self._template[self._SOFT_RECONFIGURATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template(default=default)
            self._default_template[self._DETECTION_FIELD] = self.detection.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            return self._default_template
        else:
            self._template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template()
            self._template[self._DETECTION_FIELD] = self.detection.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        remove_private_as_payload = self.remove_private_as.get_payload()
        if remove_private_as_payload:
            payload[self._REMOVE_PRIVATE_AS_FIELD] = remove_private_as_payload
        detection_payload = self.detection.get_payload()
        if detection_payload:
            payload[self._DETECTION_FIELD] = detection_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_evpn(self):
        
        payload = {self._EVPN_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_evpn(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_evpn(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BGP_NEIGHBOR(object):

    _BGP_NEIGHBOR_FIELD = "bgp-neighbor"
    _AS_NUMBER_FIELD = "as-number"
    _BGP_NEIGHBOR_STATE_FIELD = "bgp-neighbor-state"
    _AF_SPECIFIC_CONFIG_FIELD = "af-specific-config"
    _BGP_NEIGHBOR_STATISTICS_FIELD = "bgp-neighbor-statistics"
    _DEFAULT_ACTION_FIELD = "default-action"
    _PREFIX_LIST_FIELD = "prefix-list"
    _PEER_ADDRESS_TYPE_FIELD = "peer-address-type"

    def __init__(self):
        self._template = {}
        self._template[self._AS_NUMBER_FIELD] = None
        self._template[self._BGP_NEIGHBOR_STATE_FIELD] = None
        self._template[self._AF_SPECIFIC_CONFIG_FIELD] = None
        self._template[self._BGP_NEIGHBOR_STATISTICS_FIELD] = None
        self._template[self._DEFAULT_ACTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._PEER_ADDRESS_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bgp_neighbor_state = BGP_NEIGHBOR_STATE()
        self._af_specific_config = AF_SPECIFIC_CONFIG()
        self._bgp_neighbor_statistics = BGP_NEIGHBOR_STATISTICS()
        self._prefix_list = PREFIX_LIST()
        self._peer_address_type = PEER_ADDRESS_TYPE()

    @property
    def bgp_neighbor_state(self):
        return self._bgp_neighbor_state

    @property
    def af_specific_config(self):
        return self._af_specific_config

    @property
    def bgp_neighbor_statistics(self):
        return self._bgp_neighbor_statistics

    @property
    def prefix_list(self):
        return self._prefix_list

    @property
    def peer_address_type(self):
        return self._peer_address_type

    def set_as_number(self, value):
        self._template[self._AS_NUMBER_FIELD] = value

    def set_default_action(self, value):
        self._template[self._DEFAULT_ACTION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BGP_NEIGHBOR_STATE_FIELD] = self.bgp_neighbor_state.get_template(default=default)
            self._default_template[self._AF_SPECIFIC_CONFIG_FIELD] = self.af_specific_config.get_template(default=default)
            self._default_template[self._BGP_NEIGHBOR_STATISTICS_FIELD] = self.bgp_neighbor_statistics.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            self._default_template[self._PEER_ADDRESS_TYPE_FIELD] = self.peer_address_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BGP_NEIGHBOR_STATE_FIELD] = self.bgp_neighbor_state.get_template()
            self._template[self._AF_SPECIFIC_CONFIG_FIELD] = self.af_specific_config.get_template()
            self._template[self._BGP_NEIGHBOR_STATISTICS_FIELD] = self.bgp_neighbor_statistics.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            self._template[self._PEER_ADDRESS_TYPE_FIELD] = self.peer_address_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bgp_neighbor_state_payload = self.bgp_neighbor_state.get_payload()
        if bgp_neighbor_state_payload:
            payload[self._BGP_NEIGHBOR_STATE_FIELD] = bgp_neighbor_state_payload
        af_specific_config_payload = self.af_specific_config.get_payload()
        if af_specific_config_payload:
            payload[self._AF_SPECIFIC_CONFIG_FIELD] = af_specific_config_payload
        bgp_neighbor_statistics_payload = self.bgp_neighbor_statistics.get_payload()
        if bgp_neighbor_statistics_payload:
            payload[self._BGP_NEIGHBOR_STATISTICS_FIELD] = bgp_neighbor_statistics_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        peer_address_type_payload = self.peer_address_type.get_payload()
        if peer_address_type_payload:
            payload[self._PEER_ADDRESS_TYPE_FIELD] = peer_address_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_neighbor(self):
        
        payload = {self._BGP_NEIGHBOR_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_neighbor(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_neighbor(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class UNICAST(object):

    _UNICAST_FIELD = "unicast"
    _SEND_COMMUNITY_FIELD = "send-community"
    _ADVERTISEMENT_INTERVAL_FIELD = "advertisement-interval"
    _SOO_FIELD = "soo"
    _WEIGHT_FIELD = "weight"
    _MAXIMUM_PREFIX_FIELD = "maximum-prefix"
    _NEXT_HOP_SELF_FIELD = "next-hop-self"
    _SPLIT_UPDATE_GROUP_FIELD = "split-update-group"
    _DEFAULT_ORIGINATE_FIELD = "default-originate"
    _ROUTE_REFLECTOR_CLIENT_FIELD = "route-reflector-client"
    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _NEXT_HOP_UNCHANGED_FIELD = "next-hop-unchanged"
    _DETECTION_FIELD = "detection"
    _PREFIX_LIST_FIELD = "prefix-list"
    _ALLOWAS_IN_FIELD = "allowas-in"
    _PROPAGATE_DMZLINK_BW_FIELD = "propagate-dmzlink-bw"
    _ACTIVE_FIELD = "active"
    _SOFT_RECONFIGURATION_FIELD = "soft-reconfiguration"

    def __init__(self):
        self._template = {}
        self._template[self._SEND_COMMUNITY_FIELD] = None
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._MAXIMUM_PREFIX_FIELD] = None
        self._template[self._NEXT_HOP_SELF_FIELD] = None
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = None
        self._template[self._DEFAULT_ORIGINATE_FIELD] = None
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = None
        self._template[self._REMOVE_PRIVATE_AS_FIELD] = None
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = None
        self._template[self._DETECTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._ALLOWAS_IN_FIELD] = None
        self._template[self._PROPAGATE_DMZLINK_BW_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._template[self._SOFT_RECONFIGURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._default_originate = DEFAULT_ORIGINATE()
        self._remove_private_as = REMOVE_PRIVATE_AS()
        self._detection = DETECTION()
        self._prefix_list = PREFIX_LIST()

    @property
    def default_originate(self):
        return self._default_originate

    @property
    def remove_private_as(self):
        return self._remove_private_as

    @property
    def detection(self):
        return self._detection

    @property
    def prefix_list(self):
        return self._prefix_list

    def set_send_community(self, value):
        self._template[self._SEND_COMMUNITY_FIELD] = value

    def set_advertisement_interval(self, value):
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_maximum_prefix(self, value):
        self._template[self._MAXIMUM_PREFIX_FIELD] = value

    def set_next_hop_self(self, value):
        self._template[self._NEXT_HOP_SELF_FIELD] = value

    def set_split_update_group(self, value):
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = value

    def set_route_reflector_client(self, value):
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = value

    def set_next_hop_unchanged(self, value):
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = value

    def set_allowas_in(self, value):
        self._template[self._ALLOWAS_IN_FIELD] = value

    def set_propagate_dmzlink_bw(self, value):
        self._template[self._PROPAGATE_DMZLINK_BW_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

    def set_soft_reconfiguration(self, value):
        self._template[self._SOFT_RECONFIGURATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._DEFAULT_ORIGINATE_FIELD] = self.default_originate.get_template(default=default)
            self._default_template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template(default=default)
            self._default_template[self._DETECTION_FIELD] = self.detection.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            return self._default_template
        else:
            self._template[self._DEFAULT_ORIGINATE_FIELD] = self.default_originate.get_template()
            self._template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template()
            self._template[self._DETECTION_FIELD] = self.detection.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        default_originate_payload = self.default_originate.get_payload()
        if default_originate_payload:
            payload[self._DEFAULT_ORIGINATE_FIELD] = default_originate_payload
        remove_private_as_payload = self.remove_private_as.get_payload()
        if remove_private_as_payload:
            payload[self._REMOVE_PRIVATE_AS_FIELD] = remove_private_as_payload
        detection_payload = self.detection.get_payload()
        if detection_payload:
            payload[self._DETECTION_FIELD] = detection_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_unicast(self):
        
        payload = {self._UNICAST_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_unicast(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_unicast(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIX_FILTER(object):

    _PREFIX_FILTER_FIELD = "prefix-filter"
    _ACTION_FIELD = "action"
    _STATISTICS_FIELD = "statistics"
    _IP_ADDRESS_GROUP_FIELD = "ip-address-group"

    def __init__(self):
        self._template = {}
        self._template[self._ACTION_FIELD] = None
        self._template[self._STATISTICS_FIELD] = None
        self._template[self._IP_ADDRESS_GROUP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._action = ACTION()
        self._statistics = STATISTICS()
        self._ip_address_group = IP_ADDRESS_GROUP()

    @property
    def action(self):
        return self._action

    @property
    def statistics(self):
        return self._statistics

    @property
    def ip_address_group(self):
        return self._ip_address_group

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ACTION_FIELD] = self.action.get_template(default=default)
            self._default_template[self._STATISTICS_FIELD] = self.statistics.get_template(default=default)
            self._default_template[self._IP_ADDRESS_GROUP_FIELD] = self.ip_address_group.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ACTION_FIELD] = self.action.get_template()
            self._template[self._STATISTICS_FIELD] = self.statistics.get_template()
            self._template[self._IP_ADDRESS_GROUP_FIELD] = self.ip_address_group.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        action_payload = self.action.get_payload()
        if action_payload:
            payload[self._ACTION_FIELD] = action_payload
        statistics_payload = self.statistics.get_payload()
        if statistics_payload:
            payload[self._STATISTICS_FIELD] = statistics_payload
        ip_address_group_payload = self.ip_address_group.get_payload()
        if ip_address_group_payload:
            payload[self._IP_ADDRESS_GROUP_FIELD] = ip_address_group_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_prefix_filter(self):
        
        payload = {self._PREFIX_FILTER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_prefix_filter(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_prefix_filter(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class L3VPNVRFPIPE(object):

    _L3VPNVRFPIPE_FIELD = "l3vpnVrfPipe"
    _COLOR_FIELD = "color"
    _SERVICECLASS_FIELD = "serviceClass"
    _DSNAME_FIELD = "dsName"
    _PIPEMODE_FIELD = "pipeMode"

    def __init__(self):
        self._template = {}
        self._template[self._COLOR_FIELD] = None
        self._template[self._SERVICECLASS_FIELD] = None
        self._template[self._DSNAME_FIELD] = None
        self._template[self._PIPEMODE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_color(self, value):
        self._template[self._COLOR_FIELD] = value

    def set_serviceclass(self, value):
        self._template[self._SERVICECLASS_FIELD] = value

    def set_dsname(self, value):
        self._template[self._DSNAME_FIELD] = value

    def set_pipemode(self, value):
        self._template[self._PIPEMODE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_l3vpnvrfpipe(self):
        
        payload = {self._L3VPNVRFPIPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_l3vpnvrfpipe(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_l3vpnvrfpipe(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class L3VPNTTLMODE(object):

    _L3VPNTTLMODE_FIELD = "l3vpnTtlMode"
    _TTLMODE_FIELD = "ttlMode"

    def __init__(self):
        self._template = {}
        self._template[self._TTLMODE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ttlmode(self, value):
        self._template[self._TTLMODE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_l3vpnttlmode(self):
        
        payload = {self._L3VPNTTLMODE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_l3vpnttlmode(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_l3vpnttlmode(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class NSAP(object):

    _NSAP_FIELD = "nsap"
    _UNICAST_FIELD = "unicast"

    def __init__(self):
        self._template = {}
        self._template[self._UNICAST_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._unicast = UNICAST()

    @property
    def unicast(self):
        return self._unicast

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._UNICAST_FIELD] = self.unicast.get_template(default=default)
            return self._default_template
        else:
            self._template[self._UNICAST_FIELD] = self.unicast.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        unicast_payload = self.unicast.get_payload()
        if unicast_payload:
            payload[self._UNICAST_FIELD] = unicast_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_nsap(self):
        
        payload = {self._NSAP_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_nsap(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_nsap(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class AF_SPECIFIC_CONFIG(object):

    _AF_SPECIFIC_CONFIG_FIELD = "af-specific-config"
    _VPNV6_FIELD = "vpnv6"
    _NSAP_FIELD = "nsap"
    _VPNV4_FIELD = "vpnv4"
    _L2VPN_FIELD = "l2vpn"
    _IPV4_FIELD = "ipv4"
    _IPV6_FIELD = "ipv6"
    _RTFILTER_FIELD = "rtfilter"

    def __init__(self):
        self._template = {}
        self._template[self._VPNV6_FIELD] = None
        self._template[self._NSAP_FIELD] = None
        self._template[self._VPNV4_FIELD] = None
        self._template[self._L2VPN_FIELD] = None
        self._template[self._IPV4_FIELD] = None
        self._template[self._IPV6_FIELD] = None
        self._template[self._RTFILTER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._vpnv6 = VPNV6()
        self._nsap = NSAP()
        self._vpnv4 = VPNV4()
        self._l2vpn = L2VPN()
        self._ipv4 = IPV4()
        self._ipv6 = IPV6()
        self._rtfilter = RTFILTER()

    @property
    def vpnv6(self):
        return self._vpnv6

    @property
    def nsap(self):
        return self._nsap

    @property
    def vpnv4(self):
        return self._vpnv4

    @property
    def l2vpn(self):
        return self._l2vpn

    @property
    def ipv4(self):
        return self._ipv4

    @property
    def ipv6(self):
        return self._ipv6

    @property
    def rtfilter(self):
        return self._rtfilter

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._VPNV6_FIELD] = self.vpnv6.get_template(default=default)
            self._default_template[self._NSAP_FIELD] = self.nsap.get_template(default=default)
            self._default_template[self._VPNV4_FIELD] = self.vpnv4.get_template(default=default)
            self._default_template[self._L2VPN_FIELD] = self.l2vpn.get_template(default=default)
            self._default_template[self._IPV4_FIELD] = self.ipv4.get_template(default=default)
            self._default_template[self._IPV6_FIELD] = self.ipv6.get_template(default=default)
            self._default_template[self._RTFILTER_FIELD] = self.rtfilter.get_template(default=default)
            return self._default_template
        else:
            self._template[self._VPNV6_FIELD] = self.vpnv6.get_template()
            self._template[self._NSAP_FIELD] = self.nsap.get_template()
            self._template[self._VPNV4_FIELD] = self.vpnv4.get_template()
            self._template[self._L2VPN_FIELD] = self.l2vpn.get_template()
            self._template[self._IPV4_FIELD] = self.ipv4.get_template()
            self._template[self._IPV6_FIELD] = self.ipv6.get_template()
            self._template[self._RTFILTER_FIELD] = self.rtfilter.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        vpnv6_payload = self.vpnv6.get_payload()
        if vpnv6_payload:
            payload[self._VPNV6_FIELD] = vpnv6_payload
        nsap_payload = self.nsap.get_payload()
        if nsap_payload:
            payload[self._NSAP_FIELD] = nsap_payload
        vpnv4_payload = self.vpnv4.get_payload()
        if vpnv4_payload:
            payload[self._VPNV4_FIELD] = vpnv4_payload
        l2vpn_payload = self.l2vpn.get_payload()
        if l2vpn_payload:
            payload[self._L2VPN_FIELD] = l2vpn_payload
        ipv4_payload = self.ipv4.get_payload()
        if ipv4_payload:
            payload[self._IPV4_FIELD] = ipv4_payload
        ipv6_payload = self.ipv6.get_payload()
        if ipv6_payload:
            payload[self._IPV6_FIELD] = ipv6_payload
        rtfilter_payload = self.rtfilter.get_payload()
        if rtfilter_payload:
            payload[self._RTFILTER_FIELD] = rtfilter_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_af_specific_config(self):
        
        payload = {self._AF_SPECIFIC_CONFIG_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_af_specific_config(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_af_specific_config(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPNTARGET(object):

    _VPNTARGET_FIELD = "vpnTarget"
    _VRFRTTYPE_FIELD = "vrfRTType"
    _VRFRTVALUE_FIELD = "vrfRTValue"

    def __init__(self):
        self._template = {}
        self._template[self._VRFRTTYPE_FIELD] = None
        self._template[self._VRFRTVALUE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_vrfrttype(self, value):
        self._template[self._VRFRTTYPE_FIELD] = value

    def set_vrfrtvalue(self, value):
        self._template[self._VRFRTVALUE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpntarget(self):
        
        payload = {self._VPNTARGET_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpntarget(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpntarget(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MULTICAST(object):

    _MULTICAST_FIELD = "multicast"
    _SEND_COMMUNITY_FIELD = "send-community"
    _ADVERTISEMENT_INTERVAL_FIELD = "advertisement-interval"
    _SOO_FIELD = "soo"
    _WEIGHT_FIELD = "weight"
    _MAXIMUM_PREFIX_FIELD = "maximum-prefix"
    _NEXT_HOP_SELF_FIELD = "next-hop-self"
    _SPLIT_UPDATE_GROUP_FIELD = "split-update-group"
    _DEFAULT_ORIGINATE_FIELD = "default-originate"
    _ROUTE_REFLECTOR_CLIENT_FIELD = "route-reflector-client"
    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _NEXT_HOP_UNCHANGED_FIELD = "next-hop-unchanged"
    _DETECTION_FIELD = "detection"
    _PREFIX_LIST_FIELD = "prefix-list"
    _ALLOWAS_IN_FIELD = "allowas-in"
    _PROPAGATE_DMZLINK_BW_FIELD = "propagate-dmzlink-bw"
    _ACTIVE_FIELD = "active"
    _SOFT_RECONFIGURATION_FIELD = "soft-reconfiguration"

    def __init__(self):
        self._template = {}
        self._template[self._SEND_COMMUNITY_FIELD] = None
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._MAXIMUM_PREFIX_FIELD] = None
        self._template[self._NEXT_HOP_SELF_FIELD] = None
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = None
        self._template[self._DEFAULT_ORIGINATE_FIELD] = None
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = None
        self._template[self._REMOVE_PRIVATE_AS_FIELD] = None
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = None
        self._template[self._DETECTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._ALLOWAS_IN_FIELD] = None
        self._template[self._PROPAGATE_DMZLINK_BW_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._template[self._SOFT_RECONFIGURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._default_originate = DEFAULT_ORIGINATE()
        self._remove_private_as = REMOVE_PRIVATE_AS()
        self._detection = DETECTION()
        self._prefix_list = PREFIX_LIST()

    @property
    def default_originate(self):
        return self._default_originate

    @property
    def remove_private_as(self):
        return self._remove_private_as

    @property
    def detection(self):
        return self._detection

    @property
    def prefix_list(self):
        return self._prefix_list

    def set_send_community(self, value):
        self._template[self._SEND_COMMUNITY_FIELD] = value

    def set_advertisement_interval(self, value):
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_maximum_prefix(self, value):
        self._template[self._MAXIMUM_PREFIX_FIELD] = value

    def set_next_hop_self(self, value):
        self._template[self._NEXT_HOP_SELF_FIELD] = value

    def set_split_update_group(self, value):
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = value

    def set_route_reflector_client(self, value):
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = value

    def set_next_hop_unchanged(self, value):
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = value

    def set_allowas_in(self, value):
        self._template[self._ALLOWAS_IN_FIELD] = value

    def set_propagate_dmzlink_bw(self, value):
        self._template[self._PROPAGATE_DMZLINK_BW_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

    def set_soft_reconfiguration(self, value):
        self._template[self._SOFT_RECONFIGURATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._DEFAULT_ORIGINATE_FIELD] = self.default_originate.get_template(default=default)
            self._default_template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template(default=default)
            self._default_template[self._DETECTION_FIELD] = self.detection.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            return self._default_template
        else:
            self._template[self._DEFAULT_ORIGINATE_FIELD] = self.default_originate.get_template()
            self._template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template()
            self._template[self._DETECTION_FIELD] = self.detection.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        default_originate_payload = self.default_originate.get_payload()
        if default_originate_payload:
            payload[self._DEFAULT_ORIGINATE_FIELD] = default_originate_payload
        remove_private_as_payload = self.remove_private_as.get_payload()
        if remove_private_as_payload:
            payload[self._REMOVE_PRIVATE_AS_FIELD] = remove_private_as_payload
        detection_payload = self.detection.get_payload()
        if detection_payload:
            payload[self._DETECTION_FIELD] = detection_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_multicast(self):
        
        payload = {self._MULTICAST_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_multicast(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_multicast(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IP_ADDRESS_GROUP(object):

    _IP_ADDRESS_GROUP_FIELD = "ip-address-group"
    _UPPER_FIELD = "upper"
    _IP_HOST_ADDRESS_FIELD = "ip-host-address"
    _PREFIX_FIELD = "prefix"
    _LOWER_FIELD = "lower"
    _IP_ADDRESS_FIELD = "ip-address"

    def __init__(self):
        self._template = {}
        self._template[self._UPPER_FIELD] = None
        self._template[self._IP_HOST_ADDRESS_FIELD] = None
        self._template[self._PREFIX_FIELD] = None
        self._template[self._LOWER_FIELD] = None
        self._template[self._IP_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefix = PREFIX()

    @property
    def prefix(self):
        return self._prefix

    def set_upper(self, value):
        self._template[self._UPPER_FIELD] = value

    def set_ip_host_address(self, value):
        self._template[self._IP_HOST_ADDRESS_FIELD] = value

    def set_lower(self, value):
        self._template[self._LOWER_FIELD] = value

    def set_ip_address(self, value):
        self._template[self._IP_ADDRESS_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIX_FIELD] = self.prefix.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIX_FIELD] = self.prefix.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefix_payload = self.prefix.get_payload()
        if prefix_payload:
            payload[self._PREFIX_FIELD] = prefix_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ip_address_group(self):
        
        payload = {self._IP_ADDRESS_GROUP_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ip_address_group(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ip_address_group(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPN_INTERFACE(object):

    _VPN_INTERFACE_FIELD = "vpn-interface"
    _VPN_INSTANCE_NAME_FIELD = "vpn-instance-name"
    _ODL_L3VPN_ADJACENCY_FIELD = "odl-l3vpn:adjacency"
    _ADJACENCY_FIELD = "adjacency"
    _NAME_FIELD = "name"

    def __init__(self):
        self._template = {}
        self._template[self._VPN_INSTANCE_NAME_FIELD] = None
        self._template[self._ODL_L3VPN_ADJACENCY_FIELD] = None
        self._template[self._ADJACENCY_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._adjacency = ADJACENCY()

    @property
    def adjacency(self):
        return self._adjacency

    def set_vpn_instance_name(self, value):
        self._template[self._VPN_INSTANCE_NAME_FIELD] = value

    def set_odl_l3vpn_adjacency(self, value):
        self._template[self._ODL_L3VPN_ADJACENCY_FIELD] = value

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ADJACENCY_FIELD] = self.adjacency.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ADJACENCY_FIELD] = self.adjacency.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        adjacency_payload = self.adjacency.get_payload()
        if adjacency_payload:
            payload[self._ADJACENCY_FIELD] = adjacency_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpn_interface(self):
        
        payload = {self._VPN_INTERFACE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpn_interface(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpn_interface(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ACTION(object):

    _ACTION_FIELD = "action"
    _HW_PATH_ACTION_FIELD = "hw-path-action"
    _SET_NW_DST_ACTION_FIELD = "set-nw-dst-action"
    _SET_TP_DST_ACTION_FIELD = "set-tp-dst-action"
    _SET_VLAN_CFI_ACTION_FIELD = "set-vlan-cfi-action"
    _SW_PATH_ACTION_FIELD = "sw-path-action"
    _GROUP_ACTION_FIELD = "group-action"
    _DROP_ACTION_FIELD = "drop-action"
    _STRIP_VLAN_ACTION_FIELD = "strip-vlan-action"
    _FLOOD_ALL_ACTION_FIELD = "flood-all-action"
    _SET_VLAN_PCP_ACTION_FIELD = "set-vlan-pcp-action"
    _PUSH_VLAN_ACTION_FIELD = "push-vlan-action"
    _FLOOD_ACTION_FIELD = "flood-action"
    _SET_QUEUE_ACTION_FIELD = "set-queue-action"
    _COPY_TTL_OUT_FIELD = "copy-ttl-out"
    _PUSH_MPLS_ACTION_FIELD = "push-mpls-action"
    _DEC_MPLS_TTL_FIELD = "dec-mpls-ttl"
    _POP_VLAN_ACTION_FIELD = "pop-vlan-action"
    _SET_DL_TYPE_ACTION_FIELD = "set-dl-type-action"
    _CONTROLLER_ACTION_FIELD = "controller-action"
    _SET_NW_TTL_ACTION_FIELD = "set-nw-ttl-action"
    _PUSH_PBB_ACTION_FIELD = "push-pbb-action"
    _DEC_NW_TTL_FIELD = "dec-nw-ttl"
    _LOOPBACK_ACTION_FIELD = "loopback-action"
    _SET_DL_DST_ACTION_FIELD = "set-dl-dst-action"
    _COPY_TTL_IN_FIELD = "copy-ttl-in"
    _OUTPUT_ACTION_FIELD = "output-action"
    _SET_NW_TOS_ACTION_FIELD = "set-nw-tos-action"
    _SET_VLAN_ID_ACTION_FIELD = "set-vlan-id-action"
    _SET_DL_SRC_ACTION_FIELD = "set-dl-src-action"
    _SET_TP_SRC_ACTION_FIELD = "set-tp-src-action"
    _SET_NEXT_HOP_ACTION_FIELD = "set-next-hop-action"
    _POP_MPLS_ACTION_FIELD = "pop-mpls-action"
    _POP_PBB_ACTION_FIELD = "pop-pbb-action"
    _SET_FIELD_FIELD = "set-field"
    _SET_NW_SRC_ACTION_FIELD = "set-nw-src-action"
    _SET_MPLS_TTL_ACTION_FIELD = "set-mpls-ttl-action"

    def __init__(self):
        self._template = {}
        self._template[self._HW_PATH_ACTION_FIELD] = None
        self._template[self._SET_NW_DST_ACTION_FIELD] = None
        self._template[self._SET_TP_DST_ACTION_FIELD] = None
        self._template[self._SET_VLAN_CFI_ACTION_FIELD] = None
        self._template[self._SW_PATH_ACTION_FIELD] = None
        self._template[self._GROUP_ACTION_FIELD] = None
        self._template[self._DROP_ACTION_FIELD] = None
        self._template[self._STRIP_VLAN_ACTION_FIELD] = None
        self._template[self._FLOOD_ALL_ACTION_FIELD] = None
        self._template[self._SET_VLAN_PCP_ACTION_FIELD] = None
        self._template[self._PUSH_VLAN_ACTION_FIELD] = None
        self._template[self._FLOOD_ACTION_FIELD] = None
        self._template[self._SET_QUEUE_ACTION_FIELD] = None
        self._template[self._COPY_TTL_OUT_FIELD] = None
        self._template[self._PUSH_MPLS_ACTION_FIELD] = None
        self._template[self._DEC_MPLS_TTL_FIELD] = None
        self._template[self._POP_VLAN_ACTION_FIELD] = None
        self._template[self._SET_DL_TYPE_ACTION_FIELD] = None
        self._template[self._CONTROLLER_ACTION_FIELD] = None
        self._template[self._SET_NW_TTL_ACTION_FIELD] = None
        self._template[self._PUSH_PBB_ACTION_FIELD] = None
        self._template[self._DEC_NW_TTL_FIELD] = None
        self._template[self._LOOPBACK_ACTION_FIELD] = None
        self._template[self._SET_DL_DST_ACTION_FIELD] = None
        self._template[self._COPY_TTL_IN_FIELD] = None
        self._template[self._OUTPUT_ACTION_FIELD] = None
        self._template[self._SET_NW_TOS_ACTION_FIELD] = None
        self._template[self._SET_VLAN_ID_ACTION_FIELD] = None
        self._template[self._SET_DL_SRC_ACTION_FIELD] = None
        self._template[self._SET_TP_SRC_ACTION_FIELD] = None
        self._template[self._SET_NEXT_HOP_ACTION_FIELD] = None
        self._template[self._POP_MPLS_ACTION_FIELD] = None
        self._template[self._POP_PBB_ACTION_FIELD] = None
        self._template[self._SET_FIELD_FIELD] = None
        self._template[self._SET_NW_SRC_ACTION_FIELD] = None
        self._template[self._SET_MPLS_TTL_ACTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_hw_path_action(self, value):
        self._template[self._HW_PATH_ACTION_FIELD] = value

    def set_set_nw_dst_action(self, value):
        self._template[self._SET_NW_DST_ACTION_FIELD] = value

    def set_set_tp_dst_action(self, value):
        self._template[self._SET_TP_DST_ACTION_FIELD] = value

    def set_set_vlan_cfi_action(self, value):
        self._template[self._SET_VLAN_CFI_ACTION_FIELD] = value

    def set_sw_path_action(self, value):
        self._template[self._SW_PATH_ACTION_FIELD] = value

    def set_group_action(self, value):
        self._template[self._GROUP_ACTION_FIELD] = value

    def set_drop_action(self, value):
        self._template[self._DROP_ACTION_FIELD] = value

    def set_strip_vlan_action(self, value):
        self._template[self._STRIP_VLAN_ACTION_FIELD] = value

    def set_flood_all_action(self, value):
        self._template[self._FLOOD_ALL_ACTION_FIELD] = value

    def set_set_vlan_pcp_action(self, value):
        self._template[self._SET_VLAN_PCP_ACTION_FIELD] = value

    def set_push_vlan_action(self, value):
        self._template[self._PUSH_VLAN_ACTION_FIELD] = value

    def set_flood_action(self, value):
        self._template[self._FLOOD_ACTION_FIELD] = value

    def set_set_queue_action(self, value):
        self._template[self._SET_QUEUE_ACTION_FIELD] = value

    def set_copy_ttl_out(self, value):
        self._template[self._COPY_TTL_OUT_FIELD] = value

    def set_push_mpls_action(self, value):
        self._template[self._PUSH_MPLS_ACTION_FIELD] = value

    def set_dec_mpls_ttl(self, value):
        self._template[self._DEC_MPLS_TTL_FIELD] = value

    def set_pop_vlan_action(self, value):
        self._template[self._POP_VLAN_ACTION_FIELD] = value

    def set_set_dl_type_action(self, value):
        self._template[self._SET_DL_TYPE_ACTION_FIELD] = value

    def set_controller_action(self, value):
        self._template[self._CONTROLLER_ACTION_FIELD] = value

    def set_set_nw_ttl_action(self, value):
        self._template[self._SET_NW_TTL_ACTION_FIELD] = value

    def set_push_pbb_action(self, value):
        self._template[self._PUSH_PBB_ACTION_FIELD] = value

    def set_dec_nw_ttl(self, value):
        self._template[self._DEC_NW_TTL_FIELD] = value

    def set_loopback_action(self, value):
        self._template[self._LOOPBACK_ACTION_FIELD] = value

    def set_set_dl_dst_action(self, value):
        self._template[self._SET_DL_DST_ACTION_FIELD] = value

    def set_copy_ttl_in(self, value):
        self._template[self._COPY_TTL_IN_FIELD] = value

    def set_output_action(self, value):
        self._template[self._OUTPUT_ACTION_FIELD] = value

    def set_set_nw_tos_action(self, value):
        self._template[self._SET_NW_TOS_ACTION_FIELD] = value

    def set_set_vlan_id_action(self, value):
        self._template[self._SET_VLAN_ID_ACTION_FIELD] = value

    def set_set_dl_src_action(self, value):
        self._template[self._SET_DL_SRC_ACTION_FIELD] = value

    def set_set_tp_src_action(self, value):
        self._template[self._SET_TP_SRC_ACTION_FIELD] = value

    def set_set_next_hop_action(self, value):
        self._template[self._SET_NEXT_HOP_ACTION_FIELD] = value

    def set_pop_mpls_action(self, value):
        self._template[self._POP_MPLS_ACTION_FIELD] = value

    def set_pop_pbb_action(self, value):
        self._template[self._POP_PBB_ACTION_FIELD] = value

    def set_set_field(self, value):
        self._template[self._SET_FIELD_FIELD] = value

    def set_set_nw_src_action(self, value):
        self._template[self._SET_NW_SRC_ACTION_FIELD] = value

    def set_set_mpls_ttl_action(self, value):
        self._template[self._SET_MPLS_TTL_ACTION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_action(self):
        
        payload = {self._ACTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_action(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_action(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VPLS(object):

    _VPLS_FIELD = "vpls"
    _SEND_COMMUNITY_FIELD = "send-community"
    _ADVERTISEMENT_INTERVAL_FIELD = "advertisement-interval"
    _WEIGHT_FIELD = "weight"
    _MAXIMUM_PREFIX_FIELD = "maximum-prefix"
    _NEXT_HOP_SELF_FIELD = "next-hop-self"
    _SPLIT_UPDATE_GROUP_FIELD = "split-update-group"
    _ROUTE_REFLECTOR_CLIENT_FIELD = "route-reflector-client"
    _REMOVE_PRIVATE_AS_FIELD = "remove-private-as"
    _NEXT_HOP_UNCHANGED_FIELD = "next-hop-unchanged"
    _DETECTION_FIELD = "detection"
    _PREFIX_LIST_FIELD = "prefix-list"
    _ALLOWAS_IN_FIELD = "allowas-in"
    _SOO_FIELD = "soo"
    _ACTIVE_FIELD = "active"
    _SOFT_RECONFIGURATION_FIELD = "soft-reconfiguration"

    def __init__(self):
        self._template = {}
        self._template[self._SEND_COMMUNITY_FIELD] = None
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._MAXIMUM_PREFIX_FIELD] = None
        self._template[self._NEXT_HOP_SELF_FIELD] = None
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = None
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = None
        self._template[self._REMOVE_PRIVATE_AS_FIELD] = None
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = None
        self._template[self._DETECTION_FIELD] = None
        self._template[self._PREFIX_LIST_FIELD] = None
        self._template[self._ALLOWAS_IN_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._template[self._SOFT_RECONFIGURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._remove_private_as = REMOVE_PRIVATE_AS()
        self._detection = DETECTION()
        self._prefix_list = PREFIX_LIST()

    @property
    def remove_private_as(self):
        return self._remove_private_as

    @property
    def detection(self):
        return self._detection

    @property
    def prefix_list(self):
        return self._prefix_list

    def set_send_community(self, value):
        self._template[self._SEND_COMMUNITY_FIELD] = value

    def set_advertisement_interval(self, value):
        self._template[self._ADVERTISEMENT_INTERVAL_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_maximum_prefix(self, value):
        self._template[self._MAXIMUM_PREFIX_FIELD] = value

    def set_next_hop_self(self, value):
        self._template[self._NEXT_HOP_SELF_FIELD] = value

    def set_split_update_group(self, value):
        self._template[self._SPLIT_UPDATE_GROUP_FIELD] = value

    def set_route_reflector_client(self, value):
        self._template[self._ROUTE_REFLECTOR_CLIENT_FIELD] = value

    def set_next_hop_unchanged(self, value):
        self._template[self._NEXT_HOP_UNCHANGED_FIELD] = value

    def set_allowas_in(self, value):
        self._template[self._ALLOWAS_IN_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

    def set_soft_reconfiguration(self, value):
        self._template[self._SOFT_RECONFIGURATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template(default=default)
            self._default_template[self._DETECTION_FIELD] = self.detection.get_template(default=default)
            self._default_template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template(default=default)
            return self._default_template
        else:
            self._template[self._REMOVE_PRIVATE_AS_FIELD] = self.remove_private_as.get_template()
            self._template[self._DETECTION_FIELD] = self.detection.get_template()
            self._template[self._PREFIX_LIST_FIELD] = self.prefix_list.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        remove_private_as_payload = self.remove_private_as.get_payload()
        if remove_private_as_payload:
            payload[self._REMOVE_PRIVATE_AS_FIELD] = remove_private_as_payload
        detection_payload = self.detection.get_payload()
        if detection_payload:
            payload[self._DETECTION_FIELD] = detection_payload
        prefix_list_payload = self.prefix_list.get_payload()
        if prefix_list_payload:
            payload[self._PREFIX_LIST_FIELD] = prefix_list_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vpls(self):
        
        payload = {self._VPLS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vpls(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vpls(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class APPLY_LABEL_MODE(object):

    _APPLY_LABEL_MODE_FIELD = "apply-label-mode"
    _APPLY_LABEL_PER_INSTANCE_FIELD = "apply-label-per-instance"
    _APPLY_LABEL_PER_ROUTE_FIELD = "apply-label-per-route"

    def __init__(self):
        self._template = {}
        self._template[self._APPLY_LABEL_PER_INSTANCE_FIELD] = None
        self._template[self._APPLY_LABEL_PER_ROUTE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_apply_label_per_instance(self, value):
        self._template[self._APPLY_LABEL_PER_INSTANCE_FIELD] = value

    def set_apply_label_per_route(self, value):
        self._template[self._APPLY_LABEL_PER_ROUTE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_apply_label_mode(self):
        
        payload = {self._APPLY_LABEL_MODE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_apply_label_mode(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_apply_label_mode(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIX_LIMIT_ACTION(object):

    _PREFIX_LIMIT_ACTION_FIELD = "prefix-limit-action"
    _ALERT_PERCENT_VALUE_FIELD = "alert-percent-value"
    _ROUTE_UNCHANGED_FIELD = "route-unchanged"
    _SIMPLE_ALERT_FIELD = "simple-alert"

    def __init__(self):
        self._template = {}
        self._template[self._ALERT_PERCENT_VALUE_FIELD] = None
        self._template[self._ROUTE_UNCHANGED_FIELD] = None
        self._template[self._SIMPLE_ALERT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_alert_percent_value(self, value):
        self._template[self._ALERT_PERCENT_VALUE_FIELD] = value

    def set_route_unchanged(self, value):
        self._template[self._ROUTE_UNCHANGED_FIELD] = value

    def set_simple_alert(self, value):
        self._template[self._SIMPLE_ALERT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_prefix_limit_action(self):
        
        payload = {self._PREFIX_LIMIT_ACTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_prefix_limit_action(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_prefix_limit_action(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

