from copy import deepcopy
import json
from SDN.odl.interface.restconf import rest_session



class BGP_AF_IPV4_VPN_INSTANCE(object):

    _BGP_AF_IPV4_VPN_INSTANCE_FIELD = "bgp-af-ipv4-vpn-instance"
    _ROUTER_ID_FIELD = "router-id"
    _L3VPN_ROUTER_ID_FIELD = "l3vpn:router-id"
    _AUTO_FRR_FIELD = "auto-frr"
    _L3VPN_VPN_INSTANCE_NAME_FIELD = "l3vpn:vpn-instance-name"
    _BGPPEERS_FIELD = "bgpPeers"
    _VPN_INSTANCE_NAME_FIELD = "vpn-instance-name"
    _L3VPN_BGPPEERS_FIELD = "l3vpn:bgpPeers"
    _L3VPN_AUTO_FRR_FIELD = "l3vpn:auto-frr"

    def __init__(self):
        self._template = {}
        self._template[self._ROUTER_ID_FIELD] = None
        self._template[self._L3VPN_ROUTER_ID_FIELD] = None
        self._template[self._AUTO_FRR_FIELD] = None
        self._template[self._L3VPN_VPN_INSTANCE_NAME_FIELD] = None
        self._template[self._BGPPEERS_FIELD] = None
        self._template[self._VPN_INSTANCE_NAME_FIELD] = None
        self._template[self._L3VPN_BGPPEERS_FIELD] = None
        self._template[self._L3VPN_AUTO_FRR_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._router_id = ROUTER_ID()
        self._bgppeers = BGPPEERS()

    @property
    def router_id(self):
        return self._router_id

    @property
    def bgppeers(self):
        return self._bgppeers

    def set_l3vpn_router_id(self, value):
        self._template[self._L3VPN_ROUTER_ID_FIELD] = value

    def set_auto_frr(self, value):
        self._template[self._AUTO_FRR_FIELD] = value

    def set_l3vpn_vpn_instance_name(self, value):
        self._template[self._L3VPN_VPN_INSTANCE_NAME_FIELD] = value

    def set_vpn_instance_name(self, value):
        self._template[self._VPN_INSTANCE_NAME_FIELD] = value

    def set_l3vpn_bgppeers(self, value):
        self._template[self._L3VPN_BGPPEERS_FIELD] = value

    def set_l3vpn_auto_frr(self, value):
        self._template[self._L3VPN_AUTO_FRR_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ROUTER_ID_FIELD] = self.router_id.get_template(default=default)
            self._default_template[self._BGPPEERS_FIELD] = self.bgppeers.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ROUTER_ID_FIELD] = self.router_id.get_template()
            self._template[self._BGPPEERS_FIELD] = self.bgppeers.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        router_id_payload = self.router_id.get_payload()
        if router_id_payload:
            payload[self._ROUTER_ID_FIELD] = router_id_payload
        bgppeers_payload = self.bgppeers.get_payload()
        if bgppeers_payload:
            payload[self._BGPPEERS_FIELD] = bgppeers_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_af_ipv4_vpn_instance(self):
        
        payload = {self._BGP_AF_IPV4_VPN_INSTANCE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_af_ipv4_vpn_instance(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_af_ipv4_vpn_instance(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MATCH_ENTRY_VALUE(object):

    _MATCH_ENTRY_VALUE_FIELD = "match-entry-value"
    _ETH_DST_FIELD = "eth-dst"
    _IPV6_SRC_FIELD = "ipv6-src"
    _IPV6_FLABEL_FIELD = "ipv6-flabel"
    _IP_ECN_FIELD = "ip-ecn"
    _VLAN_VID_FIELD = "vlan-vid"
    _ARP_TPA_FIELD = "arp-tpa"
    _MPLS_BOS_FIELD = "mpls-bos"
    _ICMPV6_CODE_FIELD = "icmpv6-code"
    _IP_PROTO_FIELD = "ip-proto"
    _ETH_SRC_FIELD = "eth-src"
    _UDP_DST_FIELD = "udp-dst"
    _IP_DSCP_FIELD = "ip-dscp"
    _VLAN_PCP_FIELD = "vlan-pcp"
    _MPLS_TC_FIELD = "mpls-tc"
    _ARP_SPA_FIELD = "arp-spa"
    _IPV6_EXTHDR_FIELD = "ipv6-exthdr"
    _TCP_DST_FIELD = "tcp-dst"
    _ICMPV4_TYPE_FIELD = "icmpv4-type"
    _IPV6_DST_FIELD = "ipv6-dst"
    _UDP_SRC_FIELD = "udp-src"
    _ARP_SHA_FIELD = "arp-sha"
    _IN_PHY_PORT_FIELD = "in-phy-port"
    _ICMPV6_TYPE_FIELD = "icmpv6-type"
    _METADATA_FIELD = "metadata"
    _ARP_THA_FIELD = "arp-tha"
    _IPV4_DST_FIELD = "ipv4-dst"
    _SCTP_DST_FIELD = "sctp-dst"
    _IPV6_ND_TARGET_FIELD = "ipv6-nd-target"
    _IPV4_SRC_FIELD = "ipv4-src"
    _IPV6_ND_TLL_FIELD = "ipv6-nd-tll"
    _TUNNEL_ID_FIELD = "tunnel-id"
    _SCTP_SRC_FIELD = "sctp-src"
    _ETH_TYPE_FIELD = "eth-type"
    _PBB_ISID_FIELD = "pbb-isid"
    _TCP_SRC_FIELD = "tcp-src"
    _IPV6_ND_SLL_FIELD = "ipv6-nd-sll"
    _ICMPV4_CODE_FIELD = "icmpv4-code"
    _MPLS_LABEL_FIELD = "mpls-label"
    _IN_PORT_FIELD = "in-port"
    _ARP_OP_FIELD = "arp-op"

    def __init__(self):
        self._template = {}
        self._template[self._ETH_DST_FIELD] = None
        self._template[self._IPV6_SRC_FIELD] = None
        self._template[self._IPV6_FLABEL_FIELD] = None
        self._template[self._IP_ECN_FIELD] = None
        self._template[self._VLAN_VID_FIELD] = None
        self._template[self._ARP_TPA_FIELD] = None
        self._template[self._MPLS_BOS_FIELD] = None
        self._template[self._ICMPV6_CODE_FIELD] = None
        self._template[self._IP_PROTO_FIELD] = None
        self._template[self._ETH_SRC_FIELD] = None
        self._template[self._UDP_DST_FIELD] = None
        self._template[self._IP_DSCP_FIELD] = None
        self._template[self._VLAN_PCP_FIELD] = None
        self._template[self._MPLS_TC_FIELD] = None
        self._template[self._ARP_SPA_FIELD] = None
        self._template[self._IPV6_EXTHDR_FIELD] = None
        self._template[self._TCP_DST_FIELD] = None
        self._template[self._ICMPV4_TYPE_FIELD] = None
        self._template[self._IPV6_DST_FIELD] = None
        self._template[self._UDP_SRC_FIELD] = None
        self._template[self._ARP_SHA_FIELD] = None
        self._template[self._IN_PHY_PORT_FIELD] = None
        self._template[self._ICMPV6_TYPE_FIELD] = None
        self._template[self._METADATA_FIELD] = None
        self._template[self._ARP_THA_FIELD] = None
        self._template[self._IPV4_DST_FIELD] = None
        self._template[self._SCTP_DST_FIELD] = None
        self._template[self._IPV6_ND_TARGET_FIELD] = None
        self._template[self._IPV4_SRC_FIELD] = None
        self._template[self._IPV6_ND_TLL_FIELD] = None
        self._template[self._TUNNEL_ID_FIELD] = None
        self._template[self._SCTP_SRC_FIELD] = None
        self._template[self._ETH_TYPE_FIELD] = None
        self._template[self._PBB_ISID_FIELD] = None
        self._template[self._TCP_SRC_FIELD] = None
        self._template[self._IPV6_ND_SLL_FIELD] = None
        self._template[self._ICMPV4_CODE_FIELD] = None
        self._template[self._MPLS_LABEL_FIELD] = None
        self._template[self._IN_PORT_FIELD] = None
        self._template[self._ARP_OP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._metadata = METADATA()

    @property
    def metadata(self):
        return self._metadata

    def set_eth_dst(self, value):
        self._template[self._ETH_DST_FIELD] = value

    def set_ipv6_src(self, value):
        self._template[self._IPV6_SRC_FIELD] = value

    def set_ipv6_flabel(self, value):
        self._template[self._IPV6_FLABEL_FIELD] = value

    def set_ip_ecn(self, value):
        self._template[self._IP_ECN_FIELD] = value

    def set_vlan_vid(self, value):
        self._template[self._VLAN_VID_FIELD] = value

    def set_arp_tpa(self, value):
        self._template[self._ARP_TPA_FIELD] = value

    def set_mpls_bos(self, value):
        self._template[self._MPLS_BOS_FIELD] = value

    def set_icmpv6_code(self, value):
        self._template[self._ICMPV6_CODE_FIELD] = value

    def set_ip_proto(self, value):
        self._template[self._IP_PROTO_FIELD] = value

    def set_eth_src(self, value):
        self._template[self._ETH_SRC_FIELD] = value

    def set_udp_dst(self, value):
        self._template[self._UDP_DST_FIELD] = value

    def set_ip_dscp(self, value):
        self._template[self._IP_DSCP_FIELD] = value

    def set_vlan_pcp(self, value):
        self._template[self._VLAN_PCP_FIELD] = value

    def set_mpls_tc(self, value):
        self._template[self._MPLS_TC_FIELD] = value

    def set_arp_spa(self, value):
        self._template[self._ARP_SPA_FIELD] = value

    def set_ipv6_exthdr(self, value):
        self._template[self._IPV6_EXTHDR_FIELD] = value

    def set_tcp_dst(self, value):
        self._template[self._TCP_DST_FIELD] = value

    def set_icmpv4_type(self, value):
        self._template[self._ICMPV4_TYPE_FIELD] = value

    def set_ipv6_dst(self, value):
        self._template[self._IPV6_DST_FIELD] = value

    def set_udp_src(self, value):
        self._template[self._UDP_SRC_FIELD] = value

    def set_arp_sha(self, value):
        self._template[self._ARP_SHA_FIELD] = value

    def set_in_phy_port(self, value):
        self._template[self._IN_PHY_PORT_FIELD] = value

    def set_icmpv6_type(self, value):
        self._template[self._ICMPV6_TYPE_FIELD] = value

    def set_arp_tha(self, value):
        self._template[self._ARP_THA_FIELD] = value

    def set_ipv4_dst(self, value):
        self._template[self._IPV4_DST_FIELD] = value

    def set_sctp_dst(self, value):
        self._template[self._SCTP_DST_FIELD] = value

    def set_ipv6_nd_target(self, value):
        self._template[self._IPV6_ND_TARGET_FIELD] = value

    def set_ipv4_src(self, value):
        self._template[self._IPV4_SRC_FIELD] = value

    def set_ipv6_nd_tll(self, value):
        self._template[self._IPV6_ND_TLL_FIELD] = value

    def set_tunnel_id(self, value):
        self._template[self._TUNNEL_ID_FIELD] = value

    def set_sctp_src(self, value):
        self._template[self._SCTP_SRC_FIELD] = value

    def set_eth_type(self, value):
        self._template[self._ETH_TYPE_FIELD] = value

    def set_pbb_isid(self, value):
        self._template[self._PBB_ISID_FIELD] = value

    def set_tcp_src(self, value):
        self._template[self._TCP_SRC_FIELD] = value

    def set_ipv6_nd_sll(self, value):
        self._template[self._IPV6_ND_SLL_FIELD] = value

    def set_icmpv4_code(self, value):
        self._template[self._ICMPV4_CODE_FIELD] = value

    def set_mpls_label(self, value):
        self._template[self._MPLS_LABEL_FIELD] = value

    def set_in_port(self, value):
        self._template[self._IN_PORT_FIELD] = value

    def set_arp_op(self, value):
        self._template[self._ARP_OP_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._METADATA_FIELD] = self.metadata.get_template(default=default)
            return self._default_template
        else:
            self._template[self._METADATA_FIELD] = self.metadata.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        metadata_payload = self.metadata.get_payload()
        if metadata_payload:
            payload[self._METADATA_FIELD] = metadata_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_match_entry_value(self):
        
        payload = {self._MATCH_ENTRY_VALUE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_match_entry_value(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_match_entry_value(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class METER(object):

    _METER_FIELD = "meter"
    _METER_ID_FIELD = "meter-id"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METER_ID_FIELD = "opendaylight-flow-table-statistics:meter-id"

    def __init__(self):
        self._template = {}
        self._template[self._METER_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METER_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_meter_id(self, value):
        self._template[self._METER_ID_FIELD] = value

    def set_opendaylight_flow_table_statistics_meter_id(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METER_ID_FIELD] = value

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

    def create_meter(self):
        
        payload = {self._METER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_meter(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_meter(self):
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


class OSPF_LINK_ATTRIBUTES(object):

    _OSPF_LINK_ATTRIBUTES_FIELD = "ospf-link-attributes"
    _TED_FIELD = "ted"
    _OSPF_TOPOLOGY_TED_FIELD = "ospf-topology:ted"
    _OSPF_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD = "ospf-topology:multi-topology-id"
    _MULTI_TOPOLOGY_ID_FIELD = "multi-topology-id"

    def __init__(self):
        self._template = {}
        self._template[self._TED_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_TED_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = None
        self._template[self._MULTI_TOPOLOGY_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ted = TED()

    @property
    def ted(self):
        return self._ted

    def set_ospf_topology_ted(self, value):
        self._template[self._OSPF_TOPOLOGY_TED_FIELD] = value

    def set_ospf_topology_multi_topology_id(self, value):
        self._template[self._OSPF_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = value

    def set_multi_topology_id(self, value):
        self._template[self._MULTI_TOPOLOGY_ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TED_FIELD] = self.ted.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TED_FIELD] = self.ted.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ted_payload = self.ted.get_payload()
        if ted_payload:
            payload[self._TED_FIELD] = ted_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ospf_link_attributes(self):
        
        payload = {self._OSPF_LINK_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ospf_link_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ospf_link_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PREFIX(object):

    _PREFIX_FIELD = "prefix"
    _L3_UNICAST_IGP_TOPOLOGY_PREFIX_FIELD = "l3-unicast-igp-topology:prefix"
    _L3_UNICAST_IGP_TOPOLOGY_METRIC_FIELD = "l3-unicast-igp-topology:metric"
    _PREFIX_FIELD = "prefix"
    _L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD = "l3-unicast-igp-topology:flag"
    _OSPF_PREFIX_ATTRIBUTES_FIELD = "ospf-prefix-attributes"
    _OSPF_TOPOLOGY_OSPF_PREFIX_ATTRIBUTES_FIELD = "ospf-topology:ospf-prefix-attributes"
    _METRIC_FIELD = "metric"

    def __init__(self):
        self._template = {}
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_PREFIX_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_METRIC_FIELD] = None
        self._template[self._PREFIX_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = None
        self._template[self._OSPF_PREFIX_ATTRIBUTES_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_OSPF_PREFIX_ATTRIBUTES_FIELD] = None
        self._template[self._METRIC_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ospf_prefix_attributes = OSPF_PREFIX_ATTRIBUTES()

    @property
    def ospf_prefix_attributes(self):
        return self._ospf_prefix_attributes

    def set_l3_unicast_igp_topology_prefix(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_PREFIX_FIELD] = value

    def set_l3_unicast_igp_topology_metric(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_METRIC_FIELD] = value

    def set_l3_unicast_igp_topology_flag(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = value

    def set_ospf_topology_ospf_prefix_attributes(self, value):
        self._template[self._OSPF_TOPOLOGY_OSPF_PREFIX_ATTRIBUTES_FIELD] = value

    def set_metric(self, value):
        self._template[self._METRIC_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._OSPF_PREFIX_ATTRIBUTES_FIELD] = self.ospf_prefix_attributes.get_template(default=default)
            return self._default_template
        else:
            self._template[self._OSPF_PREFIX_ATTRIBUTES_FIELD] = self.ospf_prefix_attributes.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ospf_prefix_attributes_payload = self.ospf_prefix_attributes.get_payload()
        if ospf_prefix_attributes_payload:
            payload[self._OSPF_PREFIX_ATTRIBUTES_FIELD] = ospf_prefix_attributes_payload
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


class BGP_AF_IPV6_VPN_INSTANCES(object):

    _BGP_AF_IPV6_VPN_INSTANCES_FIELD = "bgp-af-ipv6-vpn-instances"
    _L3VPN_BGP_AF_IPV6_VPN_INSTANCE_FIELD = "l3vpn:bgp-af-ipv6-vpn-instance"
    _BGP_AF_IPV6_VPN_INSTANCE_FIELD = "bgp-af-ipv6-vpn-instance"

    def __init__(self):
        self._template = {}
        self._template[self._L3VPN_BGP_AF_IPV6_VPN_INSTANCE_FIELD] = None
        self._template[self._BGP_AF_IPV6_VPN_INSTANCE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bgp_af_ipv6_vpn_instance = BGP_AF_IPV6_VPN_INSTANCE()

    @property
    def bgp_af_ipv6_vpn_instance(self):
        return self._bgp_af_ipv6_vpn_instance

    def set_l3vpn_bgp_af_ipv6_vpn_instance(self, value):
        self._template[self._L3VPN_BGP_AF_IPV6_VPN_INSTANCE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BGP_AF_IPV6_VPN_INSTANCE_FIELD] = self.bgp_af_ipv6_vpn_instance.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BGP_AF_IPV6_VPN_INSTANCE_FIELD] = self.bgp_af_ipv6_vpn_instance.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bgp_af_ipv6_vpn_instance_payload = self.bgp_af_ipv6_vpn_instance.get_payload()
        if bgp_af_ipv6_vpn_instance_payload:
            payload[self._BGP_AF_IPV6_VPN_INSTANCE_FIELD] = bgp_af_ipv6_vpn_instance_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_af_ipv6_vpn_instances(self):
        
        payload = {self._BGP_AF_IPV6_VPN_INSTANCES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_af_ipv6_vpn_instances(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_af_ipv6_vpn_instances(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class RESPONCE_TIME(object):

    _RESPONCE_TIME_FIELD = "responce-time"
    _RESPONCE_INTERVAL_FIELD = "responce-interval"
    _RESPONCE_TIME_DISABLE_FIELD = "responce-time-disable"

    def __init__(self):
        self._template = {}
        self._template[self._RESPONCE_INTERVAL_FIELD] = None
        self._template[self._RESPONCE_TIME_DISABLE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_responce_interval(self, value):
        self._template[self._RESPONCE_INTERVAL_FIELD] = value

    def set_responce_time_disable(self, value):
        self._template[self._RESPONCE_TIME_DISABLE_FIELD] = value

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

    def create_responce_time(self):
        
        payload = {self._RESPONCE_TIME_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_responce_time(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_responce_time(self):
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


class MATCH_TYPE(object):

    _MATCH_TYPE_FIELD = "match-type"
    _FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD = "flow-node-inventory:support-state"
    _FLOW_NODE_INVENTORY_MATCH_FIELD = "flow-node-inventory:match"
    _SUPPORT_STATE_FIELD = "support-state"
    _MATCH_FIELD = "match"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_MATCH_FIELD] = None
        self._template[self._SUPPORT_STATE_FIELD] = None
        self._template[self._MATCH_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._match = MATCH()

    @property
    def match(self):
        return self._match

    def set_flow_node_inventory_support_state(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD] = value

    def set_flow_node_inventory_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MATCH_FIELD] = value

    def set_support_state(self, value):
        self._template[self._SUPPORT_STATE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MATCH_FIELD] = self.match.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MATCH_FIELD] = self.match.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        match_payload = self.match.get_payload()
        if match_payload:
            payload[self._MATCH_FIELD] = match_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_match_type(self):
        
        payload = {self._MATCH_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_match_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_match_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ISIS_TOPOLOGY_ATTRIBUTES(object):

    _ISIS_TOPOLOGY_ATTRIBUTES_FIELD = "isis-topology-attributes"
    _NET_FIELD = "net"
    _ISIS_TOPOLOGY_NET_FIELD = "isis-topology:net"

    def __init__(self):
        self._template = {}
        self._template[self._NET_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_NET_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_net(self, value):
        self._template[self._NET_FIELD] = value

    def set_isis_topology_net(self, value):
        self._template[self._ISIS_TOPOLOGY_NET_FIELD] = value

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

    def create_isis_topology_attributes(self):
        
        payload = {self._ISIS_TOPOLOGY_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_isis_topology_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_isis_topology_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MAX_LSP_BANDWIDTH(object):

    _MAX_LSP_BANDWIDTH_FIELD = "max-lsp-bandwidth"
    _OSPF_TOPOLOGY_BANDWIDTH_FIELD = "ospf-topology:bandwidth"
    _PRIORITY_FIELD = "priority"
    _BANDWIDTH_FIELD = "bandwidth"
    _OSPF_TOPOLOGY_PRIORITY_FIELD = "ospf-topology:priority"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_BANDWIDTH_FIELD] = None
        self._template[self._PRIORITY_FIELD] = None
        self._template[self._BANDWIDTH_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_PRIORITY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_BANDWIDTH_FIELD] = value

    def set_priority(self, value):
        self._template[self._PRIORITY_FIELD] = value

    def set_bandwidth(self, value):
        self._template[self._BANDWIDTH_FIELD] = value

    def set_ospf_topology_priority(self, value):
        self._template[self._OSPF_TOPOLOGY_PRIORITY_FIELD] = value

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

    def create_max_lsp_bandwidth(self):
        
        payload = {self._MAX_LSP_BANDWIDTH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_max_lsp_bandwidth(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_max_lsp_bandwidth(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class GROUP(object):

    _GROUP_FIELD = "group"
    _GROUP_TYPE_FIELD = "group-type"
    _GROUP_ID_FIELD = "group-id"
    _BARRIER_FIELD = "barrier"
    _GROUP_NAME_FIELD = "group-name"
    _BUCKETS_FIELD = "buckets"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_STATISTICS_FIELD = "opendaylight-group-statistics:group-statistics"
    _FLOW_NODE_INVENTORY_BUCKETS_FIELD = "flow-node-inventory:buckets"
    _GROUP_STATISTICS_FIELD = "group-statistics"
    _CONTAINER_NAME_FIELD = "container-name"
    _FLOW_NODE_INVENTORY_BARRIER_FIELD = "flow-node-inventory:barrier"
    _GROUP_DESC_FIELD = "group-desc"
    _FLOW_NODE_INVENTORY_CONTAINER_NAME_FIELD = "flow-node-inventory:container-name"
    _FLOW_NODE_INVENTORY_GROUP_TYPE_FIELD = "flow-node-inventory:group-type"
    _FLOW_NODE_INVENTORY_GROUP_ID_FIELD = "flow-node-inventory:group-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_DESC_FIELD = "opendaylight-group-statistics:group-desc"
    _FLOW_NODE_INVENTORY_GROUP_NAME_FIELD = "flow-node-inventory:group-name"

    def __init__(self):
        self._template = {}
        self._template[self._GROUP_TYPE_FIELD] = None
        self._template[self._GROUP_ID_FIELD] = None
        self._template[self._BARRIER_FIELD] = None
        self._template[self._GROUP_NAME_FIELD] = None
        self._template[self._BUCKETS_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_STATISTICS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_BUCKETS_FIELD] = None
        self._template[self._GROUP_STATISTICS_FIELD] = None
        self._template[self._CONTAINER_NAME_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_BARRIER_FIELD] = None
        self._template[self._GROUP_DESC_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_CONTAINER_NAME_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_GROUP_TYPE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_GROUP_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_DESC_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_GROUP_NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._buckets = BUCKETS()
        self._group_statistics = GROUP_STATISTICS()
        self._group_desc = GROUP_DESC()

    @property
    def buckets(self):
        return self._buckets

    @property
    def group_statistics(self):
        return self._group_statistics

    @property
    def group_desc(self):
        return self._group_desc

    def set_group_type(self, value):
        self._template[self._GROUP_TYPE_FIELD] = value

    def set_group_id(self, value):
        self._template[self._GROUP_ID_FIELD] = value

    def set_barrier(self, value):
        self._template[self._BARRIER_FIELD] = value

    def set_group_name(self, value):
        self._template[self._GROUP_NAME_FIELD] = value

    def set_opendaylight_group_statistics_group_statistics(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_STATISTICS_FIELD] = value

    def set_flow_node_inventory_buckets(self, value):
        self._template[self._FLOW_NODE_INVENTORY_BUCKETS_FIELD] = value

    def set_container_name(self, value):
        self._template[self._CONTAINER_NAME_FIELD] = value

    def set_flow_node_inventory_barrier(self, value):
        self._template[self._FLOW_NODE_INVENTORY_BARRIER_FIELD] = value

    def set_flow_node_inventory_container_name(self, value):
        self._template[self._FLOW_NODE_INVENTORY_CONTAINER_NAME_FIELD] = value

    def set_flow_node_inventory_group_type(self, value):
        self._template[self._FLOW_NODE_INVENTORY_GROUP_TYPE_FIELD] = value

    def set_flow_node_inventory_group_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_GROUP_ID_FIELD] = value

    def set_opendaylight_group_statistics_group_desc(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_DESC_FIELD] = value

    def set_flow_node_inventory_group_name(self, value):
        self._template[self._FLOW_NODE_INVENTORY_GROUP_NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BUCKETS_FIELD] = self.buckets.get_template(default=default)
            self._default_template[self._GROUP_STATISTICS_FIELD] = self.group_statistics.get_template(default=default)
            self._default_template[self._GROUP_DESC_FIELD] = self.group_desc.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BUCKETS_FIELD] = self.buckets.get_template()
            self._template[self._GROUP_STATISTICS_FIELD] = self.group_statistics.get_template()
            self._template[self._GROUP_DESC_FIELD] = self.group_desc.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        buckets_payload = self.buckets.get_payload()
        if buckets_payload:
            payload[self._BUCKETS_FIELD] = buckets_payload
        group_statistics_payload = self.group_statistics.get_payload()
        if group_statistics_payload:
            payload[self._GROUP_STATISTICS_FIELD] = group_statistics_payload
        group_desc_payload = self.group_desc.get_payload()
        if group_desc_payload:
            payload[self._GROUP_DESC_FIELD] = group_desc_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_group(self):
        
        payload = {self._GROUP_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_group(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_group(self):
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


class FLOW_TABLE_STATISTICS(object):

    _FLOW_TABLE_STATISTICS_FIELD = "flow-table-statistics"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_PACKETS_MATCHED_FIELD = "opendaylight-flow-table-statistics:packets-matched"
    _PACKETS_LOOKED_UP_FIELD = "packets-looked-up"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_PACKETS_LOOKED_UP_FIELD = "opendaylight-flow-table-statistics:packets-looked-up"
    _PACKETS_MATCHED_FIELD = "packets-matched"
    _ACTIVE_FLOWS_FIELD = "active-flows"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ACTIVE_FLOWS_FIELD = "opendaylight-flow-table-statistics:active-flows"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_PACKETS_MATCHED_FIELD] = None
        self._template[self._PACKETS_LOOKED_UP_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_PACKETS_LOOKED_UP_FIELD] = None
        self._template[self._PACKETS_MATCHED_FIELD] = None
        self._template[self._ACTIVE_FLOWS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ACTIVE_FLOWS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_flow_table_statistics_packets_matched(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_PACKETS_MATCHED_FIELD] = value

    def set_packets_looked_up(self, value):
        self._template[self._PACKETS_LOOKED_UP_FIELD] = value

    def set_opendaylight_flow_table_statistics_packets_looked_up(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_PACKETS_LOOKED_UP_FIELD] = value

    def set_packets_matched(self, value):
        self._template[self._PACKETS_MATCHED_FIELD] = value

    def set_active_flows(self, value):
        self._template[self._ACTIVE_FLOWS_FIELD] = value

    def set_opendaylight_flow_table_statistics_active_flows(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ACTIVE_FLOWS_FIELD] = value

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

    def create_flow_table_statistics(self):
        
        payload = {self._FLOW_TABLE_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_table_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_table_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IGP_LINK_ATTRIBUTES(object):

    _IGP_LINK_ATTRIBUTES_FIELD = "igp-link-attributes"
    _ISIS_TOPOLOGY_ISIS_LINK_ATTRIBUTES_FIELD = "isis-topology:isis-link-attributes"
    _NAME_FIELD = "name"
    _ISIS_LINK_ATTRIBUTES_FIELD = "isis-link-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_METRIC_FIELD = "l3-unicast-igp-topology:metric"
    _OSPF_LINK_ATTRIBUTES_FIELD = "ospf-link-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD = "l3-unicast-igp-topology:flag"
    _OSPF_TOPOLOGY_OSPF_LINK_ATTRIBUTES_FIELD = "ospf-topology:ospf-link-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD = "l3-unicast-igp-topology:name"
    _METRIC_FIELD = "metric"

    def __init__(self):
        self._template = {}
        self._template[self._ISIS_TOPOLOGY_ISIS_LINK_ATTRIBUTES_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._template[self._ISIS_LINK_ATTRIBUTES_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_METRIC_FIELD] = None
        self._template[self._OSPF_LINK_ATTRIBUTES_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_OSPF_LINK_ATTRIBUTES_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD] = None
        self._template[self._METRIC_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._isis_link_attributes = ISIS_LINK_ATTRIBUTES()
        self._ospf_link_attributes = OSPF_LINK_ATTRIBUTES()

    @property
    def isis_link_attributes(self):
        return self._isis_link_attributes

    @property
    def ospf_link_attributes(self):
        return self._ospf_link_attributes

    def set_isis_topology_isis_link_attributes(self, value):
        self._template[self._ISIS_TOPOLOGY_ISIS_LINK_ATTRIBUTES_FIELD] = value

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_l3_unicast_igp_topology_metric(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_METRIC_FIELD] = value

    def set_l3_unicast_igp_topology_flag(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = value

    def set_ospf_topology_ospf_link_attributes(self, value):
        self._template[self._OSPF_TOPOLOGY_OSPF_LINK_ATTRIBUTES_FIELD] = value

    def set_l3_unicast_igp_topology_name(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD] = value

    def set_metric(self, value):
        self._template[self._METRIC_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ISIS_LINK_ATTRIBUTES_FIELD] = self.isis_link_attributes.get_template(default=default)
            self._default_template[self._OSPF_LINK_ATTRIBUTES_FIELD] = self.ospf_link_attributes.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ISIS_LINK_ATTRIBUTES_FIELD] = self.isis_link_attributes.get_template()
            self._template[self._OSPF_LINK_ATTRIBUTES_FIELD] = self.ospf_link_attributes.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        isis_link_attributes_payload = self.isis_link_attributes.get_payload()
        if isis_link_attributes_payload:
            payload[self._ISIS_LINK_ATTRIBUTES_FIELD] = isis_link_attributes_payload
        ospf_link_attributes_payload = self.ospf_link_attributes.get_payload()
        if ospf_link_attributes_payload:
            payload[self._OSPF_LINK_ATTRIBUTES_FIELD] = ospf_link_attributes_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_igp_link_attributes(self):
        
        payload = {self._IGP_LINK_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_igp_link_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_igp_link_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PROTOCOL_MATCH_FIELDS(object):

    _PROTOCOL_MATCH_FIELDS_FIELD = "protocol-match-fields"
    _MPLS_TC_FIELD = "mpls-tc"
    _OPENDAYLIGHT_GROUP_STATISTICS_MPLS_BOS_FIELD = "opendaylight-group-statistics:mpls-bos"
    _PBB_FIELD = "pbb"
    _MPLS_BOS_FIELD = "mpls-bos"
    _MPLS_LABEL_FIELD = "mpls-label"
    _OPENDAYLIGHT_GROUP_STATISTICS_MPLS_TC_FIELD = "opendaylight-group-statistics:mpls-tc"
    _OPENDAYLIGHT_GROUP_STATISTICS_MPLS_LABEL_FIELD = "opendaylight-group-statistics:mpls-label"
    _OPENDAYLIGHT_GROUP_STATISTICS_PBB_FIELD = "opendaylight-group-statistics:pbb"

    def __init__(self):
        self._template = {}
        self._template[self._MPLS_TC_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MPLS_BOS_FIELD] = None
        self._template[self._PBB_FIELD] = None
        self._template[self._MPLS_BOS_FIELD] = None
        self._template[self._MPLS_LABEL_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MPLS_TC_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MPLS_LABEL_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PBB_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._pbb = PBB()

    @property
    def pbb(self):
        return self._pbb

    def set_mpls_tc(self, value):
        self._template[self._MPLS_TC_FIELD] = value

    def set_opendaylight_group_statistics_mpls_bos(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MPLS_BOS_FIELD] = value

    def set_mpls_bos(self, value):
        self._template[self._MPLS_BOS_FIELD] = value

    def set_mpls_label(self, value):
        self._template[self._MPLS_LABEL_FIELD] = value

    def set_opendaylight_group_statistics_mpls_tc(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MPLS_TC_FIELD] = value

    def set_opendaylight_group_statistics_mpls_label(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MPLS_LABEL_FIELD] = value

    def set_opendaylight_group_statistics_pbb(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PBB_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PBB_FIELD] = self.pbb.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PBB_FIELD] = self.pbb.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        pbb_payload = self.pbb.get_payload()
        if pbb_payload:
            payload[self._PBB_FIELD] = pbb_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_protocol_match_fields(self):
        
        payload = {self._PROTOCOL_MATCH_FIELDS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_protocol_match_fields(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_protocol_match_fields(self):
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


class METER_FEATURES(object):

    _METER_FEATURES_FIELD = "meter-features"
    _OPENDAYLIGHT_METER_STATISTICS_MAX_METER_FIELD = "opendaylight-meter-statistics:max_meter"
    _OPENDAYLIGHT_METER_STATISTICS_MAX_BANDS_FIELD = "opendaylight-meter-statistics:max_bands"
    _OPENDAYLIGHT_METER_STATISTICS_MAX_COLOR_FIELD = "opendaylight-meter-statistics:max_color"
    _MAX_BANDS_FIELD = "max_bands"
    _MAX_METER_FIELD = "max_meter"
    _OPENDAYLIGHT_METER_STATISTICS_METER_BAND_SUPPORTED_FIELD = "opendaylight-meter-statistics:meter-band-supported"
    _OPENDAYLIGHT_METER_STATISTICS_METER_CAPABILITIES_SUPPORTED_FIELD = "opendaylight-meter-statistics:meter-capabilities-supported"
    _MAX_COLOR_FIELD = "max_color"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_MAX_METER_FIELD] = None
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_MAX_BANDS_FIELD] = None
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_MAX_COLOR_FIELD] = None
        self._template[self._MAX_BANDS_FIELD] = None
        self._template[self._MAX_METER_FIELD] = None
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_METER_BAND_SUPPORTED_FIELD] = None
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_METER_CAPABILITIES_SUPPORTED_FIELD] = None
        self._template[self._MAX_COLOR_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_meter_statistics_max_meter(self, value):
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_MAX_METER_FIELD] = value

    def set_opendaylight_meter_statistics_max_bands(self, value):
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_MAX_BANDS_FIELD] = value

    def set_opendaylight_meter_statistics_max_color(self, value):
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_MAX_COLOR_FIELD] = value

    def set_max_bands(self, value):
        self._template[self._MAX_BANDS_FIELD] = value

    def set_max_meter(self, value):
        self._template[self._MAX_METER_FIELD] = value

    def set_opendaylight_meter_statistics_meter_band_supported(self, value):
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_METER_BAND_SUPPORTED_FIELD] = value

    def set_opendaylight_meter_statistics_meter_capabilities_supported(self, value):
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_METER_CAPABILITIES_SUPPORTED_FIELD] = value

    def set_max_color(self, value):
        self._template[self._MAX_COLOR_FIELD] = value

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

    def create_meter_features(self):
        
        payload = {self._METER_FEATURES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_meter_features(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_meter_features(self):
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


class SOURCE(object):

    _SOURCE_FIELD = "source"
    _SOURCE_TP_FIELD = "source-tp"
    _SOURCE_NODE_FIELD = "source-node"

    def __init__(self):
        self._template = {}
        self._template[self._SOURCE_TP_FIELD] = None
        self._template[self._SOURCE_NODE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_source_tp(self, value):
        self._template[self._SOURCE_TP_FIELD] = value

    def set_source_node(self, value):
        self._template[self._SOURCE_NODE_FIELD] = value

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

    def create_source(self):
        
        payload = {self._SOURCE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_source(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_source(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class AGGREGATE_FLOW_STATISTICS(object):

    _AGGREGATE_FLOW_STATISTICS_FIELD = "aggregate-flow-statistics"
    _OPENDAYLIGHT_FLOW_STATISTICS_PACKET_COUNT_FIELD = "opendaylight-flow-statistics:packet-count"
    _BYTE_COUNT_FIELD = "byte-count"
    _OPENDAYLIGHT_FLOW_STATISTICS_FLOW_COUNT_FIELD = "opendaylight-flow-statistics:flow-count"
    _FLOW_COUNT_FIELD = "flow-count"
    _OPENDAYLIGHT_FLOW_STATISTICS_BYTE_COUNT_FIELD = "opendaylight-flow-statistics:byte-count"
    _PACKET_COUNT_FIELD = "packet-count"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_PACKET_COUNT_FIELD] = None
        self._template[self._BYTE_COUNT_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_FLOW_COUNT_FIELD] = None
        self._template[self._FLOW_COUNT_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_BYTE_COUNT_FIELD] = None
        self._template[self._PACKET_COUNT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_flow_statistics_packet_count(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_PACKET_COUNT_FIELD] = value

    def set_byte_count(self, value):
        self._template[self._BYTE_COUNT_FIELD] = value

    def set_opendaylight_flow_statistics_flow_count(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_FLOW_COUNT_FIELD] = value

    def set_flow_count(self, value):
        self._template[self._FLOW_COUNT_FIELD] = value

    def set_opendaylight_flow_statistics_byte_count(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_BYTE_COUNT_FIELD] = value

    def set_packet_count(self, value):
        self._template[self._PACKET_COUNT_FIELD] = value

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

    def create_aggregate_flow_statistics(self):
        
        payload = {self._AGGREGATE_FLOW_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_aggregate_flow_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_aggregate_flow_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class OSPF_NODE_ATTRIBUTES(object):

    _OSPF_NODE_ATTRIBUTES_FIELD = "ospf-node-attributes"
    _TED_FIELD = "ted"
    _OSPF_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD = "ospf-topology:multi-topology-id"
    _CAPABILITIES_FIELD = "capabilities"
    _DR_INTERFACE_ID_FIELD = "dr-interface-id"
    _OSPF_TOPOLOGY_TED_FIELD = "ospf-topology:ted"
    _OSPF_TOPOLOGY_CAPABILITIES_FIELD = "ospf-topology:capabilities"
    _OSPF_TOPOLOGY_ROUTER_TYPE_FIELD = "ospf-topology:router-type"
    _OSPF_TOPOLOGY_DR_INTERFACE_ID_FIELD = "ospf-topology:dr-interface-id"

    def __init__(self):
        self._template = {}
        self._template[self._TED_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = None
        self._template[self._CAPABILITIES_FIELD] = None
        self._template[self._DR_INTERFACE_ID_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_TED_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_CAPABILITIES_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_ROUTER_TYPE_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_DR_INTERFACE_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ted = TED()
        self._ospf_topology_router_type = OSPF_TOPOLOGY_ROUTER_TYPE()

    @property
    def ted(self):
        return self._ted

    @property
    def ospf_topology_router_type(self):
        return self._ospf_topology_router_type

    def set_ospf_topology_multi_topology_id(self, value):
        self._template[self._OSPF_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = value

    def set_capabilities(self, value):
        self._template[self._CAPABILITIES_FIELD] = value

    def set_dr_interface_id(self, value):
        self._template[self._DR_INTERFACE_ID_FIELD] = value

    def set_ospf_topology_ted(self, value):
        self._template[self._OSPF_TOPOLOGY_TED_FIELD] = value

    def set_ospf_topology_capabilities(self, value):
        self._template[self._OSPF_TOPOLOGY_CAPABILITIES_FIELD] = value

    def set_ospf_topology_dr_interface_id(self, value):
        self._template[self._OSPF_TOPOLOGY_DR_INTERFACE_ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TED_FIELD] = self.ted.get_template(default=default)
            self._default_template[self._OSPF_TOPOLOGY_ROUTER_TYPE_FIELD] = self.ospf_topology_router_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TED_FIELD] = self.ted.get_template()
            self._template[self._OSPF_TOPOLOGY_ROUTER_TYPE_FIELD] = self.ospf_topology_router_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ted_payload = self.ted.get_payload()
        if ted_payload:
            payload[self._TED_FIELD] = ted_payload
        ospf_topology_router_type_payload = self.ospf_topology_router_type.get_payload()
        if ospf_topology_router_type_payload:
            payload[self._OSPF_TOPOLOGY_ROUTER_TYPE_FIELD] = ospf_topology_router_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ospf_node_attributes(self):
        
        payload = {self._OSPF_NODE_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ospf_node_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ospf_node_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ORIGINAL_NODE(object):

    _ORIGINAL_NODE_FIELD = "original-node"
    _NODE_FIELD = "node"
    _OPENDAYLIGHT_TOPOLOGY_VIEW_NODE_FIELD = "opendaylight-topology-view:node"
    _OPENDAYLIGHT_TOPOLOGY_VIEW_TOPOLOGY_FIELD = "opendaylight-topology-view:topology"
    _TOPOLOGY_FIELD = "topology"

    def __init__(self):
        self._template = {}
        self._template[self._NODE_FIELD] = None
        self._template[self._OPENDAYLIGHT_TOPOLOGY_VIEW_NODE_FIELD] = None
        self._template[self._OPENDAYLIGHT_TOPOLOGY_VIEW_TOPOLOGY_FIELD] = None
        self._template[self._TOPOLOGY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._node = NODE()
        self._topology = TOPOLOGY()

    @property
    def node(self):
        return self._node

    @property
    def topology(self):
        return self._topology

    def set_opendaylight_topology_view_node(self, value):
        self._template[self._OPENDAYLIGHT_TOPOLOGY_VIEW_NODE_FIELD] = value

    def set_opendaylight_topology_view_topology(self, value):
        self._template[self._OPENDAYLIGHT_TOPOLOGY_VIEW_TOPOLOGY_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._NODE_FIELD] = self.node.get_template(default=default)
            self._default_template[self._TOPOLOGY_FIELD] = self.topology.get_template(default=default)
            return self._default_template
        else:
            self._template[self._NODE_FIELD] = self.node.get_template()
            self._template[self._TOPOLOGY_FIELD] = self.topology.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        node_payload = self.node.get_payload()
        if node_payload:
            payload[self._NODE_FIELD] = node_payload
        topology_payload = self.topology.get_payload()
        if topology_payload:
            payload[self._TOPOLOGY_FIELD] = topology_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_original_node(self):
        
        payload = {self._ORIGINAL_NODE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_original_node(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_original_node(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ISIS_TOPOLOGY_ROUTER_TYPE(object):

    _ISIS_TOPOLOGY_ROUTER_TYPE_FIELD = "isis-topology:router-type"
    _ISIS_TOPOLOGY_LEVEL_1_FIELD = "isis-topology:level-1"
    _ISIS_TOPOLOGY_LEVEL_2_FIELD = "isis-topology:level-2"
    _ISIS_TOPOLOGY_LEVEL_1_2_FIELD = "isis-topology:level-1-2"

    def __init__(self):
        self._template = {}
        self._template[self._ISIS_TOPOLOGY_LEVEL_1_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_LEVEL_2_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_LEVEL_1_2_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_isis_topology_level_1(self, value):
        self._template[self._ISIS_TOPOLOGY_LEVEL_1_FIELD] = value

    def set_isis_topology_level_2(self, value):
        self._template[self._ISIS_TOPOLOGY_LEVEL_2_FIELD] = value

    def set_isis_topology_level_1_2(self, value):
        self._template[self._ISIS_TOPOLOGY_LEVEL_1_2_FIELD] = value

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

    def create_isis_topology_router_type(self):
        
        payload = {self._ISIS_TOPOLOGY_ROUTER_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_isis_topology_router_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_isis_topology_router_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MATCH(object):

    _MATCH_FIELD = "match"
    _FLOW_NODE_INVENTORY_IP_MATCH_FIELD = "flow-node-inventory:ip-match"
    _EXTENSION_LIST_FIELD = "extension-list"
    _FLOW_NODE_INVENTORY_ICMPV6_MATCH_FIELD = "flow-node-inventory:icmpv6-match"
    _FLOW_NODE_INVENTORY_VLAN_MATCH_FIELD = "flow-node-inventory:vlan-match"
    _FLOW_NODE_INVENTORY_METADATA_FIELD = "flow-node-inventory:metadata"
    _FLOW_NODE_INVENTORY_ICMPV4_MATCH_FIELD = "flow-node-inventory:icmpv4-match"
    _FLOW_NODE_INVENTORY_ETHERNET_MATCH_FIELD = "flow-node-inventory:ethernet-match"
    _ETHERNET_MATCH_FIELD = "ethernet-match"
    _PROTOCOL_MATCH_FIELDS_FIELD = "protocol-match-fields"
    _VLAN_MATCH_FIELD = "vlan-match"
    _IN_PHY_PORT_FIELD = "in-phy-port"
    _FLOW_NODE_INVENTORY_TUNNEL_FIELD = "flow-node-inventory:tunnel"
    _FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD = "flow-node-inventory:layer-4-match"
    _METADATA_FIELD = "metadata"
    _FLOW_NODE_INVENTORY_IN_PHY_PORT_FIELD = "flow-node-inventory:in-phy-port"
    _FLOW_NODE_INVENTORY_IN_PORT_FIELD = "flow-node-inventory:in-port"
    _TCP_FLAG_MATCH_FIELD = "tcp-flag-match"
    _FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD = "flow-node-inventory:layer-3-match"
    _IP_MATCH_FIELD = "ip-match"
    _TUNNEL_FIELD = "tunnel"
    _ICMPV4_MATCH_FIELD = "icmpv4-match"
    _OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_LIST_FIELD = "openflowplugin-extension-general:extension-list"
    _FLOW_NODE_INVENTORY_TCP_FLAG_MATCH_FIELD = "flow-node-inventory:tcp-flag-match"
    _FLOW_NODE_INVENTORY_PROTOCOL_MATCH_FIELDS_FIELD = "flow-node-inventory:protocol-match-fields"
    _IN_PORT_FIELD = "in-port"
    _ICMPV6_MATCH_FIELD = "icmpv6-match"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_IP_MATCH_FIELD] = None
        self._template[self._EXTENSION_LIST_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ICMPV6_MATCH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_VLAN_MATCH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_METADATA_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ICMPV4_MATCH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ETHERNET_MATCH_FIELD] = None
        self._template[self._ETHERNET_MATCH_FIELD] = None
        self._template[self._PROTOCOL_MATCH_FIELDS_FIELD] = None
        self._template[self._VLAN_MATCH_FIELD] = None
        self._template[self._IN_PHY_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TUNNEL_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD] = None
        self._template[self._METADATA_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IN_PHY_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IN_PORT_FIELD] = None
        self._template[self._TCP_FLAG_MATCH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD] = None
        self._template[self._IP_MATCH_FIELD] = None
        self._template[self._TUNNEL_FIELD] = None
        self._template[self._ICMPV4_MATCH_FIELD] = None
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_LIST_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TCP_FLAG_MATCH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_PROTOCOL_MATCH_FIELDS_FIELD] = None
        self._template[self._IN_PORT_FIELD] = None
        self._template[self._ICMPV6_MATCH_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._extension_list = EXTENSION_LIST()
        self._ethernet_match = ETHERNET_MATCH()
        self._protocol_match_fields = PROTOCOL_MATCH_FIELDS()
        self._vlan_match = VLAN_MATCH()
        self._flow_node_inventory_layer_4_match = FLOW_NODE_INVENTORY_LAYER_4_MATCH()
        self._metadata = METADATA()
        self._tcp_flag_match = TCP_FLAG_MATCH()
        self._flow_node_inventory_layer_3_match = FLOW_NODE_INVENTORY_LAYER_3_MATCH()
        self._ip_match = IP_MATCH()
        self._tunnel = TUNNEL()
        self._icmpv4_match = ICMPV4_MATCH()
        self._icmpv6_match = ICMPV6_MATCH()

    @property
    def extension_list(self):
        return self._extension_list

    @property
    def ethernet_match(self):
        return self._ethernet_match

    @property
    def protocol_match_fields(self):
        return self._protocol_match_fields

    @property
    def vlan_match(self):
        return self._vlan_match

    @property
    def flow_node_inventory_layer_4_match(self):
        return self._flow_node_inventory_layer_4_match

    @property
    def metadata(self):
        return self._metadata

    @property
    def tcp_flag_match(self):
        return self._tcp_flag_match

    @property
    def flow_node_inventory_layer_3_match(self):
        return self._flow_node_inventory_layer_3_match

    @property
    def ip_match(self):
        return self._ip_match

    @property
    def tunnel(self):
        return self._tunnel

    @property
    def icmpv4_match(self):
        return self._icmpv4_match

    @property
    def icmpv6_match(self):
        return self._icmpv6_match

    def set_flow_node_inventory_ip_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IP_MATCH_FIELD] = value

    def set_flow_node_inventory_icmpv6_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ICMPV6_MATCH_FIELD] = value

    def set_flow_node_inventory_vlan_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_VLAN_MATCH_FIELD] = value

    def set_flow_node_inventory_metadata(self, value):
        self._template[self._FLOW_NODE_INVENTORY_METADATA_FIELD] = value

    def set_flow_node_inventory_icmpv4_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ICMPV4_MATCH_FIELD] = value

    def set_flow_node_inventory_ethernet_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ETHERNET_MATCH_FIELD] = value

    def set_in_phy_port(self, value):
        self._template[self._IN_PHY_PORT_FIELD] = value

    def set_flow_node_inventory_tunnel(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TUNNEL_FIELD] = value

    def set_flow_node_inventory_in_phy_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IN_PHY_PORT_FIELD] = value

    def set_flow_node_inventory_in_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IN_PORT_FIELD] = value

    def set_openflowplugin_extension_general_extension_list(self, value):
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_LIST_FIELD] = value

    def set_flow_node_inventory_tcp_flag_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TCP_FLAG_MATCH_FIELD] = value

    def set_flow_node_inventory_protocol_match_fields(self, value):
        self._template[self._FLOW_NODE_INVENTORY_PROTOCOL_MATCH_FIELDS_FIELD] = value

    def set_in_port(self, value):
        self._template[self._IN_PORT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._EXTENSION_LIST_FIELD] = self.extension_list.get_template(default=default)
            self._default_template[self._ETHERNET_MATCH_FIELD] = self.ethernet_match.get_template(default=default)
            self._default_template[self._PROTOCOL_MATCH_FIELDS_FIELD] = self.protocol_match_fields.get_template(default=default)
            self._default_template[self._VLAN_MATCH_FIELD] = self.vlan_match.get_template(default=default)
            self._default_template[self._FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD] = self.flow_node_inventory_layer_4_match.get_template(default=default)
            self._default_template[self._METADATA_FIELD] = self.metadata.get_template(default=default)
            self._default_template[self._TCP_FLAG_MATCH_FIELD] = self.tcp_flag_match.get_template(default=default)
            self._default_template[self._FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD] = self.flow_node_inventory_layer_3_match.get_template(default=default)
            self._default_template[self._IP_MATCH_FIELD] = self.ip_match.get_template(default=default)
            self._default_template[self._TUNNEL_FIELD] = self.tunnel.get_template(default=default)
            self._default_template[self._ICMPV4_MATCH_FIELD] = self.icmpv4_match.get_template(default=default)
            self._default_template[self._ICMPV6_MATCH_FIELD] = self.icmpv6_match.get_template(default=default)
            return self._default_template
        else:
            self._template[self._EXTENSION_LIST_FIELD] = self.extension_list.get_template()
            self._template[self._ETHERNET_MATCH_FIELD] = self.ethernet_match.get_template()
            self._template[self._PROTOCOL_MATCH_FIELDS_FIELD] = self.protocol_match_fields.get_template()
            self._template[self._VLAN_MATCH_FIELD] = self.vlan_match.get_template()
            self._template[self._FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD] = self.flow_node_inventory_layer_4_match.get_template()
            self._template[self._METADATA_FIELD] = self.metadata.get_template()
            self._template[self._TCP_FLAG_MATCH_FIELD] = self.tcp_flag_match.get_template()
            self._template[self._FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD] = self.flow_node_inventory_layer_3_match.get_template()
            self._template[self._IP_MATCH_FIELD] = self.ip_match.get_template()
            self._template[self._TUNNEL_FIELD] = self.tunnel.get_template()
            self._template[self._ICMPV4_MATCH_FIELD] = self.icmpv4_match.get_template()
            self._template[self._ICMPV6_MATCH_FIELD] = self.icmpv6_match.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        extension_list_payload = self.extension_list.get_payload()
        if extension_list_payload:
            payload[self._EXTENSION_LIST_FIELD] = extension_list_payload
        ethernet_match_payload = self.ethernet_match.get_payload()
        if ethernet_match_payload:
            payload[self._ETHERNET_MATCH_FIELD] = ethernet_match_payload
        protocol_match_fields_payload = self.protocol_match_fields.get_payload()
        if protocol_match_fields_payload:
            payload[self._PROTOCOL_MATCH_FIELDS_FIELD] = protocol_match_fields_payload
        vlan_match_payload = self.vlan_match.get_payload()
        if vlan_match_payload:
            payload[self._VLAN_MATCH_FIELD] = vlan_match_payload
        flow_node_inventory_layer_4_match_payload = self.flow_node_inventory_layer_4_match.get_payload()
        if flow_node_inventory_layer_4_match_payload:
            payload[self._FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD] = flow_node_inventory_layer_4_match_payload
        metadata_payload = self.metadata.get_payload()
        if metadata_payload:
            payload[self._METADATA_FIELD] = metadata_payload
        tcp_flag_match_payload = self.tcp_flag_match.get_payload()
        if tcp_flag_match_payload:
            payload[self._TCP_FLAG_MATCH_FIELD] = tcp_flag_match_payload
        flow_node_inventory_layer_3_match_payload = self.flow_node_inventory_layer_3_match.get_payload()
        if flow_node_inventory_layer_3_match_payload:
            payload[self._FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD] = flow_node_inventory_layer_3_match_payload
        ip_match_payload = self.ip_match.get_payload()
        if ip_match_payload:
            payload[self._IP_MATCH_FIELD] = ip_match_payload
        tunnel_payload = self.tunnel.get_payload()
        if tunnel_payload:
            payload[self._TUNNEL_FIELD] = tunnel_payload
        icmpv4_match_payload = self.icmpv4_match.get_payload()
        if icmpv4_match_payload:
            payload[self._ICMPV4_MATCH_FIELD] = icmpv4_match_payload
        icmpv6_match_payload = self.icmpv6_match.get_payload()
        if icmpv6_match_payload:
            payload[self._ICMPV6_MATCH_FIELD] = icmpv6_match_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_match(self):
        
        payload = {self._MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class NODE_CONNECTOR(object):

    _NODE_CONNECTOR_FIELD = "node-connector"
    _PEER_FEATURES_FIELD = "peer-features"
    _ADDRESSES_FIELD = "addresses"
    _STP_STATUS_AWARE_NODE_CONNECTOR_STATUS_FIELD = "stp-status-aware-node-connector:status"
    _OPENDAYLIGHT_PORT_STATISTICS_FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD = "opendaylight-port-statistics:flow-capable-node-connector-statistics"
    _SUPPORTED_FIELD = "supported"
    _MAXIMUM_SPEED_FIELD = "maximum-speed"
    _FLOW_NODE_INVENTORY_CURRENT_FEATURE_FIELD = "flow-node-inventory:current-feature"
    _ID_FIELD = "id"
    _FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD = "flow-capable-node-connector-statistics"
    _FLOW_NODE_INVENTORY_CURRENT_SPEED_FIELD = "flow-node-inventory:current-speed"
    _FLOW_NODE_INVENTORY_PEER_FEATURES_FIELD = "flow-node-inventory:peer-features"
    _CURRENT_FEATURE_FIELD = "current-feature"
    _STATE_FIELD = "state"
    _FLOW_NODE_INVENTORY_HARDWARE_ADDRESS_FIELD = "flow-node-inventory:hardware-address"
    _FLOW_NODE_INVENTORY_MAXIMUM_SPEED_FIELD = "flow-node-inventory:maximum-speed"
    _HARDWARE_ADDRESS_FIELD = "hardware-address"
    _STATUS_FIELD = "status"
    _FLOW_NODE_INVENTORY_ADVERTISED_FEATURES_FIELD = "flow-node-inventory:advertised-features"
    _PORT_NUMBER_FIELD = "port-number"
    _ADDRESS_TRACKER_ADDRESSES_FIELD = "address-tracker:addresses"
    _FLOW_NODE_INVENTORY_STATE_FIELD = "flow-node-inventory:state"
    _FLOW_NODE_INVENTORY_SUPPORTED_FIELD = "flow-node-inventory:supported"
    _CONFIGURATION_FIELD = "configuration"
    _ADVERTISED_FEATURES_FIELD = "advertised-features"
    _FLOW_NODE_INVENTORY_PORT_NUMBER_FIELD = "flow-node-inventory:port-number"
    _NAME_FIELD = "name"
    _FLOW_NODE_INVENTORY_NAME_FIELD = "flow-node-inventory:name"
    _FLOW_NODE_INVENTORY_CONFIGURATION_FIELD = "flow-node-inventory:configuration"
    _QUEUE_FIELD = "queue"
    _FLOW_NODE_INVENTORY_QUEUE_FIELD = "flow-node-inventory:queue"
    _CURRENT_SPEED_FIELD = "current-speed"

    def __init__(self):
        self._template = {}
        self._template[self._PEER_FEATURES_FIELD] = None
        self._template[self._ADDRESSES_FIELD] = None
        self._template[self._STP_STATUS_AWARE_NODE_CONNECTOR_STATUS_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD] = None
        self._template[self._SUPPORTED_FIELD] = None
        self._template[self._MAXIMUM_SPEED_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_CURRENT_FEATURE_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._template[self._FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_CURRENT_SPEED_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_PEER_FEATURES_FIELD] = None
        self._template[self._CURRENT_FEATURE_FIELD] = None
        self._template[self._STATE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_HARDWARE_ADDRESS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_MAXIMUM_SPEED_FIELD] = None
        self._template[self._HARDWARE_ADDRESS_FIELD] = None
        self._template[self._STATUS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ADVERTISED_FEATURES_FIELD] = None
        self._template[self._PORT_NUMBER_FIELD] = None
        self._template[self._ADDRESS_TRACKER_ADDRESSES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_STATE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_FIELD] = None
        self._template[self._CONFIGURATION_FIELD] = None
        self._template[self._ADVERTISED_FEATURES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_PORT_NUMBER_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_NAME_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_CONFIGURATION_FIELD] = None
        self._template[self._QUEUE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_QUEUE_FIELD] = None
        self._template[self._CURRENT_SPEED_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._addresses = ADDRESSES()
        self._flow_capable_node_connector_statistics = FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS()
        self._state = STATE()
        self._configuration = CONFIGURATION()
        self._queue = QUEUE()

    @property
    def addresses(self):
        return self._addresses

    @property
    def flow_capable_node_connector_statistics(self):
        return self._flow_capable_node_connector_statistics

    @property
    def state(self):
        return self._state

    @property
    def configuration(self):
        return self._configuration

    @property
    def queue(self):
        return self._queue

    def set_peer_features(self, value):
        self._template[self._PEER_FEATURES_FIELD] = value

    def set_stp_status_aware_node_connector_status(self, value):
        self._template[self._STP_STATUS_AWARE_NODE_CONNECTOR_STATUS_FIELD] = value

    def set_opendaylight_port_statistics_flow_capable_node_connector_statistics(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD] = value

    def set_supported(self, value):
        self._template[self._SUPPORTED_FIELD] = value

    def set_maximum_speed(self, value):
        self._template[self._MAXIMUM_SPEED_FIELD] = value

    def set_flow_node_inventory_current_feature(self, value):
        self._template[self._FLOW_NODE_INVENTORY_CURRENT_FEATURE_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_flow_node_inventory_current_speed(self, value):
        self._template[self._FLOW_NODE_INVENTORY_CURRENT_SPEED_FIELD] = value

    def set_flow_node_inventory_peer_features(self, value):
        self._template[self._FLOW_NODE_INVENTORY_PEER_FEATURES_FIELD] = value

    def set_current_feature(self, value):
        self._template[self._CURRENT_FEATURE_FIELD] = value

    def set_flow_node_inventory_hardware_address(self, value):
        self._template[self._FLOW_NODE_INVENTORY_HARDWARE_ADDRESS_FIELD] = value

    def set_flow_node_inventory_maximum_speed(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MAXIMUM_SPEED_FIELD] = value

    def set_hardware_address(self, value):
        self._template[self._HARDWARE_ADDRESS_FIELD] = value

    def set_status(self, value):
        self._template[self._STATUS_FIELD] = value

    def set_flow_node_inventory_advertised_features(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ADVERTISED_FEATURES_FIELD] = value

    def set_port_number(self, value):
        self._template[self._PORT_NUMBER_FIELD] = value

    def set_address_tracker_addresses(self, value):
        self._template[self._ADDRESS_TRACKER_ADDRESSES_FIELD] = value

    def set_flow_node_inventory_state(self, value):
        self._template[self._FLOW_NODE_INVENTORY_STATE_FIELD] = value

    def set_flow_node_inventory_supported(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_FIELD] = value

    def set_advertised_features(self, value):
        self._template[self._ADVERTISED_FEATURES_FIELD] = value

    def set_flow_node_inventory_port_number(self, value):
        self._template[self._FLOW_NODE_INVENTORY_PORT_NUMBER_FIELD] = value

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_flow_node_inventory_name(self, value):
        self._template[self._FLOW_NODE_INVENTORY_NAME_FIELD] = value

    def set_flow_node_inventory_configuration(self, value):
        self._template[self._FLOW_NODE_INVENTORY_CONFIGURATION_FIELD] = value

    def set_flow_node_inventory_queue(self, value):
        self._template[self._FLOW_NODE_INVENTORY_QUEUE_FIELD] = value

    def set_current_speed(self, value):
        self._template[self._CURRENT_SPEED_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ADDRESSES_FIELD] = self.addresses.get_template(default=default)
            self._default_template[self._FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD] = self.flow_capable_node_connector_statistics.get_template(default=default)
            self._default_template[self._STATE_FIELD] = self.state.get_template(default=default)
            self._default_template[self._CONFIGURATION_FIELD] = self.configuration.get_template(default=default)
            self._default_template[self._QUEUE_FIELD] = self.queue.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ADDRESSES_FIELD] = self.addresses.get_template()
            self._template[self._FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD] = self.flow_capable_node_connector_statistics.get_template()
            self._template[self._STATE_FIELD] = self.state.get_template()
            self._template[self._CONFIGURATION_FIELD] = self.configuration.get_template()
            self._template[self._QUEUE_FIELD] = self.queue.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        addresses_payload = self.addresses.get_payload()
        if addresses_payload:
            payload[self._ADDRESSES_FIELD] = addresses_payload
        flow_capable_node_connector_statistics_payload = self.flow_capable_node_connector_statistics.get_payload()
        if flow_capable_node_connector_statistics_payload:
            payload[self._FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD] = flow_capable_node_connector_statistics_payload
        state_payload = self.state.get_payload()
        if state_payload:
            payload[self._STATE_FIELD] = state_payload
        configuration_payload = self.configuration.get_payload()
        if configuration_payload:
            payload[self._CONFIGURATION_FIELD] = configuration_payload
        queue_payload = self.queue.get_payload()
        if queue_payload:
            payload[self._QUEUE_FIELD] = queue_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_node_connector(self):
        
        payload = {self._NODE_CONNECTOR_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_node_connector(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_node_connector(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TIME_DIVISION_MULTIPLEX_CAPABLE(object):

    _TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD = "time-division-multiplex-capable"
    _OSPF_TOPOLOGY_INDICATION_FIELD = "ospf-topology:indication"
    _INDICATION_FIELD = "indication"
    _OSPF_TOPOLOGY_MINIMUM_LSP_BANDWIDTH_FIELD = "ospf-topology:minimum-lsp-bandwidth"
    _MINIMUM_LSP_BANDWIDTH_FIELD = "minimum-lsp-bandwidth"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_INDICATION_FIELD] = None
        self._template[self._INDICATION_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MINIMUM_LSP_BANDWIDTH_FIELD] = None
        self._template[self._MINIMUM_LSP_BANDWIDTH_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_indication(self, value):
        self._template[self._OSPF_TOPOLOGY_INDICATION_FIELD] = value

    def set_indication(self, value):
        self._template[self._INDICATION_FIELD] = value

    def set_ospf_topology_minimum_lsp_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_MINIMUM_LSP_BANDWIDTH_FIELD] = value

    def set_minimum_lsp_bandwidth(self, value):
        self._template[self._MINIMUM_LSP_BANDWIDTH_FIELD] = value

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

    def create_time_division_multiplex_capable(self):
        
        payload = {self._TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_time_division_multiplex_capable(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_time_division_multiplex_capable(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SWITCH_FEATURES(object):

    _SWITCH_FEATURES_FIELD = "switch-features"
    _FLOW_NODE_INVENTORY_MAX_TABLES_FIELD = "flow-node-inventory:max_tables"
    _MAX_BUFFERS_FIELD = "max_buffers"
    _FLOW_NODE_INVENTORY_CAPABILITIES_FIELD = "flow-node-inventory:capabilities"
    _MAX_TABLES_FIELD = "max_tables"
    _FLOW_NODE_INVENTORY_MAX_BUFFERS_FIELD = "flow-node-inventory:max_buffers"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_MAX_TABLES_FIELD] = None
        self._template[self._MAX_BUFFERS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_CAPABILITIES_FIELD] = None
        self._template[self._MAX_TABLES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_MAX_BUFFERS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_flow_node_inventory_max_tables(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MAX_TABLES_FIELD] = value

    def set_max_buffers(self, value):
        self._template[self._MAX_BUFFERS_FIELD] = value

    def set_flow_node_inventory_capabilities(self, value):
        self._template[self._FLOW_NODE_INVENTORY_CAPABILITIES_FIELD] = value

    def set_max_tables(self, value):
        self._template[self._MAX_TABLES_FIELD] = value

    def set_flow_node_inventory_max_buffers(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MAX_BUFFERS_FIELD] = value

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

    def create_switch_features(self):
        
        payload = {self._SWITCH_FEATURES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_switch_features(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_switch_features(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS(object):

    _FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD = "flow-capable-node-connector-queue-statistics"
    _OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMITTED_PACKETS_FIELD = "opendaylight-queue-statistics:transmitted-packets"
    _TRANSMITTED_BYTES_FIELD = "transmitted-bytes"
    _TRANSMISSION_ERRORS_FIELD = "transmission-errors"
    _OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMITTED_BYTES_FIELD = "opendaylight-queue-statistics:transmitted-bytes"
    _TRANSMITTED_PACKETS_FIELD = "transmitted-packets"
    _OPENDAYLIGHT_QUEUE_STATISTICS_DURATION_FIELD = "opendaylight-queue-statistics:duration"
    _OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMISSION_ERRORS_FIELD = "opendaylight-queue-statistics:transmission-errors"
    _DURATION_FIELD = "duration"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMITTED_PACKETS_FIELD] = None
        self._template[self._TRANSMITTED_BYTES_FIELD] = None
        self._template[self._TRANSMISSION_ERRORS_FIELD] = None
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMITTED_BYTES_FIELD] = None
        self._template[self._TRANSMITTED_PACKETS_FIELD] = None
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_DURATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMISSION_ERRORS_FIELD] = None
        self._template[self._DURATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._duration = DURATION()

    @property
    def duration(self):
        return self._duration

    def set_opendaylight_queue_statistics_transmitted_packets(self, value):
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMITTED_PACKETS_FIELD] = value

    def set_transmitted_bytes(self, value):
        self._template[self._TRANSMITTED_BYTES_FIELD] = value

    def set_transmission_errors(self, value):
        self._template[self._TRANSMISSION_ERRORS_FIELD] = value

    def set_opendaylight_queue_statistics_transmitted_bytes(self, value):
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMITTED_BYTES_FIELD] = value

    def set_transmitted_packets(self, value):
        self._template[self._TRANSMITTED_PACKETS_FIELD] = value

    def set_opendaylight_queue_statistics_duration(self, value):
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_DURATION_FIELD] = value

    def set_opendaylight_queue_statistics_transmission_errors(self, value):
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_TRANSMISSION_ERRORS_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._DURATION_FIELD] = self.duration.get_template(default=default)
            return self._default_template
        else:
            self._template[self._DURATION_FIELD] = self.duration.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        duration_payload = self.duration.get_payload()
        if duration_payload:
            payload[self._DURATION_FIELD] = duration_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_flow_capable_node_connector_queue_statistics(self):
        
        payload = {self._FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_capable_node_connector_queue_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_capable_node_connector_queue_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TCP_FLAG_MATCH(object):

    _TCP_FLAG_MATCH_FIELD = "tcp-flag-match"
    _TCP_FLAG_FIELD = "tcp-flag"
    _OPENDAYLIGHT_GROUP_STATISTICS_TCP_FLAG_FIELD = "opendaylight-group-statistics:tcp-flag"

    def __init__(self):
        self._template = {}
        self._template[self._TCP_FLAG_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TCP_FLAG_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_tcp_flag(self, value):
        self._template[self._TCP_FLAG_FIELD] = value

    def set_opendaylight_group_statistics_tcp_flag(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TCP_FLAG_FIELD] = value

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

    def create_tcp_flag_match(self):
        
        payload = {self._TCP_FLAG_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_tcp_flag_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_tcp_flag_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class FLOW_NODE_INVENTORY_LAYER_3_MATCH(object):

    _FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD = "flow-node-inventory:layer-3-match"
    _FLOW_NODE_INVENTORY_IPV6_ND_TLL_FIELD = "flow-node-inventory:ipv6-nd-tll"
    _FLOW_NODE_INVENTORY_IPV4_DESTINATION_FIELD = "flow-node-inventory:ipv4-destination"
    _FLOW_NODE_INVENTORY_ARP_TARGET_TRANSPORT_ADDRESS_FIELD = "flow-node-inventory:arp-target-transport-address"
    _FLOW_NODE_INVENTORY_ARP_SOURCE_HARDWARE_ADDRESS_FIELD = "flow-node-inventory:arp-source-hardware-address"
    _FLOW_NODE_INVENTORY_IPV4_SOURCE_FIELD = "flow-node-inventory:ipv4-source"
    _FLOW_NODE_INVENTORY_TUNNEL_IPV4_SOURCE_FIELD = "flow-node-inventory:tunnel-ipv4-source"
    _FLOW_NODE_INVENTORY_ARP_TARGET_HARDWARE_ADDRESS_FIELD = "flow-node-inventory:arp-target-hardware-address"
    _FLOW_NODE_INVENTORY_IPV6_LABEL_FIELD = "flow-node-inventory:ipv6-label"
    _FLOW_NODE_INVENTORY_TUNNEL_IPV4_DESTINATION_FIELD = "flow-node-inventory:tunnel-ipv4-destination"
    _FLOW_NODE_INVENTORY_IPV6_SOURCE_FIELD = "flow-node-inventory:ipv6-source"
    _FLOW_NODE_INVENTORY_IPV6_ND_SLL_FIELD = "flow-node-inventory:ipv6-nd-sll"
    _FLOW_NODE_INVENTORY_IPV6_ND_TARGET_FIELD = "flow-node-inventory:ipv6-nd-target"
    _FLOW_NODE_INVENTORY_IPV6_DESTINATION_FIELD = "flow-node-inventory:ipv6-destination"
    _FLOW_NODE_INVENTORY_ARP_OP_FIELD = "flow-node-inventory:arp-op"
    _FLOW_NODE_INVENTORY_ARP_SOURCE_TRANSPORT_ADDRESS_FIELD = "flow-node-inventory:arp-source-transport-address"
    _FLOW_NODE_INVENTORY_IPV6_EXT_HEADER_FIELD = "flow-node-inventory:ipv6-ext-header"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_IPV6_ND_TLL_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV4_DESTINATION_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ARP_TARGET_TRANSPORT_ADDRESS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ARP_SOURCE_HARDWARE_ADDRESS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV4_SOURCE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TUNNEL_IPV4_SOURCE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ARP_TARGET_HARDWARE_ADDRESS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV6_LABEL_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TUNNEL_IPV4_DESTINATION_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV6_SOURCE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV6_ND_SLL_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV6_ND_TARGET_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV6_DESTINATION_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ARP_OP_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ARP_SOURCE_TRANSPORT_ADDRESS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IPV6_EXT_HEADER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_flow_node_inventory_ipv6_nd_tll(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_ND_TLL_FIELD] = value

    def set_flow_node_inventory_ipv4_destination(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV4_DESTINATION_FIELD] = value

    def set_flow_node_inventory_arp_target_transport_address(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ARP_TARGET_TRANSPORT_ADDRESS_FIELD] = value

    def set_flow_node_inventory_arp_source_hardware_address(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ARP_SOURCE_HARDWARE_ADDRESS_FIELD] = value

    def set_flow_node_inventory_ipv4_source(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV4_SOURCE_FIELD] = value

    def set_flow_node_inventory_tunnel_ipv4_source(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TUNNEL_IPV4_SOURCE_FIELD] = value

    def set_flow_node_inventory_arp_target_hardware_address(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ARP_TARGET_HARDWARE_ADDRESS_FIELD] = value

    def set_flow_node_inventory_ipv6_label(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_LABEL_FIELD] = value

    def set_flow_node_inventory_tunnel_ipv4_destination(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TUNNEL_IPV4_DESTINATION_FIELD] = value

    def set_flow_node_inventory_ipv6_source(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_SOURCE_FIELD] = value

    def set_flow_node_inventory_ipv6_nd_sll(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_ND_SLL_FIELD] = value

    def set_flow_node_inventory_ipv6_nd_target(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_ND_TARGET_FIELD] = value

    def set_flow_node_inventory_ipv6_destination(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_DESTINATION_FIELD] = value

    def set_flow_node_inventory_arp_op(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ARP_OP_FIELD] = value

    def set_flow_node_inventory_arp_source_transport_address(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ARP_SOURCE_TRANSPORT_ADDRESS_FIELD] = value

    def set_flow_node_inventory_ipv6_ext_header(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IPV6_EXT_HEADER_FIELD] = value

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

    def create_flow_node_inventory_layer_3_match(self):
        
        payload = {self._FLOW_NODE_INVENTORY_LAYER_3_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_node_inventory_layer_3_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_node_inventory_layer_3_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TABLE_FEATURE_PROPERTIES(object):

    _TABLE_FEATURE_PROPERTIES_FIELD = "table-feature-properties"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD = "opendaylight-flow-table-statistics:table-feature-prop-type"
    _ORDER_FIELD = "order"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ORDER_FIELD = "opendaylight-flow-table-statistics:order"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD] = None
        self._template[self._ORDER_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ORDER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._opendaylight_flow_table_statistics_table_feature_prop_type = OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE()

    @property
    def opendaylight_flow_table_statistics_table_feature_prop_type(self):
        return self._opendaylight_flow_table_statistics_table_feature_prop_type

    def set_order(self, value):
        self._template[self._ORDER_FIELD] = value

    def set_opendaylight_flow_table_statistics_order(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ORDER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD] = self.opendaylight_flow_table_statistics_table_feature_prop_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD] = self.opendaylight_flow_table_statistics_table_feature_prop_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        opendaylight_flow_table_statistics_table_feature_prop_type_payload = self.opendaylight_flow_table_statistics_table_feature_prop_type.get_payload()
        if opendaylight_flow_table_statistics_table_feature_prop_type_payload:
            payload[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD] = opendaylight_flow_table_statistics_table_feature_prop_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_table_feature_properties(self):
        
        payload = {self._TABLE_FEATURE_PROPERTIES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_table_feature_properties(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_table_feature_properties(self):
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


class BGP_AF_IPV4_VPN_INSTANCES(object):

    _BGP_AF_IPV4_VPN_INSTANCES_FIELD = "bgp-af-ipv4-vpn-instances"
    _BGP_AF_IPV4_VPN_INSTANCE_FIELD = "bgp-af-ipv4-vpn-instance"
    _L3VPN_BGP_AF_IPV4_VPN_INSTANCE_FIELD = "l3vpn:bgp-af-ipv4-vpn-instance"

    def __init__(self):
        self._template = {}
        self._template[self._BGP_AF_IPV4_VPN_INSTANCE_FIELD] = None
        self._template[self._L3VPN_BGP_AF_IPV4_VPN_INSTANCE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bgp_af_ipv4_vpn_instance = BGP_AF_IPV4_VPN_INSTANCE()

    @property
    def bgp_af_ipv4_vpn_instance(self):
        return self._bgp_af_ipv4_vpn_instance

    def set_l3vpn_bgp_af_ipv4_vpn_instance(self, value):
        self._template[self._L3VPN_BGP_AF_IPV4_VPN_INSTANCE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BGP_AF_IPV4_VPN_INSTANCE_FIELD] = self.bgp_af_ipv4_vpn_instance.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BGP_AF_IPV4_VPN_INSTANCE_FIELD] = self.bgp_af_ipv4_vpn_instance.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bgp_af_ipv4_vpn_instance_payload = self.bgp_af_ipv4_vpn_instance.get_payload()
        if bgp_af_ipv4_vpn_instance_payload:
            payload[self._BGP_AF_IPV4_VPN_INSTANCE_FIELD] = bgp_af_ipv4_vpn_instance_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_af_ipv4_vpn_instances(self):
        
        payload = {self._BGP_AF_IPV4_VPN_INSTANCES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_af_ipv4_vpn_instances(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_af_ipv4_vpn_instances(self):
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


class OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE(object):

    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD = "opendaylight-flow-table-statistics:table-feature-prop-type"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTIONS_FIELD = "opendaylight-flow-table-statistics:instructions"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_MISS_FIELD = "opendaylight-flow-table-statistics:write-actions-miss"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_SETFIELD_FIELD = "opendaylight-flow-table-statistics:write-setfield"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLES_MISS_FIELD = "opendaylight-flow-table-statistics:tables-miss"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLES_FIELD = "opendaylight-flow-table-statistics:tables"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTIONS_MISS_FIELD = "opendaylight-flow-table-statistics:instructions-miss"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_MISS_FIELD = "opendaylight-flow-table-statistics:apply-actions-miss"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WILDCARD_SETFIELD_FIELD = "opendaylight-flow-table-statistics:wildcard-setfield"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_SETFIELD_MISS_FIELD = "opendaylight-flow-table-statistics:write-setfield-miss"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_SETFIELD_FIELD = "opendaylight-flow-table-statistics:apply-setfield"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_FIELD = "opendaylight-flow-table-statistics:write-actions"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_MATCH_SETFIELD_FIELD = "opendaylight-flow-table-statistics:match-setfield"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_FIELD = "opendaylight-flow-table-statistics:apply-actions"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_SETFIELD_MISS_FIELD = "opendaylight-flow-table-statistics:apply-setfield-miss"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_MISS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_SETFIELD_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLES_MISS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLES_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTIONS_MISS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_MISS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WILDCARD_SETFIELD_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_SETFIELD_MISS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_SETFIELD_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_MATCH_SETFIELD_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_SETFIELD_MISS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_flow_table_statistics_instructions(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTIONS_FIELD] = value

    def set_opendaylight_flow_table_statistics_write_actions_miss(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_MISS_FIELD] = value

    def set_opendaylight_flow_table_statistics_write_setfield(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_SETFIELD_FIELD] = value

    def set_opendaylight_flow_table_statistics_tables_miss(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLES_MISS_FIELD] = value

    def set_opendaylight_flow_table_statistics_tables(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLES_FIELD] = value

    def set_opendaylight_flow_table_statistics_instructions_miss(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTIONS_MISS_FIELD] = value

    def set_opendaylight_flow_table_statistics_apply_actions_miss(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_MISS_FIELD] = value

    def set_opendaylight_flow_table_statistics_wildcard_setfield(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WILDCARD_SETFIELD_FIELD] = value

    def set_opendaylight_flow_table_statistics_write_setfield_miss(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_SETFIELD_MISS_FIELD] = value

    def set_opendaylight_flow_table_statistics_apply_setfield(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_SETFIELD_FIELD] = value

    def set_opendaylight_flow_table_statistics_write_actions(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_FIELD] = value

    def set_opendaylight_flow_table_statistics_match_setfield(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_MATCH_SETFIELD_FIELD] = value

    def set_opendaylight_flow_table_statistics_apply_actions(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_FIELD] = value

    def set_opendaylight_flow_table_statistics_apply_setfield_miss(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_SETFIELD_MISS_FIELD] = value

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

    def create_opendaylight_flow_table_statistics_table_feature_prop_type(self):
        
        payload = {self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROP_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_opendaylight_flow_table_statistics_table_feature_prop_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_opendaylight_flow_table_statistics_table_feature_prop_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TERMINATION_POINT(object):

    _TERMINATION_POINT_FIELD = "termination-point"
    _OPENDAYLIGHT_TOPOLOGY_INVENTORY_INVENTORY_NODE_CONNECTOR_REF_FIELD = "opendaylight-topology-inventory:inventory-node-connector-ref"
    _IGP_TERMINATION_POINT_ATTRIBUTES_FIELD = "igp-termination-point-attributes"
    _INVENTORY_NODE_CONNECTOR_REF_FIELD = "inventory-node-connector-ref"
    _L3_UNICAST_IGP_TOPOLOGY_IGP_TERMINATION_POINT_ATTRIBUTES_FIELD = "l3-unicast-igp-topology:igp-termination-point-attributes"
    _TP_ID_FIELD = "tp-id"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_TOPOLOGY_INVENTORY_INVENTORY_NODE_CONNECTOR_REF_FIELD] = None
        self._template[self._IGP_TERMINATION_POINT_ATTRIBUTES_FIELD] = None
        self._template[self._INVENTORY_NODE_CONNECTOR_REF_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IGP_TERMINATION_POINT_ATTRIBUTES_FIELD] = None
        self._template[self._TP_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._igp_termination_point_attributes = IGP_TERMINATION_POINT_ATTRIBUTES()

    @property
    def igp_termination_point_attributes(self):
        return self._igp_termination_point_attributes

    def set_opendaylight_topology_inventory_inventory_node_connector_ref(self, value):
        self._template[self._OPENDAYLIGHT_TOPOLOGY_INVENTORY_INVENTORY_NODE_CONNECTOR_REF_FIELD] = value

    def set_inventory_node_connector_ref(self, value):
        self._template[self._INVENTORY_NODE_CONNECTOR_REF_FIELD] = value

    def set_l3_unicast_igp_topology_igp_termination_point_attributes(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IGP_TERMINATION_POINT_ATTRIBUTES_FIELD] = value

    def set_tp_id(self, value):
        self._template[self._TP_ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._IGP_TERMINATION_POINT_ATTRIBUTES_FIELD] = self.igp_termination_point_attributes.get_template(default=default)
            return self._default_template
        else:
            self._template[self._IGP_TERMINATION_POINT_ATTRIBUTES_FIELD] = self.igp_termination_point_attributes.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        igp_termination_point_attributes_payload = self.igp_termination_point_attributes.get_payload()
        if igp_termination_point_attributes_payload:
            payload[self._IGP_TERMINATION_POINT_ATTRIBUTES_FIELD] = igp_termination_point_attributes_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_termination_point(self):
        
        payload = {self._TERMINATION_POINT_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_termination_point(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_termination_point(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class INSTRUCTIONS(object):

    _INSTRUCTIONS_FIELD = "instructions"
    _INSTRUCTION_FIELD = "instruction"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD = "opendaylight-flow-table-statistics:instruction"

    def __init__(self):
        self._template = {}
        self._template[self._INSTRUCTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._instruction = INSTRUCTION()
        self._opendaylight_flow_table_statistics_instruction = OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION()

    @property
    def instruction(self):
        return self._instruction

    @property
    def opendaylight_flow_table_statistics_instruction(self):
        return self._opendaylight_flow_table_statistics_instruction

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._INSTRUCTION_FIELD] = self.instruction.get_template(default=default)
            self._default_template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = self.opendaylight_flow_table_statistics_instruction.get_template(default=default)
            return self._default_template
        else:
            self._template[self._INSTRUCTION_FIELD] = self.instruction.get_template()
            self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = self.opendaylight_flow_table_statistics_instruction.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        instruction_payload = self.instruction.get_payload()
        if instruction_payload:
            payload[self._INSTRUCTION_FIELD] = instruction_payload
        opendaylight_flow_table_statistics_instruction_payload = self.opendaylight_flow_table_statistics_instruction.get_payload()
        if opendaylight_flow_table_statistics_instruction_payload:
            payload[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = opendaylight_flow_table_statistics_instruction_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_instructions(self):
        
        payload = {self._INSTRUCTIONS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_instructions(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_instructions(self):
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


class SRLG(object):

    _SRLG_FIELD = "srlg"
    _OSPF_TOPOLOGY_INTERFACE_SWITCHING_CAPABILITIES_FIELD = "ospf-topology:interface-switching-capabilities"
    _SRLG_VALUES_FIELD = "srlg-values"
    _INTERFACE_SWITCHING_CAPABILITIES_FIELD = "interface-switching-capabilities"
    _OSPF_TOPOLOGY_SRLG_VALUES_FIELD = "ospf-topology:srlg-values"
    _OSPF_TOPOLOGY_LINK_PROTECTION_TYPE_FIELD = "ospf-topology:link-protection-type"
    _LINK_PROTECTION_TYPE_FIELD = "link-protection-type"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_INTERFACE_SWITCHING_CAPABILITIES_FIELD] = None
        self._template[self._SRLG_VALUES_FIELD] = None
        self._template[self._INTERFACE_SWITCHING_CAPABILITIES_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_SRLG_VALUES_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_LINK_PROTECTION_TYPE_FIELD] = None
        self._template[self._LINK_PROTECTION_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._srlg_values = SRLG_VALUES()
        self._interface_switching_capabilities = INTERFACE_SWITCHING_CAPABILITIES()

    @property
    def srlg_values(self):
        return self._srlg_values

    @property
    def interface_switching_capabilities(self):
        return self._interface_switching_capabilities

    def set_ospf_topology_interface_switching_capabilities(self, value):
        self._template[self._OSPF_TOPOLOGY_INTERFACE_SWITCHING_CAPABILITIES_FIELD] = value

    def set_ospf_topology_srlg_values(self, value):
        self._template[self._OSPF_TOPOLOGY_SRLG_VALUES_FIELD] = value

    def set_ospf_topology_link_protection_type(self, value):
        self._template[self._OSPF_TOPOLOGY_LINK_PROTECTION_TYPE_FIELD] = value

    def set_link_protection_type(self, value):
        self._template[self._LINK_PROTECTION_TYPE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._SRLG_VALUES_FIELD] = self.srlg_values.get_template(default=default)
            self._default_template[self._INTERFACE_SWITCHING_CAPABILITIES_FIELD] = self.interface_switching_capabilities.get_template(default=default)
            return self._default_template
        else:
            self._template[self._SRLG_VALUES_FIELD] = self.srlg_values.get_template()
            self._template[self._INTERFACE_SWITCHING_CAPABILITIES_FIELD] = self.interface_switching_capabilities.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        srlg_values_payload = self.srlg_values.get_payload()
        if srlg_values_payload:
            payload[self._SRLG_VALUES_FIELD] = srlg_values_payload
        interface_switching_capabilities_payload = self.interface_switching_capabilities.get_payload()
        if interface_switching_capabilities_payload:
            payload[self._INTERFACE_SWITCHING_CAPABILITIES_FIELD] = interface_switching_capabilities_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_srlg(self):
        
        payload = {self._SRLG_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_srlg(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_srlg(self):
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


class IGP_NODE_ATTRIBUTES(object):

    _IGP_NODE_ATTRIBUTES_FIELD = "igp-node-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_PREFIX_FIELD = "l3-unicast-igp-topology:prefix"
    _NAME_FIELD = "name"
    _PREFIX_FIELD = "prefix"
    _ISIS_NODE_ATTRIBUTES_FIELD = "isis-node-attributes"
    _OSPF_TOPOLOGY_OSPF_NODE_ATTRIBUTES_FIELD = "ospf-topology:ospf-node-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD = "l3-unicast-igp-topology:flag"
    _L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD = "l3-unicast-igp-topology:name"
    _L3_UNICAST_IGP_TOPOLOGY_ROUTER_ID_FIELD = "l3-unicast-igp-topology:router-id"
    _OSPF_NODE_ATTRIBUTES_FIELD = "ospf-node-attributes"
    _ISIS_TOPOLOGY_ISIS_NODE_ATTRIBUTES_FIELD = "isis-topology:isis-node-attributes"

    def __init__(self):
        self._template = {}
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_PREFIX_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._template[self._PREFIX_FIELD] = None
        self._template[self._ISIS_NODE_ATTRIBUTES_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_OSPF_NODE_ATTRIBUTES_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_ROUTER_ID_FIELD] = None
        self._template[self._OSPF_NODE_ATTRIBUTES_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ISIS_NODE_ATTRIBUTES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._prefix = PREFIX()
        self._isis_node_attributes = ISIS_NODE_ATTRIBUTES()
        self._ospf_node_attributes = OSPF_NODE_ATTRIBUTES()

    @property
    def prefix(self):
        return self._prefix

    @property
    def isis_node_attributes(self):
        return self._isis_node_attributes

    @property
    def ospf_node_attributes(self):
        return self._ospf_node_attributes

    def set_l3_unicast_igp_topology_prefix(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_PREFIX_FIELD] = value

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_ospf_topology_ospf_node_attributes(self, value):
        self._template[self._OSPF_TOPOLOGY_OSPF_NODE_ATTRIBUTES_FIELD] = value

    def set_l3_unicast_igp_topology_flag(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = value

    def set_l3_unicast_igp_topology_name(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD] = value

    def set_l3_unicast_igp_topology_router_id(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_ROUTER_ID_FIELD] = value

    def set_isis_topology_isis_node_attributes(self, value):
        self._template[self._ISIS_TOPOLOGY_ISIS_NODE_ATTRIBUTES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._PREFIX_FIELD] = self.prefix.get_template(default=default)
            self._default_template[self._ISIS_NODE_ATTRIBUTES_FIELD] = self.isis_node_attributes.get_template(default=default)
            self._default_template[self._OSPF_NODE_ATTRIBUTES_FIELD] = self.ospf_node_attributes.get_template(default=default)
            return self._default_template
        else:
            self._template[self._PREFIX_FIELD] = self.prefix.get_template()
            self._template[self._ISIS_NODE_ATTRIBUTES_FIELD] = self.isis_node_attributes.get_template()
            self._template[self._OSPF_NODE_ATTRIBUTES_FIELD] = self.ospf_node_attributes.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        prefix_payload = self.prefix.get_payload()
        if prefix_payload:
            payload[self._PREFIX_FIELD] = prefix_payload
        isis_node_attributes_payload = self.isis_node_attributes.get_payload()
        if isis_node_attributes_payload:
            payload[self._ISIS_NODE_ATTRIBUTES_FIELD] = isis_node_attributes_payload
        ospf_node_attributes_payload = self.ospf_node_attributes.get_payload()
        if ospf_node_attributes_payload:
            payload[self._OSPF_NODE_ATTRIBUTES_FIELD] = ospf_node_attributes_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_igp_node_attributes(self):
        
        payload = {self._IGP_NODE_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_igp_node_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_igp_node_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class OSPF_TOPOLOGY_ATTRIBUTES(object):

    _OSPF_TOPOLOGY_ATTRIBUTES_FIELD = "ospf-topology-attributes"
    _OSPF_TOPOLOGY_AREA_ID_FIELD = "ospf-topology:area-id"
    _AREA_ID_FIELD = "area-id"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_AREA_ID_FIELD] = None
        self._template[self._AREA_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_area_id(self, value):
        self._template[self._OSPF_TOPOLOGY_AREA_ID_FIELD] = value

    def set_area_id(self, value):
        self._template[self._AREA_ID_FIELD] = value

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

    def create_ospf_topology_attributes(self):
        
        payload = {self._OSPF_TOPOLOGY_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ospf_topology_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ospf_topology_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class USER_TOKENS(object):

    _USER_TOKENS_FIELD = "user_tokens"
    _TIMESTAMP_FIELD = "timestamp"
    _EXPIRATION_FIELD = "expiration"
    _TOKENID_FIELD = "tokenid"

    def __init__(self):
        self._template = {}
        self._template[self._TIMESTAMP_FIELD] = None
        self._template[self._EXPIRATION_FIELD] = None
        self._template[self._TOKENID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_timestamp(self, value):
        self._template[self._TIMESTAMP_FIELD] = value

    def set_expiration(self, value):
        self._template[self._EXPIRATION_FIELD] = value

    def set_tokenid(self, value):
        self._template[self._TOKENID_FIELD] = value

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

    def create_user_tokens(self):
        
        payload = {self._USER_TOKENS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_user_tokens(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_user_tokens(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BYTES(object):

    _BYTES_FIELD = "bytes"
    _RECEIVED_FIELD = "received"
    _TRANSMITTED_FIELD = "transmitted"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVED_FIELD = "opendaylight-port-statistics:received"
    _OPENDAYLIGHT_PORT_STATISTICS_TRANSMITTED_FIELD = "opendaylight-port-statistics:transmitted"

    def __init__(self):
        self._template = {}
        self._template[self._RECEIVED_FIELD] = None
        self._template[self._TRANSMITTED_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVED_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMITTED_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_received(self, value):
        self._template[self._RECEIVED_FIELD] = value

    def set_transmitted(self, value):
        self._template[self._TRANSMITTED_FIELD] = value

    def set_opendaylight_port_statistics_received(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVED_FIELD] = value

    def set_opendaylight_port_statistics_transmitted(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMITTED_FIELD] = value

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

    def create_bytes(self):
        
        payload = {self._BYTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bytes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bytes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SERVER(object):

    _SERVER_FIELD = "server"
    _IP_HOST_ADDRESS_FIELD = "ip-host-address"
    _IP_ADDRESS_FIELD = "ip-address"

    def __init__(self):
        self._template = {}
        self._template[self._IP_HOST_ADDRESS_FIELD] = None
        self._template[self._IP_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ip_host_address(self, value):
        self._template[self._IP_HOST_ADDRESS_FIELD] = value

    def set_ip_address(self, value):
        self._template[self._IP_ADDRESS_FIELD] = value

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

    def create_server(self):
        
        payload = {self._SERVER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_server(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_server(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TUNNEL(object):

    _TUNNEL_FIELD = "tunnel"
    _TUNNEL_MASK_FIELD = "tunnel-mask"
    _TUNNEL_ID_FIELD = "tunnel-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_TUNNEL_MASK_FIELD = "opendaylight-group-statistics:tunnel-mask"
    _OPENDAYLIGHT_GROUP_STATISTICS_TUNNEL_ID_FIELD = "opendaylight-group-statistics:tunnel-id"

    def __init__(self):
        self._template = {}
        self._template[self._TUNNEL_MASK_FIELD] = None
        self._template[self._TUNNEL_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TUNNEL_MASK_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TUNNEL_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_tunnel_mask(self, value):
        self._template[self._TUNNEL_MASK_FIELD] = value

    def set_tunnel_id(self, value):
        self._template[self._TUNNEL_ID_FIELD] = value

    def set_opendaylight_group_statistics_tunnel_mask(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TUNNEL_MASK_FIELD] = value

    def set_opendaylight_group_statistics_tunnel_id(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TUNNEL_ID_FIELD] = value

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

    def create_tunnel(self):
        
        payload = {self._TUNNEL_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_tunnel(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_tunnel(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PACKET_SWITCH_CAPABLE(object):

    _PACKET_SWITCH_CAPABLE_FIELD = "packet-switch-capable"
    _OSPF_TOPOLOGY_INTERFACE_MTU_FIELD = "ospf-topology:interface-mtu"
    _INTERFACE_MTU_FIELD = "interface-mtu"
    _OSPF_TOPOLOGY_MINIMUM_LSP_BANDWIDTH_FIELD = "ospf-topology:minimum-lsp-bandwidth"
    _MINIMUM_LSP_BANDWIDTH_FIELD = "minimum-lsp-bandwidth"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_INTERFACE_MTU_FIELD] = None
        self._template[self._INTERFACE_MTU_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MINIMUM_LSP_BANDWIDTH_FIELD] = None
        self._template[self._MINIMUM_LSP_BANDWIDTH_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_interface_mtu(self, value):
        self._template[self._OSPF_TOPOLOGY_INTERFACE_MTU_FIELD] = value

    def set_interface_mtu(self, value):
        self._template[self._INTERFACE_MTU_FIELD] = value

    def set_ospf_topology_minimum_lsp_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_MINIMUM_LSP_BANDWIDTH_FIELD] = value

    def set_minimum_lsp_bandwidth(self, value):
        self._template[self._MINIMUM_LSP_BANDWIDTH_FIELD] = value

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

    def create_packet_switch_capable(self):
        
        payload = {self._PACKET_SWITCH_CAPABLE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_packet_switch_capable(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_packet_switch_capable(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BGPPEERS(object):

    _BGPPEERS_FIELD = "bgpPeers"
    _BGPPEER_FIELD = "bgpPeer"
    _L3VPN_BGPPEER_FIELD = "l3vpn:bgpPeer"

    def __init__(self):
        self._template = {}
        self._template[self._BGPPEER_FIELD] = None
        self._template[self._L3VPN_BGPPEER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bgppeer = BGPPEER()

    @property
    def bgppeer(self):
        return self._bgppeer

    def set_l3vpn_bgppeer(self, value):
        self._template[self._L3VPN_BGPPEER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BGPPEER_FIELD] = self.bgppeer.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BGPPEER_FIELD] = self.bgppeer.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bgppeer_payload = self.bgppeer.get_payload()
        if bgppeer_payload:
            payload[self._BGPPEER_FIELD] = bgppeer_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgppeers(self):
        
        payload = {self._BGPPEERS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgppeers(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgppeers(self):
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


class FLOW_HASH_ID_MAP(object):

    _FLOW_HASH_ID_MAP_FIELD = "flow-hash-id-map"
    _FLOW_NODE_INVENTORY_HASH_FIELD = "flow-node-inventory:hash"
    _FLOW_ID_FIELD = "flow-id"
    _HASH_FIELD = "hash"
    _FLOW_NODE_INVENTORY_FLOW_ID_FIELD = "flow-node-inventory:flow-id"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_HASH_FIELD] = None
        self._template[self._FLOW_ID_FIELD] = None
        self._template[self._HASH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_FLOW_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_flow_node_inventory_hash(self, value):
        self._template[self._FLOW_NODE_INVENTORY_HASH_FIELD] = value

    def set_flow_id(self, value):
        self._template[self._FLOW_ID_FIELD] = value

    def set_hash(self, value):
        self._template[self._HASH_FIELD] = value

    def set_flow_node_inventory_flow_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_FLOW_ID_FIELD] = value

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

    def create_flow_hash_id_map(self):
        
        payload = {self._FLOW_HASH_ID_MAP_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_hash_id_map(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_hash_id_map(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PBB(object):

    _PBB_FIELD = "pbb"
    _PBB_ISID_FIELD = "pbb-isid"
    _OPENDAYLIGHT_GROUP_STATISTICS_PBB_MASK_FIELD = "opendaylight-group-statistics:pbb-mask"
    _OPENDAYLIGHT_GROUP_STATISTICS_PBB_ISID_FIELD = "opendaylight-group-statistics:pbb-isid"
    _PBB_MASK_FIELD = "pbb-mask"

    def __init__(self):
        self._template = {}
        self._template[self._PBB_ISID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PBB_MASK_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PBB_ISID_FIELD] = None
        self._template[self._PBB_MASK_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_pbb_isid(self, value):
        self._template[self._PBB_ISID_FIELD] = value

    def set_opendaylight_group_statistics_pbb_mask(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PBB_MASK_FIELD] = value

    def set_opendaylight_group_statistics_pbb_isid(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PBB_ISID_FIELD] = value

    def set_pbb_mask(self, value):
        self._template[self._PBB_MASK_FIELD] = value

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

    def create_pbb(self):
        
        payload = {self._PBB_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_pbb(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_pbb(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ICMPV6_MATCH(object):

    _ICMPV6_MATCH_FIELD = "icmpv6-match"
    _OPENDAYLIGHT_GROUP_STATISTICS_ICMPV6_CODE_FIELD = "opendaylight-group-statistics:icmpv6-code"
    _ICMPV6_TYPE_FIELD = "icmpv6-type"
    _ICMPV6_CODE_FIELD = "icmpv6-code"
    _OPENDAYLIGHT_GROUP_STATISTICS_ICMPV6_TYPE_FIELD = "opendaylight-group-statistics:icmpv6-type"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV6_CODE_FIELD] = None
        self._template[self._ICMPV6_TYPE_FIELD] = None
        self._template[self._ICMPV6_CODE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV6_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_icmpv6_code(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV6_CODE_FIELD] = value

    def set_icmpv6_type(self, value):
        self._template[self._ICMPV6_TYPE_FIELD] = value

    def set_icmpv6_code(self, value):
        self._template[self._ICMPV6_CODE_FIELD] = value

    def set_opendaylight_group_statistics_icmpv6_type(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV6_TYPE_FIELD] = value

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

    def create_icmpv6_match(self):
        
        payload = {self._ICMPV6_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_icmpv6_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_icmpv6_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class INSTRUCTION(object):

    _INSTRUCTION_FIELD = "instruction"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD = "opendaylight-flow-table-statistics:instruction"
    _ORDER_FIELD = "order"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ORDER_FIELD = "opendaylight-flow-table-statistics:order"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = None
        self._template[self._ORDER_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ORDER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._opendaylight_flow_table_statistics_instruction = OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION()

    @property
    def opendaylight_flow_table_statistics_instruction(self):
        return self._opendaylight_flow_table_statistics_instruction

    def set_order(self, value):
        self._template[self._ORDER_FIELD] = value

    def set_opendaylight_flow_table_statistics_order(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_ORDER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = self.opendaylight_flow_table_statistics_instruction.get_template(default=default)
            return self._default_template
        else:
            self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = self.opendaylight_flow_table_statistics_instruction.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        opendaylight_flow_table_statistics_instruction_payload = self.opendaylight_flow_table_statistics_instruction.get_payload()
        if opendaylight_flow_table_statistics_instruction_payload:
            payload[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD] = opendaylight_flow_table_statistics_instruction_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_instruction(self):
        
        payload = {self._INSTRUCTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_instruction(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_instruction(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SRLG_VALUES(object):

    _SRLG_VALUES_FIELD = "srlg-values"
    _OSPF_TOPOLOGY_SRLG_VALUE_FIELD = "ospf-topology:srlg-value"
    _SRLG_VALUE_FIELD = "srlg-value"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_SRLG_VALUE_FIELD] = None
        self._template[self._SRLG_VALUE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_srlg_value(self, value):
        self._template[self._OSPF_TOPOLOGY_SRLG_VALUE_FIELD] = value

    def set_srlg_value(self, value):
        self._template[self._SRLG_VALUE_FIELD] = value

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

    def create_srlg_values(self):
        
        payload = {self._SRLG_VALUES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_srlg_values(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_srlg_values(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VALIDATION_TIME(object):

    _VALIDATION_TIME_FIELD = "validation-time"
    _PREFIX_VALIDATION_TIME_FIELD = "prefix-validation-time"
    _DISABLE_FIELD = "disable"

    def __init__(self):
        self._template = {}
        self._template[self._PREFIX_VALIDATION_TIME_FIELD] = None
        self._template[self._DISABLE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_prefix_validation_time(self, value):
        self._template[self._PREFIX_VALIDATION_TIME_FIELD] = value

    def set_disable(self, value):
        self._template[self._DISABLE_FIELD] = value

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

    def create_validation_time(self):
        
        payload = {self._VALIDATION_TIME_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_validation_time(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_validation_time(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TED(object):

    _TED_FIELD = "ted"
    _SRLG_FIELD = "srlg"
    _OSPF_TOPOLOGY_UNRESERVED_BANDWIDTH_FIELD = "ospf-topology:unreserved-bandwidth"
    _COLOR_FIELD = "color"
    _MAX_LINK_BANDWIDTH_FIELD = "max-link-bandwidth"
    _TE_DEFAULT_METRIC_FIELD = "te-default-metric"
    _MAX_RESV_LINK_BANDWIDTH_FIELD = "max-resv-link-bandwidth"
    _OSPF_TOPOLOGY_COLOR_FIELD = "ospf-topology:color"
    _OSPF_TOPOLOGY_TE_DEFAULT_METRIC_FIELD = "ospf-topology:te-default-metric"
    _OSPF_TOPOLOGY_SRLG_FIELD = "ospf-topology:srlg"
    _OSPF_TOPOLOGY_MAX_RESV_LINK_BANDWIDTH_FIELD = "ospf-topology:max-resv-link-bandwidth"
    _UNRESERVED_BANDWIDTH_FIELD = "unreserved-bandwidth"
    _OSPF_TOPOLOGY_MAX_LINK_BANDWIDTH_FIELD = "ospf-topology:max-link-bandwidth"

    def __init__(self):
        self._template = {}
        self._template[self._SRLG_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_UNRESERVED_BANDWIDTH_FIELD] = None
        self._template[self._COLOR_FIELD] = None
        self._template[self._MAX_LINK_BANDWIDTH_FIELD] = None
        self._template[self._TE_DEFAULT_METRIC_FIELD] = None
        self._template[self._MAX_RESV_LINK_BANDWIDTH_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_COLOR_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_TE_DEFAULT_METRIC_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_SRLG_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MAX_RESV_LINK_BANDWIDTH_FIELD] = None
        self._template[self._UNRESERVED_BANDWIDTH_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MAX_LINK_BANDWIDTH_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._srlg = SRLG()
        self._unreserved_bandwidth = UNRESERVED_BANDWIDTH()

    @property
    def srlg(self):
        return self._srlg

    @property
    def unreserved_bandwidth(self):
        return self._unreserved_bandwidth

    def set_ospf_topology_unreserved_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_UNRESERVED_BANDWIDTH_FIELD] = value

    def set_color(self, value):
        self._template[self._COLOR_FIELD] = value

    def set_max_link_bandwidth(self, value):
        self._template[self._MAX_LINK_BANDWIDTH_FIELD] = value

    def set_te_default_metric(self, value):
        self._template[self._TE_DEFAULT_METRIC_FIELD] = value

    def set_max_resv_link_bandwidth(self, value):
        self._template[self._MAX_RESV_LINK_BANDWIDTH_FIELD] = value

    def set_ospf_topology_color(self, value):
        self._template[self._OSPF_TOPOLOGY_COLOR_FIELD] = value

    def set_ospf_topology_te_default_metric(self, value):
        self._template[self._OSPF_TOPOLOGY_TE_DEFAULT_METRIC_FIELD] = value

    def set_ospf_topology_srlg(self, value):
        self._template[self._OSPF_TOPOLOGY_SRLG_FIELD] = value

    def set_ospf_topology_max_resv_link_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_MAX_RESV_LINK_BANDWIDTH_FIELD] = value

    def set_ospf_topology_max_link_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_MAX_LINK_BANDWIDTH_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._SRLG_FIELD] = self.srlg.get_template(default=default)
            self._default_template[self._UNRESERVED_BANDWIDTH_FIELD] = self.unreserved_bandwidth.get_template(default=default)
            return self._default_template
        else:
            self._template[self._SRLG_FIELD] = self.srlg.get_template()
            self._template[self._UNRESERVED_BANDWIDTH_FIELD] = self.unreserved_bandwidth.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        srlg_payload = self.srlg.get_payload()
        if srlg_payload:
            payload[self._SRLG_FIELD] = srlg_payload
        unreserved_bandwidth_payload = self.unreserved_bandwidth.get_payload()
        if unreserved_bandwidth_payload:
            payload[self._UNRESERVED_BANDWIDTH_FIELD] = unreserved_bandwidth_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ted(self):
        
        payload = {self._TED_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ted(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ted(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MODULE(object):

    _MODULE_FIELD = "module"
    _CONFIGURATION_FIELD = "configuration"
    _TYPE_FIELD = "type"
    _NAME_FIELD = "name"

    def __init__(self):
        self._template = {}
        self._template[self._CONFIGURATION_FIELD] = None
        self._template[self._TYPE_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._configuration = CONFIGURATION()

    @property
    def configuration(self):
        return self._configuration

    def set_type(self, value):
        self._template[self._TYPE_FIELD] = value

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._CONFIGURATION_FIELD] = self.configuration.get_template(default=default)
            return self._default_template
        else:
            self._template[self._CONFIGURATION_FIELD] = self.configuration.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        configuration_payload = self.configuration.get_payload()
        if configuration_payload:
            payload[self._CONFIGURATION_FIELD] = configuration_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_module(self):
        
        payload = {self._MODULE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_module(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_module(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SUPPORTING_NODE(object):

    _SUPPORTING_NODE_FIELD = "supporting-node"
    _TOPOLOGY_REF_FIELD = "topology-ref"
    _NODE_REF_FIELD = "node-ref"

    def __init__(self):
        self._template = {}
        self._template[self._TOPOLOGY_REF_FIELD] = None
        self._template[self._NODE_REF_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_topology_ref(self, value):
        self._template[self._TOPOLOGY_REF_FIELD] = value

    def set_node_ref(self, value):
        self._template[self._NODE_REF_FIELD] = value

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

    def create_supporting_node(self):
        
        payload = {self._SUPPORTING_NODE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_supporting_node(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_supporting_node(self):
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


class DURATION(object):

    _DURATION_FIELD = "duration"
    _OPENDAYLIGHT_GROUP_STATISTICS_NANOSECOND_FIELD = "opendaylight-group-statistics:nanosecond"
    _SECOND_FIELD = "second"
    _NANOSECOND_FIELD = "nanosecond"
    _OPENDAYLIGHT_GROUP_STATISTICS_SECOND_FIELD = "opendaylight-group-statistics:second"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_NANOSECOND_FIELD] = None
        self._template[self._SECOND_FIELD] = None
        self._template[self._NANOSECOND_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SECOND_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_nanosecond(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_NANOSECOND_FIELD] = value

    def set_second(self, value):
        self._template[self._SECOND_FIELD] = value

    def set_nanosecond(self, value):
        self._template[self._NANOSECOND_FIELD] = value

    def set_opendaylight_group_statistics_second(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SECOND_FIELD] = value

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

    def create_duration(self):
        
        payload = {self._DURATION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_duration(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_duration(self):
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


class FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS(object):

    _FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD = "flow-capable-node-connector-statistics"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_OVER_RUN_ERROR_FIELD = "opendaylight-port-statistics:receive-over-run-error"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_CRC_ERROR_FIELD = "opendaylight-port-statistics:receive-crc-error"
    _OPENDAYLIGHT_PORT_STATISTICS_TRANSMIT_ERRORS_FIELD = "opendaylight-port-statistics:transmit-errors"
    _OPENDAYLIGHT_PORT_STATISTICS_COLLISION_COUNT_FIELD = "opendaylight-port-statistics:collision-count"
    _BYTES_FIELD = "bytes"
    _RECEIVE_DROPS_FIELD = "receive-drops"
    _DURATION_FIELD = "duration"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_FRAME_ERROR_FIELD = "opendaylight-port-statistics:receive-frame-error"
    _OPENDAYLIGHT_PORT_STATISTICS_DURATION_FIELD = "opendaylight-port-statistics:duration"
    _OPENDAYLIGHT_PORT_STATISTICS_BYTES_FIELD = "opendaylight-port-statistics:bytes"
    _OPENDAYLIGHT_PORT_STATISTICS_PACKETS_FIELD = "opendaylight-port-statistics:packets"
    _RECEIVE_CRC_ERROR_FIELD = "receive-crc-error"
    _RECEIVE_FRAME_ERROR_FIELD = "receive-frame-error"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_ERRORS_FIELD = "opendaylight-port-statistics:receive-errors"
    _RECEIVE_ERRORS_FIELD = "receive-errors"
    _COLLISION_COUNT_FIELD = "collision-count"
    _TRANSMIT_ERRORS_FIELD = "transmit-errors"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_DROPS_FIELD = "opendaylight-port-statistics:receive-drops"
    _RECEIVE_OVER_RUN_ERROR_FIELD = "receive-over-run-error"
    _PACKETS_FIELD = "packets"
    _OPENDAYLIGHT_PORT_STATISTICS_TRANSMIT_DROPS_FIELD = "opendaylight-port-statistics:transmit-drops"
    _TRANSMIT_DROPS_FIELD = "transmit-drops"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_OVER_RUN_ERROR_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_CRC_ERROR_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMIT_ERRORS_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_COLLISION_COUNT_FIELD] = None
        self._template[self._BYTES_FIELD] = None
        self._template[self._RECEIVE_DROPS_FIELD] = None
        self._template[self._DURATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_FRAME_ERROR_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_DURATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_BYTES_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_PACKETS_FIELD] = None
        self._template[self._RECEIVE_CRC_ERROR_FIELD] = None
        self._template[self._RECEIVE_FRAME_ERROR_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_ERRORS_FIELD] = None
        self._template[self._RECEIVE_ERRORS_FIELD] = None
        self._template[self._COLLISION_COUNT_FIELD] = None
        self._template[self._TRANSMIT_ERRORS_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_DROPS_FIELD] = None
        self._template[self._RECEIVE_OVER_RUN_ERROR_FIELD] = None
        self._template[self._PACKETS_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMIT_DROPS_FIELD] = None
        self._template[self._TRANSMIT_DROPS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bytes = BYTES()
        self._duration = DURATION()
        self._packets = PACKETS()

    @property
    def bytes(self):
        return self._bytes

    @property
    def duration(self):
        return self._duration

    @property
    def packets(self):
        return self._packets

    def set_opendaylight_port_statistics_receive_over_run_error(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_OVER_RUN_ERROR_FIELD] = value

    def set_opendaylight_port_statistics_receive_crc_error(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_CRC_ERROR_FIELD] = value

    def set_opendaylight_port_statistics_transmit_errors(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMIT_ERRORS_FIELD] = value

    def set_opendaylight_port_statistics_collision_count(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_COLLISION_COUNT_FIELD] = value

    def set_receive_drops(self, value):
        self._template[self._RECEIVE_DROPS_FIELD] = value

    def set_opendaylight_port_statistics_receive_frame_error(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_FRAME_ERROR_FIELD] = value

    def set_opendaylight_port_statistics_duration(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_DURATION_FIELD] = value

    def set_opendaylight_port_statistics_bytes(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_BYTES_FIELD] = value

    def set_opendaylight_port_statistics_packets(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_PACKETS_FIELD] = value

    def set_receive_crc_error(self, value):
        self._template[self._RECEIVE_CRC_ERROR_FIELD] = value

    def set_receive_frame_error(self, value):
        self._template[self._RECEIVE_FRAME_ERROR_FIELD] = value

    def set_opendaylight_port_statistics_receive_errors(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_ERRORS_FIELD] = value

    def set_receive_errors(self, value):
        self._template[self._RECEIVE_ERRORS_FIELD] = value

    def set_collision_count(self, value):
        self._template[self._COLLISION_COUNT_FIELD] = value

    def set_transmit_errors(self, value):
        self._template[self._TRANSMIT_ERRORS_FIELD] = value

    def set_opendaylight_port_statistics_receive_drops(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVE_DROPS_FIELD] = value

    def set_receive_over_run_error(self, value):
        self._template[self._RECEIVE_OVER_RUN_ERROR_FIELD] = value

    def set_opendaylight_port_statistics_transmit_drops(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMIT_DROPS_FIELD] = value

    def set_transmit_drops(self, value):
        self._template[self._TRANSMIT_DROPS_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BYTES_FIELD] = self.bytes.get_template(default=default)
            self._default_template[self._DURATION_FIELD] = self.duration.get_template(default=default)
            self._default_template[self._PACKETS_FIELD] = self.packets.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BYTES_FIELD] = self.bytes.get_template()
            self._template[self._DURATION_FIELD] = self.duration.get_template()
            self._template[self._PACKETS_FIELD] = self.packets.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bytes_payload = self.bytes.get_payload()
        if bytes_payload:
            payload[self._BYTES_FIELD] = bytes_payload
        duration_payload = self.duration.get_payload()
        if duration_payload:
            payload[self._DURATION_FIELD] = duration_payload
        packets_payload = self.packets.get_payload()
        if packets_payload:
            payload[self._PACKETS_FIELD] = packets_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_flow_capable_node_connector_statistics(self):
        
        payload = {self._FLOW_CAPABLE_NODE_CONNECTOR_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_capable_node_connector_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_capable_node_connector_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class INSTRUCTION_TYPE(object):

    _INSTRUCTION_TYPE_FIELD = "instruction-type"
    _FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD = "flow-node-inventory:support-state"
    _INSTRUCTION_FIELD = "instruction"
    _SUPPORT_STATE_FIELD = "support-state"
    _FLOW_NODE_INVENTORY_INSTRUCTION_FIELD = "flow-node-inventory:instruction"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD] = None
        self._template[self._INSTRUCTION_FIELD] = None
        self._template[self._SUPPORT_STATE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_INSTRUCTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._instruction = INSTRUCTION()

    @property
    def instruction(self):
        return self._instruction

    def set_flow_node_inventory_support_state(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD] = value

    def set_support_state(self, value):
        self._template[self._SUPPORT_STATE_FIELD] = value

    def set_flow_node_inventory_instruction(self, value):
        self._template[self._FLOW_NODE_INVENTORY_INSTRUCTION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._INSTRUCTION_FIELD] = self.instruction.get_template(default=default)
            return self._default_template
        else:
            self._template[self._INSTRUCTION_FIELD] = self.instruction.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        instruction_payload = self.instruction.get_payload()
        if instruction_payload:
            payload[self._INSTRUCTION_FIELD] = instruction_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_instruction_type(self):
        
        payload = {self._INSTRUCTION_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_instruction_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_instruction_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BGP_AF_IPV6_VPN_INSTANCE(object):

    _BGP_AF_IPV6_VPN_INSTANCE_FIELD = "bgp-af-ipv6-vpn-instance"
    _ROUTER_ID_FIELD = "router-id"
    _L3VPN_ROUTER_ID_FIELD = "l3vpn:router-id"
    _AUTO_FRR_FIELD = "auto-frr"
    _L3VPN_VPN_INSTANCE_NAME_FIELD = "l3vpn:vpn-instance-name"
    _BGPPEERS_FIELD = "bgpPeers"
    _VPN_INSTANCE_NAME_FIELD = "vpn-instance-name"
    _L3VPN_BGPPEERS_FIELD = "l3vpn:bgpPeers"
    _L3VPN_AUTO_FRR_FIELD = "l3vpn:auto-frr"

    def __init__(self):
        self._template = {}
        self._template[self._ROUTER_ID_FIELD] = None
        self._template[self._L3VPN_ROUTER_ID_FIELD] = None
        self._template[self._AUTO_FRR_FIELD] = None
        self._template[self._L3VPN_VPN_INSTANCE_NAME_FIELD] = None
        self._template[self._BGPPEERS_FIELD] = None
        self._template[self._VPN_INSTANCE_NAME_FIELD] = None
        self._template[self._L3VPN_BGPPEERS_FIELD] = None
        self._template[self._L3VPN_AUTO_FRR_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._router_id = ROUTER_ID()
        self._bgppeers = BGPPEERS()

    @property
    def router_id(self):
        return self._router_id

    @property
    def bgppeers(self):
        return self._bgppeers

    def set_l3vpn_router_id(self, value):
        self._template[self._L3VPN_ROUTER_ID_FIELD] = value

    def set_auto_frr(self, value):
        self._template[self._AUTO_FRR_FIELD] = value

    def set_l3vpn_vpn_instance_name(self, value):
        self._template[self._L3VPN_VPN_INSTANCE_NAME_FIELD] = value

    def set_vpn_instance_name(self, value):
        self._template[self._VPN_INSTANCE_NAME_FIELD] = value

    def set_l3vpn_bgppeers(self, value):
        self._template[self._L3VPN_BGPPEERS_FIELD] = value

    def set_l3vpn_auto_frr(self, value):
        self._template[self._L3VPN_AUTO_FRR_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ROUTER_ID_FIELD] = self.router_id.get_template(default=default)
            self._default_template[self._BGPPEERS_FIELD] = self.bgppeers.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ROUTER_ID_FIELD] = self.router_id.get_template()
            self._template[self._BGPPEERS_FIELD] = self.bgppeers.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        router_id_payload = self.router_id.get_payload()
        if router_id_payload:
            payload[self._ROUTER_ID_FIELD] = router_id_payload
        bgppeers_payload = self.bgppeers.get_payload()
        if bgppeers_payload:
            payload[self._BGPPEERS_FIELD] = bgppeers_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bgp_af_ipv6_vpn_instance(self):
        
        payload = {self._BGP_AF_IPV6_VPN_INSTANCE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgp_af_ipv6_vpn_instance(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgp_af_ipv6_vpn_instance(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class OSPF_TOPOLOGY_ROUTER_TYPE(object):

    _OSPF_TOPOLOGY_ROUTER_TYPE_FIELD = "ospf-topology:router-type"
    _OSPF_TOPOLOGY_INTERNAL_FIELD = "ospf-topology:internal"
    _OSPF_TOPOLOGY_ASBR_FIELD = "ospf-topology:asbr"
    _OSPF_TOPOLOGY_ABR_FIELD = "ospf-topology:abr"
    _OSPF_TOPOLOGY_PSEUDONODE_FIELD = "ospf-topology:pseudonode"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_INTERNAL_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_ASBR_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_ABR_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_PSEUDONODE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_internal(self, value):
        self._template[self._OSPF_TOPOLOGY_INTERNAL_FIELD] = value

    def set_ospf_topology_asbr(self, value):
        self._template[self._OSPF_TOPOLOGY_ASBR_FIELD] = value

    def set_ospf_topology_abr(self, value):
        self._template[self._OSPF_TOPOLOGY_ABR_FIELD] = value

    def set_ospf_topology_pseudonode(self, value):
        self._template[self._OSPF_TOPOLOGY_PSEUDONODE_FIELD] = value

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

    def create_ospf_topology_router_type(self):
        
        payload = {self._OSPF_TOPOLOGY_ROUTER_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ospf_topology_router_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ospf_topology_router_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class L3VPN_CONFIG_TYPE(object):

    _L3VPN_CONFIG_TYPE_FIELD = "l3vpn:config-type"
    _L3VPN_ENABLE_AUTO_SELECT_FIELD = "l3vpn:enable-auto-select"
    _L3VPN_IP_ADDRESS_FIELD = "l3vpn:ip-address"

    def __init__(self):
        self._template = {}
        self._template[self._L3VPN_ENABLE_AUTO_SELECT_FIELD] = None
        self._template[self._L3VPN_IP_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_l3vpn_enable_auto_select(self, value):
        self._template[self._L3VPN_ENABLE_AUTO_SELECT_FIELD] = value

    def set_l3vpn_ip_address(self, value):
        self._template[self._L3VPN_IP_ADDRESS_FIELD] = value

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

    def create_l3vpn_config_type(self):
        
        payload = {self._L3VPN_CONFIG_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_l3vpn_config_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_l3vpn_config_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class METADATA(object):

    _METADATA_FIELD = "metadata"
    _OPENDAYLIGHT_GROUP_STATISTICS_METADATA_MASK_FIELD = "opendaylight-group-statistics:metadata-mask"
    _OPENDAYLIGHT_GROUP_STATISTICS_METADATA_FIELD = "opendaylight-group-statistics:metadata"
    _METADATA_MASK_FIELD = "metadata-mask"
    _METADATA_FIELD = "metadata"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_METADATA_MASK_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_METADATA_FIELD] = None
        self._template[self._METADATA_MASK_FIELD] = None
        self._template[self._METADATA_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_metadata_mask(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_METADATA_MASK_FIELD] = value

    def set_opendaylight_group_statistics_metadata(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_METADATA_FIELD] = value

    def set_metadata_mask(self, value):
        self._template[self._METADATA_MASK_FIELD] = value

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

    def create_metadata(self):
        
        payload = {self._METADATA_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_metadata(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_metadata(self):
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


class STATE(object):

    _STATE_FIELD = "state"
    _FLOW_NODE_INVENTORY_LINK_DOWN_FIELD = "flow-node-inventory:link-down"
    _FLOW_NODE_INVENTORY_LIVE_FIELD = "flow-node-inventory:live"
    _LIVE_FIELD = "live"
    _LINK_DOWN_FIELD = "link-down"
    _FLOW_NODE_INVENTORY_BLOCKED_FIELD = "flow-node-inventory:blocked"
    _BLOCKED_FIELD = "blocked"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_LINK_DOWN_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_LIVE_FIELD] = None
        self._template[self._LIVE_FIELD] = None
        self._template[self._LINK_DOWN_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_BLOCKED_FIELD] = None
        self._template[self._BLOCKED_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_flow_node_inventory_link_down(self, value):
        self._template[self._FLOW_NODE_INVENTORY_LINK_DOWN_FIELD] = value

    def set_flow_node_inventory_live(self, value):
        self._template[self._FLOW_NODE_INVENTORY_LIVE_FIELD] = value

    def set_live(self, value):
        self._template[self._LIVE_FIELD] = value

    def set_link_down(self, value):
        self._template[self._LINK_DOWN_FIELD] = value

    def set_flow_node_inventory_blocked(self, value):
        self._template[self._FLOW_NODE_INVENTORY_BLOCKED_FIELD] = value

    def set_blocked(self, value):
        self._template[self._BLOCKED_FIELD] = value

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

    def create_state(self):
        
        payload = {self._STATE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_state(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_state(self):
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


class BUCKETS(object):

    _BUCKETS_FIELD = "buckets"
    _OPENDAYLIGHT_GROUP_STATISTICS_BUCKET_FIELD = "opendaylight-group-statistics:bucket"
    _BUCKET_FIELD = "bucket"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKET_FIELD] = None
        self._template[self._BUCKET_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bucket = BUCKET()

    @property
    def bucket(self):
        return self._bucket

    def set_opendaylight_group_statistics_bucket(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKET_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BUCKET_FIELD] = self.bucket.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BUCKET_FIELD] = self.bucket.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bucket_payload = self.bucket.get_payload()
        if bucket_payload:
            payload[self._BUCKET_FIELD] = bucket_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_buckets(self):
        
        payload = {self._BUCKETS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_buckets(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_buckets(self):
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


class TOPOLOGY_TYPES(object):

    _TOPOLOGY_TYPES_FIELD = "topology-types"
    _L3_UNICAST_IGP_TOPOLOGY_FIELD = "l3-unicast-igp-topology"
    _L3_UNICAST_IGP_TOPOLOGY_L3_UNICAST_IGP_TOPOLOGY_FIELD = "l3-unicast-igp-topology:l3-unicast-igp-topology"

    def __init__(self):
        self._template = {}
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_L3_UNICAST_IGP_TOPOLOGY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._l3_unicast_igp_topology = L3_UNICAST_IGP_TOPOLOGY()

    @property
    def l3_unicast_igp_topology(self):
        return self._l3_unicast_igp_topology

    def set_l3_unicast_igp_topology_l3_unicast_igp_topology(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_L3_UNICAST_IGP_TOPOLOGY_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._L3_UNICAST_IGP_TOPOLOGY_FIELD] = self.l3_unicast_igp_topology.get_template(default=default)
            return self._default_template
        else:
            self._template[self._L3_UNICAST_IGP_TOPOLOGY_FIELD] = self.l3_unicast_igp_topology.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        l3_unicast_igp_topology_payload = self.l3_unicast_igp_topology.get_payload()
        if l3_unicast_igp_topology_payload:
            payload[self._L3_UNICAST_IGP_TOPOLOGY_FIELD] = l3_unicast_igp_topology_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_topology_types(self):
        
        payload = {self._TOPOLOGY_TYPES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_topology_types(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_topology_types(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class OPENDAYLIGHT_GROUP_STATISTICS_ACTION(object):

    _OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD = "opendaylight-group-statistics:action"
    _OPENDAYLIGHT_GROUP_STATISTICS_DEC_NW_TTL_FIELD = "opendaylight-group-statistics:dec-nw-ttl"
    _OPENDAYLIGHT_GROUP_STATISTICS_OUTPUT_ACTION_FIELD = "opendaylight-group-statistics:output-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_TP_SRC_ACTION_FIELD = "opendaylight-group-statistics:set-tp-src-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_TOS_ACTION_FIELD = "opendaylight-group-statistics:set-nw-tos-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ACTION_FIELD = "opendaylight-group-statistics:group-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_PUSH_VLAN_ACTION_FIELD = "opendaylight-group-statistics:push-vlan-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_SRC_ACTION_FIELD = "opendaylight-group-statistics:set-nw-src-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_POP_MPLS_ACTION_FIELD = "opendaylight-group-statistics:pop-mpls-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_COPY_TTL_IN_FIELD = "opendaylight-group-statistics:copy-ttl-in"
    _OPENDAYLIGHT_GROUP_STATISTICS_SW_PATH_ACTION_FIELD = "opendaylight-group-statistics:sw-path-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_TP_DST_ACTION_FIELD = "opendaylight-group-statistics:set-tp-dst-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_NEXT_HOP_ACTION_FIELD = "opendaylight-group-statistics:set-next-hop-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_ID_ACTION_FIELD = "opendaylight-group-statistics:set-vlan-id-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_SRC_ACTION_FIELD = "opendaylight-group-statistics:set-dl-src-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_DST_ACTION_FIELD = "opendaylight-group-statistics:set-dl-dst-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_PUSH_MPLS_ACTION_FIELD = "opendaylight-group-statistics:push-mpls-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_CONTROLLER_ACTION_FIELD = "opendaylight-group-statistics:controller-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_FLOOD_ACTION_FIELD = "opendaylight-group-statistics:flood-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_MPLS_TTL_ACTION_FIELD = "opendaylight-group-statistics:set-mpls-ttl-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_PCP_ACTION_FIELD = "opendaylight-group-statistics:set-vlan-pcp-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_FIELD_FIELD = "opendaylight-group-statistics:set-field"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_DST_ACTION_FIELD = "opendaylight-group-statistics:set-nw-dst-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_DEC_MPLS_TTL_FIELD = "opendaylight-group-statistics:dec-mpls-ttl"
    _OPENDAYLIGHT_GROUP_STATISTICS_POP_VLAN_ACTION_FIELD = "opendaylight-group-statistics:pop-vlan-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_FLOOD_ALL_ACTION_FIELD = "opendaylight-group-statistics:flood-all-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_COPY_TTL_OUT_FIELD = "opendaylight-group-statistics:copy-ttl-out"
    _OPENDAYLIGHT_GROUP_STATISTICS_HW_PATH_ACTION_FIELD = "opendaylight-group-statistics:hw-path-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_TYPE_ACTION_FIELD = "opendaylight-group-statistics:set-dl-type-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_QUEUE_ACTION_FIELD = "opendaylight-group-statistics:set-queue-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_STRIP_VLAN_ACTION_FIELD = "opendaylight-group-statistics:strip-vlan-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_POP_PBB_ACTION_FIELD = "opendaylight-group-statistics:pop-pbb-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_DROP_ACTION_FIELD = "opendaylight-group-statistics:drop-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_LOOPBACK_ACTION_FIELD = "opendaylight-group-statistics:loopback-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_TTL_ACTION_FIELD = "opendaylight-group-statistics:set-nw-ttl-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_PUSH_PBB_ACTION_FIELD = "opendaylight-group-statistics:push-pbb-action"
    _OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_CFI_ACTION_FIELD = "opendaylight-group-statistics:set-vlan-cfi-action"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DEC_NW_TTL_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_OUTPUT_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_TP_SRC_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_TOS_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PUSH_VLAN_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_SRC_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_POP_MPLS_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_COPY_TTL_IN_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SW_PATH_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_TP_DST_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NEXT_HOP_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_ID_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_SRC_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_DST_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PUSH_MPLS_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_CONTROLLER_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_FLOOD_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_MPLS_TTL_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_PCP_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_FIELD_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_DST_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DEC_MPLS_TTL_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_POP_VLAN_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_FLOOD_ALL_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_COPY_TTL_OUT_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_HW_PATH_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_TYPE_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_QUEUE_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_STRIP_VLAN_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_POP_PBB_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DROP_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_LOOPBACK_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_TTL_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PUSH_PBB_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_CFI_ACTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_dec_nw_ttl(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DEC_NW_TTL_FIELD] = value

    def set_opendaylight_group_statistics_output_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_OUTPUT_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_tp_src_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_TP_SRC_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_nw_tos_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_TOS_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_group_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_push_vlan_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PUSH_VLAN_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_nw_src_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_SRC_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_pop_mpls_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_POP_MPLS_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_copy_ttl_in(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_COPY_TTL_IN_FIELD] = value

    def set_opendaylight_group_statistics_sw_path_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SW_PATH_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_tp_dst_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_TP_DST_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_next_hop_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NEXT_HOP_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_vlan_id_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_ID_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_dl_src_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_SRC_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_dl_dst_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_DST_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_push_mpls_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PUSH_MPLS_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_controller_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_CONTROLLER_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_flood_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_FLOOD_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_mpls_ttl_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_MPLS_TTL_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_vlan_pcp_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_PCP_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_field(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_FIELD_FIELD] = value

    def set_opendaylight_group_statistics_set_nw_dst_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_DST_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_dec_mpls_ttl(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DEC_MPLS_TTL_FIELD] = value

    def set_opendaylight_group_statistics_pop_vlan_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_POP_VLAN_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_flood_all_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_FLOOD_ALL_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_copy_ttl_out(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_COPY_TTL_OUT_FIELD] = value

    def set_opendaylight_group_statistics_hw_path_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_HW_PATH_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_dl_type_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_DL_TYPE_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_queue_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_QUEUE_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_strip_vlan_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_STRIP_VLAN_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_pop_pbb_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_POP_PBB_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_drop_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DROP_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_loopback_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_LOOPBACK_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_nw_ttl_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_NW_TTL_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_push_pbb_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PUSH_PBB_ACTION_FIELD] = value

    def set_opendaylight_group_statistics_set_vlan_cfi_action(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_SET_VLAN_CFI_ACTION_FIELD] = value

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

    def create_opendaylight_group_statistics_action(self):
        
        payload = {self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_opendaylight_group_statistics_action(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_opendaylight_group_statistics_action(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class CACHE_SERVER_CONFIG(object):

    _CACHE_SERVER_CONFIG_FIELD = "cache-server-config"
    _USER_NAME_FIELD = "user-name"
    _PURGE_TIME_FIELD = "purge-time"
    _PREFERENCE_VALUE_FIELD = "preference-value"
    _REFRESH_TIME_FIELD = "refresh-time"
    _SERVER_FIELD = "server"
    _RESPONCE_TIME_FIELD = "responce-time"
    _PASSWORD_FIELD = "password"
    _TRANSPORT_FIELD = "transport"

    def __init__(self):
        self._template = {}
        self._template[self._USER_NAME_FIELD] = None
        self._template[self._PURGE_TIME_FIELD] = None
        self._template[self._PREFERENCE_VALUE_FIELD] = None
        self._template[self._REFRESH_TIME_FIELD] = None
        self._template[self._SERVER_FIELD] = None
        self._template[self._RESPONCE_TIME_FIELD] = None
        self._template[self._PASSWORD_FIELD] = None
        self._template[self._TRANSPORT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._refresh_time = REFRESH_TIME()
        self._server = SERVER()
        self._responce_time = RESPONCE_TIME()
        self._transport = TRANSPORT()

    @property
    def refresh_time(self):
        return self._refresh_time

    @property
    def server(self):
        return self._server

    @property
    def responce_time(self):
        return self._responce_time

    @property
    def transport(self):
        return self._transport

    def set_user_name(self, value):
        self._template[self._USER_NAME_FIELD] = value

    def set_purge_time(self, value):
        self._template[self._PURGE_TIME_FIELD] = value

    def set_preference_value(self, value):
        self._template[self._PREFERENCE_VALUE_FIELD] = value

    def set_password(self, value):
        self._template[self._PASSWORD_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._REFRESH_TIME_FIELD] = self.refresh_time.get_template(default=default)
            self._default_template[self._SERVER_FIELD] = self.server.get_template(default=default)
            self._default_template[self._RESPONCE_TIME_FIELD] = self.responce_time.get_template(default=default)
            self._default_template[self._TRANSPORT_FIELD] = self.transport.get_template(default=default)
            return self._default_template
        else:
            self._template[self._REFRESH_TIME_FIELD] = self.refresh_time.get_template()
            self._template[self._SERVER_FIELD] = self.server.get_template()
            self._template[self._RESPONCE_TIME_FIELD] = self.responce_time.get_template()
            self._template[self._TRANSPORT_FIELD] = self.transport.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        refresh_time_payload = self.refresh_time.get_payload()
        if refresh_time_payload:
            payload[self._REFRESH_TIME_FIELD] = refresh_time_payload
        server_payload = self.server.get_payload()
        if server_payload:
            payload[self._SERVER_FIELD] = server_payload
        responce_time_payload = self.responce_time.get_payload()
        if responce_time_payload:
            payload[self._RESPONCE_TIME_FIELD] = responce_time_payload
        transport_payload = self.transport.get_payload()
        if transport_payload:
            payload[self._TRANSPORT_FIELD] = transport_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_cache_server_config(self):
        
        payload = {self._CACHE_SERVER_CONFIG_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_cache_server_config(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_cache_server_config(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class INTERFACE(object):

    _INTERFACE_FIELD = "interface"
    _ODL_INTERFACE_TENANT_ID_FIELD = "odl-interface:tenant-id"
    _LOCAL_IP_FIELD = "local-ip"
    _ODL_INTERFACE_STACKED_VLAN_ID_FIELD = "odl-interface:stacked_vlan-id"
    _ODL_INTERFACE_NUMLABELS_FIELD = "odl-interface:numLabels"
    _OF_PORT_ID_FIELD = "of-port-id"
    _VLAN_ID_FIELD = "vlan-id"
    _ODL_INTERFACE_TUNNEL_TYPE_FIELD = "odl-interface:tunnel-type"
    _ODL_INTERFACE_LOCAL_IP_FIELD = "odl-interface:local-ip"
    _TYPE_FIELD = "type"
    _STACKED_VLAN_ID_FIELD = "stacked_vlan-id"
    _TENANT_ID_FIELD = "tenant-id"
    _ODL_INTERFACE_OF_PORT_ID_FIELD = "odl-interface:of-port-id"
    _DESCRIPTION_FIELD = "description"
    _REMOTE_IP_FIELD = "remote-ip"
    _ODL_INTERFACE_VLAN_ID_FIELD = "odl-interface:vlan-id"
    _ODL_INTERFACE_BASE_INTERFACE_FIELD = "odl-interface:base-interface"
    _NUMLABELS_FIELD = "numLabels"
    _ODL_INTERFACE_GATEWAY_IP_FIELD = "odl-interface:gateway-ip"
    _NAME_FIELD = "name"
    _BASE_INTERFACE_FIELD = "base-interface"
    _LINK_UP_DOWN_TRAP_ENABLE_FIELD = "link-up-down-trap-enable"
    _ENABLED_FIELD = "enabled"
    _TUNNEL_TYPE_FIELD = "tunnel-type"
    _ODL_INTERFACE_LABELSTACK_FIELD = "odl-interface:labelStack"
    _ODL_INTERFACE_REMOTE_IP_FIELD = "odl-interface:remote-ip"
    _GATEWAY_IP_FIELD = "gateway-ip"

    def __init__(self):
        self._template = {}
        self._template[self._ODL_INTERFACE_TENANT_ID_FIELD] = None
        self._template[self._LOCAL_IP_FIELD] = None
        self._template[self._ODL_INTERFACE_STACKED_VLAN_ID_FIELD] = None
        self._template[self._ODL_INTERFACE_NUMLABELS_FIELD] = None
        self._template[self._OF_PORT_ID_FIELD] = None
        self._template[self._VLAN_ID_FIELD] = None
        self._template[self._ODL_INTERFACE_TUNNEL_TYPE_FIELD] = None
        self._template[self._ODL_INTERFACE_LOCAL_IP_FIELD] = None
        self._template[self._TYPE_FIELD] = None
        self._template[self._STACKED_VLAN_ID_FIELD] = None
        self._template[self._TENANT_ID_FIELD] = None
        self._template[self._ODL_INTERFACE_OF_PORT_ID_FIELD] = None
        self._template[self._DESCRIPTION_FIELD] = None
        self._template[self._REMOTE_IP_FIELD] = None
        self._template[self._ODL_INTERFACE_VLAN_ID_FIELD] = None
        self._template[self._ODL_INTERFACE_BASE_INTERFACE_FIELD] = None
        self._template[self._NUMLABELS_FIELD] = None
        self._template[self._ODL_INTERFACE_GATEWAY_IP_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._template[self._BASE_INTERFACE_FIELD] = None
        self._template[self._LINK_UP_DOWN_TRAP_ENABLE_FIELD] = None
        self._template[self._ENABLED_FIELD] = None
        self._template[self._TUNNEL_TYPE_FIELD] = None
        self._template[self._ODL_INTERFACE_LABELSTACK_FIELD] = None
        self._template[self._ODL_INTERFACE_REMOTE_IP_FIELD] = None
        self._template[self._GATEWAY_IP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._vlan_id = VLAN_ID()

    @property
    def vlan_id(self):
        return self._vlan_id

    def set_odl_interface_tenant_id(self, value):
        self._template[self._ODL_INTERFACE_TENANT_ID_FIELD] = value

    def set_local_ip(self, value):
        self._template[self._LOCAL_IP_FIELD] = value

    def set_odl_interface_stacked_vlan_id(self, value):
        self._template[self._ODL_INTERFACE_STACKED_VLAN_ID_FIELD] = value

    def set_odl_interface_numlabels(self, value):
        self._template[self._ODL_INTERFACE_NUMLABELS_FIELD] = value

    def set_of_port_id(self, value):
        self._template[self._OF_PORT_ID_FIELD] = value

    def set_odl_interface_tunnel_type(self, value):
        self._template[self._ODL_INTERFACE_TUNNEL_TYPE_FIELD] = value

    def set_odl_interface_local_ip(self, value):
        self._template[self._ODL_INTERFACE_LOCAL_IP_FIELD] = value

    def set_type(self, value):
        self._template[self._TYPE_FIELD] = value

    def set_stacked_vlan_id(self, value):
        self._template[self._STACKED_VLAN_ID_FIELD] = value

    def set_tenant_id(self, value):
        self._template[self._TENANT_ID_FIELD] = value

    def set_odl_interface_of_port_id(self, value):
        self._template[self._ODL_INTERFACE_OF_PORT_ID_FIELD] = value

    def set_description(self, value):
        self._template[self._DESCRIPTION_FIELD] = value

    def set_remote_ip(self, value):
        self._template[self._REMOTE_IP_FIELD] = value

    def set_odl_interface_vlan_id(self, value):
        self._template[self._ODL_INTERFACE_VLAN_ID_FIELD] = value

    def set_odl_interface_base_interface(self, value):
        self._template[self._ODL_INTERFACE_BASE_INTERFACE_FIELD] = value

    def set_numlabels(self, value):
        self._template[self._NUMLABELS_FIELD] = value

    def set_odl_interface_gateway_ip(self, value):
        self._template[self._ODL_INTERFACE_GATEWAY_IP_FIELD] = value

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_base_interface(self, value):
        self._template[self._BASE_INTERFACE_FIELD] = value

    def set_link_up_down_trap_enable(self, value):
        self._template[self._LINK_UP_DOWN_TRAP_ENABLE_FIELD] = value

    def set_enabled(self, value):
        self._template[self._ENABLED_FIELD] = value

    def set_tunnel_type(self, value):
        self._template[self._TUNNEL_TYPE_FIELD] = value

    def set_odl_interface_labelstack(self, value):
        self._template[self._ODL_INTERFACE_LABELSTACK_FIELD] = value

    def set_odl_interface_remote_ip(self, value):
        self._template[self._ODL_INTERFACE_REMOTE_IP_FIELD] = value

    def set_gateway_ip(self, value):
        self._template[self._GATEWAY_IP_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._VLAN_ID_FIELD] = self.vlan_id.get_template(default=default)
            return self._default_template
        else:
            self._template[self._VLAN_ID_FIELD] = self.vlan_id.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        vlan_id_payload = self.vlan_id.get_payload()
        if vlan_id_payload:
            payload[self._VLAN_ID_FIELD] = vlan_id_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_interface(self):
        
        payload = {self._INTERFACE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_interface(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_interface(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class CONFIGURATION(object):

    _CONFIGURATION_FIELD = "configuration"
    _SHUTDOWN_IMPL_SECRET_FIELD = "shutdown-impl:secret"
    _STATISTICS_MANAGER_DATA_BROKER_FIELD = "statistics-manager:data-broker"
    _ARP_HANDLER_IMPL_ARP_FLOW_TABLE_ID_FIELD = "arp-handler-impl:arp-flow-table-id"
    _DISTRIBUTED_ENTITY_OWNERSHIP_SERVICE_DATA_STORE_FIELD = "distributed-entity-ownership-service:data-store"
    _MAIN_IMPL_REACTIVE_FLOW_HARD_TIMEOUT_FIELD = "main-impl:reactive-flow-hard-timeout"
    _THREADPOOL_IMPL_SCHEDULED_MAX_THREAD_COUNT_FIELD = "threadpool-impl-scheduled:max-thread-count"
    _OPENFLOW_PROVIDER_IMPL_RPC_REGISTRY_FIELD = "openflow-provider-impl:rpc-registry"
    _LOOP_REMOVER_IMPL_GRAPH_REFRESH_DELAY_FIELD = "loop-remover-impl:graph-refresh-delay"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_NOTIFICATION_ADAPTER_FIELD = "opendaylight-sal-binding-broker-impl:binding-notification-adapter"
    _ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_COMMIT_QUEUE_SIZE_FIELD = "odl-concurrent-data-broker-cfg:max-data-broker-commit-queue-size"
    _NETCONF_NORTHBOUND_IMPL_AGGREGATOR_FIELD = "netconf-northbound-impl:aggregator"
    _INTERFACEMGR_IMPL_BROKER_FIELD = "interfacemgr-impl:broker"
    _PROTOCOL_FRAMEWORK_EXECUTOR_FIELD = "protocol-framework:executor"
    _DISTRIBUTED_DATASTORE_PROVIDER_OPERATIONAL_SCHEMA_SERVICE_FIELD = "distributed-datastore-provider:operational-schema-service"
    _PROTOCOL_FRAMEWORK_CONNECT_TIME_FIELD = "protocol-framework:connect-time"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_PARK_FIELD = "opendaylight-sal-dom-broker-impl:notification-queue-park"
    _PROTOCOL_FRAMEWORK_TIMEOUT_FIELD = "protocol-framework:timeout"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_BROKER_IMPL_FIELD = "opendaylight-sal-binding-broker-impl:binding-broker-impl"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_ADDRESS_FIELD = "openflow-switch-connection-provider-impl:address"
    _THREADPOOL_IMPL_FLEXIBLE_MINTHREADCOUNT_FIELD = "threadpool-impl-flexible:minThreadCount"
    _AAA_AUTHN_MDSAL_STORE_CFG_DOM_BROKER_FIELD = "aaa-authn-mdsal-store-cfg:dom-broker"
    _LOOP_REMOVER_IMPL_TOPOLOGY_ID_FIELD = "loop-remover-impl:topology-id"
    _OPENFLOW_PROVIDER_IMPL_ROLE_FIELD = "openflow-provider-impl:role"
    _FIBMANAGER_IMPL_BROKER_FIELD = "fibmanager-impl:broker"
    _MAIN_IMPL_REACTIVE_FLOW_TABLE_ID_FIELD = "main-impl:reactive-flow-table-id"
    _AAA_AUTHN_MDSAL_STORE_CFG_DATA_BROKER_FIELD = "aaa-authn-mdsal-store-cfg:data-broker"
    _ARP_HANDLER_IMPL_DATA_BROKER_FIELD = "arp-handler-impl:data-broker"
    _MAIN_IMPL_DROPALL_FLOW_PRIORITY_FIELD = "main-impl:dropall-flow-priority"
    _LLDP_SPEAKER_ADDRESS_DESTINATION_FIELD = "lldp-speaker:address-destination"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_SCHEMA_SERVICE_FIELD = "opendaylight-sal-dom-broker-impl:schema-service"
    _XSQL_DATA_BROKER_FIELD = "XSQL:data-broker"
    _FORWARDINGRULES_MANAGER_RPC_REGISTRY_FIELD = "forwardingrules-manager:rpc-registry"
    _ARP_HANDLER_IMPL_FLOOD_FLOW_PRIORITY_FIELD = "arp-handler-impl:flood-flow-priority"
    _LLDP_SPEAKER_DATA_BROKER_FIELD = "lldp-speaker:data-broker"
    _ARP_HANDLER_IMPL_IS_HYBRID_MODE_FIELD = "arp-handler-impl:is-hybrid-mode"
    _VPNSERVICE_IMPL_ODLINTERFACE_FIELD = "vpnservice-impl:odlinterface"
    _DISTRIBUTED_DATASTORE_PROVIDER_OPERATIONAL_PROPERTIES_FIELD = "distributed-datastore-provider:operational-properties"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_PORT_FIELD = "openflow-switch-connection-provider-impl:port"
    _PROTOCOL_FRAMEWORK_MAX_ATTEMPTS_FIELD = "protocol-framework:max-attempts"
    _NETTY_TIMER_TICKS_PER_WHEEL_FIELD = "netty-timer:ticks-per-wheel"
    _HOST_TRACKER_IMPL_DATA_BROKER_FIELD = "host-tracker-impl:data-broker"
    _ARP_HANDLER_IMPL_FLOOD_FLOW_IDLE_TIMEOUT_FIELD = "arp-handler-impl:flood-flow-idle-timeout"
    _ARP_HANDLER_IMPL_IS_PROACTIVE_FLOOD_MODE_FIELD = "arp-handler-impl:is-proactive-flood-mode"
    _THREADPOOL_IMPL_FLEXIBLE_QUEUECAPACITY_FIELD = "threadpool-impl-flexible:queueCapacity"
    _OF_SWITCH_CONFIG_PUSHER_RPC_REGISTRY_FIELD = "of-switch-config-pusher:rpc-registry"
    _NETTY_TIMER_TICK_DURATION_FIELD = "netty-timer:tick-duration"
    _LOOP_REMOVER_IMPL_RPC_REGISTRY_FIELD = "loop-remover-impl:rpc-registry"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_SWITCH_IDLE_TIMEOUT_FIELD = "openflow-switch-connection-provider-impl:switch-idle-timeout"
    _LOOP_REMOVER_IMPL_LLDP_FLOW_IDLE_TIMEOUT_FIELD = "loop-remover-impl:lldp-flow-idle-timeout"
    _OPENDAYLIGHT_INMEMORY_DATASTORE_PROVIDER_INMEMORY_OPERATIONAL_DATASTORE_PROVIDER_FIELD = "opendaylight-inmemory-datastore-provider:inmemory-operational-datastore-provider"
    _PROTOCOL_FRAMEWORK_MAX_SLEEP_FIELD = "protocol-framework:max-sleep"
    _DISTRIBUTED_DATASTORE_PROVIDER_CONFIG_SCHEMA_SERVICE_FIELD = "distributed-datastore-provider:config-schema-service"
    _THREADPOOL_IMPL_FLEXIBLE_THREADFACTORY_FIELD = "threadpool-impl-flexible:threadFactory"
    _TOPOLOGY_MANAGER_IMPL_BROKER_FIELD = "topology-manager-impl:broker"
    _NEXTHOPMGR_IMPL_MDSALUTIL_FIELD = "nexthopmgr-impl:mdsalutil"
    _STATISTICS_MANAGER_NOTIFICATION_SERVICE_FIELD = "statistics-manager:notification-service"
    _THREADPOOL_IMPL_FLEXIBLE_MAX_THREAD_COUNT_FIELD = "threadpool-impl-flexible:max-thread-count"
    _FIBMANAGER_IMPL_MDSALUTIL_FIELD = "fibmanager-impl:mdsalutil"
    _LOOP_REMOVER_IMPL_DATA_BROKER_FIELD = "loop-remover-impl:data-broker"
    _NETTY_TIMER_THREAD_FACTORY_FIELD = "netty-timer:thread-factory"
    _PROTOCOL_FRAMEWORK_RECONNECT_TIMEOUT_FIELD = "protocol-framework:reconnect-timeout"
    _MAIN_IMPL_DATA_BROKER_FIELD = "main-impl:data-broker"
    _PROTOCOL_FRAMEWORK_SLEEP_FACTOR_FIELD = "protocol-framework:sleep-factor"
    _ARP_HANDLER_IMPL_NOTIFICATION_SERVICE_FIELD = "arp-handler-impl:notification-service"
    _LOOP_REMOVER_IMPL_LLDP_FLOW_PRIORITY_FIELD = "loop-remover-impl:lldp-flow-priority"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_ROOT_SCHEMA_SERVICE_FIELD = "opendaylight-sal-dom-broker-impl:root-schema-service"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_FUTURE_CALLBACK_QUEUE_SIZE_FIELD = "opendaylight-sal-dom-broker-impl:max-data-broker-future-callback-queue-size"
    _ARP_HANDLER_IMPL_FLOOD_FLOW_HARD_TIMEOUT_FIELD = "arp-handler-impl:flood-flow-hard-timeout"
    _MAIN_IMPL_IS_INSTALL_DROPALL_FLOW_FIELD = "main-impl:is-install-dropall-flow"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_TRANSPORT_PROTOCOL_FIELD = "openflow-switch-connection-provider-impl:transport-protocol"
    _MAIN_IMPL_IS_LEARNING_ONLY_MODE_FIELD = "main-impl:is-learning-only-mode"
    _OPENDAYLIGHT_REST_CONNECTOR_WEBSOCKET_PORT_FIELD = "opendaylight-rest-connector:websocket-port"
    _ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_FUTURE_CALLBACK_QUEUE_SIZE_FIELD = "odl-concurrent-data-broker-cfg:max-data-broker-future-callback-queue-size"
    _XSQL_ASYNC_DATA_BROKER_FIELD = "XSQL:async-data-broker"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_NOTIFICATION_ADAPTER_FIELD = "opendaylight-sal-binding-broker-impl:notification-adapter"
    _NEXTHOPMGR_IMPL_RPC_REGISTRY_FIELD = "nexthopmgr-impl:rpc-registry"
    _OPENDAYLIGHT_PINGPONG_BROKER_DATA_BROKER_FIELD = "opendaylight-pingpong-broker:data-broker"
    _REMOTE_RPC_CONNECTOR_ENABLE_METRIC_CAPTURE_FIELD = "remote-rpc-connector:enable-metric-capture"
    _LOOP_REMOVER_IMPL_LLDP_FLOW_HARD_TIMEOUT_FIELD = "loop-remover-impl:lldp-flow-hard-timeout"
    _AAA_AUTHN_MDSAL_STORE_CFG_TIMETOWAIT_FIELD = "aaa-authn-mdsal-store-cfg:timeToWait"
    _VPNSERVICE_IMPL_MDSALUTIL_FIELD = "vpnservice-impl:mdsalutil"
    _OPENFLOW_PROVIDER_IMPL_OPENFLOW_PLUGIN_PROVIDER_FIELD = "openflow-provider-impl:openflow-plugin-provider"
    _THREADPOOL_IMPL_THREADPOOL_FIELD = "threadpool-impl:threadpool"
    _ARP_HANDLER_IMPL_ARP_FLOW_IDLE_TIMEOUT_FIELD = "arp-handler-impl:arp-flow-idle-timeout"
    _ARP_HANDLER_IMPL_ARP_FLOW_HARD_TIMEOUT_FIELD = "arp-handler-impl:arp-flow-hard-timeout"
    _AAA_AUTHN_MDSAL_STORE_CFG_TIMETOLIVE_FIELD = "aaa-authn-mdsal-store-cfg:timeToLive"
    _ARP_HANDLER_IMPL_FLOOD_FLOW_TABLE_ID_FIELD = "arp-handler-impl:flood-flow-table-id"
    _HOST_TRACKER_IMPL_NOTIFICATION_SERVICE_FIELD = "host-tracker-impl:notification-service"
    _NEXTHOPMGR_IMPL_BROKER_FIELD = "nexthopmgr-impl:broker"
    _NETCONF_NORTHBOUND_IMPL_CONNECTION_TIMEOUT_MILLIS_FIELD = "netconf-northbound-impl:connection-timeout-millis"
    _DISTRIBUTED_DATASTORE_PROVIDER_CONFIG_PROPERTIES_FIELD = "distributed-datastore-provider:config-properties"
    _OPENDAYLIGHT_INMEMORY_DATASTORE_PROVIDER_INMEMORY_CONFIG_DATASTORE_PROVIDER_FIELD = "opendaylight-inmemory-datastore-provider:inmemory-config-datastore-provider"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_NOTIFICATION_PUBLISH_ADAPTER_FIELD = "opendaylight-sal-binding-broker-impl:notification-publish-adapter"
    _BGPMANAGER_IMPL_BROKER_FIELD = "bgpmanager-impl:broker"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_CONFIG_DATA_STORE_FIELD = "opendaylight-sal-dom-broker-impl:config-data-store"
    _IDMANAGER_IMPL_BROKER_FIELD = "idmanager-impl:broker"
    _THREADPOOL_IMPL_SCHEDULED_THREADFACTORY_FIELD = "threadpool-impl-scheduled:threadFactory"
    _LLDP_SPEAKER_RPC_REGISTRY_FIELD = "lldp-speaker:rpc-registry"
    _MAIN_IMPL_RPC_REGISTRY_FIELD = "main-impl:rpc-registry"
    _XSQL_SCHEMA_SERVICE_FIELD = "XSQL:schema-service"
    _STATISTICS_MANAGER_STATISTICS_MANAGER_SETTINGS_FIELD = "statistics-manager:statistics-manager-settings"
    _MAIN_IMPL_REACTIVE_FLOW_PRIORITY_FIELD = "main-impl:reactive-flow-priority"
    _MAIN_IMPL_NOTIFICATION_SERVICE_FIELD = "main-impl:notification-service"
    _MDSALUTIL_IMPL_BROKER_FIELD = "mdsalutil-impl:broker"
    _INVENTORY_MANAGER_IMPL_BROKER_FIELD = "inventory-manager-impl:broker"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_USE_BARRIER_FIELD = "openflow-switch-connection-provider-impl:use-barrier"
    _ADDRESS_TRACKER_IMPL_OBSERVE_ADDRESSES_FROM_FIELD = "address-tracker-impl:observe-addresses-from"
    _ODL_CONCURRENT_DATA_BROKER_CFG_SCHEMA_SERVICE_FIELD = "odl-concurrent-data-broker-cfg:schema-service"
    _STATISTICS_MANAGER_RPC_REGISTRY_FIELD = "statistics-manager:rpc-registry"
    _ARP_HANDLER_IMPL_RPC_REGISTRY_FIELD = "arp-handler-impl:rpc-registry"
    _PROTOCOL_FRAMEWORK_MIN_SLEEP_FIELD = "protocol-framework:min-sleep"
    _LOOP_REMOVER_IMPL_LLDP_FLOW_TABLE_ID_FIELD = "loop-remover-impl:lldp-flow-table-id"
    _THREADPOOL_IMPL_FIXED_MAX_THREAD_COUNT_FIELD = "threadpool-impl-fixed:max-thread-count"
    _OF_SWITCH_CONFIG_PUSHER_DATA_BROKER_FIELD = "of-switch-config-pusher:data-broker"
    _OPENFLOW_PROVIDER_IMPL_OPENFLOW_SWITCH_CONNECTION_PROVIDER_FIELD = "openflow-provider-impl:openflow-switch-connection-provider"
    _VPNSERVICE_IMPL_BGPMANAGER_FIELD = "vpnservice-impl:bgpmanager"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_STATISTICS_FIELD = "openflow-switch-connection-provider-impl:statistics"
    _PROTOCOL_FRAMEWORK_DEADLINE_FIELD = "protocol-framework:deadline"
    _VPNSERVICE_IMPL_BROKER_FIELD = "vpnservice-impl:broker"
    _NETCONF_NORTHBOUND_IMPL_TIMER_FIELD = "netconf-northbound-impl:timer"
    _LOOP_REMOVER_IMPL_NOTIFICATION_SERVICE_FIELD = "loop-remover-impl:notification-service"
    _NETCONF_NORTHBOUND_IMPL_WORKER_THREAD_GROUP_FIELD = "netconf-northbound-impl:worker-thread-group"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_DATA_COMPATIBLE_BROKER_FIELD = "opendaylight-sal-binding-broker-impl:binding-data-compatible-broker"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_OPERATIONAL_DATA_STORE_FIELD = "opendaylight-sal-dom-broker-impl:operational-data-store"
    _HOST_TRACKER_IMPL_TOPOLOGY_ID_FIELD = "host-tracker-impl:topology-id"
    _ODL_CONCURRENT_DATA_BROKER_CFG_CONFIG_DATA_STORE_FIELD = "odl-concurrent-data-broker-cfg:config-data-store"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_ASYNC_DATA_BROKER_FIELD = "opendaylight-sal-dom-broker-impl:async-data-broker"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_TLS_FIELD = "openflow-switch-connection-provider-impl:tls"
    _OPENFLOW_PROVIDER_IMPL_NOTIFICATION_SERVICE_FIELD = "openflow-provider-impl:notification-service"
    _THREADGROUP_THREAD_COUNT_FIELD = "threadgroup:thread-count"
    _ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_FUTURE_CALLBACK_POOL_SIZE_FIELD = "odl-concurrent-data-broker-cfg:max-data-broker-future-callback-pool-size"
    _PACKET_HANDLER_IMPL_NOTIFICATION_SERVICE_FIELD = "packet-handler-impl:notification-service"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_SPIN_FIELD = "opendaylight-sal-dom-broker-impl:notification-queue-spin"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_THREADS_FIELD = "openflow-switch-connection-provider-impl:threads"
    _REMOTE_RPC_CONNECTOR_ACTOR_SYSTEM_NAME_FIELD = "remote-rpc-connector:actor-system-name"
    _THREADPOOL_IMPL_NAME_PREFIX_FIELD = "threadpool-impl:name-prefix"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_NOTIFICATION_PUBLISH_ADAPTER_FIELD = "opendaylight-sal-binding-broker-impl:binding-notification-publish-adapter"
    _REMOTE_RPC_CONNECTOR_BOUNDED_MAILBOX_CAPACITY_FIELD = "remote-rpc-connector:bounded-mailbox-capacity"
    _ARP_HANDLER_IMPL_FLOOD_FLOW_INSTALLATION_DELAY_FIELD = "arp-handler-impl:flood-flow-installation-delay"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_FORWARDED_DATA_BROKER_FIELD = "opendaylight-sal-binding-broker-impl:binding-forwarded-data-broker"
    _ODL_CONCURRENT_DATA_BROKER_CFG_OPERATIONAL_DATA_STORE_FIELD = "odl-concurrent-data-broker-cfg:operational-data-store"
    _OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_WAIT_FOR_SCHEMA_FIELD = "opendaylight-sal-binding-broker-impl:wait-for-schema"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_FUTURE_CALLBACK_POOL_SIZE_FIELD = "opendaylight-sal-dom-broker-impl:max-data-broker-future-callback-pool-size"
    _MAIN_IMPL_DROPALL_FLOW_HARD_TIMEOUT_FIELD = "main-impl:dropall-flow-hard-timeout"
    _AAA_AUTHN_MDSAL_STORE_CFG_PASSWORD_FIELD = "aaa-authn-mdsal-store-cfg:password"
    _NEXTHOPMGR_IMPL_ODLINTERFACE_FIELD = "nexthopmgr-impl:odlinterface"
    _NETCONF_NORTHBOUND_IMPL_SERVER_MONITOR_FIELD = "netconf-northbound-impl:server-monitor"
    _ADDRESS_TRACKER_IMPL_DATA_BROKER_FIELD = "address-tracker-impl:data-broker"
    _VPNSERVICE_IMPL_RPCREGISTRY_FIELD = "vpnservice-impl:rpcregistry"
    _MAIN_IMPL_DROPALL_FLOW_TABLE_ID_FIELD = "main-impl:dropall-flow-table-id"
    _REMOTE_RPC_CONNECTOR_DOM_BROKER_FIELD = "remote-rpc-connector:dom-broker"
    _NETCONF_NORTHBOUND_IMPL_MAPPERS_FIELD = "netconf-northbound-impl:mappers"
    _FORWARDINGRULES_MANAGER_DATA_BROKER_FIELD = "forwardingrules-manager:data-broker"
    _MAIN_IMPL_DROPALL_FLOW_IDLE_TIMEOUT_FIELD = "main-impl:dropall-flow-idle-timeout"
    _FIBMANAGER_IMPL_VPNMANAGER_FIELD = "fibmanager-impl:vpnmanager"
    _ADDRESS_TRACKER_IMPL_NOTIFICATION_SERVICE_FIELD = "address-tracker-impl:notification-service"
    _NETCONF_NORTHBOUND_IMPL_BOSS_THREAD_GROUP_FIELD = "netconf-northbound-impl:boss-thread-group"
    _PROTOCOL_FRAMEWORK_TIMED_RECONNECT_EXECUTOR_FIELD = "protocol-framework:timed-reconnect-executor"
    _ADDRESS_TRACKER_IMPL_TIMESTAMP_UPDATE_INTERVAL_FIELD = "address-tracker-impl:timestamp-update-interval"
    _LOOP_REMOVER_IMPL_IS_INSTALL_LLDP_FLOW_FIELD = "loop-remover-impl:is-install-lldp-flow"
    _TOPOLOGY_LLDP_DISCOVERY_IMPL_BROKER_FIELD = "topology-lldp-discovery-impl:broker"
    _MAIN_IMPL_REACTIVE_FLOW_IDLE_TIMEOUT_FIELD = "main-impl:reactive-flow-idle-timeout"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_DEPTH_FIELD = "opendaylight-sal-dom-broker-impl:notification-queue-depth"
    _OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_OPENFLOW_SWITCH_CONNECTION_PROVIDER_FIELD = "openflow-switch-connection-provider-impl:openflow-switch-connection-provider"
    _IDMANAGER_IMPL_RPC_REGISTRY_FIELD = "idmanager-impl:rpc-registry"
    _ARP_HANDLER_IMPL_ARP_FLOW_PRIORITY_FIELD = "arp-handler-impl:arp-flow-priority"
    _OPENDAYLIGHT_REST_CONNECTOR_DOM_BROKER_FIELD = "opendaylight-rest-connector:dom-broker"
    _PROTOCOL_FRAMEWORK_RECONNECT_EXECUTOR_FIELD = "protocol-framework:reconnect-executor"
    _OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_COMMIT_QUEUE_SIZE_FIELD = "opendaylight-sal-dom-broker-impl:max-data-broker-commit-queue-size"
    _OPENFLOW_PROVIDER_IMPL_DATA_BROKER_FIELD = "openflow-provider-impl:data-broker"
    _THREADPOOL_IMPL_FLEXIBLE_KEEPALIVEMILLIS_FIELD = "threadpool-impl-flexible:keepAliveMillis"
    _THREADPOOL_IMPL_FIXED_THREADFACTORY_FIELD = "threadpool-impl-fixed:threadFactory"

    def __init__(self):
        self._template = {}
        self._template[self._SHUTDOWN_IMPL_SECRET_FIELD] = None
        self._template[self._STATISTICS_MANAGER_DATA_BROKER_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_TABLE_ID_FIELD] = None
        self._template[self._DISTRIBUTED_ENTITY_OWNERSHIP_SERVICE_DATA_STORE_FIELD] = None
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_HARD_TIMEOUT_FIELD] = None
        self._template[self._THREADPOOL_IMPL_SCHEDULED_MAX_THREAD_COUNT_FIELD] = None
        self._template[self._OPENFLOW_PROVIDER_IMPL_RPC_REGISTRY_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_GRAPH_REFRESH_DELAY_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_NOTIFICATION_ADAPTER_FIELD] = None
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_COMMIT_QUEUE_SIZE_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_AGGREGATOR_FIELD] = None
        self._template[self._INTERFACEMGR_IMPL_BROKER_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_EXECUTOR_FIELD] = None
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_OPERATIONAL_SCHEMA_SERVICE_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_CONNECT_TIME_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_PARK_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_TIMEOUT_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_BROKER_IMPL_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_ADDRESS_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_MINTHREADCOUNT_FIELD] = None
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_DOM_BROKER_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_TOPOLOGY_ID_FIELD] = None
        self._template[self._OPENFLOW_PROVIDER_IMPL_ROLE_FIELD] = None
        self._template[self._FIBMANAGER_IMPL_BROKER_FIELD] = None
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_TABLE_ID_FIELD] = None
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_DATA_BROKER_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_DATA_BROKER_FIELD] = None
        self._template[self._MAIN_IMPL_DROPALL_FLOW_PRIORITY_FIELD] = None
        self._template[self._LLDP_SPEAKER_ADDRESS_DESTINATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_SCHEMA_SERVICE_FIELD] = None
        self._template[self._XSQL_DATA_BROKER_FIELD] = None
        self._template[self._FORWARDINGRULES_MANAGER_RPC_REGISTRY_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_PRIORITY_FIELD] = None
        self._template[self._LLDP_SPEAKER_DATA_BROKER_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_IS_HYBRID_MODE_FIELD] = None
        self._template[self._VPNSERVICE_IMPL_ODLINTERFACE_FIELD] = None
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_OPERATIONAL_PROPERTIES_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_PORT_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_MAX_ATTEMPTS_FIELD] = None
        self._template[self._NETTY_TIMER_TICKS_PER_WHEEL_FIELD] = None
        self._template[self._HOST_TRACKER_IMPL_DATA_BROKER_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_IDLE_TIMEOUT_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_IS_PROACTIVE_FLOOD_MODE_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_QUEUECAPACITY_FIELD] = None
        self._template[self._OF_SWITCH_CONFIG_PUSHER_RPC_REGISTRY_FIELD] = None
        self._template[self._NETTY_TIMER_TICK_DURATION_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_RPC_REGISTRY_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_SWITCH_IDLE_TIMEOUT_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_IDLE_TIMEOUT_FIELD] = None
        self._template[self._OPENDAYLIGHT_INMEMORY_DATASTORE_PROVIDER_INMEMORY_OPERATIONAL_DATASTORE_PROVIDER_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_MAX_SLEEP_FIELD] = None
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_CONFIG_SCHEMA_SERVICE_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_THREADFACTORY_FIELD] = None
        self._template[self._TOPOLOGY_MANAGER_IMPL_BROKER_FIELD] = None
        self._template[self._NEXTHOPMGR_IMPL_MDSALUTIL_FIELD] = None
        self._template[self._STATISTICS_MANAGER_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_MAX_THREAD_COUNT_FIELD] = None
        self._template[self._FIBMANAGER_IMPL_MDSALUTIL_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_DATA_BROKER_FIELD] = None
        self._template[self._NETTY_TIMER_THREAD_FACTORY_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_RECONNECT_TIMEOUT_FIELD] = None
        self._template[self._MAIN_IMPL_DATA_BROKER_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_SLEEP_FACTOR_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_PRIORITY_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_ROOT_SCHEMA_SERVICE_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_FUTURE_CALLBACK_QUEUE_SIZE_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_HARD_TIMEOUT_FIELD] = None
        self._template[self._MAIN_IMPL_IS_INSTALL_DROPALL_FLOW_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_TRANSPORT_PROTOCOL_FIELD] = None
        self._template[self._MAIN_IMPL_IS_LEARNING_ONLY_MODE_FIELD] = None
        self._template[self._OPENDAYLIGHT_REST_CONNECTOR_WEBSOCKET_PORT_FIELD] = None
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_FUTURE_CALLBACK_QUEUE_SIZE_FIELD] = None
        self._template[self._XSQL_ASYNC_DATA_BROKER_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_NOTIFICATION_ADAPTER_FIELD] = None
        self._template[self._NEXTHOPMGR_IMPL_RPC_REGISTRY_FIELD] = None
        self._template[self._OPENDAYLIGHT_PINGPONG_BROKER_DATA_BROKER_FIELD] = None
        self._template[self._REMOTE_RPC_CONNECTOR_ENABLE_METRIC_CAPTURE_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_HARD_TIMEOUT_FIELD] = None
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_TIMETOWAIT_FIELD] = None
        self._template[self._VPNSERVICE_IMPL_MDSALUTIL_FIELD] = None
        self._template[self._OPENFLOW_PROVIDER_IMPL_OPENFLOW_PLUGIN_PROVIDER_FIELD] = None
        self._template[self._THREADPOOL_IMPL_THREADPOOL_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_IDLE_TIMEOUT_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_HARD_TIMEOUT_FIELD] = None
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_TIMETOLIVE_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_TABLE_ID_FIELD] = None
        self._template[self._HOST_TRACKER_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._NEXTHOPMGR_IMPL_BROKER_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_CONNECTION_TIMEOUT_MILLIS_FIELD] = None
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_CONFIG_PROPERTIES_FIELD] = None
        self._template[self._OPENDAYLIGHT_INMEMORY_DATASTORE_PROVIDER_INMEMORY_CONFIG_DATASTORE_PROVIDER_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_NOTIFICATION_PUBLISH_ADAPTER_FIELD] = None
        self._template[self._BGPMANAGER_IMPL_BROKER_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_CONFIG_DATA_STORE_FIELD] = None
        self._template[self._IDMANAGER_IMPL_BROKER_FIELD] = None
        self._template[self._THREADPOOL_IMPL_SCHEDULED_THREADFACTORY_FIELD] = None
        self._template[self._LLDP_SPEAKER_RPC_REGISTRY_FIELD] = None
        self._template[self._MAIN_IMPL_RPC_REGISTRY_FIELD] = None
        self._template[self._XSQL_SCHEMA_SERVICE_FIELD] = None
        self._template[self._STATISTICS_MANAGER_STATISTICS_MANAGER_SETTINGS_FIELD] = None
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_PRIORITY_FIELD] = None
        self._template[self._MAIN_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._MDSALUTIL_IMPL_BROKER_FIELD] = None
        self._template[self._INVENTORY_MANAGER_IMPL_BROKER_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_USE_BARRIER_FIELD] = None
        self._template[self._ADDRESS_TRACKER_IMPL_OBSERVE_ADDRESSES_FROM_FIELD] = None
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_SCHEMA_SERVICE_FIELD] = None
        self._template[self._STATISTICS_MANAGER_RPC_REGISTRY_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_RPC_REGISTRY_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_MIN_SLEEP_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_TABLE_ID_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FIXED_MAX_THREAD_COUNT_FIELD] = None
        self._template[self._OF_SWITCH_CONFIG_PUSHER_DATA_BROKER_FIELD] = None
        self._template[self._OPENFLOW_PROVIDER_IMPL_OPENFLOW_SWITCH_CONNECTION_PROVIDER_FIELD] = None
        self._template[self._VPNSERVICE_IMPL_BGPMANAGER_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_STATISTICS_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_DEADLINE_FIELD] = None
        self._template[self._VPNSERVICE_IMPL_BROKER_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_TIMER_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_WORKER_THREAD_GROUP_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_DATA_COMPATIBLE_BROKER_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_OPERATIONAL_DATA_STORE_FIELD] = None
        self._template[self._HOST_TRACKER_IMPL_TOPOLOGY_ID_FIELD] = None
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_CONFIG_DATA_STORE_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_ASYNC_DATA_BROKER_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_TLS_FIELD] = None
        self._template[self._OPENFLOW_PROVIDER_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._THREADGROUP_THREAD_COUNT_FIELD] = None
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_FUTURE_CALLBACK_POOL_SIZE_FIELD] = None
        self._template[self._PACKET_HANDLER_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_SPIN_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_THREADS_FIELD] = None
        self._template[self._REMOTE_RPC_CONNECTOR_ACTOR_SYSTEM_NAME_FIELD] = None
        self._template[self._THREADPOOL_IMPL_NAME_PREFIX_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_NOTIFICATION_PUBLISH_ADAPTER_FIELD] = None
        self._template[self._REMOTE_RPC_CONNECTOR_BOUNDED_MAILBOX_CAPACITY_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_INSTALLATION_DELAY_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_FORWARDED_DATA_BROKER_FIELD] = None
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_OPERATIONAL_DATA_STORE_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_WAIT_FOR_SCHEMA_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_FUTURE_CALLBACK_POOL_SIZE_FIELD] = None
        self._template[self._MAIN_IMPL_DROPALL_FLOW_HARD_TIMEOUT_FIELD] = None
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_PASSWORD_FIELD] = None
        self._template[self._NEXTHOPMGR_IMPL_ODLINTERFACE_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_SERVER_MONITOR_FIELD] = None
        self._template[self._ADDRESS_TRACKER_IMPL_DATA_BROKER_FIELD] = None
        self._template[self._VPNSERVICE_IMPL_RPCREGISTRY_FIELD] = None
        self._template[self._MAIN_IMPL_DROPALL_FLOW_TABLE_ID_FIELD] = None
        self._template[self._REMOTE_RPC_CONNECTOR_DOM_BROKER_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_MAPPERS_FIELD] = None
        self._template[self._FORWARDINGRULES_MANAGER_DATA_BROKER_FIELD] = None
        self._template[self._MAIN_IMPL_DROPALL_FLOW_IDLE_TIMEOUT_FIELD] = None
        self._template[self._FIBMANAGER_IMPL_VPNMANAGER_FIELD] = None
        self._template[self._ADDRESS_TRACKER_IMPL_NOTIFICATION_SERVICE_FIELD] = None
        self._template[self._NETCONF_NORTHBOUND_IMPL_BOSS_THREAD_GROUP_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_TIMED_RECONNECT_EXECUTOR_FIELD] = None
        self._template[self._ADDRESS_TRACKER_IMPL_TIMESTAMP_UPDATE_INTERVAL_FIELD] = None
        self._template[self._LOOP_REMOVER_IMPL_IS_INSTALL_LLDP_FLOW_FIELD] = None
        self._template[self._TOPOLOGY_LLDP_DISCOVERY_IMPL_BROKER_FIELD] = None
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_IDLE_TIMEOUT_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_DEPTH_FIELD] = None
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_OPENFLOW_SWITCH_CONNECTION_PROVIDER_FIELD] = None
        self._template[self._IDMANAGER_IMPL_RPC_REGISTRY_FIELD] = None
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_PRIORITY_FIELD] = None
        self._template[self._OPENDAYLIGHT_REST_CONNECTOR_DOM_BROKER_FIELD] = None
        self._template[self._PROTOCOL_FRAMEWORK_RECONNECT_EXECUTOR_FIELD] = None
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_COMMIT_QUEUE_SIZE_FIELD] = None
        self._template[self._OPENFLOW_PROVIDER_IMPL_DATA_BROKER_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_KEEPALIVEMILLIS_FIELD] = None
        self._template[self._THREADPOOL_IMPL_FIXED_THREADFACTORY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_shutdown_impl_secret(self, value):
        self._template[self._SHUTDOWN_IMPL_SECRET_FIELD] = value

    def set_statistics_manager_data_broker(self, value):
        self._template[self._STATISTICS_MANAGER_DATA_BROKER_FIELD] = value

    def set_arp_handler_impl_arp_flow_table_id(self, value):
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_TABLE_ID_FIELD] = value

    def set_distributed_entity_ownership_service_data_store(self, value):
        self._template[self._DISTRIBUTED_ENTITY_OWNERSHIP_SERVICE_DATA_STORE_FIELD] = value

    def set_main_impl_reactive_flow_hard_timeout(self, value):
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_HARD_TIMEOUT_FIELD] = value

    def set_threadpool_impl_scheduled_max_thread_count(self, value):
        self._template[self._THREADPOOL_IMPL_SCHEDULED_MAX_THREAD_COUNT_FIELD] = value

    def set_openflow_provider_impl_rpc_registry(self, value):
        self._template[self._OPENFLOW_PROVIDER_IMPL_RPC_REGISTRY_FIELD] = value

    def set_loop_remover_impl_graph_refresh_delay(self, value):
        self._template[self._LOOP_REMOVER_IMPL_GRAPH_REFRESH_DELAY_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_binding_notification_adapter(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_NOTIFICATION_ADAPTER_FIELD] = value

    def set_odl_concurrent_data_broker_cfg_max_data_broker_commit_queue_size(self, value):
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_COMMIT_QUEUE_SIZE_FIELD] = value

    def set_netconf_northbound_impl_aggregator(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_AGGREGATOR_FIELD] = value

    def set_interfacemgr_impl_broker(self, value):
        self._template[self._INTERFACEMGR_IMPL_BROKER_FIELD] = value

    def set_protocol_framework_executor(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_EXECUTOR_FIELD] = value

    def set_distributed_datastore_provider_operational_schema_service(self, value):
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_OPERATIONAL_SCHEMA_SERVICE_FIELD] = value

    def set_protocol_framework_connect_time(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_CONNECT_TIME_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_notification_queue_park(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_PARK_FIELD] = value

    def set_protocol_framework_timeout(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_TIMEOUT_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_binding_broker_impl(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_BROKER_IMPL_FIELD] = value

    def set_openflow_switch_connection_provider_impl_address(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_ADDRESS_FIELD] = value

    def set_threadpool_impl_flexible_minthreadcount(self, value):
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_MINTHREADCOUNT_FIELD] = value

    def set_aaa_authn_mdsal_store_cfg_dom_broker(self, value):
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_DOM_BROKER_FIELD] = value

    def set_loop_remover_impl_topology_id(self, value):
        self._template[self._LOOP_REMOVER_IMPL_TOPOLOGY_ID_FIELD] = value

    def set_openflow_provider_impl_role(self, value):
        self._template[self._OPENFLOW_PROVIDER_IMPL_ROLE_FIELD] = value

    def set_fibmanager_impl_broker(self, value):
        self._template[self._FIBMANAGER_IMPL_BROKER_FIELD] = value

    def set_main_impl_reactive_flow_table_id(self, value):
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_TABLE_ID_FIELD] = value

    def set_aaa_authn_mdsal_store_cfg_data_broker(self, value):
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_DATA_BROKER_FIELD] = value

    def set_arp_handler_impl_data_broker(self, value):
        self._template[self._ARP_HANDLER_IMPL_DATA_BROKER_FIELD] = value

    def set_main_impl_dropall_flow_priority(self, value):
        self._template[self._MAIN_IMPL_DROPALL_FLOW_PRIORITY_FIELD] = value

    def set_lldp_speaker_address_destination(self, value):
        self._template[self._LLDP_SPEAKER_ADDRESS_DESTINATION_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_schema_service(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_SCHEMA_SERVICE_FIELD] = value

    def set_xsql_data_broker(self, value):
        self._template[self._XSQL_DATA_BROKER_FIELD] = value

    def set_forwardingrules_manager_rpc_registry(self, value):
        self._template[self._FORWARDINGRULES_MANAGER_RPC_REGISTRY_FIELD] = value

    def set_arp_handler_impl_flood_flow_priority(self, value):
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_PRIORITY_FIELD] = value

    def set_lldp_speaker_data_broker(self, value):
        self._template[self._LLDP_SPEAKER_DATA_BROKER_FIELD] = value

    def set_arp_handler_impl_is_hybrid_mode(self, value):
        self._template[self._ARP_HANDLER_IMPL_IS_HYBRID_MODE_FIELD] = value

    def set_vpnservice_impl_odlinterface(self, value):
        self._template[self._VPNSERVICE_IMPL_ODLINTERFACE_FIELD] = value

    def set_distributed_datastore_provider_operational_properties(self, value):
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_OPERATIONAL_PROPERTIES_FIELD] = value

    def set_openflow_switch_connection_provider_impl_port(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_PORT_FIELD] = value

    def set_protocol_framework_max_attempts(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_MAX_ATTEMPTS_FIELD] = value

    def set_netty_timer_ticks_per_wheel(self, value):
        self._template[self._NETTY_TIMER_TICKS_PER_WHEEL_FIELD] = value

    def set_host_tracker_impl_data_broker(self, value):
        self._template[self._HOST_TRACKER_IMPL_DATA_BROKER_FIELD] = value

    def set_arp_handler_impl_flood_flow_idle_timeout(self, value):
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_IDLE_TIMEOUT_FIELD] = value

    def set_arp_handler_impl_is_proactive_flood_mode(self, value):
        self._template[self._ARP_HANDLER_IMPL_IS_PROACTIVE_FLOOD_MODE_FIELD] = value

    def set_threadpool_impl_flexible_queuecapacity(self, value):
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_QUEUECAPACITY_FIELD] = value

    def set_of_switch_config_pusher_rpc_registry(self, value):
        self._template[self._OF_SWITCH_CONFIG_PUSHER_RPC_REGISTRY_FIELD] = value

    def set_netty_timer_tick_duration(self, value):
        self._template[self._NETTY_TIMER_TICK_DURATION_FIELD] = value

    def set_loop_remover_impl_rpc_registry(self, value):
        self._template[self._LOOP_REMOVER_IMPL_RPC_REGISTRY_FIELD] = value

    def set_openflow_switch_connection_provider_impl_switch_idle_timeout(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_SWITCH_IDLE_TIMEOUT_FIELD] = value

    def set_loop_remover_impl_lldp_flow_idle_timeout(self, value):
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_IDLE_TIMEOUT_FIELD] = value

    def set_opendaylight_inmemory_datastore_provider_inmemory_operational_datastore_provider(self, value):
        self._template[self._OPENDAYLIGHT_INMEMORY_DATASTORE_PROVIDER_INMEMORY_OPERATIONAL_DATASTORE_PROVIDER_FIELD] = value

    def set_protocol_framework_max_sleep(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_MAX_SLEEP_FIELD] = value

    def set_distributed_datastore_provider_config_schema_service(self, value):
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_CONFIG_SCHEMA_SERVICE_FIELD] = value

    def set_threadpool_impl_flexible_threadfactory(self, value):
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_THREADFACTORY_FIELD] = value

    def set_topology_manager_impl_broker(self, value):
        self._template[self._TOPOLOGY_MANAGER_IMPL_BROKER_FIELD] = value

    def set_nexthopmgr_impl_mdsalutil(self, value):
        self._template[self._NEXTHOPMGR_IMPL_MDSALUTIL_FIELD] = value

    def set_statistics_manager_notification_service(self, value):
        self._template[self._STATISTICS_MANAGER_NOTIFICATION_SERVICE_FIELD] = value

    def set_threadpool_impl_flexible_max_thread_count(self, value):
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_MAX_THREAD_COUNT_FIELD] = value

    def set_fibmanager_impl_mdsalutil(self, value):
        self._template[self._FIBMANAGER_IMPL_MDSALUTIL_FIELD] = value

    def set_loop_remover_impl_data_broker(self, value):
        self._template[self._LOOP_REMOVER_IMPL_DATA_BROKER_FIELD] = value

    def set_netty_timer_thread_factory(self, value):
        self._template[self._NETTY_TIMER_THREAD_FACTORY_FIELD] = value

    def set_protocol_framework_reconnect_timeout(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_RECONNECT_TIMEOUT_FIELD] = value

    def set_main_impl_data_broker(self, value):
        self._template[self._MAIN_IMPL_DATA_BROKER_FIELD] = value

    def set_protocol_framework_sleep_factor(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_SLEEP_FACTOR_FIELD] = value

    def set_arp_handler_impl_notification_service(self, value):
        self._template[self._ARP_HANDLER_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_loop_remover_impl_lldp_flow_priority(self, value):
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_PRIORITY_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_root_schema_service(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_ROOT_SCHEMA_SERVICE_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_max_data_broker_future_callback_queue_size(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_FUTURE_CALLBACK_QUEUE_SIZE_FIELD] = value

    def set_arp_handler_impl_flood_flow_hard_timeout(self, value):
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_HARD_TIMEOUT_FIELD] = value

    def set_main_impl_is_install_dropall_flow(self, value):
        self._template[self._MAIN_IMPL_IS_INSTALL_DROPALL_FLOW_FIELD] = value

    def set_openflow_switch_connection_provider_impl_transport_protocol(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_TRANSPORT_PROTOCOL_FIELD] = value

    def set_main_impl_is_learning_only_mode(self, value):
        self._template[self._MAIN_IMPL_IS_LEARNING_ONLY_MODE_FIELD] = value

    def set_opendaylight_rest_connector_websocket_port(self, value):
        self._template[self._OPENDAYLIGHT_REST_CONNECTOR_WEBSOCKET_PORT_FIELD] = value

    def set_odl_concurrent_data_broker_cfg_max_data_broker_future_callback_queue_size(self, value):
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_FUTURE_CALLBACK_QUEUE_SIZE_FIELD] = value

    def set_xsql_async_data_broker(self, value):
        self._template[self._XSQL_ASYNC_DATA_BROKER_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_notification_adapter(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_NOTIFICATION_ADAPTER_FIELD] = value

    def set_nexthopmgr_impl_rpc_registry(self, value):
        self._template[self._NEXTHOPMGR_IMPL_RPC_REGISTRY_FIELD] = value

    def set_opendaylight_pingpong_broker_data_broker(self, value):
        self._template[self._OPENDAYLIGHT_PINGPONG_BROKER_DATA_BROKER_FIELD] = value

    def set_remote_rpc_connector_enable_metric_capture(self, value):
        self._template[self._REMOTE_RPC_CONNECTOR_ENABLE_METRIC_CAPTURE_FIELD] = value

    def set_loop_remover_impl_lldp_flow_hard_timeout(self, value):
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_HARD_TIMEOUT_FIELD] = value

    def set_aaa_authn_mdsal_store_cfg_timetowait(self, value):
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_TIMETOWAIT_FIELD] = value

    def set_vpnservice_impl_mdsalutil(self, value):
        self._template[self._VPNSERVICE_IMPL_MDSALUTIL_FIELD] = value

    def set_openflow_provider_impl_openflow_plugin_provider(self, value):
        self._template[self._OPENFLOW_PROVIDER_IMPL_OPENFLOW_PLUGIN_PROVIDER_FIELD] = value

    def set_threadpool_impl_threadpool(self, value):
        self._template[self._THREADPOOL_IMPL_THREADPOOL_FIELD] = value

    def set_arp_handler_impl_arp_flow_idle_timeout(self, value):
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_IDLE_TIMEOUT_FIELD] = value

    def set_arp_handler_impl_arp_flow_hard_timeout(self, value):
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_HARD_TIMEOUT_FIELD] = value

    def set_aaa_authn_mdsal_store_cfg_timetolive(self, value):
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_TIMETOLIVE_FIELD] = value

    def set_arp_handler_impl_flood_flow_table_id(self, value):
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_TABLE_ID_FIELD] = value

    def set_host_tracker_impl_notification_service(self, value):
        self._template[self._HOST_TRACKER_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_nexthopmgr_impl_broker(self, value):
        self._template[self._NEXTHOPMGR_IMPL_BROKER_FIELD] = value

    def set_netconf_northbound_impl_connection_timeout_millis(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_CONNECTION_TIMEOUT_MILLIS_FIELD] = value

    def set_distributed_datastore_provider_config_properties(self, value):
        self._template[self._DISTRIBUTED_DATASTORE_PROVIDER_CONFIG_PROPERTIES_FIELD] = value

    def set_opendaylight_inmemory_datastore_provider_inmemory_config_datastore_provider(self, value):
        self._template[self._OPENDAYLIGHT_INMEMORY_DATASTORE_PROVIDER_INMEMORY_CONFIG_DATASTORE_PROVIDER_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_notification_publish_adapter(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_NOTIFICATION_PUBLISH_ADAPTER_FIELD] = value

    def set_bgpmanager_impl_broker(self, value):
        self._template[self._BGPMANAGER_IMPL_BROKER_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_config_data_store(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_CONFIG_DATA_STORE_FIELD] = value

    def set_idmanager_impl_broker(self, value):
        self._template[self._IDMANAGER_IMPL_BROKER_FIELD] = value

    def set_threadpool_impl_scheduled_threadfactory(self, value):
        self._template[self._THREADPOOL_IMPL_SCHEDULED_THREADFACTORY_FIELD] = value

    def set_lldp_speaker_rpc_registry(self, value):
        self._template[self._LLDP_SPEAKER_RPC_REGISTRY_FIELD] = value

    def set_main_impl_rpc_registry(self, value):
        self._template[self._MAIN_IMPL_RPC_REGISTRY_FIELD] = value

    def set_xsql_schema_service(self, value):
        self._template[self._XSQL_SCHEMA_SERVICE_FIELD] = value

    def set_statistics_manager_statistics_manager_settings(self, value):
        self._template[self._STATISTICS_MANAGER_STATISTICS_MANAGER_SETTINGS_FIELD] = value

    def set_main_impl_reactive_flow_priority(self, value):
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_PRIORITY_FIELD] = value

    def set_main_impl_notification_service(self, value):
        self._template[self._MAIN_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_mdsalutil_impl_broker(self, value):
        self._template[self._MDSALUTIL_IMPL_BROKER_FIELD] = value

    def set_inventory_manager_impl_broker(self, value):
        self._template[self._INVENTORY_MANAGER_IMPL_BROKER_FIELD] = value

    def set_openflow_switch_connection_provider_impl_use_barrier(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_USE_BARRIER_FIELD] = value

    def set_address_tracker_impl_observe_addresses_from(self, value):
        self._template[self._ADDRESS_TRACKER_IMPL_OBSERVE_ADDRESSES_FROM_FIELD] = value

    def set_odl_concurrent_data_broker_cfg_schema_service(self, value):
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_SCHEMA_SERVICE_FIELD] = value

    def set_statistics_manager_rpc_registry(self, value):
        self._template[self._STATISTICS_MANAGER_RPC_REGISTRY_FIELD] = value

    def set_arp_handler_impl_rpc_registry(self, value):
        self._template[self._ARP_HANDLER_IMPL_RPC_REGISTRY_FIELD] = value

    def set_protocol_framework_min_sleep(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_MIN_SLEEP_FIELD] = value

    def set_loop_remover_impl_lldp_flow_table_id(self, value):
        self._template[self._LOOP_REMOVER_IMPL_LLDP_FLOW_TABLE_ID_FIELD] = value

    def set_threadpool_impl_fixed_max_thread_count(self, value):
        self._template[self._THREADPOOL_IMPL_FIXED_MAX_THREAD_COUNT_FIELD] = value

    def set_of_switch_config_pusher_data_broker(self, value):
        self._template[self._OF_SWITCH_CONFIG_PUSHER_DATA_BROKER_FIELD] = value

    def set_openflow_provider_impl_openflow_switch_connection_provider(self, value):
        self._template[self._OPENFLOW_PROVIDER_IMPL_OPENFLOW_SWITCH_CONNECTION_PROVIDER_FIELD] = value

    def set_vpnservice_impl_bgpmanager(self, value):
        self._template[self._VPNSERVICE_IMPL_BGPMANAGER_FIELD] = value

    def set_openflow_switch_connection_provider_impl_statistics(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_STATISTICS_FIELD] = value

    def set_protocol_framework_deadline(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_DEADLINE_FIELD] = value

    def set_vpnservice_impl_broker(self, value):
        self._template[self._VPNSERVICE_IMPL_BROKER_FIELD] = value

    def set_netconf_northbound_impl_timer(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_TIMER_FIELD] = value

    def set_loop_remover_impl_notification_service(self, value):
        self._template[self._LOOP_REMOVER_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_netconf_northbound_impl_worker_thread_group(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_WORKER_THREAD_GROUP_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_binding_data_compatible_broker(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_DATA_COMPATIBLE_BROKER_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_operational_data_store(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_OPERATIONAL_DATA_STORE_FIELD] = value

    def set_host_tracker_impl_topology_id(self, value):
        self._template[self._HOST_TRACKER_IMPL_TOPOLOGY_ID_FIELD] = value

    def set_odl_concurrent_data_broker_cfg_config_data_store(self, value):
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_CONFIG_DATA_STORE_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_async_data_broker(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_ASYNC_DATA_BROKER_FIELD] = value

    def set_openflow_switch_connection_provider_impl_tls(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_TLS_FIELD] = value

    def set_openflow_provider_impl_notification_service(self, value):
        self._template[self._OPENFLOW_PROVIDER_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_threadgroup_thread_count(self, value):
        self._template[self._THREADGROUP_THREAD_COUNT_FIELD] = value

    def set_odl_concurrent_data_broker_cfg_max_data_broker_future_callback_pool_size(self, value):
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_MAX_DATA_BROKER_FUTURE_CALLBACK_POOL_SIZE_FIELD] = value

    def set_packet_handler_impl_notification_service(self, value):
        self._template[self._PACKET_HANDLER_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_notification_queue_spin(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_SPIN_FIELD] = value

    def set_openflow_switch_connection_provider_impl_threads(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_THREADS_FIELD] = value

    def set_remote_rpc_connector_actor_system_name(self, value):
        self._template[self._REMOTE_RPC_CONNECTOR_ACTOR_SYSTEM_NAME_FIELD] = value

    def set_threadpool_impl_name_prefix(self, value):
        self._template[self._THREADPOOL_IMPL_NAME_PREFIX_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_binding_notification_publish_adapter(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_NOTIFICATION_PUBLISH_ADAPTER_FIELD] = value

    def set_remote_rpc_connector_bounded_mailbox_capacity(self, value):
        self._template[self._REMOTE_RPC_CONNECTOR_BOUNDED_MAILBOX_CAPACITY_FIELD] = value

    def set_arp_handler_impl_flood_flow_installation_delay(self, value):
        self._template[self._ARP_HANDLER_IMPL_FLOOD_FLOW_INSTALLATION_DELAY_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_binding_forwarded_data_broker(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_BINDING_FORWARDED_DATA_BROKER_FIELD] = value

    def set_odl_concurrent_data_broker_cfg_operational_data_store(self, value):
        self._template[self._ODL_CONCURRENT_DATA_BROKER_CFG_OPERATIONAL_DATA_STORE_FIELD] = value

    def set_opendaylight_sal_binding_broker_impl_wait_for_schema(self, value):
        self._template[self._OPENDAYLIGHT_SAL_BINDING_BROKER_IMPL_WAIT_FOR_SCHEMA_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_max_data_broker_future_callback_pool_size(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_FUTURE_CALLBACK_POOL_SIZE_FIELD] = value

    def set_main_impl_dropall_flow_hard_timeout(self, value):
        self._template[self._MAIN_IMPL_DROPALL_FLOW_HARD_TIMEOUT_FIELD] = value

    def set_aaa_authn_mdsal_store_cfg_password(self, value):
        self._template[self._AAA_AUTHN_MDSAL_STORE_CFG_PASSWORD_FIELD] = value

    def set_nexthopmgr_impl_odlinterface(self, value):
        self._template[self._NEXTHOPMGR_IMPL_ODLINTERFACE_FIELD] = value

    def set_netconf_northbound_impl_server_monitor(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_SERVER_MONITOR_FIELD] = value

    def set_address_tracker_impl_data_broker(self, value):
        self._template[self._ADDRESS_TRACKER_IMPL_DATA_BROKER_FIELD] = value

    def set_vpnservice_impl_rpcregistry(self, value):
        self._template[self._VPNSERVICE_IMPL_RPCREGISTRY_FIELD] = value

    def set_main_impl_dropall_flow_table_id(self, value):
        self._template[self._MAIN_IMPL_DROPALL_FLOW_TABLE_ID_FIELD] = value

    def set_remote_rpc_connector_dom_broker(self, value):
        self._template[self._REMOTE_RPC_CONNECTOR_DOM_BROKER_FIELD] = value

    def set_netconf_northbound_impl_mappers(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_MAPPERS_FIELD] = value

    def set_forwardingrules_manager_data_broker(self, value):
        self._template[self._FORWARDINGRULES_MANAGER_DATA_BROKER_FIELD] = value

    def set_main_impl_dropall_flow_idle_timeout(self, value):
        self._template[self._MAIN_IMPL_DROPALL_FLOW_IDLE_TIMEOUT_FIELD] = value

    def set_fibmanager_impl_vpnmanager(self, value):
        self._template[self._FIBMANAGER_IMPL_VPNMANAGER_FIELD] = value

    def set_address_tracker_impl_notification_service(self, value):
        self._template[self._ADDRESS_TRACKER_IMPL_NOTIFICATION_SERVICE_FIELD] = value

    def set_netconf_northbound_impl_boss_thread_group(self, value):
        self._template[self._NETCONF_NORTHBOUND_IMPL_BOSS_THREAD_GROUP_FIELD] = value

    def set_protocol_framework_timed_reconnect_executor(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_TIMED_RECONNECT_EXECUTOR_FIELD] = value

    def set_address_tracker_impl_timestamp_update_interval(self, value):
        self._template[self._ADDRESS_TRACKER_IMPL_TIMESTAMP_UPDATE_INTERVAL_FIELD] = value

    def set_loop_remover_impl_is_install_lldp_flow(self, value):
        self._template[self._LOOP_REMOVER_IMPL_IS_INSTALL_LLDP_FLOW_FIELD] = value

    def set_topology_lldp_discovery_impl_broker(self, value):
        self._template[self._TOPOLOGY_LLDP_DISCOVERY_IMPL_BROKER_FIELD] = value

    def set_main_impl_reactive_flow_idle_timeout(self, value):
        self._template[self._MAIN_IMPL_REACTIVE_FLOW_IDLE_TIMEOUT_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_notification_queue_depth(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_NOTIFICATION_QUEUE_DEPTH_FIELD] = value

    def set_openflow_switch_connection_provider_impl_openflow_switch_connection_provider(self, value):
        self._template[self._OPENFLOW_SWITCH_CONNECTION_PROVIDER_IMPL_OPENFLOW_SWITCH_CONNECTION_PROVIDER_FIELD] = value

    def set_idmanager_impl_rpc_registry(self, value):
        self._template[self._IDMANAGER_IMPL_RPC_REGISTRY_FIELD] = value

    def set_arp_handler_impl_arp_flow_priority(self, value):
        self._template[self._ARP_HANDLER_IMPL_ARP_FLOW_PRIORITY_FIELD] = value

    def set_opendaylight_rest_connector_dom_broker(self, value):
        self._template[self._OPENDAYLIGHT_REST_CONNECTOR_DOM_BROKER_FIELD] = value

    def set_protocol_framework_reconnect_executor(self, value):
        self._template[self._PROTOCOL_FRAMEWORK_RECONNECT_EXECUTOR_FIELD] = value

    def set_opendaylight_sal_dom_broker_impl_max_data_broker_commit_queue_size(self, value):
        self._template[self._OPENDAYLIGHT_SAL_DOM_BROKER_IMPL_MAX_DATA_BROKER_COMMIT_QUEUE_SIZE_FIELD] = value

    def set_openflow_provider_impl_data_broker(self, value):
        self._template[self._OPENFLOW_PROVIDER_IMPL_DATA_BROKER_FIELD] = value

    def set_threadpool_impl_flexible_keepalivemillis(self, value):
        self._template[self._THREADPOOL_IMPL_FLEXIBLE_KEEPALIVEMILLIS_FIELD] = value

    def set_threadpool_impl_fixed_threadfactory(self, value):
        self._template[self._THREADPOOL_IMPL_FIXED_THREADFACTORY_FIELD] = value

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

    def create_configuration(self):
        
        payload = {self._CONFIGURATION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_configuration(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_configuration(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class UNRESERVED_BANDWIDTH(object):

    _UNRESERVED_BANDWIDTH_FIELD = "unreserved-bandwidth"
    _OSPF_TOPOLOGY_BANDWIDTH_FIELD = "ospf-topology:bandwidth"
    _PRIORITY_FIELD = "priority"
    _BANDWIDTH_FIELD = "bandwidth"
    _OSPF_TOPOLOGY_PRIORITY_FIELD = "ospf-topology:priority"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_BANDWIDTH_FIELD] = None
        self._template[self._PRIORITY_FIELD] = None
        self._template[self._BANDWIDTH_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_PRIORITY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_BANDWIDTH_FIELD] = value

    def set_priority(self, value):
        self._template[self._PRIORITY_FIELD] = value

    def set_bandwidth(self, value):
        self._template[self._BANDWIDTH_FIELD] = value

    def set_ospf_topology_priority(self, value):
        self._template[self._OSPF_TOPOLOGY_PRIORITY_FIELD] = value

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

    def create_unreserved_bandwidth(self):
        
        payload = {self._UNRESERVED_BANDWIDTH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_unreserved_bandwidth(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_unreserved_bandwidth(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TOPOLOGY(object):

    _TOPOLOGY_FIELD = "topology"
    _NODE_FIELD = "node"
    _L3_UNICAST_IGP_TOPOLOGY_IGP_TOPOLOGY_ATTRIBUTES_FIELD = "l3-unicast-igp-topology:igp-topology-attributes"
    _UNDERLAY_TOPOLOGY_FIELD = "underlay-topology"
    _SERVER_PROVIDED_FIELD = "server-provided"
    _OPENDAYLIGHT_TOPOLOGY_VIEW_ORIGINAL_TOPOLOGY_FIELD = "opendaylight-topology-view:original-topology"
    _TOPOLOGY_TYPES_FIELD = "topology-types"
    _IGP_TOPOLOGY_ATTRIBUTES_FIELD = "igp-topology-attributes"
    _LINK_FIELD = "link"
    _TOPOLOGY_ID_FIELD = "topology-id"

    def __init__(self):
        self._template = {}
        self._template[self._NODE_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IGP_TOPOLOGY_ATTRIBUTES_FIELD] = None
        self._template[self._UNDERLAY_TOPOLOGY_FIELD] = None
        self._template[self._SERVER_PROVIDED_FIELD] = None
        self._template[self._OPENDAYLIGHT_TOPOLOGY_VIEW_ORIGINAL_TOPOLOGY_FIELD] = None
        self._template[self._TOPOLOGY_TYPES_FIELD] = None
        self._template[self._IGP_TOPOLOGY_ATTRIBUTES_FIELD] = None
        self._template[self._LINK_FIELD] = None
        self._template[self._TOPOLOGY_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._node = NODE()
        self._underlay_topology = UNDERLAY_TOPOLOGY()
        self._topology_types = TOPOLOGY_TYPES()
        self._igp_topology_attributes = IGP_TOPOLOGY_ATTRIBUTES()
        self._link = LINK()

    @property
    def node(self):
        return self._node

    @property
    def underlay_topology(self):
        return self._underlay_topology

    @property
    def topology_types(self):
        return self._topology_types

    @property
    def igp_topology_attributes(self):
        return self._igp_topology_attributes

    @property
    def link(self):
        return self._link

    def set_l3_unicast_igp_topology_igp_topology_attributes(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IGP_TOPOLOGY_ATTRIBUTES_FIELD] = value

    def set_server_provided(self, value):
        self._template[self._SERVER_PROVIDED_FIELD] = value

    def set_opendaylight_topology_view_original_topology(self, value):
        self._template[self._OPENDAYLIGHT_TOPOLOGY_VIEW_ORIGINAL_TOPOLOGY_FIELD] = value

    def set_topology_id(self, value):
        self._template[self._TOPOLOGY_ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._NODE_FIELD] = self.node.get_template(default=default)
            self._default_template[self._UNDERLAY_TOPOLOGY_FIELD] = self.underlay_topology.get_template(default=default)
            self._default_template[self._TOPOLOGY_TYPES_FIELD] = self.topology_types.get_template(default=default)
            self._default_template[self._IGP_TOPOLOGY_ATTRIBUTES_FIELD] = self.igp_topology_attributes.get_template(default=default)
            self._default_template[self._LINK_FIELD] = self.link.get_template(default=default)
            return self._default_template
        else:
            self._template[self._NODE_FIELD] = self.node.get_template()
            self._template[self._UNDERLAY_TOPOLOGY_FIELD] = self.underlay_topology.get_template()
            self._template[self._TOPOLOGY_TYPES_FIELD] = self.topology_types.get_template()
            self._template[self._IGP_TOPOLOGY_ATTRIBUTES_FIELD] = self.igp_topology_attributes.get_template()
            self._template[self._LINK_FIELD] = self.link.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        node_payload = self.node.get_payload()
        if node_payload:
            payload[self._NODE_FIELD] = node_payload
        underlay_topology_payload = self.underlay_topology.get_payload()
        if underlay_topology_payload:
            payload[self._UNDERLAY_TOPOLOGY_FIELD] = underlay_topology_payload
        topology_types_payload = self.topology_types.get_payload()
        if topology_types_payload:
            payload[self._TOPOLOGY_TYPES_FIELD] = topology_types_payload
        igp_topology_attributes_payload = self.igp_topology_attributes.get_payload()
        if igp_topology_attributes_payload:
            payload[self._IGP_TOPOLOGY_ATTRIBUTES_FIELD] = igp_topology_attributes_payload
        link_payload = self.link.get_payload()
        if link_payload:
            payload[self._LINK_FIELD] = link_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_topology(self):
        
        payload = {self._TOPOLOGY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_topology(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_topology(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class EXTENSION(object):

    _EXTENSION_FIELD = "extension"
    _OPENFLOWPLUGIN_EXTENSION_GENERAL_DOS_EKIS_FIELD = "openflowplugin-extension-general:dos-ekis"
    _DOS_EKIS_FIELD = "dos-ekis"

    def __init__(self):
        self._template = {}
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_DOS_EKIS_FIELD] = None
        self._template[self._DOS_EKIS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_openflowplugin_extension_general_dos_ekis(self, value):
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_DOS_EKIS_FIELD] = value

    def set_dos_ekis(self, value):
        self._template[self._DOS_EKIS_FIELD] = value

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

    def create_extension(self):
        
        payload = {self._EXTENSION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_extension(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_extension(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class NODE_IDENTIFIER(object):

    _NODE_IDENTIFIER_FIELD = "node-identifier"
    _OPENDAYLIGHT_TOPOLOGY_TYPE_FIELD = "opendaylight-topology:type"
    _IDENTIFIER_FIELD = "identifier"
    _TYPE_FIELD = "type"
    _OPENDAYLIGHT_TOPOLOGY_IDENTIFIER_FIELD = "opendaylight-topology:identifier"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_TOPOLOGY_TYPE_FIELD] = None
        self._template[self._IDENTIFIER_FIELD] = None
        self._template[self._TYPE_FIELD] = None
        self._template[self._OPENDAYLIGHT_TOPOLOGY_IDENTIFIER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_topology_type(self, value):
        self._template[self._OPENDAYLIGHT_TOPOLOGY_TYPE_FIELD] = value

    def set_identifier(self, value):
        self._template[self._IDENTIFIER_FIELD] = value

    def set_type(self, value):
        self._template[self._TYPE_FIELD] = value

    def set_opendaylight_topology_identifier(self, value):
        self._template[self._OPENDAYLIGHT_TOPOLOGY_IDENTIFIER_FIELD] = value

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

    def create_node_identifier(self):
        
        payload = {self._NODE_IDENTIFIER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_node_identifier(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_node_identifier(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ICMPV4_MATCH(object):

    _ICMPV4_MATCH_FIELD = "icmpv4-match"
    _ICMPV4_TYPE_FIELD = "icmpv4-type"
    _ICMPV4_CODE_FIELD = "icmpv4-code"
    _OPENDAYLIGHT_GROUP_STATISTICS_ICMPV4_CODE_FIELD = "opendaylight-group-statistics:icmpv4-code"
    _OPENDAYLIGHT_GROUP_STATISTICS_ICMPV4_TYPE_FIELD = "opendaylight-group-statistics:icmpv4-type"

    def __init__(self):
        self._template = {}
        self._template[self._ICMPV4_TYPE_FIELD] = None
        self._template[self._ICMPV4_CODE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV4_CODE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV4_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_icmpv4_type(self, value):
        self._template[self._ICMPV4_TYPE_FIELD] = value

    def set_icmpv4_code(self, value):
        self._template[self._ICMPV4_CODE_FIELD] = value

    def set_opendaylight_group_statistics_icmpv4_code(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV4_CODE_FIELD] = value

    def set_opendaylight_group_statistics_icmpv4_type(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ICMPV4_TYPE_FIELD] = value

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

    def create_icmpv4_match(self):
        
        payload = {self._ICMPV4_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_icmpv4_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_icmpv4_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IP_MATCH(object):

    _IP_MATCH_FIELD = "ip-match"
    _OPENDAYLIGHT_GROUP_STATISTICS_IP_PROTO_FIELD = "opendaylight-group-statistics:ip-proto"
    _OPENDAYLIGHT_GROUP_STATISTICS_IP_PROTOCOL_FIELD = "opendaylight-group-statistics:ip-protocol"
    _IP_ECN_FIELD = "ip-ecn"
    _IP_PROTOCOL_FIELD = "ip-protocol"
    _OPENDAYLIGHT_GROUP_STATISTICS_IP_ECN_FIELD = "opendaylight-group-statistics:ip-ecn"
    _IP_PROTO_FIELD = "ip-proto"
    _IP_DSCP_FIELD = "ip-dscp"
    _OPENDAYLIGHT_GROUP_STATISTICS_IP_DSCP_FIELD = "opendaylight-group-statistics:ip-dscp"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_PROTO_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_PROTOCOL_FIELD] = None
        self._template[self._IP_ECN_FIELD] = None
        self._template[self._IP_PROTOCOL_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_ECN_FIELD] = None
        self._template[self._IP_PROTO_FIELD] = None
        self._template[self._IP_DSCP_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_DSCP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_ip_proto(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_PROTO_FIELD] = value

    def set_opendaylight_group_statistics_ip_protocol(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_PROTOCOL_FIELD] = value

    def set_ip_ecn(self, value):
        self._template[self._IP_ECN_FIELD] = value

    def set_ip_protocol(self, value):
        self._template[self._IP_PROTOCOL_FIELD] = value

    def set_opendaylight_group_statistics_ip_ecn(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_ECN_FIELD] = value

    def set_ip_proto(self, value):
        self._template[self._IP_PROTO_FIELD] = value

    def set_ip_dscp(self, value):
        self._template[self._IP_DSCP_FIELD] = value

    def set_opendaylight_group_statistics_ip_dscp(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_IP_DSCP_FIELD] = value

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

    def create_ip_match(self):
        
        payload = {self._IP_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ip_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ip_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VALIDATION_CONFIG(object):

    _VALIDATION_CONFIG_FIELD = "validation-config"
    _ENABLE_FIELD = "enable"
    _ENABLE_IBGP_FIELD = "enable-ibgp"
    _VALIDATION_TIME_FIELD = "validation-time"

    def __init__(self):
        self._template = {}
        self._template[self._ENABLE_FIELD] = None
        self._template[self._ENABLE_IBGP_FIELD] = None
        self._template[self._VALIDATION_TIME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._validation_time = VALIDATION_TIME()

    @property
    def validation_time(self):
        return self._validation_time

    def set_enable(self, value):
        self._template[self._ENABLE_FIELD] = value

    def set_enable_ibgp(self, value):
        self._template[self._ENABLE_IBGP_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._VALIDATION_TIME_FIELD] = self.validation_time.get_template(default=default)
            return self._default_template
        else:
            self._template[self._VALIDATION_TIME_FIELD] = self.validation_time.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        validation_time_payload = self.validation_time.get_payload()
        if validation_time_payload:
            payload[self._VALIDATION_TIME_FIELD] = validation_time_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_validation_config(self):
        
        payload = {self._VALIDATION_CONFIG_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_validation_config(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_validation_config(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class QUEUE(object):

    _QUEUE_FIELD = "queue"
    _FLOW_NODE_INVENTORY_PROPERTY_FIELD = "flow-node-inventory:property"
    _FLOW_NODE_INVENTORY_PORT_FIELD = "flow-node-inventory:port"
    _FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD = "flow-capable-node-connector-queue-statistics"
    _FLOW_NODE_INVENTORY_QUEUE_ID_FIELD = "flow-node-inventory:queue-id"
    _OPENDAYLIGHT_QUEUE_STATISTICS_FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD = "opendaylight-queue-statistics:flow-capable-node-connector-queue-statistics"
    _QUEUE_ID_FIELD = "queue-id"
    _PROPERTY_FIELD = "property"
    _PORT_FIELD = "port"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_PROPERTY_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_PORT_FIELD] = None
        self._template[self._FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_QUEUE_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD] = None
        self._template[self._QUEUE_ID_FIELD] = None
        self._template[self._PROPERTY_FIELD] = None
        self._template[self._PORT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._flow_capable_node_connector_queue_statistics = FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS()

    @property
    def flow_capable_node_connector_queue_statistics(self):
        return self._flow_capable_node_connector_queue_statistics

    def set_flow_node_inventory_property(self, value):
        self._template[self._FLOW_NODE_INVENTORY_PROPERTY_FIELD] = value

    def set_flow_node_inventory_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_PORT_FIELD] = value

    def set_flow_node_inventory_queue_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_QUEUE_ID_FIELD] = value

    def set_opendaylight_queue_statistics_flow_capable_node_connector_queue_statistics(self, value):
        self._template[self._OPENDAYLIGHT_QUEUE_STATISTICS_FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD] = value

    def set_queue_id(self, value):
        self._template[self._QUEUE_ID_FIELD] = value

    def set_property(self, value):
        self._template[self._PROPERTY_FIELD] = value

    def set_port(self, value):
        self._template[self._PORT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD] = self.flow_capable_node_connector_queue_statistics.get_template(default=default)
            return self._default_template
        else:
            self._template[self._FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD] = self.flow_capable_node_connector_queue_statistics.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        flow_capable_node_connector_queue_statistics_payload = self.flow_capable_node_connector_queue_statistics.get_payload()
        if flow_capable_node_connector_queue_statistics_payload:
            payload[self._FLOW_CAPABLE_NODE_CONNECTOR_QUEUE_STATISTICS_FIELD] = flow_capable_node_connector_queue_statistics_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_queue(self):
        
        payload = {self._QUEUE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_queue(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_queue(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TABLE_FEATURE_CONTAINER(object):

    _TABLE_FEATURE_CONTAINER_FIELD = "table-feature-container"
    _TABLE_FEATURES_FIELD = "table-features"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURES_FIELD = "opendaylight-flow-table-statistics:table-features"

    def __init__(self):
        self._template = {}
        self._template[self._TABLE_FEATURES_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._table_features = TABLE_FEATURES()

    @property
    def table_features(self):
        return self._table_features

    def set_opendaylight_flow_table_statistics_table_features(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TABLE_FEATURES_FIELD] = self.table_features.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TABLE_FEATURES_FIELD] = self.table_features.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        table_features_payload = self.table_features.get_payload()
        if table_features_payload:
            payload[self._TABLE_FEATURES_FIELD] = table_features_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_table_feature_container(self):
        
        payload = {self._TABLE_FEATURE_CONTAINER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_table_feature_container(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_table_feature_container(self):
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


class ISO(object):

    _ISO_FIELD = "iso"
    _ISO_PSEUDONODE_ID_FIELD = "iso-pseudonode-id"
    _ISIS_TOPOLOGY_ISO_PSEUDONODE_ID_FIELD = "isis-topology:iso-pseudonode-id"
    _ISIS_TOPOLOGY_ISO_SYSTEM_ID_FIELD = "isis-topology:iso-system-id"
    _ISO_SYSTEM_ID_FIELD = "iso-system-id"

    def __init__(self):
        self._template = {}
        self._template[self._ISO_PSEUDONODE_ID_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ISO_PSEUDONODE_ID_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ISO_SYSTEM_ID_FIELD] = None
        self._template[self._ISO_SYSTEM_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_iso_pseudonode_id(self, value):
        self._template[self._ISO_PSEUDONODE_ID_FIELD] = value

    def set_isis_topology_iso_pseudonode_id(self, value):
        self._template[self._ISIS_TOPOLOGY_ISO_PSEUDONODE_ID_FIELD] = value

    def set_isis_topology_iso_system_id(self, value):
        self._template[self._ISIS_TOPOLOGY_ISO_SYSTEM_ID_FIELD] = value

    def set_iso_system_id(self, value):
        self._template[self._ISO_SYSTEM_ID_FIELD] = value

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

    def create_iso(self):
        
        payload = {self._ISO_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_iso(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_iso(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SUPPORTED_INSTRUCTIONS(object):

    _SUPPORTED_INSTRUCTIONS_FIELD = "supported-instructions"
    _FLOW_NODE_INVENTORY_INSTRUCTION_TYPE_FIELD = "flow-node-inventory:instruction-type"
    _INSTRUCTION_TYPE_FIELD = "instruction-type"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_INSTRUCTION_TYPE_FIELD] = None
        self._template[self._INSTRUCTION_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._instruction_type = INSTRUCTION_TYPE()

    @property
    def instruction_type(self):
        return self._instruction_type

    def set_flow_node_inventory_instruction_type(self, value):
        self._template[self._FLOW_NODE_INVENTORY_INSTRUCTION_TYPE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._INSTRUCTION_TYPE_FIELD] = self.instruction_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._INSTRUCTION_TYPE_FIELD] = self.instruction_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        instruction_type_payload = self.instruction_type.get_payload()
        if instruction_type_payload:
            payload[self._INSTRUCTION_TYPE_FIELD] = instruction_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_supported_instructions(self):
        
        payload = {self._SUPPORTED_INSTRUCTIONS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_supported_instructions(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_supported_instructions(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ACTION(object):

    _ACTION_FIELD = "action"
    _OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD = "opendaylight-group-statistics:action"
    _OPENDAYLIGHT_GROUP_STATISTICS_ORDER_FIELD = "opendaylight-group-statistics:order"
    _ORDER_FIELD = "order"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ORDER_FIELD] = None
        self._template[self._ORDER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._opendaylight_group_statistics_action = OPENDAYLIGHT_GROUP_STATISTICS_ACTION()

    @property
    def opendaylight_group_statistics_action(self):
        return self._opendaylight_group_statistics_action

    def set_opendaylight_group_statistics_order(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ORDER_FIELD] = value

    def set_order(self, value):
        self._template[self._ORDER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = self.opendaylight_group_statistics_action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = self.opendaylight_group_statistics_action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        opendaylight_group_statistics_action_payload = self.opendaylight_group_statistics_action.get_payload()
        if opendaylight_group_statistics_action_payload:
            payload[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = opendaylight_group_statistics_action_payload
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


class ETHERNET_DESTINATION(object):

    _ETHERNET_DESTINATION_FIELD = "ethernet-destination"
    _OPENDAYLIGHT_GROUP_STATISTICS_MASK_FIELD = "opendaylight-group-statistics:mask"
    _OPENDAYLIGHT_GROUP_STATISTICS_ADDRESS_FIELD = "opendaylight-group-statistics:address"
    _MASK_FIELD = "mask"
    _ADDRESS_FIELD = "address"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MASK_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ADDRESS_FIELD] = None
        self._template[self._MASK_FIELD] = None
        self._template[self._ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_mask(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MASK_FIELD] = value

    def set_opendaylight_group_statistics_address(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ADDRESS_FIELD] = value

    def set_mask(self, value):
        self._template[self._MASK_FIELD] = value

    def set_address(self, value):
        self._template[self._ADDRESS_FIELD] = value

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

    def create_ethernet_destination(self):
        
        payload = {self._ETHERNET_DESTINATION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ethernet_destination(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ethernet_destination(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


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


class ADDRESSES(object):

    _ADDRESSES_FIELD = "addresses"
    _ADDRESS_TRACKER_VLAN_FIELD = "address-tracker:vlan"
    _FIRST_SEEN_FIELD = "first-seen"
    _IP_FIELD = "ip"
    _ADDRESS_TRACKER_IP_FIELD = "address-tracker:ip"
    _VLAN_FIELD = "vlan"
    _LAST_SEEN_FIELD = "last-seen"
    _ADDRESS_TRACKER_MAC_FIELD = "address-tracker:mac"
    _MAC_FIELD = "mac"
    _ADDRESS_TRACKER_LAST_SEEN_FIELD = "address-tracker:last-seen"
    _ID_FIELD = "id"
    _ADDRESS_TRACKER_ID_FIELD = "address-tracker:id"
    _ADDRESS_TRACKER_FIRST_SEEN_FIELD = "address-tracker:first-seen"

    def __init__(self):
        self._template = {}
        self._template[self._ADDRESS_TRACKER_VLAN_FIELD] = None
        self._template[self._FIRST_SEEN_FIELD] = None
        self._template[self._IP_FIELD] = None
        self._template[self._ADDRESS_TRACKER_IP_FIELD] = None
        self._template[self._VLAN_FIELD] = None
        self._template[self._LAST_SEEN_FIELD] = None
        self._template[self._ADDRESS_TRACKER_MAC_FIELD] = None
        self._template[self._MAC_FIELD] = None
        self._template[self._ADDRESS_TRACKER_LAST_SEEN_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._template[self._ADDRESS_TRACKER_ID_FIELD] = None
        self._template[self._ADDRESS_TRACKER_FIRST_SEEN_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_address_tracker_vlan(self, value):
        self._template[self._ADDRESS_TRACKER_VLAN_FIELD] = value

    def set_first_seen(self, value):
        self._template[self._FIRST_SEEN_FIELD] = value

    def set_ip(self, value):
        self._template[self._IP_FIELD] = value

    def set_address_tracker_ip(self, value):
        self._template[self._ADDRESS_TRACKER_IP_FIELD] = value

    def set_vlan(self, value):
        self._template[self._VLAN_FIELD] = value

    def set_last_seen(self, value):
        self._template[self._LAST_SEEN_FIELD] = value

    def set_address_tracker_mac(self, value):
        self._template[self._ADDRESS_TRACKER_MAC_FIELD] = value

    def set_mac(self, value):
        self._template[self._MAC_FIELD] = value

    def set_address_tracker_last_seen(self, value):
        self._template[self._ADDRESS_TRACKER_LAST_SEEN_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_address_tracker_id(self, value):
        self._template[self._ADDRESS_TRACKER_ID_FIELD] = value

    def set_address_tracker_first_seen(self, value):
        self._template[self._ADDRESS_TRACKER_FIRST_SEEN_FIELD] = value

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

    def create_addresses(self):
        
        payload = {self._ADDRESSES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_addresses(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_addresses(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class EXTENSION_LIST(object):

    _EXTENSION_LIST_FIELD = "extension-list"
    _EXTENSION_KEY_FIELD = "extension-key"
    _OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_KEY_FIELD = "openflowplugin-extension-general:extension-key"
    _OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_FIELD = "openflowplugin-extension-general:extension"
    _EXTENSION_FIELD = "extension"

    def __init__(self):
        self._template = {}
        self._template[self._EXTENSION_KEY_FIELD] = None
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_KEY_FIELD] = None
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_FIELD] = None
        self._template[self._EXTENSION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._extension = EXTENSION()

    @property
    def extension(self):
        return self._extension

    def set_extension_key(self, value):
        self._template[self._EXTENSION_KEY_FIELD] = value

    def set_openflowplugin_extension_general_extension_key(self, value):
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_KEY_FIELD] = value

    def set_openflowplugin_extension_general_extension(self, value):
        self._template[self._OPENFLOWPLUGIN_EXTENSION_GENERAL_EXTENSION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._EXTENSION_FIELD] = self.extension.get_template(default=default)
            return self._default_template
        else:
            self._template[self._EXTENSION_FIELD] = self.extension.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        extension_payload = self.extension.get_payload()
        if extension_payload:
            payload[self._EXTENSION_FIELD] = extension_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_extension_list(self):
        
        payload = {self._EXTENSION_LIST_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_extension_list(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_extension_list(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IGP_TERMINATION_POINT_ATTRIBUTES(object):

    _IGP_TERMINATION_POINT_ATTRIBUTES_FIELD = "igp-termination-point-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD = "l3-unicast-igp-topology:termination-point-type"

    def __init__(self):
        self._template = {}
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._l3_unicast_igp_topology_termination_point_type = L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE()

    @property
    def l3_unicast_igp_topology_termination_point_type(self):
        return self._l3_unicast_igp_topology_termination_point_type

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD] = self.l3_unicast_igp_topology_termination_point_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD] = self.l3_unicast_igp_topology_termination_point_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        l3_unicast_igp_topology_termination_point_type_payload = self.l3_unicast_igp_topology_termination_point_type.get_payload()
        if l3_unicast_igp_topology_termination_point_type_payload:
            payload[self._L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD] = l3_unicast_igp_topology_termination_point_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_igp_termination_point_attributes(self):
        
        payload = {self._IGP_TERMINATION_POINT_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_igp_termination_point_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_igp_termination_point_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SUPPORTED_MATCH_TYPES(object):

    _SUPPORTED_MATCH_TYPES_FIELD = "supported-match-types"
    _FLOW_NODE_INVENTORY_MATCH_TYPE_FIELD = "flow-node-inventory:match-type"
    _MATCH_TYPE_FIELD = "match-type"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_MATCH_TYPE_FIELD] = None
        self._template[self._MATCH_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._match_type = MATCH_TYPE()

    @property
    def match_type(self):
        return self._match_type

    def set_flow_node_inventory_match_type(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MATCH_TYPE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MATCH_TYPE_FIELD] = self.match_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MATCH_TYPE_FIELD] = self.match_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        match_type_payload = self.match_type.get_payload()
        if match_type_payload:
            payload[self._MATCH_TYPE_FIELD] = match_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_supported_match_types(self):
        
        payload = {self._SUPPORTED_MATCH_TYPES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_supported_match_types(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_supported_match_types(self):
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


class L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE(object):

    _L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD = "l3-unicast-igp-topology:termination-point-type"
    _L3_UNICAST_IGP_TOPOLOGY_UNNUMBERED_ID_FIELD = "l3-unicast-igp-topology:unnumbered-id"
    _L3_UNICAST_IGP_TOPOLOGY_IP_ADDRESS_FIELD = "l3-unicast-igp-topology:ip-address"

    def __init__(self):
        self._template = {}
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_UNNUMBERED_ID_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IP_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_l3_unicast_igp_topology_unnumbered_id(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_UNNUMBERED_ID_FIELD] = value

    def set_l3_unicast_igp_topology_ip_address(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IP_ADDRESS_FIELD] = value

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

    def create_l3_unicast_igp_topology_termination_point_type(self):
        
        payload = {self._L3_UNICAST_IGP_TOPOLOGY_TERMINATION_POINT_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_l3_unicast_igp_topology_termination_point_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_l3_unicast_igp_topology_termination_point_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TABLE(object):

    _TABLE_FIELD = "table"
    _FLOW_NODE_INVENTORY_ID_FIELD = "flow-node-inventory:id"
    _TABLE_FEATURES_FIELD = "table-features"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_CONTAINER_FIELD = "opendaylight-flow-table-statistics:table-feature-container"
    _FLOW_NODE_INVENTORY_FLOW_FIELD = "flow-node-inventory:flow"
    _FLOW_FIELD = "flow"
    _TABLE_FEATURE_CONTAINER_FIELD = "table-feature-container"
    _FLOW_TABLE_STATISTICS_FIELD = "flow-table-statistics"
    _AGGREGATE_FLOW_STATISTICS_FIELD = "aggregate-flow-statistics"
    _FLOW_HASH_ID_MAP_FIELD = "flow-hash-id-map"
    _FLOW_NODE_INVENTORY_TABLE_FEATURES_FIELD = "flow-node-inventory:table-features"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_FLOW_TABLE_STATISTICS_FIELD = "opendaylight-flow-table-statistics:flow-table-statistics"
    _FLOW_NODE_INVENTORY_FLOW_HASH_ID_MAP_FIELD = "flow-node-inventory:flow-hash-id-map"
    _OPENDAYLIGHT_FLOW_STATISTICS_AGGREGATE_FLOW_STATISTICS_FIELD = "opendaylight-flow-statistics:aggregate-flow-statistics"
    _ID_FIELD = "id"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_ID_FIELD] = None
        self._template[self._TABLE_FEATURES_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_CONTAINER_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_FLOW_FIELD] = None
        self._template[self._FLOW_FIELD] = None
        self._template[self._TABLE_FEATURE_CONTAINER_FIELD] = None
        self._template[self._FLOW_TABLE_STATISTICS_FIELD] = None
        self._template[self._AGGREGATE_FLOW_STATISTICS_FIELD] = None
        self._template[self._FLOW_HASH_ID_MAP_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TABLE_FEATURES_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_FLOW_TABLE_STATISTICS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_FLOW_HASH_ID_MAP_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_AGGREGATE_FLOW_STATISTICS_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._table_features = TABLE_FEATURES()
        self._flow = FLOW()
        self._table_feature_container = TABLE_FEATURE_CONTAINER()
        self._flow_table_statistics = FLOW_TABLE_STATISTICS()
        self._aggregate_flow_statistics = AGGREGATE_FLOW_STATISTICS()
        self._flow_hash_id_map = FLOW_HASH_ID_MAP()

    @property
    def table_features(self):
        return self._table_features

    @property
    def flow(self):
        return self._flow

    @property
    def table_feature_container(self):
        return self._table_feature_container

    @property
    def flow_table_statistics(self):
        return self._flow_table_statistics

    @property
    def aggregate_flow_statistics(self):
        return self._aggregate_flow_statistics

    @property
    def flow_hash_id_map(self):
        return self._flow_hash_id_map

    def set_flow_node_inventory_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ID_FIELD] = value

    def set_opendaylight_flow_table_statistics_table_feature_container(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_CONTAINER_FIELD] = value

    def set_flow_node_inventory_flow(self, value):
        self._template[self._FLOW_NODE_INVENTORY_FLOW_FIELD] = value

    def set_flow_node_inventory_table_features(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TABLE_FEATURES_FIELD] = value

    def set_opendaylight_flow_table_statistics_flow_table_statistics(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_FLOW_TABLE_STATISTICS_FIELD] = value

    def set_flow_node_inventory_flow_hash_id_map(self, value):
        self._template[self._FLOW_NODE_INVENTORY_FLOW_HASH_ID_MAP_FIELD] = value

    def set_opendaylight_flow_statistics_aggregate_flow_statistics(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_AGGREGATE_FLOW_STATISTICS_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TABLE_FEATURES_FIELD] = self.table_features.get_template(default=default)
            self._default_template[self._FLOW_FIELD] = self.flow.get_template(default=default)
            self._default_template[self._TABLE_FEATURE_CONTAINER_FIELD] = self.table_feature_container.get_template(default=default)
            self._default_template[self._FLOW_TABLE_STATISTICS_FIELD] = self.flow_table_statistics.get_template(default=default)
            self._default_template[self._AGGREGATE_FLOW_STATISTICS_FIELD] = self.aggregate_flow_statistics.get_template(default=default)
            self._default_template[self._FLOW_HASH_ID_MAP_FIELD] = self.flow_hash_id_map.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TABLE_FEATURES_FIELD] = self.table_features.get_template()
            self._template[self._FLOW_FIELD] = self.flow.get_template()
            self._template[self._TABLE_FEATURE_CONTAINER_FIELD] = self.table_feature_container.get_template()
            self._template[self._FLOW_TABLE_STATISTICS_FIELD] = self.flow_table_statistics.get_template()
            self._template[self._AGGREGATE_FLOW_STATISTICS_FIELD] = self.aggregate_flow_statistics.get_template()
            self._template[self._FLOW_HASH_ID_MAP_FIELD] = self.flow_hash_id_map.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        table_features_payload = self.table_features.get_payload()
        if table_features_payload:
            payload[self._TABLE_FEATURES_FIELD] = table_features_payload
        flow_payload = self.flow.get_payload()
        if flow_payload:
            payload[self._FLOW_FIELD] = flow_payload
        table_feature_container_payload = self.table_feature_container.get_payload()
        if table_feature_container_payload:
            payload[self._TABLE_FEATURE_CONTAINER_FIELD] = table_feature_container_payload
        flow_table_statistics_payload = self.flow_table_statistics.get_payload()
        if flow_table_statistics_payload:
            payload[self._FLOW_TABLE_STATISTICS_FIELD] = flow_table_statistics_payload
        aggregate_flow_statistics_payload = self.aggregate_flow_statistics.get_payload()
        if aggregate_flow_statistics_payload:
            payload[self._AGGREGATE_FLOW_STATISTICS_FIELD] = aggregate_flow_statistics_payload
        flow_hash_id_map_payload = self.flow_hash_id_map.get_payload()
        if flow_hash_id_map_payload:
            payload[self._FLOW_HASH_ID_MAP_FIELD] = flow_hash_id_map_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_table(self):
        
        payload = {self._TABLE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_table(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_table(self):
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


class UNDERLAY_TOPOLOGY(object):

    _UNDERLAY_TOPOLOGY_FIELD = "underlay-topology"
    _TOPOLOGY_REF_FIELD = "topology-ref"

    def __init__(self):
        self._template = {}
        self._template[self._TOPOLOGY_REF_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_topology_ref(self, value):
        self._template[self._TOPOLOGY_REF_FIELD] = value

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

    def create_underlay_topology(self):
        
        payload = {self._UNDERLAY_TOPOLOGY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_underlay_topology(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_underlay_topology(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ACTION_TYPE(object):

    _ACTION_TYPE_FIELD = "action-type"
    _ACTION_FIELD = "action"
    _FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD = "flow-node-inventory:support-state"
    _SUPPORT_STATE_FIELD = "support-state"
    _FLOW_NODE_INVENTORY_ACTION_FIELD = "flow-node-inventory:action"

    def __init__(self):
        self._template = {}
        self._template[self._ACTION_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD] = None
        self._template[self._SUPPORT_STATE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ACTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._action = ACTION()

    @property
    def action(self):
        return self._action

    def set_flow_node_inventory_support_state(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORT_STATE_FIELD] = value

    def set_support_state(self, value):
        self._template[self._SUPPORT_STATE_FIELD] = value

    def set_flow_node_inventory_action(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ACTION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ACTION_FIELD] = self.action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ACTION_FIELD] = self.action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        action_payload = self.action.get_payload()
        if action_payload:
            payload[self._ACTION_FIELD] = action_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_action_type(self):
        
        payload = {self._ACTION_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_action_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_action_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class DESTINATION(object):

    _DESTINATION_FIELD = "destination"
    _DEST_NODE_FIELD = "dest-node"
    _DEST_TP_FIELD = "dest-tp"

    def __init__(self):
        self._template = {}
        self._template[self._DEST_NODE_FIELD] = None
        self._template[self._DEST_TP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_dest_node(self, value):
        self._template[self._DEST_NODE_FIELD] = value

    def set_dest_tp(self, value):
        self._template[self._DEST_TP_FIELD] = value

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

    def create_destination(self):
        
        payload = {self._DESTINATION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_destination(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_destination(self):
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


class OSPF_PREFIX_ATTRIBUTES(object):

    _OSPF_PREFIX_ATTRIBUTES_FIELD = "ospf-prefix-attributes"
    _OSPF_TOPOLOGY_FORWARDING_ADDRESS_FIELD = "ospf-topology:forwarding-address"
    _FORWARDING_ADDRESS_FIELD = "forwarding-address"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_TOPOLOGY_FORWARDING_ADDRESS_FIELD] = None
        self._template[self._FORWARDING_ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf_topology_forwarding_address(self, value):
        self._template[self._OSPF_TOPOLOGY_FORWARDING_ADDRESS_FIELD] = value

    def set_forwarding_address(self, value):
        self._template[self._FORWARDING_ADDRESS_FIELD] = value

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

    def create_ospf_prefix_attributes(self):
        
        payload = {self._OSPF_PREFIX_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ospf_prefix_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ospf_prefix_attributes(self):
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


class VLAN_ID(object):

    _VLAN_ID_FIELD = "vlan-id"
    _VLAN_ID_FIELD = "vlan-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_PRESENT_FIELD = "opendaylight-group-statistics:vlan-id-present"
    _OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_FIELD = "opendaylight-group-statistics:vlan-id"
    _VLAN_ID_PRESENT_FIELD = "vlan-id-present"

    def __init__(self):
        self._template = {}
        self._template[self._VLAN_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_PRESENT_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_FIELD] = None
        self._template[self._VLAN_ID_PRESENT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_vlan_id_present(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_PRESENT_FIELD] = value

    def set_opendaylight_group_statistics_vlan_id(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_FIELD] = value

    def set_vlan_id_present(self, value):
        self._template[self._VLAN_ID_PRESENT_FIELD] = value

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

    def create_vlan_id(self):
        
        payload = {self._VLAN_ID_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vlan_id(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vlan_id(self):
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


class TABLE_FEATURES(object):

    _TABLE_FEATURES_FIELD = "table-features"
    _NAME_FIELD = "name"
    _TABLE_PROPERTIES_FIELD = "table-properties"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_ID_FIELD = "opendaylight-flow-table-statistics:table-id"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METADATA_MATCH_FIELD = "opendaylight-flow-table-statistics:metadata-match"
    _TABLE_ID_FIELD = "table-id"
    _MAX_ENTRIES_FIELD = "max-entries"
    _METADATA_MATCH_FIELD = "metadata-match"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_MAX_ENTRIES_FIELD = "opendaylight-flow-table-statistics:max-entries"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METADATA_WRITE_FIELD = "opendaylight-flow-table-statistics:metadata-write"
    _METADATA_WRITE_FIELD = "metadata-write"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_NAME_FIELD = "opendaylight-flow-table-statistics:name"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_PROPERTIES_FIELD = "opendaylight-flow-table-statistics:table-properties"
    _CONFIG_FIELD = "config"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_CONFIG_FIELD = "opendaylight-flow-table-statistics:config"

    def __init__(self):
        self._template = {}
        self._template[self._NAME_FIELD] = None
        self._template[self._TABLE_PROPERTIES_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METADATA_MATCH_FIELD] = None
        self._template[self._TABLE_ID_FIELD] = None
        self._template[self._MAX_ENTRIES_FIELD] = None
        self._template[self._METADATA_MATCH_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_MAX_ENTRIES_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METADATA_WRITE_FIELD] = None
        self._template[self._METADATA_WRITE_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_NAME_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_PROPERTIES_FIELD] = None
        self._template[self._CONFIG_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_CONFIG_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._table_properties = TABLE_PROPERTIES()

    @property
    def table_properties(self):
        return self._table_properties

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_opendaylight_flow_table_statistics_table_id(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_ID_FIELD] = value

    def set_opendaylight_flow_table_statistics_metadata_match(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METADATA_MATCH_FIELD] = value

    def set_table_id(self, value):
        self._template[self._TABLE_ID_FIELD] = value

    def set_max_entries(self, value):
        self._template[self._MAX_ENTRIES_FIELD] = value

    def set_metadata_match(self, value):
        self._template[self._METADATA_MATCH_FIELD] = value

    def set_opendaylight_flow_table_statistics_max_entries(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_MAX_ENTRIES_FIELD] = value

    def set_opendaylight_flow_table_statistics_metadata_write(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METADATA_WRITE_FIELD] = value

    def set_metadata_write(self, value):
        self._template[self._METADATA_WRITE_FIELD] = value

    def set_opendaylight_flow_table_statistics_name(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_NAME_FIELD] = value

    def set_opendaylight_flow_table_statistics_table_properties(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_PROPERTIES_FIELD] = value

    def set_config(self, value):
        self._template[self._CONFIG_FIELD] = value

    def set_opendaylight_flow_table_statistics_config(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_CONFIG_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TABLE_PROPERTIES_FIELD] = self.table_properties.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TABLE_PROPERTIES_FIELD] = self.table_properties.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        table_properties_payload = self.table_properties.get_payload()
        if table_properties_payload:
            payload[self._TABLE_PROPERTIES_FIELD] = table_properties_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_table_features(self):
        
        payload = {self._TABLE_FEATURES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_table_features(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_table_features(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION(object):

    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD = "opendaylight-flow-table-statistics:instruction"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_METADATA_FIELD = "opendaylight-flow-table-statistics:write-metadata"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METER_FIELD = "opendaylight-flow-table-statistics:meter"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_GO_TO_TABLE_FIELD = "opendaylight-flow-table-statistics:go-to-table"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_FIELD = "opendaylight-flow-table-statistics:write-actions"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_FIELD = "opendaylight-flow-table-statistics:apply-actions"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_CLEAR_ACTIONS_FIELD = "opendaylight-flow-table-statistics:clear-actions"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_METADATA_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METER_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_GO_TO_TABLE_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_CLEAR_ACTIONS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_flow_table_statistics_write_metadata(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_METADATA_FIELD] = value

    def set_opendaylight_flow_table_statistics_meter(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_METER_FIELD] = value

    def set_opendaylight_flow_table_statistics_go_to_table(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_GO_TO_TABLE_FIELD] = value

    def set_opendaylight_flow_table_statistics_write_actions(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_WRITE_ACTIONS_FIELD] = value

    def set_opendaylight_flow_table_statistics_apply_actions(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_APPLY_ACTIONS_FIELD] = value

    def set_opendaylight_flow_table_statistics_clear_actions(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_CLEAR_ACTIONS_FIELD] = value

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

    def create_opendaylight_flow_table_statistics_instruction(self):
        
        payload = {self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_INSTRUCTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_opendaylight_flow_table_statistics_instruction(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_opendaylight_flow_table_statistics_instruction(self):
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


class RPKI_CONFIG(object):

    _RPKI_CONFIG_FIELD = "rpki-config"
    _BESTPATH_COMPUTATION_FIELD = "bestpath-computation"
    _VALIDATION_CONFIG_FIELD = "validation-config"
    _CACHE_SERVER_CONFIG_FIELD = "cache-server-config"

    def __init__(self):
        self._template = {}
        self._template[self._BESTPATH_COMPUTATION_FIELD] = None
        self._template[self._VALIDATION_CONFIG_FIELD] = None
        self._template[self._CACHE_SERVER_CONFIG_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._bestpath_computation = BESTPATH_COMPUTATION()
        self._validation_config = VALIDATION_CONFIG()
        self._cache_server_config = CACHE_SERVER_CONFIG()

    @property
    def bestpath_computation(self):
        return self._bestpath_computation

    @property
    def validation_config(self):
        return self._validation_config

    @property
    def cache_server_config(self):
        return self._cache_server_config

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BESTPATH_COMPUTATION_FIELD] = self.bestpath_computation.get_template(default=default)
            self._default_template[self._VALIDATION_CONFIG_FIELD] = self.validation_config.get_template(default=default)
            self._default_template[self._CACHE_SERVER_CONFIG_FIELD] = self.cache_server_config.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BESTPATH_COMPUTATION_FIELD] = self.bestpath_computation.get_template()
            self._template[self._VALIDATION_CONFIG_FIELD] = self.validation_config.get_template()
            self._template[self._CACHE_SERVER_CONFIG_FIELD] = self.cache_server_config.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        bestpath_computation_payload = self.bestpath_computation.get_payload()
        if bestpath_computation_payload:
            payload[self._BESTPATH_COMPUTATION_FIELD] = bestpath_computation_payload
        validation_config_payload = self.validation_config.get_payload()
        if validation_config_payload:
            payload[self._VALIDATION_CONFIG_FIELD] = validation_config_payload
        cache_server_config_payload = self.cache_server_config.get_payload()
        if cache_server_config_payload:
            payload[self._CACHE_SERVER_CONFIG_FIELD] = cache_server_config_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_rpki_config(self):
        
        payload = {self._RPKI_CONFIG_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_rpki_config(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_rpki_config(self):
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


class LINK(object):

    _LINK_FIELD = "link"
    _IGP_LINK_ATTRIBUTES_FIELD = "igp-link-attributes"
    _DESTINATION_FIELD = "destination"
    _SOURCE_FIELD = "source"
    _SUPPORTING_LINK_FIELD = "supporting-link"
    _LINK_ID_FIELD = "link-id"
    _L3_UNICAST_IGP_TOPOLOGY_IGP_LINK_ATTRIBUTES_FIELD = "l3-unicast-igp-topology:igp-link-attributes"

    def __init__(self):
        self._template = {}
        self._template[self._IGP_LINK_ATTRIBUTES_FIELD] = None
        self._template[self._DESTINATION_FIELD] = None
        self._template[self._SOURCE_FIELD] = None
        self._template[self._SUPPORTING_LINK_FIELD] = None
        self._template[self._LINK_ID_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IGP_LINK_ATTRIBUTES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._igp_link_attributes = IGP_LINK_ATTRIBUTES()
        self._destination = DESTINATION()
        self._source = SOURCE()
        self._supporting_link = SUPPORTING_LINK()

    @property
    def igp_link_attributes(self):
        return self._igp_link_attributes

    @property
    def destination(self):
        return self._destination

    @property
    def source(self):
        return self._source

    @property
    def supporting_link(self):
        return self._supporting_link

    def set_link_id(self, value):
        self._template[self._LINK_ID_FIELD] = value

    def set_l3_unicast_igp_topology_igp_link_attributes(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_IGP_LINK_ATTRIBUTES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._IGP_LINK_ATTRIBUTES_FIELD] = self.igp_link_attributes.get_template(default=default)
            self._default_template[self._DESTINATION_FIELD] = self.destination.get_template(default=default)
            self._default_template[self._SOURCE_FIELD] = self.source.get_template(default=default)
            self._default_template[self._SUPPORTING_LINK_FIELD] = self.supporting_link.get_template(default=default)
            return self._default_template
        else:
            self._template[self._IGP_LINK_ATTRIBUTES_FIELD] = self.igp_link_attributes.get_template()
            self._template[self._DESTINATION_FIELD] = self.destination.get_template()
            self._template[self._SOURCE_FIELD] = self.source.get_template()
            self._template[self._SUPPORTING_LINK_FIELD] = self.supporting_link.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        igp_link_attributes_payload = self.igp_link_attributes.get_payload()
        if igp_link_attributes_payload:
            payload[self._IGP_LINK_ATTRIBUTES_FIELD] = igp_link_attributes_payload
        destination_payload = self.destination.get_payload()
        if destination_payload:
            payload[self._DESTINATION_FIELD] = destination_payload
        source_payload = self.source.get_payload()
        if source_payload:
            payload[self._SOURCE_FIELD] = source_payload
        supporting_link_payload = self.supporting_link.get_payload()
        if supporting_link_payload:
            payload[self._SUPPORTING_LINK_FIELD] = supporting_link_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_link(self):
        
        payload = {self._LINK_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_link(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_link(self):
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


class BESTPATH_COMPUTATION(object):

    _BESTPATH_COMPUTATION_FIELD = "bestpath-computation"
    _ALLOW_INVALID_FIELD = "allow-invalid"
    _ENABLE_FIELD = "enable"

    def __init__(self):
        self._template = {}
        self._template[self._ALLOW_INVALID_FIELD] = None
        self._template[self._ENABLE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_allow_invalid(self, value):
        self._template[self._ALLOW_INVALID_FIELD] = value

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

    def create_bestpath_computation(self):
        
        payload = {self._BESTPATH_COMPUTATION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bestpath_computation(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bestpath_computation(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class AF_CONFIGURATION(object):

    _AF_CONFIGURATION_FIELD = "af-configuration"
    _NSAP_FIELD = "nsap"
    _L2VPN_FIELD = "l2vpn"
    _IPV4_FIELD = "ipv4"
    _IPV6_FIELD = "ipv6"

    def __init__(self):
        self._template = {}
        self._template[self._NSAP_FIELD] = None
        self._template[self._L2VPN_FIELD] = None
        self._template[self._IPV4_FIELD] = None
        self._template[self._IPV6_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._nsap = NSAP()
        self._l2vpn = L2VPN()
        self._ipv4 = IPV4()
        self._ipv6 = IPV6()

    @property
    def nsap(self):
        return self._nsap

    @property
    def l2vpn(self):
        return self._l2vpn

    @property
    def ipv4(self):
        return self._ipv4

    @property
    def ipv6(self):
        return self._ipv6

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._NSAP_FIELD] = self.nsap.get_template(default=default)
            self._default_template[self._L2VPN_FIELD] = self.l2vpn.get_template(default=default)
            self._default_template[self._IPV4_FIELD] = self.ipv4.get_template(default=default)
            self._default_template[self._IPV6_FIELD] = self.ipv6.get_template(default=default)
            return self._default_template
        else:
            self._template[self._NSAP_FIELD] = self.nsap.get_template()
            self._template[self._L2VPN_FIELD] = self.l2vpn.get_template()
            self._template[self._IPV4_FIELD] = self.ipv4.get_template()
            self._template[self._IPV6_FIELD] = self.ipv6.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        nsap_payload = self.nsap.get_payload()
        if nsap_payload:
            payload[self._NSAP_FIELD] = nsap_payload
        l2vpn_payload = self.l2vpn.get_payload()
        if l2vpn_payload:
            payload[self._L2VPN_FIELD] = l2vpn_payload
        ipv4_payload = self.ipv4.get_payload()
        if ipv4_payload:
            payload[self._IPV4_FIELD] = ipv4_payload
        ipv6_payload = self.ipv6.get_payload()
        if ipv6_payload:
            payload[self._IPV6_FIELD] = ipv6_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_af_configuration(self):
        
        payload = {self._AF_CONFIGURATION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_af_configuration(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_af_configuration(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class BGPPEER(object):

    _BGPPEER_FIELD = "bgpPeer"
    _L3VPN_DESCRIPTION_FIELD = "l3vpn:description"
    _DESCRIPTION_FIELD = "description"
    _L3VPN_PEERADDR_FIELD = "l3vpn:peerAddr"
    _L3VPN_SUBSTITUTEASENABLE_FIELD = "l3vpn:substituteAsEnable"
    _REMOTEAS_FIELD = "remoteAs"
    _GROUPNAME_FIELD = "groupName"
    _SOO_FIELD = "soo"
    _L3VPN_SOO_FIELD = "l3vpn:soo"
    _L3VPN_GROUPNAME_FIELD = "l3vpn:groupName"
    _L3VPN_REMOTEAS_FIELD = "l3vpn:remoteAs"
    _SUBSTITUTEASENABLE_FIELD = "substituteAsEnable"
    _PEERADDR_FIELD = "peerAddr"

    def __init__(self):
        self._template = {}
        self._template[self._L3VPN_DESCRIPTION_FIELD] = None
        self._template[self._DESCRIPTION_FIELD] = None
        self._template[self._L3VPN_PEERADDR_FIELD] = None
        self._template[self._L3VPN_SUBSTITUTEASENABLE_FIELD] = None
        self._template[self._REMOTEAS_FIELD] = None
        self._template[self._GROUPNAME_FIELD] = None
        self._template[self._SOO_FIELD] = None
        self._template[self._L3VPN_SOO_FIELD] = None
        self._template[self._L3VPN_GROUPNAME_FIELD] = None
        self._template[self._L3VPN_REMOTEAS_FIELD] = None
        self._template[self._SUBSTITUTEASENABLE_FIELD] = None
        self._template[self._PEERADDR_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_l3vpn_description(self, value):
        self._template[self._L3VPN_DESCRIPTION_FIELD] = value

    def set_description(self, value):
        self._template[self._DESCRIPTION_FIELD] = value

    def set_l3vpn_peeraddr(self, value):
        self._template[self._L3VPN_PEERADDR_FIELD] = value

    def set_l3vpn_substituteasenable(self, value):
        self._template[self._L3VPN_SUBSTITUTEASENABLE_FIELD] = value

    def set_remoteas(self, value):
        self._template[self._REMOTEAS_FIELD] = value

    def set_groupname(self, value):
        self._template[self._GROUPNAME_FIELD] = value

    def set_soo(self, value):
        self._template[self._SOO_FIELD] = value

    def set_l3vpn_soo(self, value):
        self._template[self._L3VPN_SOO_FIELD] = value

    def set_l3vpn_groupname(self, value):
        self._template[self._L3VPN_GROUPNAME_FIELD] = value

    def set_l3vpn_remoteas(self, value):
        self._template[self._L3VPN_REMOTEAS_FIELD] = value

    def set_substituteasenable(self, value):
        self._template[self._SUBSTITUTEASENABLE_FIELD] = value

    def set_peeraddr(self, value):
        self._template[self._PEERADDR_FIELD] = value

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

    def create_bgppeer(self):
        
        payload = {self._BGPPEER_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bgppeer(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bgppeer(self):
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


class BUCKET(object):

    _BUCKET_FIELD = "bucket"
    _OPENDAYLIGHT_GROUP_STATISTICS_BUCKET_ID_FIELD = "opendaylight-group-statistics:bucket-id"
    _WEIGHT_FIELD = "weight"
    _OPENDAYLIGHT_GROUP_STATISTICS_WATCH_PORT_FIELD = "opendaylight-group-statistics:watch_port"
    _OPENDAYLIGHT_GROUP_STATISTICS_WEIGHT_FIELD = "opendaylight-group-statistics:weight"
    _OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD = "opendaylight-group-statistics:action"
    _WATCH_GROUP_FIELD = "watch_group"
    _WATCH_PORT_FIELD = "watch_port"
    _ACTION_FIELD = "action"
    _BUCKET_ID_FIELD = "bucket-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_WATCH_GROUP_FIELD = "opendaylight-group-statistics:watch_group"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKET_ID_FIELD] = None
        self._template[self._WEIGHT_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_WATCH_PORT_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_WEIGHT_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = None
        self._template[self._WATCH_GROUP_FIELD] = None
        self._template[self._WATCH_PORT_FIELD] = None
        self._template[self._ACTION_FIELD] = None
        self._template[self._BUCKET_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_WATCH_GROUP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._opendaylight_group_statistics_action = OPENDAYLIGHT_GROUP_STATISTICS_ACTION()
        self._action = ACTION()

    @property
    def opendaylight_group_statistics_action(self):
        return self._opendaylight_group_statistics_action

    @property
    def action(self):
        return self._action

    def set_opendaylight_group_statistics_bucket_id(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKET_ID_FIELD] = value

    def set_weight(self, value):
        self._template[self._WEIGHT_FIELD] = value

    def set_opendaylight_group_statistics_watch_port(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_WATCH_PORT_FIELD] = value

    def set_opendaylight_group_statistics_weight(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_WEIGHT_FIELD] = value

    def set_watch_group(self, value):
        self._template[self._WATCH_GROUP_FIELD] = value

    def set_watch_port(self, value):
        self._template[self._WATCH_PORT_FIELD] = value

    def set_bucket_id(self, value):
        self._template[self._BUCKET_ID_FIELD] = value

    def set_opendaylight_group_statistics_watch_group(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_WATCH_GROUP_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = self.opendaylight_group_statistics_action.get_template(default=default)
            self._default_template[self._ACTION_FIELD] = self.action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = self.opendaylight_group_statistics_action.get_template()
            self._template[self._ACTION_FIELD] = self.action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        opendaylight_group_statistics_action_payload = self.opendaylight_group_statistics_action.get_payload()
        if opendaylight_group_statistics_action_payload:
            payload[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTION_FIELD] = opendaylight_group_statistics_action_payload
        action_payload = self.action.get_payload()
        if action_payload:
            payload[self._ACTION_FIELD] = action_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_bucket(self):
        
        payload = {self._BUCKET_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_bucket(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_bucket(self):
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


class SUPPORTING_LINK(object):

    _SUPPORTING_LINK_FIELD = "supporting-link"
    _LINK_REF_FIELD = "link-ref"

    def __init__(self):
        self._template = {}
        self._template[self._LINK_REF_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_link_ref(self, value):
        self._template[self._LINK_REF_FIELD] = value

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

    def create_supporting_link(self):
        
        payload = {self._SUPPORTING_LINK_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_supporting_link(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_supporting_link(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ATTACHMENT_POINTS(object):

    _ATTACHMENT_POINTS_FIELD = "attachment-points"
    _CORRESPONDING_TP_FIELD = "corresponding-tp"
    _HOST_TRACKER_SERVICE_ACTIVE_FIELD = "host-tracker-service:active"
    _HOST_TRACKER_SERVICE_CORRESPONDING_TP_FIELD = "host-tracker-service:corresponding-tp"
    _HOST_TRACKER_SERVICE_TP_ID_FIELD = "host-tracker-service:tp-id"
    _TP_ID_FIELD = "tp-id"
    _ACTIVE_FIELD = "active"

    def __init__(self):
        self._template = {}
        self._template[self._CORRESPONDING_TP_FIELD] = None
        self._template[self._HOST_TRACKER_SERVICE_ACTIVE_FIELD] = None
        self._template[self._HOST_TRACKER_SERVICE_CORRESPONDING_TP_FIELD] = None
        self._template[self._HOST_TRACKER_SERVICE_TP_ID_FIELD] = None
        self._template[self._TP_ID_FIELD] = None
        self._template[self._ACTIVE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_corresponding_tp(self, value):
        self._template[self._CORRESPONDING_TP_FIELD] = value

    def set_host_tracker_service_active(self, value):
        self._template[self._HOST_TRACKER_SERVICE_ACTIVE_FIELD] = value

    def set_host_tracker_service_corresponding_tp(self, value):
        self._template[self._HOST_TRACKER_SERVICE_CORRESPONDING_TP_FIELD] = value

    def set_host_tracker_service_tp_id(self, value):
        self._template[self._HOST_TRACKER_SERVICE_TP_ID_FIELD] = value

    def set_tp_id(self, value):
        self._template[self._TP_ID_FIELD] = value

    def set_active(self, value):
        self._template[self._ACTIVE_FIELD] = value

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

    def create_attachment_points(self):
        
        payload = {self._ATTACHMENT_POINTS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_attachment_points(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_attachment_points(self):
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


class GROUP_FEATURES(object):

    _GROUP_FEATURES_FIELD = "group-features"
    _OPENDAYLIGHT_GROUP_STATISTICS_MAX_GROUPS_FIELD = "opendaylight-group-statistics:max-groups"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_CAPABILITIES_SUPPORTED_FIELD = "opendaylight-group-statistics:group-capabilities-supported"
    _OPENDAYLIGHT_GROUP_STATISTICS_ACTIONS_FIELD = "opendaylight-group-statistics:actions"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_TYPES_SUPPORTED_FIELD = "opendaylight-group-statistics:group-types-supported"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MAX_GROUPS_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_CAPABILITIES_SUPPORTED_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_TYPES_SUPPORTED_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_max_groups(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MAX_GROUPS_FIELD] = value

    def set_opendaylight_group_statistics_group_capabilities_supported(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_CAPABILITIES_SUPPORTED_FIELD] = value

    def set_opendaylight_group_statistics_actions(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ACTIONS_FIELD] = value

    def set_opendaylight_group_statistics_group_types_supported(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_TYPES_SUPPORTED_FIELD] = value

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

    def create_group_features(self):
        
        payload = {self._GROUP_FEATURES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_group_features(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_group_features(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ETHERNET_SOURCE(object):

    _ETHERNET_SOURCE_FIELD = "ethernet-source"
    _OPENDAYLIGHT_GROUP_STATISTICS_MASK_FIELD = "opendaylight-group-statistics:mask"
    _OPENDAYLIGHT_GROUP_STATISTICS_ADDRESS_FIELD = "opendaylight-group-statistics:address"
    _MASK_FIELD = "mask"
    _ADDRESS_FIELD = "address"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MASK_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ADDRESS_FIELD] = None
        self._template[self._MASK_FIELD] = None
        self._template[self._ADDRESS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_opendaylight_group_statistics_mask(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_MASK_FIELD] = value

    def set_opendaylight_group_statistics_address(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ADDRESS_FIELD] = value

    def set_mask(self, value):
        self._template[self._MASK_FIELD] = value

    def set_address(self, value):
        self._template[self._ADDRESS_FIELD] = value

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

    def create_ethernet_source(self):
        
        payload = {self._ETHERNET_SOURCE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ethernet_source(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ethernet_source(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TOKEN_LIST(object):

    _TOKEN_LIST_FIELD = "token_list"
    _USER_TOKENS_FIELD = "user_tokens"
    _USERID_FIELD = "userId"

    def __init__(self):
        self._template = {}
        self._template[self._USER_TOKENS_FIELD] = None
        self._template[self._USERID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._user_tokens = USER_TOKENS()

    @property
    def user_tokens(self):
        return self._user_tokens

    def set_userid(self, value):
        self._template[self._USERID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._USER_TOKENS_FIELD] = self.user_tokens.get_template(default=default)
            return self._default_template
        else:
            self._template[self._USER_TOKENS_FIELD] = self.user_tokens.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        user_tokens_payload = self.user_tokens.get_payload()
        if user_tokens_payload:
            payload[self._USER_TOKENS_FIELD] = user_tokens_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_token_list(self):
        
        payload = {self._TOKEN_LIST_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_token_list(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_token_list(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class PACKETS(object):

    _PACKETS_FIELD = "packets"
    _RECEIVED_FIELD = "received"
    _TRANSMITTED_FIELD = "transmitted"
    _OPENDAYLIGHT_PORT_STATISTICS_RECEIVED_FIELD = "opendaylight-port-statistics:received"
    _OPENDAYLIGHT_PORT_STATISTICS_TRANSMITTED_FIELD = "opendaylight-port-statistics:transmitted"

    def __init__(self):
        self._template = {}
        self._template[self._RECEIVED_FIELD] = None
        self._template[self._TRANSMITTED_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVED_FIELD] = None
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMITTED_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_received(self, value):
        self._template[self._RECEIVED_FIELD] = value

    def set_transmitted(self, value):
        self._template[self._TRANSMITTED_FIELD] = value

    def set_opendaylight_port_statistics_received(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_RECEIVED_FIELD] = value

    def set_opendaylight_port_statistics_transmitted(self, value):
        self._template[self._OPENDAYLIGHT_PORT_STATISTICS_TRANSMITTED_FIELD] = value

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

    def create_packets(self):
        
        payload = {self._PACKETS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_packets(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_packets(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ISIS_NODE_ATTRIBUTES(object):

    _ISIS_NODE_ATTRIBUTES_FIELD = "isis-node-attributes"
    _ISIS_TOPOLOGY_NET_FIELD = "isis-topology:net"
    _TED_FIELD = "ted"
    _ISIS_TOPOLOGY_ISO_FIELD = "isis-topology:iso"
    _ISIS_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD = "isis-topology:multi-topology-id"
    _ISO_FIELD = "iso"
    _ISIS_TOPOLOGY_TED_FIELD = "isis-topology:ted"
    _ISIS_TOPOLOGY_ROUTER_TYPE_FIELD = "isis-topology:router-type"

    def __init__(self):
        self._template = {}
        self._template[self._ISIS_TOPOLOGY_NET_FIELD] = None
        self._template[self._TED_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ISO_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = None
        self._template[self._ISO_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_TED_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ROUTER_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ted = TED()
        self._iso = ISO()
        self._isis_topology_router_type = ISIS_TOPOLOGY_ROUTER_TYPE()

    @property
    def ted(self):
        return self._ted

    @property
    def iso(self):
        return self._iso

    @property
    def isis_topology_router_type(self):
        return self._isis_topology_router_type

    def set_isis_topology_net(self, value):
        self._template[self._ISIS_TOPOLOGY_NET_FIELD] = value

    def set_isis_topology_iso(self, value):
        self._template[self._ISIS_TOPOLOGY_ISO_FIELD] = value

    def set_isis_topology_multi_topology_id(self, value):
        self._template[self._ISIS_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = value

    def set_isis_topology_ted(self, value):
        self._template[self._ISIS_TOPOLOGY_TED_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TED_FIELD] = self.ted.get_template(default=default)
            self._default_template[self._ISO_FIELD] = self.iso.get_template(default=default)
            self._default_template[self._ISIS_TOPOLOGY_ROUTER_TYPE_FIELD] = self.isis_topology_router_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TED_FIELD] = self.ted.get_template()
            self._template[self._ISO_FIELD] = self.iso.get_template()
            self._template[self._ISIS_TOPOLOGY_ROUTER_TYPE_FIELD] = self.isis_topology_router_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ted_payload = self.ted.get_payload()
        if ted_payload:
            payload[self._TED_FIELD] = ted_payload
        iso_payload = self.iso.get_payload()
        if iso_payload:
            payload[self._ISO_FIELD] = iso_payload
        isis_topology_router_type_payload = self.isis_topology_router_type.get_payload()
        if isis_topology_router_type_payload:
            payload[self._ISIS_TOPOLOGY_ROUTER_TYPE_FIELD] = isis_topology_router_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_isis_node_attributes(self):
        
        payload = {self._ISIS_NODE_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_isis_node_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_isis_node_attributes(self):
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


class IGP_TOPOLOGY_ATTRIBUTES(object):

    _IGP_TOPOLOGY_ATTRIBUTES_FIELD = "igp-topology-attributes"
    _ISIS_TOPOLOGY_ATTRIBUTES_FIELD = "isis-topology-attributes"
    _NAME_FIELD = "name"
    _OSPF_TOPOLOGY_ATTRIBUTES_FIELD = "ospf-topology-attributes"
    _L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD = "l3-unicast-igp-topology:flag"
    _L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD = "l3-unicast-igp-topology:name"
    _ISIS_TOPOLOGY_ISIS_TOPOLOGY_ATTRIBUTES_FIELD = "isis-topology:isis-topology-attributes"
    _OSPF_TOPOLOGY_OSPF_TOPOLOGY_ATTRIBUTES_FIELD = "ospf-topology:ospf-topology-attributes"

    def __init__(self):
        self._template = {}
        self._template[self._ISIS_TOPOLOGY_ATTRIBUTES_FIELD] = None
        self._template[self._NAME_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_ATTRIBUTES_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = None
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ISIS_TOPOLOGY_ATTRIBUTES_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_OSPF_TOPOLOGY_ATTRIBUTES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._isis_topology_attributes = ISIS_TOPOLOGY_ATTRIBUTES()
        self._ospf_topology_attributes = OSPF_TOPOLOGY_ATTRIBUTES()

    @property
    def isis_topology_attributes(self):
        return self._isis_topology_attributes

    @property
    def ospf_topology_attributes(self):
        return self._ospf_topology_attributes

    def set_name(self, value):
        self._template[self._NAME_FIELD] = value

    def set_l3_unicast_igp_topology_flag(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_FLAG_FIELD] = value

    def set_l3_unicast_igp_topology_name(self, value):
        self._template[self._L3_UNICAST_IGP_TOPOLOGY_NAME_FIELD] = value

    def set_isis_topology_isis_topology_attributes(self, value):
        self._template[self._ISIS_TOPOLOGY_ISIS_TOPOLOGY_ATTRIBUTES_FIELD] = value

    def set_ospf_topology_ospf_topology_attributes(self, value):
        self._template[self._OSPF_TOPOLOGY_OSPF_TOPOLOGY_ATTRIBUTES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ISIS_TOPOLOGY_ATTRIBUTES_FIELD] = self.isis_topology_attributes.get_template(default=default)
            self._default_template[self._OSPF_TOPOLOGY_ATTRIBUTES_FIELD] = self.ospf_topology_attributes.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ISIS_TOPOLOGY_ATTRIBUTES_FIELD] = self.isis_topology_attributes.get_template()
            self._template[self._OSPF_TOPOLOGY_ATTRIBUTES_FIELD] = self.ospf_topology_attributes.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        isis_topology_attributes_payload = self.isis_topology_attributes.get_payload()
        if isis_topology_attributes_payload:
            payload[self._ISIS_TOPOLOGY_ATTRIBUTES_FIELD] = isis_topology_attributes_payload
        ospf_topology_attributes_payload = self.ospf_topology_attributes.get_payload()
        if ospf_topology_attributes_payload:
            payload[self._OSPF_TOPOLOGY_ATTRIBUTES_FIELD] = ospf_topology_attributes_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_igp_topology_attributes(self):
        
        payload = {self._IGP_TOPOLOGY_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_igp_topology_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_igp_topology_attributes(self):
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


class ROUTER_ID(object):

    _ROUTER_ID_FIELD = "router-id"
    _L3VPN_CONFIG_TYPE_FIELD = "l3vpn:config-type"
    _ENABLE_FIELD = "enable"
    _L3VPN_ENABLE_FIELD = "l3vpn:enable"

    def __init__(self):
        self._template = {}
        self._template[self._L3VPN_CONFIG_TYPE_FIELD] = None
        self._template[self._ENABLE_FIELD] = None
        self._template[self._L3VPN_ENABLE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._l3vpn_config_type = L3VPN_CONFIG_TYPE()

    @property
    def l3vpn_config_type(self):
        return self._l3vpn_config_type

    def set_enable(self, value):
        self._template[self._ENABLE_FIELD] = value

    def set_l3vpn_enable(self, value):
        self._template[self._L3VPN_ENABLE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._L3VPN_CONFIG_TYPE_FIELD] = self.l3vpn_config_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._L3VPN_CONFIG_TYPE_FIELD] = self.l3vpn_config_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        l3vpn_config_type_payload = self.l3vpn_config_type.get_payload()
        if l3vpn_config_type_payload:
            payload[self._L3VPN_CONFIG_TYPE_FIELD] = l3vpn_config_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_router_id(self):
        
        payload = {self._ROUTER_ID_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_router_id(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_router_id(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ETHERNET_MATCH(object):

    _ETHERNET_MATCH_FIELD = "ethernet-match"
    _ETHERNET_SOURCE_FIELD = "ethernet-source"
    _OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_TYPE_FIELD = "opendaylight-group-statistics:ethernet-type"
    _OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_SOURCE_FIELD = "opendaylight-group-statistics:ethernet-source"
    _OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_DESTINATION_FIELD = "opendaylight-group-statistics:ethernet-destination"
    _ETHERNET_TYPE_FIELD = "ethernet-type"
    _ETHERNET_DESTINATION_FIELD = "ethernet-destination"

    def __init__(self):
        self._template = {}
        self._template[self._ETHERNET_SOURCE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_TYPE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_SOURCE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_DESTINATION_FIELD] = None
        self._template[self._ETHERNET_TYPE_FIELD] = None
        self._template[self._ETHERNET_DESTINATION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ethernet_source = ETHERNET_SOURCE()
        self._ethernet_type = ETHERNET_TYPE()
        self._ethernet_destination = ETHERNET_DESTINATION()

    @property
    def ethernet_source(self):
        return self._ethernet_source

    @property
    def ethernet_type(self):
        return self._ethernet_type

    @property
    def ethernet_destination(self):
        return self._ethernet_destination

    def set_opendaylight_group_statistics_ethernet_type(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_TYPE_FIELD] = value

    def set_opendaylight_group_statistics_ethernet_source(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_SOURCE_FIELD] = value

    def set_opendaylight_group_statistics_ethernet_destination(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_ETHERNET_DESTINATION_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ETHERNET_SOURCE_FIELD] = self.ethernet_source.get_template(default=default)
            self._default_template[self._ETHERNET_TYPE_FIELD] = self.ethernet_type.get_template(default=default)
            self._default_template[self._ETHERNET_DESTINATION_FIELD] = self.ethernet_destination.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ETHERNET_SOURCE_FIELD] = self.ethernet_source.get_template()
            self._template[self._ETHERNET_TYPE_FIELD] = self.ethernet_type.get_template()
            self._template[self._ETHERNET_DESTINATION_FIELD] = self.ethernet_destination.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ethernet_source_payload = self.ethernet_source.get_payload()
        if ethernet_source_payload:
            payload[self._ETHERNET_SOURCE_FIELD] = ethernet_source_payload
        ethernet_type_payload = self.ethernet_type.get_payload()
        if ethernet_type_payload:
            payload[self._ETHERNET_TYPE_FIELD] = ethernet_type_payload
        ethernet_destination_payload = self.ethernet_destination.get_payload()
        if ethernet_destination_payload:
            payload[self._ETHERNET_DESTINATION_FIELD] = ethernet_destination_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ethernet_match(self):
        
        payload = {self._ETHERNET_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ethernet_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ethernet_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ISIS_LINK_ATTRIBUTES(object):

    _ISIS_LINK_ATTRIBUTES_FIELD = "isis-link-attributes"
    _TED_FIELD = "ted"
    _ISIS_TOPOLOGY_TED_FIELD = "isis-topology:ted"
    _ISIS_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD = "isis-topology:multi-topology-id"
    _MULTI_TOPOLOGY_ID_FIELD = "multi-topology-id"

    def __init__(self):
        self._template = {}
        self._template[self._TED_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_TED_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = None
        self._template[self._MULTI_TOPOLOGY_ID_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ted = TED()

    @property
    def ted(self):
        return self._ted

    def set_isis_topology_ted(self, value):
        self._template[self._ISIS_TOPOLOGY_TED_FIELD] = value

    def set_isis_topology_multi_topology_id(self, value):
        self._template[self._ISIS_TOPOLOGY_MULTI_TOPOLOGY_ID_FIELD] = value

    def set_multi_topology_id(self, value):
        self._template[self._MULTI_TOPOLOGY_ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TED_FIELD] = self.ted.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TED_FIELD] = self.ted.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ted_payload = self.ted.get_payload()
        if ted_payload:
            payload[self._TED_FIELD] = ted_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_isis_link_attributes(self):
        
        payload = {self._ISIS_LINK_ATTRIBUTES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_isis_link_attributes(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_isis_link_attributes(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class GROUP_STATISTICS(object):

    _GROUP_STATISTICS_FIELD = "group-statistics"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ID_FIELD = "opendaylight-group-statistics:group-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_BUCKETS_FIELD = "opendaylight-group-statistics:buckets"
    _GROUP_ID_FIELD = "group-id"
    _BYTE_COUNT_FIELD = "byte-count"
    _REF_COUNT_FIELD = "ref-count"
    _BUCKETS_FIELD = "buckets"
    _OPENDAYLIGHT_GROUP_STATISTICS_PACKET_COUNT_FIELD = "opendaylight-group-statistics:packet-count"
    _OPENDAYLIGHT_GROUP_STATISTICS_REF_COUNT_FIELD = "opendaylight-group-statistics:ref-count"
    _DURATION_FIELD = "duration"
    _OPENDAYLIGHT_GROUP_STATISTICS_DURATION_FIELD = "opendaylight-group-statistics:duration"
    _OPENDAYLIGHT_GROUP_STATISTICS_BYTE_COUNT_FIELD = "opendaylight-group-statistics:byte-count"
    _PACKET_COUNT_FIELD = "packet-count"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKETS_FIELD] = None
        self._template[self._GROUP_ID_FIELD] = None
        self._template[self._BYTE_COUNT_FIELD] = None
        self._template[self._REF_COUNT_FIELD] = None
        self._template[self._BUCKETS_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PACKET_COUNT_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_REF_COUNT_FIELD] = None
        self._template[self._DURATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DURATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BYTE_COUNT_FIELD] = None
        self._template[self._PACKET_COUNT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._buckets = BUCKETS()
        self._duration = DURATION()

    @property
    def buckets(self):
        return self._buckets

    @property
    def duration(self):
        return self._duration

    def set_opendaylight_group_statistics_group_id(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ID_FIELD] = value

    def set_opendaylight_group_statistics_buckets(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKETS_FIELD] = value

    def set_group_id(self, value):
        self._template[self._GROUP_ID_FIELD] = value

    def set_byte_count(self, value):
        self._template[self._BYTE_COUNT_FIELD] = value

    def set_ref_count(self, value):
        self._template[self._REF_COUNT_FIELD] = value

    def set_opendaylight_group_statistics_packet_count(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_PACKET_COUNT_FIELD] = value

    def set_opendaylight_group_statistics_ref_count(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_REF_COUNT_FIELD] = value

    def set_opendaylight_group_statistics_duration(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_DURATION_FIELD] = value

    def set_opendaylight_group_statistics_byte_count(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BYTE_COUNT_FIELD] = value

    def set_packet_count(self, value):
        self._template[self._PACKET_COUNT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BUCKETS_FIELD] = self.buckets.get_template(default=default)
            self._default_template[self._DURATION_FIELD] = self.duration.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BUCKETS_FIELD] = self.buckets.get_template()
            self._template[self._DURATION_FIELD] = self.duration.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        buckets_payload = self.buckets.get_payload()
        if buckets_payload:
            payload[self._BUCKETS_FIELD] = buckets_payload
        duration_payload = self.duration.get_payload()
        if duration_payload:
            payload[self._DURATION_FIELD] = duration_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_group_statistics(self):
        
        payload = {self._GROUP_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_group_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_group_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class VLAN_MATCH(object):

    _VLAN_MATCH_FIELD = "vlan-match"
    _VLAN_ID_FIELD = "vlan-id"
    _VLAN_PCP_FIELD = "vlan-pcp"
    _OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_FIELD = "opendaylight-group-statistics:vlan-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_VLAN_PCP_FIELD = "opendaylight-group-statistics:vlan-pcp"

    def __init__(self):
        self._template = {}
        self._template[self._VLAN_ID_FIELD] = None
        self._template[self._VLAN_PCP_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_PCP_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._vlan_id = VLAN_ID()

    @property
    def vlan_id(self):
        return self._vlan_id

    def set_vlan_pcp(self, value):
        self._template[self._VLAN_PCP_FIELD] = value

    def set_opendaylight_group_statistics_vlan_id(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_ID_FIELD] = value

    def set_opendaylight_group_statistics_vlan_pcp(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_VLAN_PCP_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._VLAN_ID_FIELD] = self.vlan_id.get_template(default=default)
            return self._default_template
        else:
            self._template[self._VLAN_ID_FIELD] = self.vlan_id.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        vlan_id_payload = self.vlan_id.get_payload()
        if vlan_id_payload:
            payload[self._VLAN_ID_FIELD] = vlan_id_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_vlan_match(self):
        
        payload = {self._VLAN_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_vlan_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_vlan_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ETHERNET_TYPE(object):

    _ETHERNET_TYPE_FIELD = "ethernet-type"
    _TYPE_FIELD = "type"
    _OPENDAYLIGHT_GROUP_STATISTICS_TYPE_FIELD = "opendaylight-group-statistics:type"

    def __init__(self):
        self._template = {}
        self._template[self._TYPE_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_type(self, value):
        self._template[self._TYPE_FIELD] = value

    def set_opendaylight_group_statistics_type(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_TYPE_FIELD] = value

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

    def create_ethernet_type(self):
        
        payload = {self._ETHERNET_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ethernet_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ethernet_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TRANSPORT(object):

    _TRANSPORT_FIELD = "transport"
    _SSH_PORT_FIELD = "ssh-port"
    _TCP_PORT_FIELD = "tcp-port"

    def __init__(self):
        self._template = {}
        self._template[self._SSH_PORT_FIELD] = None
        self._template[self._TCP_PORT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ssh_port(self, value):
        self._template[self._SSH_PORT_FIELD] = value

    def set_tcp_port(self, value):
        self._template[self._TCP_PORT_FIELD] = value

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

    def create_transport(self):
        
        payload = {self._TRANSPORT_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_transport(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_transport(self):
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


class FLOW_NODE_INVENTORY_LAYER_4_MATCH(object):

    _FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD = "flow-node-inventory:layer-4-match"
    _FLOW_NODE_INVENTORY_UDP_SOURCE_PORT_FIELD = "flow-node-inventory:udp-source-port"
    _FLOW_NODE_INVENTORY_SCTP_DESTINATION_PORT_FIELD = "flow-node-inventory:sctp-destination-port"
    _FLOW_NODE_INVENTORY_TCP_SOURCE_PORT_FIELD = "flow-node-inventory:tcp-source-port"
    _FLOW_NODE_INVENTORY_SCTP_SOURCE_PORT_FIELD = "flow-node-inventory:sctp-source-port"
    _FLOW_NODE_INVENTORY_TCP_DESTINATION_PORT_FIELD = "flow-node-inventory:tcp-destination-port"
    _FLOW_NODE_INVENTORY_UDP_DESTINATION_PORT_FIELD = "flow-node-inventory:udp-destination-port"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_UDP_SOURCE_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SCTP_DESTINATION_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TCP_SOURCE_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SCTP_SOURCE_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TCP_DESTINATION_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_UDP_DESTINATION_PORT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_flow_node_inventory_udp_source_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_UDP_SOURCE_PORT_FIELD] = value

    def set_flow_node_inventory_sctp_destination_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SCTP_DESTINATION_PORT_FIELD] = value

    def set_flow_node_inventory_tcp_source_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TCP_SOURCE_PORT_FIELD] = value

    def set_flow_node_inventory_sctp_source_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SCTP_SOURCE_PORT_FIELD] = value

    def set_flow_node_inventory_tcp_destination_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TCP_DESTINATION_PORT_FIELD] = value

    def set_flow_node_inventory_udp_destination_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_UDP_DESTINATION_PORT_FIELD] = value

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

    def create_flow_node_inventory_layer_4_match(self):
        
        payload = {self._FLOW_NODE_INVENTORY_LAYER_4_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_node_inventory_layer_4_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_node_inventory_layer_4_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class NODE(object):

    _NODE_FIELD = "node"
    _GROUP_FEATURES_FIELD = "group-features"
    _NETCONF_NODE_INVENTORY_CONNECTED_FIELD = "netconf-node-inventory:connected"
    _SUPPORTED_MATCH_TYPES_FIELD = "supported-match-types"
    _FLOW_NODE_INVENTORY_HARDWARE_FIELD = "flow-node-inventory:hardware"
    _METER_FIELD = "meter"
    _HARDWARE_FIELD = "hardware"
    _SERIAL_NUMBER_FIELD = "serial-number"
    _IP_ADDRESS_FIELD = "ip-address"
    _TABLE_FIELD = "table"
    _FLOW_NODE_INVENTORY_MANUFACTURER_FIELD = "flow-node-inventory:manufacturer"
    _ID_FIELD = "id"
    _GROUP_FIELD = "group"
    _FLOW_NODE_INVENTORY_SERIAL_NUMBER_FIELD = "flow-node-inventory:serial-number"
    _FLOW_NODE_INVENTORY_METER_FIELD = "flow-node-inventory:meter"
    _METER_FEATURES_FIELD = "meter-features"
    _FLOW_NODE_INVENTORY_GROUP_FIELD = "flow-node-inventory:group"
    _NETCONF_NODE_INVENTORY_INITIAL_CAPABILITY_FIELD = "netconf-node-inventory:initial-capability"
    _NODE_CONNECTOR_FIELD = "node-connector"
    _DESCRIPTION_FIELD = "description"
    _SWITCH_FEATURES_FIELD = "switch-features"
    _FLOW_NODE_INVENTORY_SWITCH_FEATURES_FIELD = "flow-node-inventory:switch-features"
    _FLOW_NODE_INVENTORY_SOFTWARE_FIELD = "flow-node-inventory:software"
    _CONNECTED_FIELD = "connected"
    _SUPPORTED_ACTIONS_FIELD = "supported-actions"
    _FLOW_NODE_INVENTORY_DESCRIPTION_FIELD = "flow-node-inventory:description"
    _FLOW_NODE_INVENTORY_IP_ADDRESS_FIELD = "flow-node-inventory:ip-address"
    _FLOW_NODE_INVENTORY_TABLE_FIELD = "flow-node-inventory:table"
    _MANUFACTURER_FIELD = "manufacturer"
    _PASS_THROUGH_FIELD = "pass-through"
    _NETCONF_NODE_INVENTORY_PASS_THROUGH_FIELD = "netconf-node-inventory:pass-through"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_FEATURES_FIELD = "opendaylight-group-statistics:group-features"
    _FLOW_NODE_INVENTORY_SUPPORTED_ACTIONS_FIELD = "flow-node-inventory:supported-actions"
    _FLOW_NODE_INVENTORY_SUPPORTED_INSTRUCTIONS_FIELD = "flow-node-inventory:supported-instructions"
    _SUPPORTED_INSTRUCTIONS_FIELD = "supported-instructions"
    _OPENDAYLIGHT_METER_STATISTICS_METER_FEATURES_FIELD = "opendaylight-meter-statistics:meter-features"
    _SOFTWARE_FIELD = "software"
    _NETCONF_NODE_INVENTORY_CURRENT_CAPABILITY_FIELD = "netconf-node-inventory:current-capability"
    _FLOW_NODE_INVENTORY_SUPPORTED_MATCH_TYPES_FIELD = "flow-node-inventory:supported-match-types"

    def __init__(self):
        self._template = {}
        self._template[self._GROUP_FEATURES_FIELD] = None
        self._template[self._NETCONF_NODE_INVENTORY_CONNECTED_FIELD] = None
        self._template[self._SUPPORTED_MATCH_TYPES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_HARDWARE_FIELD] = None
        self._template[self._METER_FIELD] = None
        self._template[self._HARDWARE_FIELD] = None
        self._template[self._SERIAL_NUMBER_FIELD] = None
        self._template[self._IP_ADDRESS_FIELD] = None
        self._template[self._TABLE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_MANUFACTURER_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._template[self._GROUP_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SERIAL_NUMBER_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_METER_FIELD] = None
        self._template[self._METER_FEATURES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_GROUP_FIELD] = None
        self._template[self._NETCONF_NODE_INVENTORY_INITIAL_CAPABILITY_FIELD] = None
        self._template[self._NODE_CONNECTOR_FIELD] = None
        self._template[self._DESCRIPTION_FIELD] = None
        self._template[self._SWITCH_FEATURES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SWITCH_FEATURES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SOFTWARE_FIELD] = None
        self._template[self._CONNECTED_FIELD] = None
        self._template[self._SUPPORTED_ACTIONS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_DESCRIPTION_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IP_ADDRESS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TABLE_FIELD] = None
        self._template[self._MANUFACTURER_FIELD] = None
        self._template[self._PASS_THROUGH_FIELD] = None
        self._template[self._NETCONF_NODE_INVENTORY_PASS_THROUGH_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_FEATURES_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_ACTIONS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_INSTRUCTIONS_FIELD] = None
        self._template[self._SUPPORTED_INSTRUCTIONS_FIELD] = None
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_METER_FEATURES_FIELD] = None
        self._template[self._SOFTWARE_FIELD] = None
        self._template[self._NETCONF_NODE_INVENTORY_CURRENT_CAPABILITY_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_MATCH_TYPES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._group_features = GROUP_FEATURES()
        self._supported_match_types = SUPPORTED_MATCH_TYPES()
        self._meter = METER()
        self._table = TABLE()
        self._group = GROUP()
        self._meter_features = METER_FEATURES()
        self._node_connector = NODE_CONNECTOR()
        self._switch_features = SWITCH_FEATURES()
        self._supported_actions = SUPPORTED_ACTIONS()
        self._supported_instructions = SUPPORTED_INSTRUCTIONS()

    @property
    def group_features(self):
        return self._group_features

    @property
    def supported_match_types(self):
        return self._supported_match_types

    @property
    def meter(self):
        return self._meter

    @property
    def table(self):
        return self._table

    @property
    def group(self):
        return self._group

    @property
    def meter_features(self):
        return self._meter_features

    @property
    def node_connector(self):
        return self._node_connector

    @property
    def switch_features(self):
        return self._switch_features

    @property
    def supported_actions(self):
        return self._supported_actions

    @property
    def supported_instructions(self):
        return self._supported_instructions

    def set_netconf_node_inventory_connected(self, value):
        self._template[self._NETCONF_NODE_INVENTORY_CONNECTED_FIELD] = value

    def set_flow_node_inventory_hardware(self, value):
        self._template[self._FLOW_NODE_INVENTORY_HARDWARE_FIELD] = value

    def set_hardware(self, value):
        self._template[self._HARDWARE_FIELD] = value

    def set_serial_number(self, value):
        self._template[self._SERIAL_NUMBER_FIELD] = value

    def set_ip_address(self, value):
        self._template[self._IP_ADDRESS_FIELD] = value

    def set_flow_node_inventory_manufacturer(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MANUFACTURER_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_flow_node_inventory_serial_number(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SERIAL_NUMBER_FIELD] = value

    def set_flow_node_inventory_meter(self, value):
        self._template[self._FLOW_NODE_INVENTORY_METER_FIELD] = value

    def set_flow_node_inventory_group(self, value):
        self._template[self._FLOW_NODE_INVENTORY_GROUP_FIELD] = value

    def set_netconf_node_inventory_initial_capability(self, value):
        self._template[self._NETCONF_NODE_INVENTORY_INITIAL_CAPABILITY_FIELD] = value

    def set_description(self, value):
        self._template[self._DESCRIPTION_FIELD] = value

    def set_flow_node_inventory_switch_features(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SWITCH_FEATURES_FIELD] = value

    def set_flow_node_inventory_software(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SOFTWARE_FIELD] = value

    def set_connected(self, value):
        self._template[self._CONNECTED_FIELD] = value

    def set_flow_node_inventory_description(self, value):
        self._template[self._FLOW_NODE_INVENTORY_DESCRIPTION_FIELD] = value

    def set_flow_node_inventory_ip_address(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IP_ADDRESS_FIELD] = value

    def set_flow_node_inventory_table(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TABLE_FIELD] = value

    def set_manufacturer(self, value):
        self._template[self._MANUFACTURER_FIELD] = value

    def set_pass_through(self, value):
        self._template[self._PASS_THROUGH_FIELD] = value

    def set_netconf_node_inventory_pass_through(self, value):
        self._template[self._NETCONF_NODE_INVENTORY_PASS_THROUGH_FIELD] = value

    def set_opendaylight_group_statistics_group_features(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_FEATURES_FIELD] = value

    def set_flow_node_inventory_supported_actions(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_ACTIONS_FIELD] = value

    def set_flow_node_inventory_supported_instructions(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_INSTRUCTIONS_FIELD] = value

    def set_opendaylight_meter_statistics_meter_features(self, value):
        self._template[self._OPENDAYLIGHT_METER_STATISTICS_METER_FEATURES_FIELD] = value

    def set_software(self, value):
        self._template[self._SOFTWARE_FIELD] = value

    def set_netconf_node_inventory_current_capability(self, value):
        self._template[self._NETCONF_NODE_INVENTORY_CURRENT_CAPABILITY_FIELD] = value

    def set_flow_node_inventory_supported_match_types(self, value):
        self._template[self._FLOW_NODE_INVENTORY_SUPPORTED_MATCH_TYPES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._GROUP_FEATURES_FIELD] = self.group_features.get_template(default=default)
            self._default_template[self._SUPPORTED_MATCH_TYPES_FIELD] = self.supported_match_types.get_template(default=default)
            self._default_template[self._METER_FIELD] = self.meter.get_template(default=default)
            self._default_template[self._TABLE_FIELD] = self.table.get_template(default=default)
            self._default_template[self._GROUP_FIELD] = self.group.get_template(default=default)
            self._default_template[self._METER_FEATURES_FIELD] = self.meter_features.get_template(default=default)
            self._default_template[self._NODE_CONNECTOR_FIELD] = self.node_connector.get_template(default=default)
            self._default_template[self._SWITCH_FEATURES_FIELD] = self.switch_features.get_template(default=default)
            self._default_template[self._SUPPORTED_ACTIONS_FIELD] = self.supported_actions.get_template(default=default)
            self._default_template[self._SUPPORTED_INSTRUCTIONS_FIELD] = self.supported_instructions.get_template(default=default)
            return self._default_template
        else:
            self._template[self._GROUP_FEATURES_FIELD] = self.group_features.get_template()
            self._template[self._SUPPORTED_MATCH_TYPES_FIELD] = self.supported_match_types.get_template()
            self._template[self._METER_FIELD] = self.meter.get_template()
            self._template[self._TABLE_FIELD] = self.table.get_template()
            self._template[self._GROUP_FIELD] = self.group.get_template()
            self._template[self._METER_FEATURES_FIELD] = self.meter_features.get_template()
            self._template[self._NODE_CONNECTOR_FIELD] = self.node_connector.get_template()
            self._template[self._SWITCH_FEATURES_FIELD] = self.switch_features.get_template()
            self._template[self._SUPPORTED_ACTIONS_FIELD] = self.supported_actions.get_template()
            self._template[self._SUPPORTED_INSTRUCTIONS_FIELD] = self.supported_instructions.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        group_features_payload = self.group_features.get_payload()
        if group_features_payload:
            payload[self._GROUP_FEATURES_FIELD] = group_features_payload
        supported_match_types_payload = self.supported_match_types.get_payload()
        if supported_match_types_payload:
            payload[self._SUPPORTED_MATCH_TYPES_FIELD] = supported_match_types_payload
        meter_payload = self.meter.get_payload()
        if meter_payload:
            payload[self._METER_FIELD] = meter_payload
        table_payload = self.table.get_payload()
        if table_payload:
            payload[self._TABLE_FIELD] = table_payload
        group_payload = self.group.get_payload()
        if group_payload:
            payload[self._GROUP_FIELD] = group_payload
        meter_features_payload = self.meter_features.get_payload()
        if meter_features_payload:
            payload[self._METER_FEATURES_FIELD] = meter_features_payload
        node_connector_payload = self.node_connector.get_payload()
        if node_connector_payload:
            payload[self._NODE_CONNECTOR_FIELD] = node_connector_payload
        switch_features_payload = self.switch_features.get_payload()
        if switch_features_payload:
            payload[self._SWITCH_FEATURES_FIELD] = switch_features_payload
        supported_actions_payload = self.supported_actions.get_payload()
        if supported_actions_payload:
            payload[self._SUPPORTED_ACTIONS_FIELD] = supported_actions_payload
        supported_instructions_payload = self.supported_instructions.get_payload()
        if supported_instructions_payload:
            payload[self._SUPPORTED_INSTRUCTIONS_FIELD] = supported_instructions_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_node(self):
        
        payload = {self._NODE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_node(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_node(self):
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


class INTERFACE_SWITCHING_CAPABILITIES(object):

    _INTERFACE_SWITCHING_CAPABILITIES_FIELD = "interface-switching-capabilities"
    _MAX_LSP_BANDWIDTH_FIELD = "max-lsp-bandwidth"
    _TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD = "time-division-multiplex-capable"
    _ENCODING_FIELD = "encoding"
    _OSPF_TOPOLOGY_SWITCHING_CAPABILITY_FIELD = "ospf-topology:switching-capability"
    _OSPF_TOPOLOGY_MAX_LSP_BANDWIDTH_FIELD = "ospf-topology:max-lsp-bandwidth"
    _OSPF_TOPOLOGY_PACKET_SWITCH_CAPABLE_FIELD = "ospf-topology:packet-switch-capable"
    _PACKET_SWITCH_CAPABLE_FIELD = "packet-switch-capable"
    _OSPF_TOPOLOGY_ENCODING_FIELD = "ospf-topology:encoding"
    _OSPF_TOPOLOGY_TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD = "ospf-topology:time-division-multiplex-capable"
    _SWITCHING_CAPABILITY_FIELD = "switching-capability"

    def __init__(self):
        self._template = {}
        self._template[self._MAX_LSP_BANDWIDTH_FIELD] = None
        self._template[self._TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD] = None
        self._template[self._ENCODING_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_SWITCHING_CAPABILITY_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_MAX_LSP_BANDWIDTH_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_PACKET_SWITCH_CAPABLE_FIELD] = None
        self._template[self._PACKET_SWITCH_CAPABLE_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_ENCODING_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD] = None
        self._template[self._SWITCHING_CAPABILITY_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._max_lsp_bandwidth = MAX_LSP_BANDWIDTH()
        self._time_division_multiplex_capable = TIME_DIVISION_MULTIPLEX_CAPABLE()
        self._packet_switch_capable = PACKET_SWITCH_CAPABLE()

    @property
    def max_lsp_bandwidth(self):
        return self._max_lsp_bandwidth

    @property
    def time_division_multiplex_capable(self):
        return self._time_division_multiplex_capable

    @property
    def packet_switch_capable(self):
        return self._packet_switch_capable

    def set_encoding(self, value):
        self._template[self._ENCODING_FIELD] = value

    def set_ospf_topology_switching_capability(self, value):
        self._template[self._OSPF_TOPOLOGY_SWITCHING_CAPABILITY_FIELD] = value

    def set_ospf_topology_max_lsp_bandwidth(self, value):
        self._template[self._OSPF_TOPOLOGY_MAX_LSP_BANDWIDTH_FIELD] = value

    def set_ospf_topology_packet_switch_capable(self, value):
        self._template[self._OSPF_TOPOLOGY_PACKET_SWITCH_CAPABLE_FIELD] = value

    def set_ospf_topology_encoding(self, value):
        self._template[self._OSPF_TOPOLOGY_ENCODING_FIELD] = value

    def set_ospf_topology_time_division_multiplex_capable(self, value):
        self._template[self._OSPF_TOPOLOGY_TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD] = value

    def set_switching_capability(self, value):
        self._template[self._SWITCHING_CAPABILITY_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MAX_LSP_BANDWIDTH_FIELD] = self.max_lsp_bandwidth.get_template(default=default)
            self._default_template[self._TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD] = self.time_division_multiplex_capable.get_template(default=default)
            self._default_template[self._PACKET_SWITCH_CAPABLE_FIELD] = self.packet_switch_capable.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MAX_LSP_BANDWIDTH_FIELD] = self.max_lsp_bandwidth.get_template()
            self._template[self._TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD] = self.time_division_multiplex_capable.get_template()
            self._template[self._PACKET_SWITCH_CAPABLE_FIELD] = self.packet_switch_capable.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        max_lsp_bandwidth_payload = self.max_lsp_bandwidth.get_payload()
        if max_lsp_bandwidth_payload:
            payload[self._MAX_LSP_BANDWIDTH_FIELD] = max_lsp_bandwidth_payload
        time_division_multiplex_capable_payload = self.time_division_multiplex_capable.get_payload()
        if time_division_multiplex_capable_payload:
            payload[self._TIME_DIVISION_MULTIPLEX_CAPABLE_FIELD] = time_division_multiplex_capable_payload
        packet_switch_capable_payload = self.packet_switch_capable.get_payload()
        if packet_switch_capable_payload:
            payload[self._PACKET_SWITCH_CAPABLE_FIELD] = packet_switch_capable_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_interface_switching_capabilities(self):
        
        payload = {self._INTERFACE_SWITCHING_CAPABILITIES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_interface_switching_capabilities(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_interface_switching_capabilities(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class FLOW_STATISTICS(object):

    _FLOW_STATISTICS_FIELD = "flow-statistics"
    _OPENDAYLIGHT_FLOW_STATISTICS_PACKET_COUNT_FIELD = "opendaylight-flow-statistics:packet-count"
    _BYTE_COUNT_FIELD = "byte-count"
    _OPENDAYLIGHT_FLOW_STATISTICS_DURATION_FIELD = "opendaylight-flow-statistics:duration"
    _DURATION_FIELD = "duration"
    _OPENDAYLIGHT_FLOW_STATISTICS_BYTE_COUNT_FIELD = "opendaylight-flow-statistics:byte-count"
    _PACKET_COUNT_FIELD = "packet-count"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_PACKET_COUNT_FIELD] = None
        self._template[self._BYTE_COUNT_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_DURATION_FIELD] = None
        self._template[self._DURATION_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_BYTE_COUNT_FIELD] = None
        self._template[self._PACKET_COUNT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._duration = DURATION()

    @property
    def duration(self):
        return self._duration

    def set_opendaylight_flow_statistics_packet_count(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_PACKET_COUNT_FIELD] = value

    def set_byte_count(self, value):
        self._template[self._BYTE_COUNT_FIELD] = value

    def set_opendaylight_flow_statistics_duration(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_DURATION_FIELD] = value

    def set_opendaylight_flow_statistics_byte_count(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_BYTE_COUNT_FIELD] = value

    def set_packet_count(self, value):
        self._template[self._PACKET_COUNT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._DURATION_FIELD] = self.duration.get_template(default=default)
            return self._default_template
        else:
            self._template[self._DURATION_FIELD] = self.duration.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        duration_payload = self.duration.get_payload()
        if duration_payload:
            payload[self._DURATION_FIELD] = duration_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_flow_statistics(self):
        
        payload = {self._FLOW_STATISTICS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow_statistics(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow_statistics(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class REFRESH_TIME(object):

    _REFRESH_TIME_FIELD = "refresh-time"
    _REFRESH_TIME_DISABLE_FIELD = "refresh-time-disable"
    _REFRESH_INTERVAL_FIELD = "refresh-interval"

    def __init__(self):
        self._template = {}
        self._template[self._REFRESH_TIME_DISABLE_FIELD] = None
        self._template[self._REFRESH_INTERVAL_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_refresh_time_disable(self, value):
        self._template[self._REFRESH_TIME_DISABLE_FIELD] = value

    def set_refresh_interval(self, value):
        self._template[self._REFRESH_INTERVAL_FIELD] = value

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

    def create_refresh_time(self):
        
        payload = {self._REFRESH_TIME_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_refresh_time(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_refresh_time(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class L3_UNICAST_IGP_TOPOLOGY(object):

    _L3_UNICAST_IGP_TOPOLOGY_FIELD = "l3-unicast-igp-topology"
    _OSPF_FIELD = "ospf"
    _ISIS_FIELD = "isis"
    _OSPF_TOPOLOGY_OSPF_FIELD = "ospf-topology:ospf"
    _ISIS_TOPOLOGY_ISIS_FIELD = "isis-topology:isis"

    def __init__(self):
        self._template = {}
        self._template[self._OSPF_FIELD] = None
        self._template[self._ISIS_FIELD] = None
        self._template[self._OSPF_TOPOLOGY_OSPF_FIELD] = None
        self._template[self._ISIS_TOPOLOGY_ISIS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ospf(self, value):
        self._template[self._OSPF_FIELD] = value

    def set_isis(self, value):
        self._template[self._ISIS_FIELD] = value

    def set_ospf_topology_ospf(self, value):
        self._template[self._OSPF_TOPOLOGY_OSPF_FIELD] = value

    def set_isis_topology_isis(self, value):
        self._template[self._ISIS_TOPOLOGY_ISIS_FIELD] = value

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

    def create_l3_unicast_igp_topology(self):
        
        payload = {self._L3_UNICAST_IGP_TOPOLOGY_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_l3_unicast_igp_topology(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_l3_unicast_igp_topology(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class SUPPORTED_ACTIONS(object):

    _SUPPORTED_ACTIONS_FIELD = "supported-actions"
    _FLOW_NODE_INVENTORY_ACTION_TYPE_FIELD = "flow-node-inventory:action-type"
    _ACTION_TYPE_FIELD = "action-type"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_ACTION_TYPE_FIELD] = None
        self._template[self._ACTION_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._action_type = ACTION_TYPE()

    @property
    def action_type(self):
        return self._action_type

    def set_flow_node_inventory_action_type(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ACTION_TYPE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ACTION_TYPE_FIELD] = self.action_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ACTION_TYPE_FIELD] = self.action_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        action_type_payload = self.action_type.get_payload()
        if action_type_payload:
            payload[self._ACTION_TYPE_FIELD] = action_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_supported_actions(self):
        
        payload = {self._SUPPORTED_ACTIONS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_supported_actions(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_supported_actions(self):
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


class GROUP_DESC(object):

    _GROUP_DESC_FIELD = "group-desc"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_NAME_FIELD = "opendaylight-group-statistics:group-name"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ID_FIELD = "opendaylight-group-statistics:group-id"
    _OPENDAYLIGHT_GROUP_STATISTICS_BUCKETS_FIELD = "opendaylight-group-statistics:buckets"
    _GROUP_TYPE_FIELD = "group-type"
    _GROUP_ID_FIELD = "group-id"
    _BARRIER_FIELD = "barrier"
    _GROUP_NAME_FIELD = "group-name"
    _OPENDAYLIGHT_GROUP_STATISTICS_GROUP_TYPE_FIELD = "opendaylight-group-statistics:group-type"
    _BUCKETS_FIELD = "buckets"
    _CONTAINER_NAME_FIELD = "container-name"
    _OPENDAYLIGHT_GROUP_STATISTICS_BARRIER_FIELD = "opendaylight-group-statistics:barrier"
    _OPENDAYLIGHT_GROUP_STATISTICS_CONTAINER_NAME_FIELD = "opendaylight-group-statistics:container-name"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_NAME_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ID_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKETS_FIELD] = None
        self._template[self._GROUP_TYPE_FIELD] = None
        self._template[self._GROUP_ID_FIELD] = None
        self._template[self._BARRIER_FIELD] = None
        self._template[self._GROUP_NAME_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_TYPE_FIELD] = None
        self._template[self._BUCKETS_FIELD] = None
        self._template[self._CONTAINER_NAME_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BARRIER_FIELD] = None
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_CONTAINER_NAME_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._buckets = BUCKETS()

    @property
    def buckets(self):
        return self._buckets

    def set_opendaylight_group_statistics_group_name(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_NAME_FIELD] = value

    def set_opendaylight_group_statistics_group_id(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_ID_FIELD] = value

    def set_opendaylight_group_statistics_buckets(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BUCKETS_FIELD] = value

    def set_group_type(self, value):
        self._template[self._GROUP_TYPE_FIELD] = value

    def set_group_id(self, value):
        self._template[self._GROUP_ID_FIELD] = value

    def set_barrier(self, value):
        self._template[self._BARRIER_FIELD] = value

    def set_group_name(self, value):
        self._template[self._GROUP_NAME_FIELD] = value

    def set_opendaylight_group_statistics_group_type(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_GROUP_TYPE_FIELD] = value

    def set_container_name(self, value):
        self._template[self._CONTAINER_NAME_FIELD] = value

    def set_opendaylight_group_statistics_barrier(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_BARRIER_FIELD] = value

    def set_opendaylight_group_statistics_container_name(self, value):
        self._template[self._OPENDAYLIGHT_GROUP_STATISTICS_CONTAINER_NAME_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._BUCKETS_FIELD] = self.buckets.get_template(default=default)
            return self._default_template
        else:
            self._template[self._BUCKETS_FIELD] = self.buckets.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        buckets_payload = self.buckets.get_payload()
        if buckets_payload:
            payload[self._BUCKETS_FIELD] = buckets_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_group_desc(self):
        
        payload = {self._GROUP_DESC_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_group_desc(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_group_desc(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class TABLE_PROPERTIES(object):

    _TABLE_PROPERTIES_FIELD = "table-properties"
    _OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROPERTIES_FIELD = "opendaylight-flow-table-statistics:table-feature-properties"
    _TABLE_FEATURE_PROPERTIES_FIELD = "table-feature-properties"

    def __init__(self):
        self._template = {}
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROPERTIES_FIELD] = None
        self._template[self._TABLE_FEATURE_PROPERTIES_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._table_feature_properties = TABLE_FEATURE_PROPERTIES()

    @property
    def table_feature_properties(self):
        return self._table_feature_properties

    def set_opendaylight_flow_table_statistics_table_feature_properties(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_TABLE_STATISTICS_TABLE_FEATURE_PROPERTIES_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._TABLE_FEATURE_PROPERTIES_FIELD] = self.table_feature_properties.get_template(default=default)
            return self._default_template
        else:
            self._template[self._TABLE_FEATURE_PROPERTIES_FIELD] = self.table_feature_properties.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        table_feature_properties_payload = self.table_feature_properties.get_payload()
        if table_feature_properties_payload:
            payload[self._TABLE_FEATURE_PROPERTIES_FIELD] = table_feature_properties_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_table_properties(self):
        
        payload = {self._TABLE_PROPERTIES_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_table_properties(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_table_properties(self):
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


class FLOW(object):

    _FLOW_FIELD = "flow"
    _FLOW_NODE_INVENTORY_FLAGS_FIELD = "flow-node-inventory:flags"
    _FLOW_NODE_INVENTORY_INSTRUCTIONS_FIELD = "flow-node-inventory:instructions"
    _OUT_PORT_FIELD = "out_port"
    _ID_FIELD = "id"
    _FLOW_NODE_INVENTORY_COOKIE_FIELD = "flow-node-inventory:cookie"
    _STRICT_FIELD = "strict"
    _FLOW_NODE_INVENTORY_HARD_TIMEOUT_FIELD = "flow-node-inventory:hard-timeout"
    _IDLE_TIMEOUT_FIELD = "idle-timeout"
    _COOKIE_MASK_FIELD = "cookie_mask"
    _INSTALLHW_FIELD = "installHw"
    _PRIORITY_FIELD = "priority"
    _CONTAINER_NAME_FIELD = "container-name"
    _TABLE_ID_FIELD = "table_id"
    _FLOW_NODE_INVENTORY_PRIORITY_FIELD = "flow-node-inventory:priority"
    _FLOW_NAME_FIELD = "flow-name"
    _MATCH_FIELD = "match"
    _FLOW_NODE_INVENTORY_FLOW_NAME_FIELD = "flow-node-inventory:flow-name"
    _BARRIER_FIELD = "barrier"
    _FLOW_NODE_INVENTORY_IDLE_TIMEOUT_FIELD = "flow-node-inventory:idle-timeout"
    _FLOW_STATISTICS_FIELD = "flow-statistics"
    _BUFFER_ID_FIELD = "buffer_id"
    _FLOW_NODE_INVENTORY_COOKIE_MASK_FIELD = "flow-node-inventory:cookie_mask"
    _FLOW_NODE_INVENTORY_INSTALLHW_FIELD = "flow-node-inventory:installHw"
    _COOKIE_FIELD = "cookie"
    _FLOW_NODE_INVENTORY_CONTAINER_NAME_FIELD = "flow-node-inventory:container-name"
    _INSTRUCTIONS_FIELD = "instructions"
    _FLOW_NODE_INVENTORY_TABLE_ID_FIELD = "flow-node-inventory:table_id"
    _FLOW_NODE_INVENTORY_ID_FIELD = "flow-node-inventory:id"
    _FLOW_NODE_INVENTORY_OUT_PORT_FIELD = "flow-node-inventory:out_port"
    _FLOW_NODE_INVENTORY_BUFFER_ID_FIELD = "flow-node-inventory:buffer_id"
    _FLOW_NODE_INVENTORY_MATCH_FIELD = "flow-node-inventory:match"
    _HARD_TIMEOUT_FIELD = "hard-timeout"
    _OUT_GROUP_FIELD = "out_group"
    _FLOW_NODE_INVENTORY_BARRIER_FIELD = "flow-node-inventory:barrier"
    _OPENDAYLIGHT_FLOW_STATISTICS_FLOW_STATISTICS_FIELD = "opendaylight-flow-statistics:flow-statistics"
    _FLAGS_FIELD = "flags"
    _FLOW_NODE_INVENTORY_OUT_GROUP_FIELD = "flow-node-inventory:out_group"
    _FLOW_NODE_INVENTORY_STRICT_FIELD = "flow-node-inventory:strict"

    def __init__(self):
        self._template = {}
        self._template[self._FLOW_NODE_INVENTORY_FLAGS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_INSTRUCTIONS_FIELD] = None
        self._template[self._OUT_PORT_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_COOKIE_FIELD] = None
        self._template[self._STRICT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_HARD_TIMEOUT_FIELD] = None
        self._template[self._IDLE_TIMEOUT_FIELD] = None
        self._template[self._COOKIE_MASK_FIELD] = None
        self._template[self._INSTALLHW_FIELD] = None
        self._template[self._PRIORITY_FIELD] = None
        self._template[self._CONTAINER_NAME_FIELD] = None
        self._template[self._TABLE_ID_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_PRIORITY_FIELD] = None
        self._template[self._FLOW_NAME_FIELD] = None
        self._template[self._MATCH_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_FLOW_NAME_FIELD] = None
        self._template[self._BARRIER_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_IDLE_TIMEOUT_FIELD] = None
        self._template[self._FLOW_STATISTICS_FIELD] = None
        self._template[self._BUFFER_ID_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_COOKIE_MASK_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_INSTALLHW_FIELD] = None
        self._template[self._COOKIE_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_CONTAINER_NAME_FIELD] = None
        self._template[self._INSTRUCTIONS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_TABLE_ID_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_ID_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_OUT_PORT_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_BUFFER_ID_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_MATCH_FIELD] = None
        self._template[self._HARD_TIMEOUT_FIELD] = None
        self._template[self._OUT_GROUP_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_BARRIER_FIELD] = None
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_FLOW_STATISTICS_FIELD] = None
        self._template[self._FLAGS_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_OUT_GROUP_FIELD] = None
        self._template[self._FLOW_NODE_INVENTORY_STRICT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._match = MATCH()
        self._flow_statistics = FLOW_STATISTICS()
        self._instructions = INSTRUCTIONS()

    @property
    def match(self):
        return self._match

    @property
    def flow_statistics(self):
        return self._flow_statistics

    @property
    def instructions(self):
        return self._instructions

    def set_flow_node_inventory_flags(self, value):
        self._template[self._FLOW_NODE_INVENTORY_FLAGS_FIELD] = value

    def set_flow_node_inventory_instructions(self, value):
        self._template[self._FLOW_NODE_INVENTORY_INSTRUCTIONS_FIELD] = value

    def set_out_port(self, value):
        self._template[self._OUT_PORT_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_flow_node_inventory_cookie(self, value):
        self._template[self._FLOW_NODE_INVENTORY_COOKIE_FIELD] = value

    def set_strict(self, value):
        self._template[self._STRICT_FIELD] = value

    def set_flow_node_inventory_hard_timeout(self, value):
        self._template[self._FLOW_NODE_INVENTORY_HARD_TIMEOUT_FIELD] = value

    def set_idle_timeout(self, value):
        self._template[self._IDLE_TIMEOUT_FIELD] = value

    def set_cookie_mask(self, value):
        self._template[self._COOKIE_MASK_FIELD] = value

    def set_installhw(self, value):
        self._template[self._INSTALLHW_FIELD] = value

    def set_priority(self, value):
        self._template[self._PRIORITY_FIELD] = value

    def set_container_name(self, value):
        self._template[self._CONTAINER_NAME_FIELD] = value

    def set_table_id(self, value):
        self._template[self._TABLE_ID_FIELD] = value

    def set_flow_node_inventory_priority(self, value):
        self._template[self._FLOW_NODE_INVENTORY_PRIORITY_FIELD] = value

    def set_flow_name(self, value):
        self._template[self._FLOW_NAME_FIELD] = value

    def set_flow_node_inventory_flow_name(self, value):
        self._template[self._FLOW_NODE_INVENTORY_FLOW_NAME_FIELD] = value

    def set_barrier(self, value):
        self._template[self._BARRIER_FIELD] = value

    def set_flow_node_inventory_idle_timeout(self, value):
        self._template[self._FLOW_NODE_INVENTORY_IDLE_TIMEOUT_FIELD] = value

    def set_buffer_id(self, value):
        self._template[self._BUFFER_ID_FIELD] = value

    def set_flow_node_inventory_cookie_mask(self, value):
        self._template[self._FLOW_NODE_INVENTORY_COOKIE_MASK_FIELD] = value

    def set_flow_node_inventory_installhw(self, value):
        self._template[self._FLOW_NODE_INVENTORY_INSTALLHW_FIELD] = value

    def set_cookie(self, value):
        self._template[self._COOKIE_FIELD] = value

    def set_flow_node_inventory_container_name(self, value):
        self._template[self._FLOW_NODE_INVENTORY_CONTAINER_NAME_FIELD] = value

    def set_flow_node_inventory_table_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_TABLE_ID_FIELD] = value

    def set_flow_node_inventory_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_ID_FIELD] = value

    def set_flow_node_inventory_out_port(self, value):
        self._template[self._FLOW_NODE_INVENTORY_OUT_PORT_FIELD] = value

    def set_flow_node_inventory_buffer_id(self, value):
        self._template[self._FLOW_NODE_INVENTORY_BUFFER_ID_FIELD] = value

    def set_flow_node_inventory_match(self, value):
        self._template[self._FLOW_NODE_INVENTORY_MATCH_FIELD] = value

    def set_hard_timeout(self, value):
        self._template[self._HARD_TIMEOUT_FIELD] = value

    def set_out_group(self, value):
        self._template[self._OUT_GROUP_FIELD] = value

    def set_flow_node_inventory_barrier(self, value):
        self._template[self._FLOW_NODE_INVENTORY_BARRIER_FIELD] = value

    def set_opendaylight_flow_statistics_flow_statistics(self, value):
        self._template[self._OPENDAYLIGHT_FLOW_STATISTICS_FLOW_STATISTICS_FIELD] = value

    def set_flags(self, value):
        self._template[self._FLAGS_FIELD] = value

    def set_flow_node_inventory_out_group(self, value):
        self._template[self._FLOW_NODE_INVENTORY_OUT_GROUP_FIELD] = value

    def set_flow_node_inventory_strict(self, value):
        self._template[self._FLOW_NODE_INVENTORY_STRICT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MATCH_FIELD] = self.match.get_template(default=default)
            self._default_template[self._FLOW_STATISTICS_FIELD] = self.flow_statistics.get_template(default=default)
            self._default_template[self._INSTRUCTIONS_FIELD] = self.instructions.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MATCH_FIELD] = self.match.get_template()
            self._template[self._FLOW_STATISTICS_FIELD] = self.flow_statistics.get_template()
            self._template[self._INSTRUCTIONS_FIELD] = self.instructions.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        match_payload = self.match.get_payload()
        if match_payload:
            payload[self._MATCH_FIELD] = match_payload
        flow_statistics_payload = self.flow_statistics.get_payload()
        if flow_statistics_payload:
            payload[self._FLOW_STATISTICS_FIELD] = flow_statistics_payload
        instructions_payload = self.instructions.get_payload()
        if instructions_payload:
            payload[self._INSTRUCTIONS_FIELD] = instructions_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_flow(self):
        
        payload = {self._FLOW_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow(self):
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

