*** Settings ***
Documentation     Test Suite for MEC Test Scenarios
Variables         ../../Config/config.py
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


*** Test Cases ***
Mec System Reset Test
    [Documentation]   Reset the system
    ${url}    catenate   ${MEC_URL}serviceList
    set suite variable   ${url}
    PostAndValidate  ${url}    ${Reset_input}    ${False}
  
Mec Service Enable Test
    [Documentation]    Enable desired services
    @{services}      create list     Ip-Tables   DNS-MASq   Telemetry
    set suite variable    $services
    ${url}    catenate   ${MEC_URL}saveList
    set suite variable   ${url}
    PostAndValidate  ${url}    ${Service_Selection_input}    ${True}

Mec Configure The Enabled Services Test
    [Documentation]    Provide the configuration to the enabled services for different Users
    ${url}    catenate   ${MEC_URL}serviceConfig
    @{data_list}=    Create List
    set suite variable   ${url}
    PostAndValidate  ${url}    ${Service_Config_input1}    ${True}
    Append To List    ${data_list}    ${data}
    set suite variable    @{data_list}
    PostAndValidate  ${url}    ${Service_Config_input2}    ${True}
    Append To List    ${data_list}    ${data}
    set suite variable    @{data_list}

Mec Validate Configuration of Enabled Service Via REST
    [Documentation]    Validatae the configuration of enabled services using REST GET Operation
    GetAndValidate    ${url}    ${data_list}




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
    [Arguments]    ${URL}   ${data_to_compare}=${data}   ${resp_text}=${True}   ${negative}=${False}
    RESTOBJ.Send Get Request    url=${URL}
    Should Be Equal As Integers    ${rest_code}    ${rest_obj.response_code}
    ${json_to_data}=    Evaluate    json.loads('${rest_obj.response_as_text}')    json
    Log To Console    ${data_to_compare}
    ${type}=    Evaluate    type(${json_to_data})==list
    Run Keyword If    ${type}==${True}     Sort List   ${data_to_compare}
    Log To Console    ${data_to_compare}
    Run Keyword If    '${resp_text}'=='${True}' and '${negative}'=='${False}'
    ...   should be equal   ${json_to_data}    ${data_to_compare}
    ...   ELSE IF    '${resp_text}'=='${True}' and '${negative}'=='${True}'
    ...   should Not be equal   ${data_to_compare}    ${json_to_data}

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






    
