*** Settings ***
Documentation     Resource file containing all the PYTHON API implementations.
Library           Collections
Library           setup_actions.py
Library           config_ip.py
Library           Devices.py
Library           OSPF.py
Library           IBGP.py
Library           operational_ph.py
Library           String
Variables         variable.py

*** Variables ***

@{Devices} =      R1    R2    R3    R4    R5
${ELEMENT}
@{load_devices_lo}
@{load_devices}
@{show_ip_interface}
@{ospf_neighbor}
@{bgp_summary}
@{clear_lo_devices}

*** Keywords ***

Setup Actions

    Log To Console            Setup Actions done here

    Run Keyword and Continue On Failure    connect_all    enable


Teardown Actions

    Log To Console            Teardown Actions done here

    Log To Console            Unconfiguring IP_Address

    ${ip_addr_R1}=    Create List    R1    ${Links_of_R1}    unconfigure
    ${ip_addr_R2}=    Create List    R2    ${Links_of_R2}    unconfigure
    ${ip_addr_R3}=    Create List    R3    ${Links_of_R3}    unconfigure
    ${ip_addr_R4}=    Create List    R4    ${Links_of_R4}    unconfigure
    ${ip_addr_R5}=    Create List    R5    ${Links_of_R5}    unconfigure
    ${ip_addr_PC1}=    Create List    PC-1    unconfigure    ${mask}
    ${ip_addr_PC2}=    Create List    Ubuntu    unconfigure    ${mask}
    ${unconfig_ip}=    Create List    ${ip_addr_R1}    ${ip_addr_R2}    ${ip_addr_R3}    ${ip_addr_R4}    ${ip_addr_R5}   ${ip_addr_PC1}   ${ip_addr_PC2}
    ${result}=    Run Keyword and Continue On Failure    start configure     ${unconfig_ip}
    Run Keyword If    ${result}==False    FAIL    Unable to clear IP address on the routers
    Log To Console            IP_Address cleared on all Routers

    Log To Console            Unconfiguring Loopback interface
    :FOR  ${var}  in  @{Devices}
    \    ${clear_lo}=    Create List    ${var}    unset
    \    Append To List    ${clear_lo_devices}    ${clear_lo}

    ${result}=    Run Keyword and Continue On Failure    start configure loopback     ${clear_lo_devices}
    Run Keyword If    ${result}==False    FAIL    Unable to clear Loopback address on the interfaces
    Log To Console            Loopback_Address cleared on all Routers

    Log To Console            Clearing OSPF configuration
    ${ospf_R1}=    Create List    R1    ${Process_id}    ${Networks_connected_to_R1}    ${Area1}    disable
    ${ospf_R2}=    Create List    R2    ${Process_id}    ${Networks_connected_to_R2}    ${Area1}    disable
    ${ospf_R3}=    Create List    R3    ${Process_id}    ${Networks_connected_to_R3}    ${Area1}    disable
    ${clear_ospf}=    Create List    ${ospf_R1}    ${ospf_R2}    ${ospf_R3}
    ${result}=    Run Keyword and Continue On Failure    start_configure_ospf   ${clear_ospf}
    Run Keyword If    ${result}==False    FAIL    Clearing OSPF on Routers has failed
    Log To Console            OSPF unconfigured in Routers

    Log To Console            Clearing BGP configuration
    ${clear_R2}=    Create List    R2    ${R2_AS_id}   ${R2_einterface}   ${R2_neighbor_AS_id}   disable  ${R4_R2_network}  ${mask}
    ${clear_R3}=    Create List    R3    ${R3_AS_id}   ${R3_einterface}   ${R3_neighbor_AS_id}   disable  ${R3_R5_network}  ${mask}
    ${clear_R4}=    Create List    R4    ${R4_AS_id}   ${R4_einterface}   ${R4_neighbor_AS_id}   disable  ${R4_R2_network}  ${mask}
    ${clear_R5}=    Create List    R5    ${R5_AS_id}   ${R5_einterface}   ${R5_neighbor_AS_id}   disable  ${R3_R5_network}  ${mask}
    ${clear_ebgp}=    Create List    ${clear_R2}    ${clear_R3}    ${clear_R4}    ${clear_R5}

    ${result}=    Run Keyword and Continue On Failure    ebgp configure     ${clear_ebgp}
    Run Keyword If    ${result}==False    FAIL    Clearing BGP on Routers has failed
    Log To Console            BGP unconfigured on Routers R2,R3,R4 and R5


