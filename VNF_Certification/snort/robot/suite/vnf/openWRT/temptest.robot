*** Settings ***
Documentation     Test Vnf Lcm Scenarios
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library		  random
Library           ../../../../util_findhost.py
Library           ../../../../lcm_library.py
#Resource          ../../../library/vnf_service.robot
#Variables         ../../../variables/vnf_config.py

*** Variables ***
${stack_name}     stack1
${stack2_name}     multiStack1
${snapshot_name}  snap1
#${snapshot_name}  catenate    snap     ${suffix}

*** Test Cases ***
OPENSTACK - Validate Vnf Lcm Scenarios: VM Creation
    [Documentation]    Test VM Creation
    Vnf Create Instance    ${stack_name}
#OPENSTACK - Validate Vnf Lcm Scenarios: Multinet VM Creation
#    [Documentation]    Test Multinet VM Creation
#    Vnf Create Instance Multinet   ${stack2_name}
