*** Settings ***
Documentation     This script contains complete NFVi E2E scenarios (a) OpenStack Deployment (b) OpenStack Services Verification (c) Life Cycle Management
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           random
Library           ../../../Framework/NFV/PythonLib/OpenStack_E2E/util_findhost.py
Library           ../../../Framework/NFV/PythonLib/OpenStack_E2E/orch_lib.py
Library           ../../../Framework/NFV/PythonLib/OpenStack_E2E/lcm_test.py
Variables         ../../../Framework/NFV/PythonLib/OpenStack_E2E/test_variables.py


*** Variables ***
${True}             True
${False}            False

*** Test Cases ***
OPENSTACK - OpenStack Deployment: Verify System Pre Install State
    [Documentation]    Verify System Pre Install State
    Set Environment     ${auth}
    ${status}    System Pre Check Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Deployment: Uninstall
    [Documentation]    Uninstall Test
    Set Environment      ${auth}
    ${status}    Uninstall OpenStack    ${stack_ip}    ${stack_user}    ${stack_pass}
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Deployment: Create Local
    [Documentation]    Create Local Conf Test
    Set Environment      ${auth}
    ${status}    Create Local    ${stack_pass}
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Deployment: Git Clone Stable Image
    [Documentation]    Git Clone Stable Image Test
    Set Environment      ${auth}
    ${status}    Clone Stable Image    ${stack_version}
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Deployment: Install
    [Documentation]    Install Test
    Set Environment      ${auth}
    ${status}    Install OpenStack    ${stack_ip}    ${stack_user}    ${stack_pass}
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Nova Service
    [Documentation]    Verify Nova Service Test
    Set Environment      ${auth}
    ${status}   Verify Nova Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Nova Legacy Service
    [Documentation]    Verify Nova Legacy Service Test
    Set Environment      ${auth}
    ${status}   Verify Nova Legacy Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Neutron Service
    [Documentation]    Verify Neutron Service Test
    Set Environment      ${auth}
    ${status}   Verify Neutron Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Keystone Service
    [Documentation]    Verify Keystone Service Test
    Set Environment      ${auth}
    ${status}   Verify Keystone Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Glance Service
    [Documentation]    Verify Glance Service Test
    Set Environment      ${auth}
    ${status}   Verify Glance Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Heat Service
    [Documentation]    Verify Heat Service Test
    Set Environment      ${auth}
    ${status}   Verify Heat Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Cinder Service
    [Documentation]    Verify Cinder Service Test
    Set Environment      ${auth}
    ${status}   Verify Cinder Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Cinderv2 Service
    [Documentation]    Verify Cinderv2 Service Test
    Set Environment      ${auth}
    ${status}   Verify Cinderv2 Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Cinderv3 Service
    [Documentation]    Verify Cinderv3 Service Test
    Set Environment      ${auth}
    ${status}   Verify Cinderv3 Services Test
    should be equal    ${status}    ${True}

