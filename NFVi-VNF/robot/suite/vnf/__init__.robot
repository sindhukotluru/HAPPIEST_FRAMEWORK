*** Settings ***
Documentation     Test Suite for VNF-DEVSTACK functionalities
Suite Setup       Start Suite
Suite Teardown    Stop Suite
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../../util_findhost.py
Library           ../../../test_vnf.py
Resource          ../../library/vnf_service.robot
Variables         ../../variables/vnf_config.py


*** Variables ***
${vm1_name}       c1
${vm2_name}       fw
${vm3_name}       ha
${vm4_name}       c2
${vm5_name}       s1
${vm6_name}       s2


*** Keywords ***
Start Suite
    [Documentation]    Configuration of Devstack VM
    Install Devstack     ${DEVSTACK_IP}   ${DEVSTACK_USER}   ${DEVSTACK_PSWD}
    @{vm_detail_list}   DEVSTACK Infrastructure Setup    ${vm1_name}  ${vm2_name}  ${vm3_name}  ${vm4_name}  ${vm5_name}  ${vm6_name}
    ${status}    Test Conf Vm    @{vm_detail_list}
    @{vm_ip}    Get Vm Ip    ${vm1_name}    ${vm2_name}    ${vm3_name}    ${vm4_name}    ${vm5_name}   ${vm6_name}
    set global variable    @{vm_ip}

Stop Suite
    Test Complete
