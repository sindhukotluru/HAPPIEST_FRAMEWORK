*** Settings ***
Documentation     Test Case To Verify Load Balancing
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../../util_findhost.py
Library           ../../../test_vnf.py
Resource          ../../library/vnf_service.robot
Variables         ../../variables/vnf_config.py

*** Variables ***


*** Test Cases ***
DEVSTACK - Validate Load Balance Traffic
    [Documentation]    Make a connection to Devstack VM and validate Load Balance
    ${status1}    Test Load Balance   ${vm_ip[0]}    ${vm_ip[2]}    ${vm_ip[4]}    ${vm_ip[5]}
