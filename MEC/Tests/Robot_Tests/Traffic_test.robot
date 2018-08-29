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


*** Variables ***
${True}              True
${False}             False
${rest_code}         200
${vlan1}             5
${vlan2}             8
@{ports}             

*** Test Cases ***

Mec Traffic Test To Validate The Service Config
    [Documentation]    Trigger Traffic To Validate The Firewall Service Conf
#    GetAndValidateStats
    Log To Console    sirish
    

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
    Run Keyword If    '${type}'=='${True}' and '${resp_text_validate}'=='${True}'    Sort List   ${json_to_data}

    Run Keyword If    '${resp_text_validate}'=='${True}'
    ...    Run Keyword If    '${negative}'=='${False}'    should be equal   ${data_to_compare}     ${json_to_data}
    ...    ELSE     should Not be equal   ${data_to_compare}    ${json_to_data}

PreRequisite
    [Documentation]    Basic device Login & pre-requisite steps before any test begins
    Log    Create Device SSH Handler and Check REST Login
    import Library    Supporting_Libs.ovs    IP=${SWITCH['IP']}    username=${SWITCH['USER']}
    ...     password=${SWITCH['PASSWORD']}    WITH NAME    OVSOBJ
    ${ovs_obj}    Get Library Instance    OVSOBJ
    set suite variable    ${ovs_obj}
    Config MEC Infra
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
    OVSOBJ.Ovs_Execute_Command    cmd=ps -ef | grep tele
    ${status}=    Evaluate    re.search(r'--in-port 1 --out-port',"""${ovs_obj.resp}""")==None    re 
    Log To Console    ${status}
    Run Keyword If    ${status}==${True}    OVSOBJ.Ovs_Execute_Command    cmd=/home/test/MEC/MEC/BkEnd/InstallScripts/ovs_tele.py --in-port 1 --out-port 2 &
#    Run Keyword If    ${status}==${True}    Log To Console   TESTTTTT>>>>>
 
Config MEC Infra
    ${cmd}=   Set Variable    cd /home/test/MEC/MEC/BkEnd/InstallScripts/;./config_infra_and_apps.py
    OVSOBJ.Ovs_Execute_Command    cmd=${cmd}
    sleep    3s
    OVSOBJ.Ovs_Execute_Command    cmd=ps -ef | grep "main.py"
    ${pattern}    Set Variable   --redis-address
    Should Match Regexp    ${ovs_obj.resp}    ${pattern}
    ${cmd}=   Set Variable   node /home/test/MEC/MEC/BkEnd/InstallScripts/index.js > /var/log/index.log &
    OVSOBJ.Ovs_Execute_Command    cmd=${cmd}
    OVSOBJ.Ovs_Execute_Command    cmd=ps -ef | grep node
    Should Match Regexp    ${ovs_obj.resp}    index
