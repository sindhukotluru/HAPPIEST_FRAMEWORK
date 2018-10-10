*** Settings ***
Documentation     Test Suite for SNMP-FUNCTIONAL Test Scenarios
Variables         ../Config/config.py
Variables         ../Variables/variables.py
Variables         ../Config/ControllerConfig.py
Library           SNMPLib.snmp_utils      WITH NAME      SNMPOBJ
Library           ODLLib.Karaf    IP=${CONTROLLER_INFO['IP']}    username=${CONTROLLER_INFO['USER']}
...               password=${CONTROLLER_INFO['PASSWORD']}    WITH NAME    CNTRLROBJ
Library           Collections
Library           String      

*** Variables ***
${IP}               192.168.203.3
${COMMUNITY}        private
${SYS_NAME}         Controller
${err_string}       'Not writable'
${True}             True
${False}            False
@{GET_OIDs}         1.3.6.1.2.1.1.4.0  1.3.6.1.2.1.1.3.0  1.3.6.1.2.1.1.6.0 

*** Test Cases ***

Verify If All Devices Are Powered Up
    ${cntrl_obj}    Get Library Instance    CNTRLROBJ
    set suite variable    ${cntrl_obj}

Bringup The Opendaylight Controller and Config plugins
    [Documentation]   CONFIGURE CONTROLLER
    ${return_code}    CNTRLROBJ.Start Karaf    clean=${True}
    Should Be True    ${return_code}
    ${return_code}    CNTRLROBJ.Configure Plugins    config_flag=install   plugins=${SNMP_PLUGINS}
    Should Be True    ${return_code}
    ${return_code}    CNTRLROBJ.Verify Installed Plugins    plugins=${SNMP_PLUGINS}
    Should Be True    ${return_code}

Verify SNMP SET operation   
    [Documentation]   SNMP SET OPERATION AND VERIFICATION
    sleep  20s 
                            SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.1.5.0  COMMUNITY=${COMMUNITY}   VALUE=${SYS_NAME}
    ${result}               SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.1.5.0  COMMUNITY=${COMMUNITY}   GETTYPE=GET
    Should Match Regexp     "${result}"  ${SYS_NAME}

Verify SNMP GET operation   
    [Documentation]   SNMP GET OPERATION AND VERIFICATION 
    ${result}              SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.25.1.2.0  COMMUNITY=${COMMUNITY}   GETTYPE=GET
    ${output}              Set Variable       @{result}[1]
    ${contains}=           Evaluate   "ERROR MESSAGE" in """${output}"""
    Should be equal        ${contains}     ${False}

Verify SNMP SET operation on READ-ONLY MIB
    [Documentation]   SNMP SET OPERATION on READ-ONLY MIB 
    ${result}                   SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.1.1.0    COMMUNITY=${COMMUNITY}   VALUE='Ubuntu'
    ${output}                   Set Variable       @{result}[1]
    ${contains}=                Evaluate   ${err_string} in """${output}"""
    Should be equal             ${contains}     ${True}

    
Verify SNMP GET-BULK operation 
    [Documentation]   SNMP GET BULK OPERATION 
    ${result}                   SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.2.2.1.7   COMMUNITY=${COMMUNITY}   GETTYPE=GET-BULK
    ${output}                   Set Variable       @{result}[1]
    ${contains}=                Evaluate   "ERROR MESSAGE" in """${output}"""
    Should be equal             ${contains}     ${False}

Verify SNMP GET-NEXT operation 
    [Documentation]   SNMP GET NEXT OPERATION 
    ${result}                   SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.1   COMMUNITY=${COMMUNITY}   GETTYPE=GET-NEXT
    ${output}                   Set Variable       @{result}[1]
    ${contains}=                Evaluate   "ERROR MESSAGE" in """${output}"""
    Should be equal             ${contains}     ${False}

Verify SNMP GET-WALK operation 
    [Documentation]   SNMP GET WALK OPERATION 
    ${result}                   SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.3.1.1.2  COMMUNITY=${COMMUNITY}   GETTYPE=GET-WALK
    ${output}                   Set Variable       @{result}[1]
    ${contains}=                Evaluate   "ERROR MESSAGE" in """${output}"""
    Should be equal             ${contains}     ${False}

Access unavailable SNMP MIB  
    [Documentation]   Accessing the SNMP MIB that does not exist
    ${result}                   SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=1.3.6.1.2.1.4.21   COMMUNITY=${COMMUNITY}   GETTYPE=GET
    ${output}                   Set Variable       @{result}[1]
    ${contains}=                Evaluate   "noSuchInstance" in """${output}"""
    Should be equal             ${contains}     ${True}

Verify Multiple SNMP GET operation
    [Documentation]   SNMP GET operation for MIBs System Contact person, UP time and location
    :FOR   ${GET_OID}   IN   @{GET_OIDs}
    \  ${result}                   SNMPOBJ.Perform odl snmp operation  IP=${IP}  OID=${GET_OID}   COMMUNITY=${COMMUNITY}   GETTYPE=GET
    \  ${output}                   Set Variable       @{result}[1]
    \  ${contains}=                Evaluate   "ERROR MESSAGE" in """${output}"""
    \  Should be equal             ${contains}     ${False}