Configure IP addresses as per the topology

    Log To Console            Configuring IP_Address

Configure ip address
    ${load_device_R1}=    Create List    R1    ${Links_of_R1}    configure
    ${load_device_R2}=    Create List    R2    ${Links_of_R2}    configure
    ${load_device_R3}=    Create List    R3    ${Links_of_R3}    configure
    ${load_device_R4}=    Create List    R4    ${Links_of_R4}    configure
    ${load_device_R5}=    Create List    R5    ${Links_of_R5}    configure
    ${load_device_PC1}=    Create List    PC-1    configure    ${mask}
    ${load_device_PC2}=    Create List    Ubuntu    configure    ${mask}
    ${load_devices}=    Create List  ${load_device_R1}  ${load_device_R2}  ${load_device_R3}  ${load_device_R4}  ${load_device_R5}  ${load_device_PC1}  ${load_device_PC2}
    ${result}=    Run Keyword and Continue On Failure    start configure     ${load_devices}
    Run Keyword If    ${result}==False    FAIL    IP address configuration failed
    Log To Console            IP_Address configured on all Routers

Set loopback interface

    Log To Console            Setting Loopback interface
    :FOR  ${var}  in  @{Devices}
    \    ${load_device}=    Create List    ${var}    set
    \    Append To List    ${load_devices_lo}    ${load_device}

    ${result}=    Run Keyword and Continue On Failure    start configure loopback     ${load_devices_lo}
    Run Keyword If    ${result}==False    FAIL    Configuring Loopback IP failed
    Log To Console            Loopback_Address configured on all Routers



Create and Assign VRFs to PE routers
    Log To Console             Configuring VRFs on PE routers

    ${load_device_R1}=    Create List    R1    ${Process_id}    ${Networks_connected_to_R1}    ${Area1}    enable
    ${load_device_R2}=    Create List    R2    ${Process_id}    ${Networks_connected_to_R2}    ${Area1}    enable
    ${load_device_R3}=    Create List    R3    ${Process_id}    ${Networks_connected_to_R3}    ${Area1}    enable
    ${load_devices}=    Create List    ${load_device_R1}    ${load_device_R2}    ${load_device_R3}
    ${result}=    Run Keyword and Continue On Failure    start_configure_ospf   ${load_devices}
    Run Keyword If    ${result}==False    FAIL    Configuring ospf on Routers has failed
    Log To Console            OSPF configured in Routers

Configure OSPF within AS2 to advertise the connected networks

    Log To Console             Configuring OSPF

Enable OSPF in devices present in AS2 and set the ospf neighbors

    ${load_device_R1}=    Create List    R1    ${Process_id}    ${Networks_connected_to_R1}    ${Area1}    enable
    ${load_device_R2}=    Create List    R2    ${Process_id}    ${Networks_connected_to_R2}    ${Area1}    enable
    ${load_device_R3}=    Create List    R3    ${Process_id}    ${Networks_connected_to_R3}    ${Area1}    enable
    ${load_devices}=    Create List    ${load_device_R1}    ${load_device_R2}    ${load_device_R3}
    ${result}=    Run Keyword and Continue On Failure    start_configure_ospf   ${load_devices}
    Run Keyword If    ${result}==False    FAIL    Configuring ospf on Routers has failed
    Log To Console            OSPF configured in Routers


Configure IBGP and source the BGP updates from the loopback0 interfaces

    Log To Console    Setting IBGP between R2 and R3


Enable IBGP and advertise the updates from the loopback interface
    ${ibgp_device_R2}=    Create List    R2    ${AS_id}    ${R3_interface}    enable
    ${ibgp_device_R3}=    Create List    R3    ${AS_id}    ${R2_interface}    enable
    ${ibgp_devices}=    Create List    ${ibgp_device_R2}    ${ibgp_device_R3}

    ${result}=    Run Keyword and Continue On Failure    start ibgp     ${ibgp_devices}
    Run Keyword If    ${result}==False    FAIL    IBGP configuration failed
    Log To Console            IBGP configured on R2 and R3 routers


