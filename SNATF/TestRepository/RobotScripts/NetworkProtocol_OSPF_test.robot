*** Settings ***
Documentation     Test Suite for router bgp functionalities
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Variables         ../Variables/NetworkProtocol_BGPvariables.py
Resource          ../../Framework/NetworkProtocol/BGP/bgp_service.robot


*** Variables ***
${cmds}  ifconfig
${match_dt}  hold time is 180, keepalive interval is 60 seconds
${match_mt}  hold time is 150, keepalive interval is 50 seconds
${match_nei}  BGP state = Established
${match_nadv}  ${NWK_ADV}/24
@{nei_l}  ${HOSTR2_INTF}   ${HOSTR3_INTF}
@{nei_el}  ${HOSTR2_INTF}   ${HOSTR3_INTF}   remote AS ${AS2}, local AS ${AS1}
@{nei_il}  ${HOSTR3_INTF}   remote AS ${AS1}, local AS ${AS1}
${cmd_sh_n3}  sudo vtysh -c 'show ip bgp neighbors ${HOSTR3_INTF}'
${cmd_lt}  sudo iperf3 -s
${cmd_it}  sudo iperf3 -c ${HOSTR2} -n ${TRSFR_TRFC}M -u
${match_trfc}  ${TRSFR_TRFC}.00 MBytes



*** Test Cases ***
Configure And Validate Router For BGP Neighbor
    [Documentation]    Connect to bgp router through ssh, Validate-Modify-ReValidate BGP Neighbor
    ${output}  Connection To Router  ${HOSTR1}  ${cmds}
    Refresh Neighbor Details On Router
    ${output}  Confirm No Neighbor On Router  ${match_nei}
    Add Neighbors On Router
    Sleep  ${SLEEP_TIME}
    ${output}  Validate Neighbor On Router  ${HOSTR1}  ${match_nei}  ${cmd_sh}  @{nei_l}



Configure And Validate Router For EBGP
    [Documentation]    Connect to bgp router through ssh, Validate-Modify-ReValidate EBGP
    ${output}  Connection To Router  ${HOSTR1}  ${cmds}
    Refresh Neighbor Details On Router
    ${output}  Confirm No Neighbor On Router  ${match_nei}
    Add Neighbors On Router
    Sleep  ${SLEEP_TIME}
    ${output}  Validate Neighbor On Router  ${HOSTR1}  ${match_nei}  ${cmd_sh}  @{nei_el}



Configure And Validate Router For IBGP
    [Documentation]    Connect to bgp router through ssh, Validate-Modify-ReValidate EBGP
    ${output}  Connection To Router  ${HOSTR1}  ${cmds}
    Refresh Neighbor Details On Router
    ${output}  Confirm No Neighbor On Router  ${match_nei}
    Add Internal Neighbors On Router
    Sleep  ${SLEEP_TIME}
    ${output}  Validate Neighbor On Router  ${HOSTR1}  ${match_nei}  ${cmd_sh_n3}  @{nei_il}
    Reset Neighbor
    Sleep  ${SLEEP_TIME}



Configure And Validate Router For BGP Network Advertisement
    [Documentation]    Connect to bgp router through ssh, Validate-Modify-ReValidate Network Advertisement
    ${output}  Connection To Router  ${HOSTR2}  ${cmds}
    Refresh Network Advertisement On Router
    ${output}  Confirm No Network Advertisement On Router  ${match_nadv}
    Add Network Advertisement On Router
    Sleep  ${SLEEP_TIME}
    ${output}  Validate Network Advertisement On Router  ${match_nadv}



Configure And Validate Router For BGP Timers
    [Documentation]    Connect to bgp router through ssh, Validate-Modify-ReValidate BGP Timer
    ${output}  Connection To Router  ${HOSTR1}  ${cmds}
    Refresh Timers Value On Router
    ${output}  Validate Default Timers Value On Router  ${match_dt}
    Modify Timers Value On Router
    ${output}  Validate Modified Timers Value On Router  ${match_mt}



Initiate And Validate Traffic To/From BGP Router
    [Documentation]    Initiate And Validate Traffic To/From BGP Router
    ${output}  Initiate And Validate Traffic  ${HOSTR1}  ${HOSTR2}  ${cmd_lt}  ${cmd_it}  ${match_trfc}
