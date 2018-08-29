*** Settings ***
Documentation     Test Suite for vpn instance
Suite Setup       Create Session    session    http://${ODL_SYSTEM_IP}:${RESTCONFPORT}    auth=${AUTH}    headers=${HEADERS}
Suite Teardown    Delete All Sessions
Variables         ../../variables/Variables.py
Variables         ../../variables/Mininet_OVS_Commands.py
Variables         ../../variables/vpnservice/configureSwitches.py    ${TOOLS_SYSTEM_IP}    ${TOOLS_SYSTEM_2_IP}
Library           SSHLibrary
Resource          ../../libraries/Utils.robot
Resource          ../../libraries/MininetKeywords.robot
Library           RequestsLibrary

*** Variables ***
${REST_CON}       /restconf/config
@{vpn_inst_values}    testVpn1    100:1    200:1    300:1    testVpn2    400:1    500:1
...               600:1
@{ietf_int_values}    s1-eth1    s1-eth2    s1-gre1    s2-eth1    s2-eth2    s2-gre1
@{vpn_int_values}    s1-eth1    testVpn1    10.0.0.1    00:00:00:00:00:01    s1-eth2    10.0.0.2    00:00:00:00:00:02
...               s2-eth1    10.0.0.3    00:00:00:00:00:03    testVpn2    s2-eth2    10.0.0.4    00:00:00:00:00:04
${REST_OPER}      /restconf/operational
@{NODE_ELEMENTS}    openflow:1    openflow:1:1    openflow:1:2    openflow:1:3    openflow:2    openflow:2:1    openflow:2:2
...               openflow:2:3

*** Test Cases ***
Veirfy The Switches
    [Documentation]    Verifies if the switches and node connectors data is available to the controller
    Check For Elements At URI    ${OPERATIONAL_NODES_API}    ${NODE_ELEMENTS}

Create VPN Instances
    [Documentation]    Creates VPN Instances through restconf
    [Tags]    Post
    ${resp}    RequestsLibrary.Post Request    session    ${VPN_INST_API}    data=${vpn_instances}
    Log    ${resp.content}
    Should Be Equal As Strings    ${resp.status_code}    204

Verify VPN instances
    [Documentation]    Verifies the vpn instances in the datastores
    [Tags]    Get
    Wait Until Keyword Succeeds    5s    1s    Check For Elements At URI    ${VPN_INST_API}    ${vpn_inst_values}
    Wait Until Keyword Succeeds    5s    1s    Check For Elements At URI    ${OPERATIONAL_VPN_INST_API}    ${vpn_inst_values}

Create ietf interfaces
    [Documentation]    Creates ietf interfaces through the restconf
    [Tags]    Post
    ${resp}    RequestsLibrary.Post Request    session    ${IETF_INTF_API}    data=${ietf_interfaces}
    Should Be Equal As Strings    ${resp.status_code}    204

Verify ietf interfaces
    [Documentation]    Verifies ietf interfaces created in datastores
    [Tags]    Get
    Wait Until Keyword Succeeds    5s    1s    Check For Elements At URI    ${IETF_INTF_API}    ${ietf_int_values}
    Wait Until Keyword Succeeds    5s    1s    Check For Elements At URI    ${OPERATIONAL_IETF_INTF_STATE_API}    ${ietf_int_values}
    @{state}=    Create List    down
    Wait Until Keyword Succeeds    2s    1s    Check For Elements Not At URI    ${OPERATIONAL_IETF_INTF_STATE_API}    ${state}

Create VPN interfaces
    [Documentation]    Creates vpn interface for the corresponding ietf interface
    [Tags]    Post
    ${resp}    RequestsLibrary.Post Request    session    ${VPN_INTF_API}    data=${vpn_interfaces}
    Should Be Equal As Strings    ${resp.status_code}    204

