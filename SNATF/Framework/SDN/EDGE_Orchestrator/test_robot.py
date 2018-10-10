*** Settings ***
Documentation     Test Vnf SNORT Scenarios
#Library           OperatingSystem
#Library           RequestsLibrary
#Library           Collections
#Library           SSHLibrary
#Library                  random
Library           /home/test/lcm/util_findhost.py
Library           /home/test/lcm/vnf_library.py
#Resource          ../../../library/vnf_service.robot
#Variables         ../../../variables/vnf_config.py

*** Variables ***
${stack_name}     Stack123
#${stack2_name}     multiStack1
#${snapshot_name}  snap1
#${snapshot_name}  catenate    snap     ${suffix}

*** Test Cases ***
OPENSTACK - Validate Snort vnf Scenarios: Setup Creation
    [Documentation]    Test VM Creation
    Vnf Create Multistack    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: ICMP Allow Test
    [Documentation]    Test ICMP
    Vnf Allow Icmp Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: ICMP All drop Test
    [Documentation]    Test ICMP
    Vnf Icmp Alldrop Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: ICMP Block Test
    [Documentation]    Test ICMP
    Vnf Block Icmp Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: HTTP Allow Test
    [Documentation]    Test HTTP
    Vnf Http Allow Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: HTTP Block Test
    [Documentation]    Test HTTP
    Vnf Http Block Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: Inline Test
    [Documentation]    Test INLINE
    Vnf Inline Test    ${stack_name}