OPENSTACK - OpenStack Services: Verify Placement Service
    [Documentation]    Verify Placement Service Test
    Set Environment      ${auth}
    ${status}   Verify Placement Services Test
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Key Pairs
    [Documentation]    Create Key Pairs Test
    Set Environment      ${auth}
    ${status}    Create Keypairs Test    ${public_key}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Image
    [Documentation]    Create Image Test
    Set Environment      ${auth}
    ${status}    Create Image Test    ${image_name}    ${image_file}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Manage Existing Router And Networks
    [Documentation]    Manage Existing Router And Networks Test
    Set Environment        ${auth}
    ${status}   Manage Existing Router And Network
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Public Network
    [Documentation]    Create Public Network Test
    Set Environment        ${auth}
    ${status}    Create Public Network Test    ${public_nw}    ${public_net_subnet}    ${ip_alloc_pool_start}    ${ip_alloc_pool_end}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Private Networks
    [Documentation]    Create Private Network Test
    Set Environment        ${auth}
    ${status}    Create Network Test    ${mgmt_nw}    ${mgmt_subnet}
    ${status}    Create Network Test    ${network_name}    ${network_subnet}
    ${status}    Create Network Test    ${network_name2}   ${network_subnet2}
    ${status}    Create Network Test    ${network_name3}   ${network_subnet3}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Router
    [Documentation]    Create Router Test
    Set Environment        ${auth}
    ${status}    Create Router Test    ${router_name}    ${public_nw}    ${mgmt_nw}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Security Group
    [Documentation]    Create Security Group Test
    Set Environment     ${auth}
    ${status}    Create Security Group Test    ${sec_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Instance Has Single Network
    [Documentation]    Create Instance Has Single Network Test
    Set Environment     ${auth}
    ${status}    Create Stack Test    ${stack_name}  ${yaml_loc}  ${yaml_name}  ${mgmt_nw}  ${image_name}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}  ${sec_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Instance Has Single Network
    [Documentation]    Delete Instance Has Single Network Test
    Set Environment     ${auth}
    ${status}    Delete Stack Test    ${stack_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Instance Has Multi Networks
    [Documentation]    Create Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Create Stack Multi Network Test    ${stack2_name}  ${yaml_loc}  ${yaml2_name}  ${mgmt_nw}  ${network_name}  ${image_name}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}  ${sec_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Snapshot
    [Documentation]    Create Snapshot Test
    Set Environment     ${auth}
    ${status}    Create Snapshot Test    ${stack2_name}    ${snapshot_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Soft Reboot Instance Has Multi Networks
    [Documentation]    Soft Reboot Instance Has Multi Networks Tests
    Set Environment     ${auth}
    ${status}    Soft Reboot Stack Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Pause Instance Has Multi Networks
    [Documentation]    Pause Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Pause Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Unpause Instance Has Multi Networks
    [Documentation]    Unpause Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Unpause Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Hard Reboot Instance Has Multi Networks
    [Documentation]    Hard Reboot Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Hard Reboot Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Suspend Instance Has Multi Networks
    [Documentation]    Suspend Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Suspend Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Resume Instance Has Multi Networks
    [Documentation]    Resume Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Resume Server Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Downgrade Image
    [Documentation]    Create Downgrade Image Test
    Set Environment      ${auth}
    ${status}    Create Image Test    ${dgrade_image}    ${image_file2}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Downgrade Instance Has Multi Networks With Image
    [Documentation]    Downgrade Instance Has Multi Networks With Image Test
    Set Environment     ${auth}
    ${status}    Downgrade Stack Test    ${stack2_name}  ${yaml_loc}  ${dg_yaml_name}  ${dgrade_image}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Upgrade Instance Has Multi Networks With Image
    [Documentation]    Upgrade Instance Has Multi Networks With Image Test
    Set Environment     ${auth}
    ${status}    Upgrade Stack Test    ${stack2_name}  ${yaml_loc}  ${ug_yaml_name}  ${image_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Instance Has Multi Networks
    [Documentation]    Delete Instance Has Multi Networks Test
    Set Environment     ${auth}
    ${status}    Delete Stack Test    ${stack2_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Instance Has Multi Networks With Snapshot Image
    [Documentation]    Create Instance Has Multi Networks With Snapshot Image Test
    Set Environment     ${auth}
    ${status}    Create Stack With Snapshot Test    ${snap_stack_name}  ${yaml_loc}  ${yaml2_name}  ${mgmt_nw}  ${network_name}  ${snapshot_name}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}  ${sec_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Instance Has Multi Networks With Snapshot Image
    [Documentation]    Delete Instance Has Multi Networks With Snapshot Image Test
    Set Environment     ${auth}
    ${status}    Delete Stack Test    ${snap_stack_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Snapshot Image
    [Documentation]    Delete Snapshot Image Test
    Set Environment     ${auth}
    ${status}    Delete Snapshot Test    ${snapshot_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Create Multiple Instances Having Multi Networks Through Single Yaml
    [Documentation]    Create Multiple Instances Having Multi Networks Through Single Yaml Test
    Set Environment     ${auth}
    ${status}    Create Stack Multi Network Multi Server Test   ${stack3_name}  ${yaml_loc}  ${yaml3_name}  ${mgmt_nw}  ${network_name}  ${image_name}  ${flavor}  ${public_key}  ${key_loc}  ${username}  ${password}  ${sec_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Soft Reboot Multi Network Multi Server Instances
    [Documentation]    Soft Reboot Multi Network Multi Server Instances Test
    Set Environment     ${auth}
    ${status}    Soft Reboot Stack Multi Network Test    ${stack3_name}  ${username}  ${key_loc}  ${public_key}  ${password}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Multi Network Multi Server Instances
    [Documentation]    Delete Multi Network Multi Server Instances Tests
    Set Environment     ${auth}
    ${status}    Delete Stack Multi Server Test    ${stack3_name}
    should be equal    ${status}    ${True}

OPENSTACK - VNF Functional: Ospf Functional Test
    [Documentation]    Ospf Functional Test
    Set Environment     ${auth}
    ${status}    Ospf Functional Test  ${stack4_name}  ${yaml_loc}  ${yaml4_name}  ${public_key}  ${key_loc}   ${sec_name}
    should be equal    ${status}    ${True}

OPENSTACK - VNF Functional: Delete Instances Used In Ospf Functional Test
    [Documentation]    Delete Instances Used In Ospf Functional Test
    Set Environment     ${auth}
    ${status}    Delete Stack Multi Server Test    ${stack4_name}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Private Networks
    [Documentation]    Delete Private Networks Test
    Set Environment     ${auth}
    ${status}    Delete Network Test    ${network_name}
    ${status}    Delete Network Test    ${network_name2}
    ${status}    Delete Network Test    ${network_name3}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Image
    [Documentation]    Delete Image Test
    Set Environment     ${auth}
    ${status}    Delete Image Test    ${image_name}
    ${status}    Delete Image Test    ${dgrade_image}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Key Pair
    [Documentation]    Delete Key Pair Test
    Set Environment      ${auth}
    ${status}    Delete Keypairs Test    ${public_key}
    should be equal    ${status}    ${True}

OPENSTACK - Life Cycle Management: Delete Security Group
    [Documentation]    Delete Security Group Test
    Set Environment     ${auth}
    ${status}    Delete Security Group Test    ${sec_name}
    should be equal    ${status}    ${True}