Enable BGP Synchronisation

    Log To Console    Enabling BGP synchronization

Enable synchronisation between border routers

    ${ibgp_sync_R2}=    Create List    R2    ${AS_id}
    ${ibgp_sync_R3}=    Create List    R3    ${AS_id}
    ${sync_enable}=    Create List    ${ibgp_sync_R2}    ${ibgp_sync_R3}

    ${result}=    Run Keyword and Continue On Failure    enable sync     ${sync_enable}
    Run Keyword If    ${result}==False    FAIL    BGP synchronization failed
    Log To Console            Enabled BGP synchronization on R2 and R3 routers

Configure EBGP and source the BGP updates from the loopback0 interfaces

    Log To Console    Configuring EBGP between devices in different autonomous systems

Enable BGP and advertise networks connected outside the autonomous system

    ${ebgp_device_R2}=    Create List    R2    ${R2_AS_id}   ${R2_einterface}   ${R2_neighbor_AS_id}   enable  ${R4_R2_network}  ${mask}
    ${ebgp_device_R3}=    Create List    R3    ${R3_AS_id}   ${R3_einterface}   ${R3_neighbor_AS_id}   enable  ${R3_R5_network}  ${mask}
    ${ebgp_device_R4}=    Create List    R4    ${R4_AS_id}   ${R4_einterface}   ${R4_neighbor_AS_id}   enable  ${R4_R2_network}  ${mask}
    ${ebgp_device_R5}=    Create List    R5    ${R5_AS_id}   ${R5_einterface}   ${R5_neighbor_AS_id}   enable  ${R3_R5_network}  ${mask}
    ${ebgp_devices}=    Create List    ${ebgp_device_R2}    ${ebgp_device_R3}    ${ebgp_device_R4}    ${ebgp_device_R5}

    ${result}=    Run Keyword and Continue On Failure    ebgp configure     ${ebgp_devices}
    Run Keyword If    ${result}==False    FAIL    EBGP configuration failed
    Log To Console            EBGP configured on Routers R2,R3,R4 and R5


Advertise loopback interface on AS1 and AS3
    ${adv_R4}=    Create List    R4    ${R4_AS_id}   ${R4_interface}   ${R4_mask}
    ${adv_R5}=    Create List    R5    ${R5_AS_id}   ${R5_interface}   ${R5_mask}
    ${adv_devices}=    Create List       ${adv_R4}    ${adv_R5}

    ${result}=    Run Keyword and Continue On Failure    advertise loopback     ${adv_devices}
    Run Keyword If    ${result}==False    FAIL    Advertising Loopback configuration failed
    Log To Console            Loopback interface is advertised to AS1 and AS3


Establish route between R2 and R3
    ${route_R2}=    Create List    R2    ${R2_AS_id}   ${R3_lointerface}
    ${route_R3}=    Create List    R3    ${R3_AS_id}   ${R2_lointerface}
    ${routes}=    Create List       ${route_R2}    ${route_R3}

    ${result}=    Run Keyword and Continue On Failure    establish route     ${routes}
    Run Keyword If    ${result}==False    FAIL    Establishment of route between R2 and R3 failed
    Log To Console            Established route between R2 and R3


Redistribute routes from OSPF into BGP
    Log To Console    Redistributing routes from OSPF into BGP
    ${redistribution_R2}=    Create List    R2    ${R2_AS_id}   ${Process_id}
    ${redistribution_R3}=    Create List    R3    ${R3_AS_id}   ${Process_id}
    ${redistribute_ospf}=    Create List       ${redistribution_R2}    ${redistribution_R3}

    ${result}=    Run Keyword and Continue On Failure    redistribute ospf   ${redistribute_ospf}
    Run Keyword If    ${result}==False    FAIL    Redistribution of routes from OSPF into BGP failed
    Log To Console            Redistributed routes from OSPF into BGP


