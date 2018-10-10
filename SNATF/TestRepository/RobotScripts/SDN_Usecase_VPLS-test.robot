*** Settings ***
Documentation     ssh into mininet vm
Suite Setup       Open Connection And Log In
Library           SSHLibrary
Library           String
Library           ../../Framework/SDN/SDN_Usecase_VPLS/Vpls
Library           Collections
Suite Teardown    Close All Connections


*** Variables ***
${HOST}                10.22.20.92
${controller}          10.22.20.143
${USERNAME}            shankar
${USERNAME1}           onos
${PASSWORD}            test123
${PASSWORD1}            rocks
${prompt}               mininet>
${controllerprompt}     onos>
${port}                 8101
${cmd_topo}             sudo mn --custom mininet/custom/simpletopo.py --topo=mytopo --controller=remote,ip=10.22.20.143

@{featurelist}           org.onosproject.drivers  org.onosproject.vpls  org.onosproject.openflow  org.onosproject.proxyarp  org.onosproject.mobility   org.onosproject.vpls

*** Test Cases ***

Execute custome topology Command And verify ping response on mininet vm
    [Documentation]    login to mininet vm and run the custom topology and test ping response initially unreachable on all hosts.
    ...                This behaviour can be adjusted as Execute Command arguments.
    #write   ${cmd_topo}  # return_stdout=True    return_rc=True
    #read until   ${prompt}
    write       pingall
    sleep       40s
    ${rc}   read until   ${prompt}
    set suite variable  ${rc}
    log     ${rc}
    Should Contain       ${rc}    100% dropped

Login to ONOS VM and activate the required feature
    [Documentation]  ensure ONOS process is running and run login to vm and  configure the interfaces identified by mininet topology
    open connection     ${controller}      port=8101
    login       onos  rocks
    #write  apps -s -a
    write   hosts
    ${test}  read until  ${controllerprompt}
    log     ${test}

    set suite variable  ${test}
    :FOR   ${ELEMENT}  IN   @{featurelist}
    \    write   app activate ${ELEMENT}

    log     apps ${featurelist} activated

configure interfaces and vlan of identified hosts from mininet
    @{output}  configure interface     ${test}
    : FOR    ${i}    IN    @{output}
    \    write    ${i}
    \    sleep    5s
    log many  @{output}

Create vpls instance with name "VPLS"
    : FOR  ${k}      IN RANGE  0  2
    \   write   vpls create VPLS
    @{addhosts}   create vpls

    : FOR    ${j}    IN    @{addhosts}
    \    write    ${j}
    \    sleep    1s

Add encapsulation to created vpls instance and verify flows

    write   vpls set-encap VPLS MPLS
    sleep   10s
    ${flows}   write   flows
    #${flows}    read until     ${prompt}
    log      ${flows}
    #should contain     ${flows}     MPLS_LABEL


verify ping in mininet
    switch connection   ${connect1}
    #Open Connection    ${HOST}
    #login    ${USERNAME}    ${PASSWORD}
    #read until   ${prompt}
    write       pingall
    sleep       40s
    ${mc}   read until   ${prompt}
    log     ${mc}
    Should not Contain       ${mc}    100% dropped


*** Keywords ***
Open Connection And Log In
   ${connect1}=  Open Connection    ${HOST}
   login    ${USERNAME}    ${PASSWORD}
   write   ${cmd_topo}  # return_stdout=True    return_rc=True
   read until   ${prompt}
   set suite variable  ${connect1}




Close All Connections
    close connection

vpls import functions
    controller feature list
    configure interface
    create vpls
    add encap
























