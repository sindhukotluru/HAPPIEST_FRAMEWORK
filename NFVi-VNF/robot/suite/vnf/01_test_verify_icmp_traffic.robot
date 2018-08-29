*** Settings ***
Documentation     Test Case To Verify ICMP Traffic On DEVSTACK
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../../util_findhost.py
Library           ../../../test_vnf.py
Resource          ../../library/vnf_service.robot
Variables         ../../variables/vnf_config.py

*** Variables ***
${vm1_name}       CLIENT1
${vm2_name}       FIREWALL
${vm3_name}       HA_PROXY
${vm4_name}       CLIENT2
${vm5_name}       SERVER1
${vm6_name}       SERVER2

*** Test Cases ***
DEVSTACK - Validate ICMP Traffic
    [Documentation]    Make a connection to Devstack VM and validate ICMP Traffic
    ${status1}   Test Traffic Icmp Success   ${vm_ip[0]}   ${vm_ip[4]}
    Sleep  60
    ${status2}   Test Traffic Icmp Failure   ${vm_ip[0]}   ${vm_ip[4]}