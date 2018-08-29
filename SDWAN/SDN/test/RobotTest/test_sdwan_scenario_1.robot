*** Settings ***
Documentation     Test Suite for SDWAN Scenarios
Library           SDN.test.sdwan_flows.SDWAN_FLOWS
Variables         ../../config.py    #Library    SSHLibrary

*** Variables ***
${status}         True
@{devices}        ${CLIENT_IP}    ${SWITCH_IP}    ${HOST1_IP}    ${HOST2_IP}
@{dest_devices}    ${CLIENT_IP}    ${HOST1_IP}    ${HOST2_IP}
${interface}      s1
${open_flow_version}    2.5.0
${protocol}       OpenFlow13
${protocolType}    tcp
${arp}            arp
${mpls}           MPLS
${ssh}            ssh

*** Test Cases ***
Verify If All Devices Are Powered Up
    Log    "Test: Verify if all Devices are Powered Up"
    ${status}    E PowerUpDevices    ${devices}
    Log    ${status}

Configure And Verify DefaultFlows
    Log    "Verify if Default Flows can be configured from Web UI"
    Log    "Verify if the Connection between OVS Switch and remote Devices is established"
    : FOR    ${remote_ip}    IN    @{dest_devices}
    \    ${status}    E PingDevices    ${SWITCH_IP}    ${SWITCH_USER}    ${SWITCH_PASSWORD}    ${remote_ip}
    \    Log    ${status}
    \    run keyword if    ${status} != True    Log    "Remote Device IP: ${remote_ip} not reachable from Switch IP: ${SWITCH_IP}"

Configure And Verify UIFlows
    Log    "Verify the MPLS and DIA Flows configured through the WebUI"
    Page Open
    E ConfigureUIFlows    ${ssh}    ${mpls}
    ${status}    V VerifyConfigFlows    ${open_flow_version}    ${protocol}    ${protocolType}    ${interface}
    Log    ${status}
    E ConfigureUIFlows    ${arp}    ${mpls}
    ${status1}    V VerifyConfigFlows    ${open_flow_version}    ${protocol}    ${arp}    ${interface}
    Log    ${status1}
    Log    "Verify the Flow Statistics table for configured flows"
    ${status2}    V VerifyFlowStatistics    ${ssh}    ${protocolType}    ${interface}    ${mpls}    ${protocol}
    Log    ${status2}
    sleep    5
    ${status3}    V VerifyFlowStatistics    ${arp}    ${arp}    ${interface}    ${mpls}    ${protocol}
    Log    ${status3}

Configure And Verify Traffic
    ${traffic}    E TrafficGenerator
    Log    "Verify if Traffic Generated is received by the Host"
    Log    ${traffic}
