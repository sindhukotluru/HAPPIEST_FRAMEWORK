*** Settings ***
Documentation     Test Suite for SDNC-FUNCTIONAL Test Scenarios
Variables         ../../Config/config.py
Variables         ../../Config/OvsConf.py
Variables         ../../Config/ControllerConfig.py
Library           Supporting_Libs.sys_utils
Library           Supporting_Libs.Karaf    IP=${CONTROLLER_INFO['IP']}    username=${CONTROLLER_INFO['USER']}
...               password=${CONTROLLER_INFO['PASSWORD']}    WITH NAME    CNTRLROBJ
Library           Collections



*** Variables ***
${True}              True
${False}             False
@{Cntrlr_data}         ${CONTROLLER_INFO['IP']}  6653

*** Test Cases ***
Configure Controller
    [Documentation]    CONFIGURE CONTROLLER
    ${return_code}    CNTRLROBJ.Start Karaf    clean=${True}
    Should Be True    ${return_code}
    ${return_code}    CNTRLROBJ.Configure Plugins    config_flag=install   plugins=${ODL_PLUGINS}
    Should Be True    ${return_code}
    ${return_code}    CNTRLROBJ.Verify Installed Plugins    plugins=${ODL_PLUGINS}
    Should Be True    ${return_code}