Verify VPN interfaces
    [Documentation]    Verifies the vpn interfaces created in datastores
    [Tags]    Get
    Wait Until Keyword Succeeds    3s    1s    Check For Elements At URI    ${VPN_INTF_API}    ${vpn_int_values}
    Wait Until Keyword Succeeds    3s    1s    Check For Elements At URI    ${OPERATIONAL_VPN_INTF_API}    ${vpn_int_values}

Verify FIB entries after create
    [Documentation]    Verifies the fib entries in the operational DS for the corresponding vpn interfaces
    [Tags]    Get
    @{fib_entries1}=    Create List    ${vpn_int_values[2]}    ${vpn_int_values[8]}
    @{fib_entries2}=    Create List    ${vpn_int_values[5]}    ${vpn_int_values[12]}
    Wait Until Keyword Succeeds    3s    1s    Check For Elements At URI    ${OPERATIONAL_FIB_ENTRIES_VRF_TABLE}${vpn_inst_values[1]}    ${fib_entries1}
    Wait Until Keyword Succeeds    3s    1s    Check For Elements At URI    ${OPERATIONAL_FIB_ENTRIES_VRF_TABLE}${vpn_inst_values[5]}    ${fib_entries2}

Verify flows
    [Documentation]    Verify flows in the switches in VM1
    [Tags]    verify in switch
    @{flow_elements}    Create List    ${vpn_int_values[2]}    ${vpn_int_values[5]}    ${vpn_int_values[8]}    ${vpn_int_values[12]}
    Log    ${flow_elements}
    Wait Until Keyword Succeeds    6s    2s    Ensure Flows Are Present    ${mininet1_conn_id_1}    ${flow_elements}
    Wait Until Keyword Succeeds    6s    2s    Ensure Flows Are Present    ${mininet2_conn_id_1}    ${flow_elements}

Verify groups
    [Documentation]    Verify groups in the switches
    [Tags]    verify in switch
    @{group_elements1}    Create List    ${vpn_int_values[3]}    ${vpn_int_values[6]}
    @{group_elements2}    Create List    ${vpn_int_values[9]}    ${vpn_int_values[13]}
    Wait Until Keyword Succeeds    5s    1s    Ensure Groups Are Present    ${mininet1_conn_id_1}    ${group_elements1}    3
    Wait Until Keyword Succeeds    5s    1s    Ensure Groups Are Present    ${mininet2_conn_id_1}    ${group_elements2}    3

Verify ping fail h1 h2
    [Documentation]    Verifies the ping between the two hosts. Ping should succeed between hosts in same vpn, (h1,h3) and (h2,h4).Ping between hosts in different vpns should fail (h1,h2) & (h3,h4). The commented out section is to be uncommented when ovs supports mpls over gre in datapath
    [Tags]    verify in switch
    ${ping_result}    Ping Between Hosts    ${mininet1_conn_id_1}    h1    h2    5
    Should Contain    ${ping_result}    100% packet loss

Verify ping pass h1 h3
    [Documentation]    Verifies the ping between the two hosts. Ping should succeed between hosts in same vpn, (h1,h3) and (h2,h4).Ping between hosts in different vpns should fail (h1,h2) & (h3,h4). The commented out section is to be uncommented when ovs supports mpls over gre in datapath
    [Tags]    verify in switch
    ${ping_result}    Ping Between Hosts    ${mininet1_conn_id_1}    h1    10.0.0.3    5
    Should Contain    ${ping_result}    100% packet loss

Delete vpn interfaces
    [Documentation]    Deletes the vpn interfaces
    [Tags]    Delete
    ${resp}    RequestsLibrary.Delete Request    session    ${VPN_INTF_API}
    Should Be Equal As Strings    ${resp.status_code}    200

Verify after deleting vpn interfaces
    [Documentation]    Verifies if vpn interfaces are deleted
    [Tags]    Verify after delete
    ${resp}    RequestsLibrary.get Request    session    ${VPN_INTF_API}    headers=${ACCEPT_XML}
    Should Be Equal As Strings    ${resp.status_code}    404

Delete ietf interfaces
    [Documentation]    Deletes the ietf interfaces
    [Tags]    Delete
    ${resp}    RequestsLibrary.Delete Request    session    ${IETF_INTF_API}
    Should Be Equal As Strings    ${resp.status_code}    200

