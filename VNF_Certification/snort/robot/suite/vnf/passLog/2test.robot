*** Settings ***
Documentation     Test Vnf Lcm Scenarios
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library		  random
Library           ../../../util_findhost.py
Library           ../../../lcm_library.py
Resource          ../../library/vnf_service.robot
Variables         ../../variables/vnf_config.py

*** Variables ***
${stack_name}     stack1
${stack2_name}     multiStack1
${snapshot_name}  snap1
#${snapshot_name}  catenate    snap     ${suffix}

*** Test Cases ***
OPENSTACK - Validate Vnf Lcm Scenarios: VM Creation
    [Documentation]    Test VM Creation
    Vnf Create Instance    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Multinet VM Creation
    [Documentation]    Test Multinet VM Creation
    Vnf Create Instance Multinet   ${stack2_name}
OPENSTACK - Validate Vnf Lcm Scenarios: VM Upgrade
    [Documentation]    Test VM Upgrade
    Vnf Update Instance    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: VM Soft Reboot
    [Documentation]    Test VM Soft Reboot
    Vnf Soft Reboot Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: VM Hard Reboot
    [Documentation]    Test VM Hard Reboot
    Vnf Hard Reboot Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: VM Create Snapshot
    [Documentation]    Test Create Snapshot
    Vnf Create Snapshot    ${stack_name}    ${snapshot_name}
OPENSTACK - Validate Vnf Lcm Scenarios: VM Delete Snapshot
    [Documentation]    Test VM Delete Snapshot
    Vnf Delete Snapshot    ${snapshot_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Pause VM
    [Documentation]    Test pause server
    Vnf Pause Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Unpause VM
    [Documentation]    Test unpause server
    Vnf Unpause Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Suspend VM
    [Documentation]    Test suspend server
    Vnf Suspend Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Resume VM
    [Documentation]    Test Resume Server
    Vnf Resume Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Delete VM
    [Documentation]    Test VM deletion
    Vnf Delete Server    ${stack_name}
OPENSTACK - Validate Vnf Lcm Scenarios: Delete Stack
    [Documentation]    Test stack deletion
    Vnf Delete Stack    ${stack_name}
