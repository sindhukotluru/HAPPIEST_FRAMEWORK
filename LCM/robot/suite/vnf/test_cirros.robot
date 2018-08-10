*** Settings ***
Documentation     Test VNF Orchestration
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library		      random
Library           ../../../util_findhost.py
Library           ../../../orch_lib.py
Variables         ../../../config_cirros.py
#Library           /home/testpc/automation/rmaity/test_demo/orch_lib.py
#Variables         /home/testpc/automation/rmaity/test_demo/config_cirros.py
#Resource          ../../library/vnf_service.robot
#Variables         ../../variables/vnf_config.py

*** Variables ***
${True}             True
${False}            False

*** Test Cases ***
OPENSTACK - Validate Vnf Orchestration: Create Image
    [Documentation]    Test Create Image
    Set Environment      ${auth}
    ${status}    Create Image Test    ${image_name}    ${image_file}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Network Creation
    [Documentation]    Test Network Creation
    Set Environment        ${auth}
    ${status}    Create Network Test    ${network_name}    ${network_subnet}
    ${status}    Create Network Test    ${network_name2}    ${network_subnet2}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Single Network VM Creation
    [Documentation]    Test Single Network VM Creation
    Set Environment     ${auth}
    ${status}    Create Stack Test    ${stack_name}  ${yaml_loc}  ${yaml_name}  ${public_nw}  ${base_image}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Single Network VM Deletion
    [Documentation]    Test Single Network VM Deletion
    Set Environment     ${auth}
    ${status}    Delete Stack Test    ${stack_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Multi Network VM Creation
    [Documentation]    Test Multi Network VM Creation
    Set Environment     ${auth}
    ${status}    Create Stack Multi Network Test    ${stack2_name}  ${yaml_loc}  ${yaml2_name}  ${public_nw}  ${network_name}  ${base_image}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Snapshot Creation
    [Documentation]    Test Snapshot Creation
    Set Environment     ${auth}
    ${status}    Create Snapshot Test    ${stack2_name}    ${snapshot_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Soft Reboot Multi Network VM
    [Documentation]    Test Soft Reboot Multi Network VM
    Set Environment     ${auth}
    ${status}    Soft Reboot Stack Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Pause Multi Network VM
    [Documentation]    Test Pause Multi Network VM
    Set Environment     ${auth}
    ${status}    Pause Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Unpause Multi Network VM
    [Documentation]    Test Unpause Multi Network VM
    Set Environment     ${auth}
    ${status}    Unpause Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Hard Reboot Multi Network VM
    [Documentation]    Test Hard Reboot Multi Network VM
    Set Environment     ${auth}
    ${status}    Hard Reboot Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Suspend Multi Network VM
    [Documentation]    Test Suspend Multi Network VM
    Set Environment     ${auth}
    ${status}    Suspend Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Resume Multi Network VM
    [Documentation]    Test Resume Multi Network VM
    Set Environment     ${auth}
    ${status}    Resume Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Multi Network VM Deletion
    [Documentation]    Test Multi Network VM Deletion
    Set Environment     ${auth}
    ${status}    Delete Stack Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Multi Network VM Creation With snapshot
    [Documentation]    Test Multi Network VM Creation With snapshot
    Set Environment     ${auth}
    ${status}    Create Stack With Snapshot Test    ${snap_stack_name}  ${yaml_loc}  ${yaml2_name}  ${public_nw}  ${network_name}  ${snapshot_name}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Multi Network Snapshot VM Deletion
    [Documentation]    Test Multi Network Snapshot VM Deletion
    Set Environment     ${auth}
    ${status}    Delete Stack Test    ${snap_stack_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Snapshot Deletion
    [Documentation]    Test Snapshot Deletion
    Set Environment     ${auth}
    ${status}    Delete Snapshot Test    ${snapshot_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Create Multi Network Multi Server VMs in single Yaml
    [Documentation]    Test Create Multi Network Multi Server VMs
    Set Environment     ${auth}
    ${status}    Create Stack Multi Network Multi Server Test   ${stack3_name}  ${yaml_loc}  ${yaml3_name}  ${public_nw}  ${network_name}  ${base_image}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Soft Reboot Multi Network Multi Server VMs
    [Documentation]    Test Soft Reboot Multi Network Multi Server VMs
    Set Environment     ${auth}
    ${status}    Soft Reboot Stack Multi Network Test    ${stack3_name}  ${username}  ${key_loc}  ${public_key}  ${password}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Delete Multi Network Multi Server VMs
    [Documentation]    Test Delete Multi Network Multi Server VMs
    Set Environment     ${auth}
    ${status}    Delete Stack Multi Server Test    ${stack3_name}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Network Deletion
    [Documentation]    Test Network Deletion
    Set Environment     ${auth}
    ${status}    Delete Network Test    ${network_name}
    ${status}    Delete Network Test    ${network_name2}
    should be equal    ${status}    ${True}

OPENSTACK - Validate Vnf Orchestration: Deletion Image
    [Documentation]    Test Deletion Image
    Set Environment     ${auth}
    ${status}    Delete Image Test    ${image_name}
    should be equal    ${status}    ${True}