Verify after deleting ietf interfaces
    [Documentation]    Verifies if ietf interfaces are deleted
    [Tags]    Verify after delete
    ${resp}    RequestsLibrary.get Request    session    ${IETF_INTF_API}    headers=${ACCEPT_XML}
    Should Be Equal As Strings    ${resp.status_code}    404

Delete VPN Instances
    [Documentation]    Deletes the VPN Instances
    [Tags]    Delete
    ${resp}    RequestsLibrary.Delete Request    session    ${VPN_INST_API}
    Should Be Equal As Strings    ${resp.status_code}    200

Verify after deleting the vpn instances
    [Documentation]    Verifies after deleting the vpn instances
    [Tags]    Verfiy after delete
    ${resp}    RequestsLibrary.get Request    session    ${VPN_INST_API}    headers=${ACCEPT_XML}
    Should Be Equal As Strings    ${resp.status_code}    404

Verify FIB entries after delete
    [Documentation]    Verifies if the fib entries are deleted in the operational DS
    [Tags]    Get
    @{fib_entries}=    Create List    ${vpn_int_values[2]}    ${vpn_int_values[5]}    ${vpn_int_values[8]}    ${vpn_int_values[12]}
    Wait Until Keyword Succeeds    3s    1s    Check For Elements Not At URI    ${OPERATIONAL_FIB_ENTRIES}    ${fib_entries}

Verify flows after delete
    [Documentation]    Verify if the flows are deleted from the switch
    [Tags]    verify in switch
    [Template]
    Wait Until Keyword Succeeds    12s    2s    Ensure Flows Are Removed    ${mininet1_conn_id_1}
    Wait Until Keyword Succeeds    12s    2s    Ensure Flows Are Removed    ${mininet2_conn_id_1}

*** Keywords ***
Ensure Flows Are Present
    [Arguments]    ${conn_id}    ${flow_elements}
    [Documentation]    Succeeds if the flows for vpn service are present
    ${output}    Send Mininet Command    ${conn_id}    ${DUMP_FLOWS_OF13}
    Log    ${output}
    Should Contain    ${output}    goto_table:20
#    Should Contain X Times    ${output}    goto_table:21    2
    Should Contain X Times    ${output}    goto_table:21    3
#    Should Contain X Times    ${output}    table=20    2
    Should Contain X Times    ${output}    table=20    6
    Should Contain X Times    ${output}    table=21    4
    : FOR    ${i}    IN    @{flow_elements}
    \    Should Contain    ${output}    ${i}

Ensure Groups Are Present
    [Arguments]    ${conn_id}    ${group_elements}    ${gre_port_id}
    [Documentation]    Succeeds if the groups for the vpn service are present
    ${output}    Send Mininet Command    ${conn_id}    ${DUMP_GROUPS_OF13}
    Log    ${output}
    Should Contain X Times    ${output}    actions=output:${gre_port_id}    1
    : FOR    ${i}    IN    @{group_elements}
    \    Should Contain    ${output}    actions=pop_mpls:0x0800,set_field:${i}

Ensure Flows Are Removed
    [Arguments]    ${conn_id}
    [Documentation]    Succeeds if the flows are removed from the switch
    ${output}    Send Mininet Command    ${conn_id}    ${DUMP_FLOWS_OF13}
    Log    ${output}
    Should Not contain    ${output}    goto_table:20
    Should Not contain    ${output}    goto_table:21
    Should Not contain    ${output}    table=20
    Should Not contain    ${output}    table=21

Ensure Groups Are Removed
    [Arguments]    ${conn_id}
    [Documentation]    Succeeds if the group entries are removed from switch
    ${output}    Send Mininet Command    ${conn_id}    ${DUMP_GROUPS_OF13}
    Log    ${output}
    Should Not Contain    ${output}    actions=output:
    Should Not Contain    ${output}    actions=pop_mpls:0x0800
