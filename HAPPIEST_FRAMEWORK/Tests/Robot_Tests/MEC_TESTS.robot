*** Settings ***
Documentation     Test Suite for MEC Test Scenarios
Variables         ../../Config/config.py
Variables         ../../Config/MEC_REST_INPUT.py
Variables         ../../Config/ControllerConfig.py
Library           Collections
Library           String
Library           Supporting_Libs.sys_utils
Suite Setup       PreRequisite
Suite Teardown    TerminateSessions
#Library           Supporting_Libs.rest_utils


*** Variables ***
${True}              True
${False}             False
${rest_code}         200
${vlan1}             5
${vlan2}             8
@{ports}             

*** Test Cases ***
Mec System Reset Test
    [Documentation]   Reset the system
    ${url}    catenate   ${MEC_URL}serviceList
    set suite variable   ${url}
    PostAndValidate  ${url}    ${Reset_input}    ${False}
    sleep  4s
  
Mec Service Enable Test
    [Documentation]    Enable desired services
    @{services}      create list     Ip-Tables   DNS-MASq   Telemetry
    set suite variable    $services
    ${url}    catenate   ${MEC_URL}saveList
    set suite variable   ${url}
    PostAndValidate  ${url}    ${Service_Selection_input}    ${True}

Mec Validate Enabled Services Via REST
    [Documentation]    Validate the enabled services using REST GET Operation
    sleep  40s
    GetAndValidate   ${url}

Mec Configure The Enabled Services Test
    [Documentation]    Provide the configuration to the enabled services for different Users
    ${url}    catenate   ${MEC_URL}serviceConfig
    @{data_list}=    Create List
    set suite variable   ${url}
    PostAndValidate  ${url}    ${Service_Config_input1}    ${True}
    sleep  15s
    Append To List    ${data_list}    ${data}
    set suite variable    @{data_list}
    PostAndValidate  ${url}    ${Service_Config_input2}    ${True}
    sleep  15s
    Append To List    ${data_list}    ${data}
    set suite variable    @{data_list}

Mec Validate Configuration of Enabled Service Via REST
    [Documentation]    Validatae the configuration of enabled services using REST GET Operation
    GetAndValidate    ${url}    ${data_list}

Mec Valildate Configuration Of Enabled Service Device level
    [Documentation]    Validatae the configuration of enabled services from Device Level
    OVSOBJ.Ovs_Execute_Command    cmd=ovs-ofctl dump-flows mec_br1
    @{dump_flows}=    Split To Lines    ${ovs_obj.resp}
    ${flows}=    Remove From List   ${dump_flows}  0
    ${flows}=    Remove From List   ${dump_flows}  0
    ${flows}=    Remove From List   ${dump_flows}  -1
    ${pattern}   Set Variable   in_port=1,dl_vlan=${vlan1} actions=mod_dl_dst.*put:(\\d+)
    ${match}   ${out_port}    Should Match Regexp    ${ovs_obj.resp}    ${pattern}
    ${out_port}   convert to integer    ${out_port}
    :FOR   ${vlan}  IN    ${vlan1}  ${vlan2}
    \    SearchForFlows    ${vlan}    ${False}    ${out_port}  ${out_port+1}  ${out_port+2}  ${out_port+3}

Mec Traffic Test To Validate The Service Config
    [Documentation]    Trigger Traffic To Validate The Firewall Service Conf
    GetAndValidateStats
    

Mec Remove One Of The Enabled User Config
    [Documentation]    Provide the configuration to the remove enabled User service
    Set To Dictionary    ${Service_Config_input2["config"]}    action    delete
    PostAndValidate  ${url}    ${Service_Config_input2}    ${True}
    sleep  10s

Mec Validate the Remove Service Conf Via REST
    [Documentation]    Ensure that the User is removed and the other User is still present
    @{removed_data}=    Create List    ${Service_Config_input2}
    @{remain_data}=    Create List     ${Service_Config_input1}
    GetAndValidate   URL=${url}    data_to_compare=${removed_data}    negative=${True}
    GetAndValidate   URL=${url}    data_to_compare=${remain_data}    negative=${False}

