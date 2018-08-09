*** Settings ***
Documentation     Test Suite for SDNC-FUNCTIONAL Test Scenarios
Variables         ../../Config/config.py
Variables         ../../Config/OvsConf.py
Variables         ../../Config/ControllerConfig.py
Library           Supporting_Libs.sys_utils
Library           Supporting_Libs.Karaf    IP=${CONTROLLER_INFO['IP']}    username=${CONTROLLER_INFO['USER']}
...               password=${CONTROLLER_INFO['PASSWORD']}    WITH NAME    CNTRLROBJ
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
    ${cntrl_obj}    Get Library Instance    CNTRLROBJ
    set suite variable    ${cntrl_obj}

Bringup The Opendaylight Controller and Config plugins
    [Documentation]   CONFIGURE CONTROLLER
    ${return_code}    CNTRLROBJ.Start Karaf    clean=${True}
    Should Be True    ${return_code}
    ${return_code}    CNTRLROBJ.Configure Plugins    config_flag=install   plugins=${OF_PLUGINS}
    Should Be True    ${return_code}
    ${return_code}    CNTRLROBJ.Verify Installed Plugins    plugins=${OF_PLUGINS}
    Should Be True    ${return_code}
