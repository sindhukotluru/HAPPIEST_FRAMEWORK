from copy import deepcopy
import json
from SDN.odl.interface.restconf import rest_session



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

