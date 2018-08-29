*** Settings ***
Documentation     Test suite for Inventory Scalability
Resource          ../../libraries/Utils.robot
Resource          ../../libraries/MininetKeywords.robot
Suite Setup       Start Suite
Suite Teardown    Stop Suite
Library           SSHLibrary
Library           ../../libraries/Common.py
Variables         ../../variables/Variables.py
Variables         ../../variables/Mininet_OVS_Commands.py


*** Variables ***
${mininet_topo_file}         custom.py
${start1}         sudo mn \ --controller=remote,ip=${ODL_SYSTEM_IP_1} --custom ${mininet_topo_file} --topo Switch1 --switch ovsk,protocols=OpenFlow13
${start2}         sudo mn \ --controller=remote,ip=${ODL_SYSTEM_IP_1} --custom ${mininet_topo_file} --topo Switch2 --switch ovsk,protocols=OpenFlow13

*** Keywords ***
Start Suite
    [Documentation]    Test suit for vpn service using mininet OF13 and OVS 2.3.1
    Log    Start the tests
    Clean Mininet System

    ${mininet1_conn_id_1}=    Open Mininet Connection and Login with SSH   ${TOOLS_SYSTEM_IP}    30s
    Set Global Variable    ${mininet1_conn_id_1}
    Set OVS_Manager and Start Mininet Topology    ${CURDIR}/${mininet_topo_file}    ${start1}

    ${mininet1_conn_id_2}=    Open Mininet Connection and Login with SSH   ${TOOLS_SYSTEM_IP}    30s
    Set Global Variable    ${mininet1_conn_id_2}
    OVS Add GRE Interface    s1    s1-gre1    gre    ${TOOLS_SYSTEM_2_IP}    ${TOOLS_SYSTEM_IP}
    Validate OVS Manager Version and OpenFlow Versions    ptcp:6644    ovs_version: "2.3.1"    OpenFlow versions 0x1:0x4
    Execute Command    sudo ovs-ofctl add-flow s1 -O OpenFlow13 arp,actions=FLOOD

    ${mininet2_conn_id_1}=    Open Mininet Connection and Login with SSH   ${TOOLS_SYSTEM_2_IP}    30s
    Set Global Variable    ${mininet2_conn_id_1}
    Set OVS_Manager and Start Mininet Topology    ${CURDIR}/${mininet_topo_file}    ${start2}

    ${mininet2_conn_id_2}=    Open Mininet Connection and Login with SSH   ${TOOLS_SYSTEM_2_IP}    30s
    Set Global Variable    ${mininet2_conn_id_2}
    OVS Add GRE Interface    s2    s2-gre1    gre    ${TOOLS_SYSTEM_IP}    ${TOOLS_SYSTEM_2_IP}
    Validate OVS Manager Version and OpenFlow Versions    ptcp:6644    ovs_version: "2.3.1"    OpenFlow versions 0x1:0x4
    Execute Command    sudo ovs-ofctl add-flow s2 -O OpenFlow13 arp,actions=FLOOD

Stop Suite
    Log    Stop the tests
    Switch Connection    ${mininet1_conn_id_1}
    Read
    Write    exit
    Read Until    ${TOOLS_SYSTEM_PROMPT}
    Close Connection
    Switch Connection    ${mininet1_conn_id_2}
    Close Connection
    Switch Connection    ${mininet2_conn_id_1}
    Read
    Write    exit
    Read Until    ${TOOLS_SYSTEM_PROMPT}
    Close Connection
    Switch Connection    ${mininet2_conn_id_2}
    Close Connection