Mec Validate the Remove Service Conf Device Level
    [Documentation]    Ensure the Device level conf if removed for removed service
    sleep  3s
    OVSOBJ.Ovs_Execute_Command    cmd=ovs-ofctl dump-flows mec_br1
    @{dump_flows}=    Split To Lines    ${ovs_obj.resp}
    ${flows}=    Remove From List   ${dump_flows}  0
    ${flows}=    Remove From List   ${dump_flows}  0
    ${flows}=    Remove From List   ${dump_flows}  -1
    ${pattern}   Set Variable   in_port=1,dl_vlan=${vlan1} actions=mod_dl_dst.*put:(\\d+)
    ${match}   ${out_port}    Should Match Regexp    ${ovs_obj.resp}    ${pattern}
    ${out_port}   convert to integer    ${out_port}
    SearchForFlows    ${vlan2}    ${True}     ${out_port}  ${out_port+1}  ${out_port+2}  ${out_port+3}
    SearchForFlows    ${vlan1}    ${False}    ${out_port}  ${out_port+1}  ${out_port+2}  ${out_port+3}




*** Keywords ***
PostAndValidate
    [Arguments]    ${URL}   ${input}   ${set_data}=${True}
    [Documentation]    To post the input and validate the response
    ${data}    Run Keyword If    ${set_data}==${True}    Make Mec Input     ${input}     ${services}
    ...    ELSE    Set Variable    ${input}
    set suite variable    &{data}
    ${data_to_json}=    Evaluate    json.dumps(${data})    json
    RESTOBJ.Send Post Request   ${URL}    ${data_to_json}
    Should Be Equal As Integers    ${rest_code}    ${rest_obj.response_code}

GetAndValidate
    [Arguments]    ${URL}   ${data_to_compare}=${data}   ${resp_text_validate}=${True}   ${negative}=${False}
    RESTOBJ.Send Get Request    url=${URL}
    Should Be Equal As Integers    ${rest_code}    ${rest_obj.response_code}
    ${json_to_data}=    Evaluate    json.loads('${rest_obj.response_as_text}')    json
    ${type}=    Evaluate    type(${json_to_data})==list
    Run Keyword If    '${type}'=='${True}' and '${resp_text_validate}'=='${True}'     Sort List   ${data_to_compare}

    Run Keyword If    '${resp_text_validate}'=='${True}'
    ...    Run Keyword If    '${negative}'=='${False}'    should be equal   ${data_to_compare}     ${json_to_data}
    ...    ELSE     should Not be equal   ${data_to_compare}    ${json_to_data}

SearchForFlows
    [Arguments]    ${vlan}    ${negative}    @{ports}
    [Documentation]   Search for flows related to services
    ${length}    Get Length    ${ports}
    ${pattern}   Set Variable     in_port=1,dl_vlan=${vlan} actions=mod_dl_dst.*put:${ports[0]}
    Run Keyword If   '${negative}'=='${False}'    Should Match Regexp    ${ovs_obj.resp}    ${pattern}
    ...    ELSE    Should Not Match Regexp    ${ovs_obj.resp}    ${pattern}
    : FOR    ${i}    IN RANGE    0  ${length}  2
    \    ${j}=   Set Variable    ${i+1}
    \    ${k}=   Set Variable    ${i+2}
    \    ${pattern}=   Run Keyword If   ${ports}[${j}]!=@{ports}[-1]
    \    ...    Set Variable   in_port=@{ports}[${j}],dl_vlan=${vlan} actions=mod_dl_dst.*put:@{ports}[${k}]
    \    ...    ELSE    Set Variable   in_port=@{ports}[-1],dl_vlan=${vlan} actions=mod_dl_dst.*put:2
    \    Run Keyword If   '${negative}'=='${False}'    Should Match Regexp    ${ovs_obj.resp}    ${pattern}
    \    ...    ELSE    Should Not Match Regexp    ${ovs_obj.resp}    ${pattern}

PreRequisite
    [Documentation]    Basic device Login & pre-requisite steps before any test begins
    Log    Create Device SSH Handler and Check REST Login
    import Library    Supporting_Libs.ovs    IP=${SWITCH['IP']}    username=${SWITCH['USER']}
    ...     password=${SWITCH['PASSWORD']}    WITH NAME    OVSOBJ
    ${ovs_obj}    Get Library Instance    OVSOBJ
    set suite variable    ${ovs_obj}
    import Library    Supporting_Libs.rest_utils.REST     content_type= ${CONTENT_TYPE}    WITH NAME    RESTOBJ
    ${rest_obj}    Get Library Instance    RESTOBJ
    set suite variable    ${rest_obj}
    PostAndValidate  ${MEC URL}login    ${Login_input}    ${False}

