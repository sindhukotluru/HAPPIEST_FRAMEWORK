*** Settings ***
Documentation     Test Vnf SNORT Scenarios
#Library           OperatingSystem
#Library           RequestsLibrary
#Library           Collections
Library           ovsconnect.py
#Library                  random
Library           gre_test.py
#Library           gre_test
#Resource          ../../../library/vnf_service.robot
#Variables         ../../../variables/vnf_config.py

*** Variables ***
#${stack_name}     Stack123
#${stack2_name}     multiStack1
#${snapshot_name}  snap1
#${snapshot_name}  catenate    snap     ${suffix}

*** Test Cases ***
OPENSTACK - Validate Snort vnf Scenarios: Setup Creation
    [Documentation]    DIA Test on WANO
    Dia Test