Redistribute connnected routes into BGP
    Log To Console    Redistributing connected routes into BGP
    ${redistribution_R4}=    Create List    R4    ${R4_AS_id}
    ${redistribution_R5}=    Create List    R5    ${R5_AS_id}
    ${connected}=    Create List       ${redistribution_R4}    ${redistribution_R5}

    ${result}=    Run Keyword and Continue On Failure    redistribute connected   ${connected}
    Run Keyword If    ${result}==False    FAIL    Redistribution of connected routes failed
    Log To Console            Redistributed connnected routes into BGP

Check if ip address is set and interface is up

    Log To Console    Checking if IP address is set and interface is up
    ${ip_set_R1}=    Create List    R1    show interfaces description
    ${ip_set_R2}=    Create List    R2    show interfaces description
    ${ip_set_R3}=    Create List    R3    show interfaces description
    ${ip_set_R4}=    Create List    R4    show interfaces description
    ${ip_set_R5}=    Create List    R5    show interfaces description
    ${show_ip_interface}=    Create List       ${ip_set_R1}    ${ip_set_R2}    ${ip_set_R3}    ${ip_set_R4}   ${ip_set_R4}
    ${result}=    Run Keyword and Continue On Failure    show ip interface     ${show_ip_interface}
    Run Keyword If    ${result}==False    FAIL    IP address not set or interface not up in  ${ELEMENT}


Ensure that different autonomous systems can communicate with each other

    Log    Autonomous system communication validated

    Log To Console            Verify Ping operation from PC-1 to Ubuntu
    ${result}=    Run Keyword and Continue On Failure   ping router    PC-1   ping    ${Host2_IP}
    Run Keyword If    ${result}==False    FAIL    Unable to reach ONL from PC-1 to Ubuntu

    Log To Console            Verify Ping operation from Ubuntu to PC-1
    ${result}=    Run Keyword and Continue On Failure   ping router    Ubuntu   ping    ${Host1_IP}
    Run Keyword If    ${result}==False    FAIL    Unable to reach VPCS from Ubuntu to PC-1

Check if OSPF neighbors are established
    Log To Console    Checking if OSPF neighbors are established
    :FOR    ${ELEMENT}    IN RANGE   0   3
    \    ${neighbor}=    Create List    @{Devices}[${ELEMENT}]    show ip ospf neighbor
    \    Append To List    ${ospf_neighbor}    ${neighbor}

    ${result}=    Run Keyword and Continue On Failure    show ospf neighbor     ${ospf_neighbor}
    Run Keyword If    ${result}==False    FAIL    OSPF neighbors are not established in the routers

Check if BGP sessions are established
    Log To Console    Checking if all BGP sessions are established
    :FOR    ${ELEMENT}    IN RANGE   1   5
    \    ${bgp}=    Create List    @{Devices}[${ELEMENT}]    show ip bgp summary
    \    Append To List    ${bgp_summary}    ${bgp}

    ${result}=    Run Keyword and Continue On Failure    show bgp summary     ${bgp_summary}
    Run Keyword If    ${result}==False    FAIL    BGP sessions are not established in the routers

Ensure the VRF reachability between PE routers

    Log To Console            Verify VRF ping from PE router R2 to Host
    ${result}=    Run Keyword and Continue On Failure   ping vrf    R2    vrf1   ${Host2_IP}
    Run Keyword If    ${result}==False    FAIL    Unable to reach Host from VRF1
    Log To Console            Verify VRF ping from PE router R3 to Host
    ${result}=    Run Keyword and Continue On Failure   ping vrf    R3    vrf1   ${Host2_IP}
    Run Keyword If    ${result}==False    FAIL    Unable to reach Host from VRF1

Enable MPLS on PE and P routers
    Log To Console            Configure MPLS on PE router
    Log To Console            Configure MPLS on P router
    ${result}=    Run Keyword and Continue On Failure   ping vrf    R2    vrf1   ${Host2_IP}
    Run Keyword If    ${result}==False    FAIL    Unable to reach Host from VRF1
    Log To Console            Verify VRF ping from PE router R3 to Host
    ${result}=    Run Keyword and Continue On Failure   ping vrf    R3    vrf1   ${Host2_IP}
    Run Keyword If    ${result}==False    FAIL    Unable to reach Host from VRF1
