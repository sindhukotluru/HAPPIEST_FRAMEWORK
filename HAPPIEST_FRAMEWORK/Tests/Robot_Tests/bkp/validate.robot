*** Settings ***
Documentation     Test Suite for SDNC-FUNCTIONAL Test Scenarios
Variables         ../../Config/config.py
Variables         ../../Config/OvsConf.py
Variables         ../../Config/ControllerConfig.py
Library           Supporting_Libs.sys_utils
Library           Supporting_Libs.Karaf    IP=${CONTROLLER_INFO['IP']}    username=${CONTROLLER_INFO['USER']}
...               password=${CONTROLLER_INFO['PASSWORD']}    WITH NAME    CNTRLROBJ
Library           Supporting_Libs.ovs    IP=${SWITCH['IP']}    username=${SWITCH['USER']}
...               password=${SWITCH['PASSWORD']}    WITH NAME    OVSOBJ
Library           Supporting_Libs.hosts    IP=${HOST1['IP']}    username=${HOST1['USER']}
...               password=${HOST1['PASSWORD']}    WITH NAME    HOST1
Library           Supporting_Libs.hosts    IP=${HOST2['IP']}    username=${HOST2['USER']}
...               password=${HOST2['PASSWORD']}    WITH NAME    HOST2
Library           Supporting_Libs.debugHelper
Library           Collections



*** Variables ***
${True}              True
${False}             False
${Match_ip}          33.33.33.1
@{Cntrlr_data}         ${CONTROLLER_INFO['IP']}  6653

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

MAC Address Based Match Flows Test - PUSH A Flow To Match SRC MAC And Forward
    &{flow_input}    create dictionary    Null=Null
    ${status}    Flow Management    ${ovs_obj}    delete    ${OVS_BRIDGE_CONF['NAME']}    ${flow_input}
    should be equal    ${status}    ${True}
    &{flow_input}    create dictionary    priority=${priority[0]}    in_port=${ports[0]}    id=1    table=0    order=0
    ...    dl_src=${mac_addr[0]}    actions=${ports[1]}
    ${status}    Flow Management    ${ovs_obj}    add    ${OVS_BRIDGE_CONF['NAME']}    ${flow_input}
    should be equal    ${status}    ${True}

MAC Address Based Match Flows Test - Check The Flow With Traffic on SRC MAC Match
    import Library    Supporting_Libs.Traffic_Generator.Scapy    ${host1_obj}    None    WITH NAME    TG
    ${tg}    Get Library Instance    TG
    set suite variable    ${tg}
    #${packet}    TG.Generate Packet To Send    pkt_type=ether    profile=${packet_profile}
    ${packet}    TG.Generate Packet To Send    pkt_type=ether
#    ${PID}    ${cap_file}    Start Capture    ${host2_obj}    ${HOST2["PORT_CONFIG"]['iface1']}
#    TG.Send Cmd To Scapy    ${packet}    ${HOST1["PORT_CONFIG"]['iface1']}    ${pkt_count}    ${interval}
#    Stop Capture    ${host2_obj}    ${PID}
#    TG.Disconnect
#    ${file_data}    Supporting_Libs.sys_utils.Get Data From File    ${host2_obj}    ${cap_file}
    ${file_data}    HOST1.Send Pkts N Capture    ${tg}    ${host2_obj}    ${HOST1["PORT_CONFIG"]['iface1']}
    ...    ${HOST2["PORT_CONFIG"]['iface1']}    ${packet}    ${pkt_count}    ${interval}
    TG.Disconnect
    ${valid_count}    Validate Output    ${mac_addr[0]}    ${file_data}
    ${zero}    convert to integer    0
    Should Not Be Equal As Integers    ${valid_count}    ${zero}
