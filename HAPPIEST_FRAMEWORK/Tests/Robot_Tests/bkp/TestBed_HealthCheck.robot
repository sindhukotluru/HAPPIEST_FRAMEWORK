*** Settings ***
Documentation     Test Suite for SDNC-FUNCTIONAL Test Scenarios
Variables         ../../Config/config.py
Variables         ../../Config/OvsConf.py
Library           Supporting_Libs.sys_utils
Library           Supporting_Libs.Karaf    IP=${CONTROLLER_IP}    username=${CONTROLLER_USER}
...               password=${CONTROLLER_PASSWORD}    WITH NAME    CNTRLROBJ
Library           Supporting_Libs.ovs    IP=${SWITCH_IP}    username=${SWITCH_USER}
...               password=${SWITCH_PASSWORD}    WITH NAME    OVSOBJ
Library           Supporting_Libs.hosts    IP=${HOST1_IP}    username=${HOST1_USER}
...               password=${HOST1_PASSWORD}    WITH NAME    HOST1
Library           Supporting_Libs.hosts    IP=${HOST2_IP}    username=${HOST2_USER}
...               password=${HOST2_PASSWORD}    WITH NAME    HOST2
Library           Supporting_Libs.debugHelper


*** Variables ***
${True}              True
${False}             False
${Match_ip}          33.33.33.1
@{Cntrlr_data}         ${CONTROLLER_IP}  6653

*** Test Cases ***
Verify If All Devices Are Powered Up
    [Documentation]    login to switch,host1 & host2
    ${ovs_obj}    Get Library Instance    OVSOBJ
    ${cntrl_obj}    Get Library Instance    CNTRLROBJ
    ${host1_obj}    Get Library Instance    HOST1
    ${host2_obj}    Get Library Instance    HOST2

    set suite variable    ${ovs_obj}
    set suite variable    ${cntrl_obj}
    set suite variable    ${host1_obj}
    set suite variable    ${host2_obj}

Configure OVS bridge
    ${status}    OVSOBJ.Create Validate Bridge    ${OVS_BRIDGE}   ${Cntrlr_data}
    Run Keyword If  ${status} != ${True}   Run Keywords
    ...    Debug Controller Failure  ${ovs_obj}  ${cntrl_obj}
    ...    AND   Fail

Add ports to OVS bridge
    ${status}    OVSOBJ.Addports Validate     ${OVS_BRIDGE}   ${OVS_BRIDGE_PORTS}
    should be equal    ${status}    ${True}

Assign IP addresses to host interfaces
    HOST1.Config Host Nic Ip    ${HOST1_PORTS[0]}   ${HOST1_IPs[0]}
    HOST2.Config Host Nic Ip    ${HOST2_PORTS[0]}   ${HOST2_IPs[0]}

MAC Address Based Match Flows Test - PUSH A Flow To Match SRC MAC And Forward
    &{flow_input}    create dictionary    Null=Null
    ${status}    Flow Management    ${ovs_obj}    delete    ${OVS_BRIDGE}    ${flow_input}
    should be equal    ${status}    ${True}
    &{flow_input}    create dictionary    priority=${priority[0]}    in_port=${ports[0]}    id=1    table=0    order=0
    ...    dl_src=${mac_addr[0]}    actions=${ports[1]}
    ${status}    Flow Management    ${ovs_obj}    add    ${OVS_BRIDGE}    ${flow_input}
    should be equal    ${status}    ${True}

MAC Address Based Match Flows Test - Check The Flow With Traffic on SRC MAC Match
    import Library    Supporting_Libs.Traffic_Generator.Scapy    ${host1_obj}    None    WITH NAME    TG
    ${packet}    TG.Generate Packet To Send    ether
    ${PID}    ${cap_file}    Start Capture    ${host2_obj}    ${HOST2_PORTS[0]}    ether host ${mac_addr[0]}
    TG.Send Cmd To Scapy    ${packet}    ${HOST1_PORTS[0]}    ${pkt_count}    ${interval}
    Stop Capture    ${host2_obj}    ${PID}
    TG.Disconnect
    #${file_data}    Get Data From File    ${host2_obj}    ${cap_file}
    ${file_data}    HOST2.Get Data From File    ${cap_file}
    ${valid_count}    Validate Output    ${mac_addr[0]}    ${file_data}
    ${zero}    convert to integer    0
    Should Not Be Equal As Integers    ${valid_count}    ${zero}
