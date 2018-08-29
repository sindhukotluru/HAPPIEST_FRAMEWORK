*** Settings ***
Documentation     Test Vnf SNORT Scenarios
#Library           OperatingSystem
#Library           RequestsLibrary
#Library           Collections
#Library           SSHLibrary
#Library		  random
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
OPENSTACK - Validate Snort vnf Scenarios: Inline Testmode Test
    [Documentation]    Test InlineTestmode
    Vnf Inline Testmode Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: Sniffer Test
    [Documentation]    Test Sniffer
    Vnf Sniffer Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: NIDSmode Test
    [Documentation]    Test NIDS
    Vnf NIDS Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: Packet Logger mode Test
    [Documentation]    Test PacketLoggerMode
    Vnf Pkt Logger Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: SSH Test
    [Documentation]    Test SSH
    Vnf Ssh Test    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: Malware Test
    [Documentation]    Test SSH
    Vnf Malware Test    ${stack_name}

#OPENSTACK - Validate Vnf Lcm Scenarios: Delete VM
#    [Documentation]    Test VM deletion
#    Vnf Delete Server    ${stack_name}
#OPENSTACK - Validate Vnf Lcm Scenarios: Delete Stack
#    [Documentation]    Test stack deletion
#    Vnf Delete Stack    ${stack_name}