TerminateSessions
    [Documentation]     Disconnect the created sessions
    Log To Console   Created SSH session is now about to terminate !!!
    OVSOBJ.Disconnect OVS

GetServicePorts
    [Arguments]    ${name}
    [Documentation]    To get the list of service ports
    OVSOBJ.Ovs_Execute_Command    cmd=lxc-info -n ${name}_container
    ${pattern}   Set Variable   (veth.*)\\r
    ${nic_list}    Get Regexp Matches     ${ovs_obj.resp}    ${pattern}
    Remove From List   ${nic_list}  0
    Log To Console    ${nic_list}
    OVSOBJ.Ovs_Execute_Command    cmd=ovs-ofctl show mec_br1
    : FOR    ${nic}    IN     @{nic_list}  
    \    ${stripped}=  Strip String    ${nic}    characters=\r
    \    ${pattern}   Set Variable    \\s(\\d+)\\(${stripped}\\):*
    \    ${match}  ${port_num}     Should Match Regexp    ${ovs_obj.resp}    ${pattern}
    \    ${port_num}   convert to integer    ${port_num}
    \    Append To List   ${ports}    ${port_num}
    set suite variable     @{ports}

GetAndValidateStats
    ${url}    catenate   ${MEC_URL}stats
    GetAndValidate   URL=${url}   resp_text_validate=${False}
    ${stats}   Set Variable    ${rest_obj.response_as_text}
    ${flag}    Evaluate    ${stats}[0]['stats']['vlan'][0]['id']==${vlan1}
    ${index}=    Run Keyword If    ${flag}==${True}
    ...    Set Variable   0
    ...    ELSE    Set Variable   1
    Log To Console    ${index}     
    ${user1_drop_count_before}   Evaluate   ${stats}[0]['stats']['vlan'][${index}]['firewall'][0]['drop_pkt_count']
    ${user1_ingress_rx_before}    Evaluate   ${stats}[0]['stats']['vlan'][${index}]['report'][0]['rx']
    ${user1_egress_tx_drop_before}   Evaluate   ${stats}[0]['stats']['vlan'][${index}]['report'][1]['tx_drop']
    import Library    Supporting_Libs.hosts    IP=${HOST1['IP']}    username=${HOST1['USER']}
    ...     password=${HOST1['PASSWORD']}    WITH NAME    SD
    ${sd_obj}    Get Library Instance    SD
    import Library    Supporting_Libs.Traffic_Generator.Scapy    ${sd_obj}    None    WITH NAME    TG
    ${packet}    TG.Generate Packet To Send    icmpv4
    TG.Send Cmd To Scapy    ${packet}    ${HOST1['PORT_CONFIG']['iface1']}    ${pkt_count}    ${interval}
    sleep    20s
    GetAndValidate   URL=${url}   resp_text_validate=${False}
    ${stats}   Set Variable    ${rest_obj.response_as_text}
    ${user1_drop_count_after}   Evaluate   ${stats}[0]['stats']['vlan'][${index}]['firewall'][0]['drop_pkt_count']
    ${user1_ingress_rx_after}    Evaluate   ${stats}[0]['stats']['vlan'][${index}]['report'][0]['rx']
    ${user1_egress_tx_drop_after}   Evaluate   ${stats}[0]['stats']['vlan'][${index}]['report'][1]['tx_drop']
    ${diff_drop_count1}=    Evaluate    ${user1_drop_count_after}-${user1_drop_count_before}
    Log Many   Drop Counters Before traffic:  ${user1_drop_count_after}
    Log Many   Drop Counters After traffic:  ${user1_drop_count_after}
    Log Many   Ingress Rx Before Traffic: ${user1_ingress_rx_before}
    Log Many   Ingress Rx After Traffic: ${user1_ingress_rx_after}
    Log Many   Egress Tx Drop Before Traffic: ${user1_egress_tx_drop_before}
    Log Many   Egress Tx Drop After Traffic: ${user1_egress_tx_drop_after}
    Should Be Equal    ${pkt_count}    ${diff_drop_count1}
 
