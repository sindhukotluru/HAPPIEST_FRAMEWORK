*** Settings ***

Metadata        Version           1.0
...             More Info         For more information about Robot Framework see http://robotframework.org
...             Author            Payal Jain
...             Date              19 Dec 2016
...             Executed At       ${HOST}
...             Test Framework    Robot Framework Python

Documentation   A test suite with tests for configuring BGP.

...             Topology:-
...                          ____________________________
...                         |             R1         AS2 |
...                         |            /  \            |
...                         |           /    \           |
...                         |         R2------ R3         |
...                         |_________|________|_________|
...                                   |        |
...                             ______|__   ___|______
...                            |      AS1| |       AS3|
...                            |    R4   | |   R5     |
...                            |_________| |__________|


Resource         ../libraries/Resource.robot
Library         DebugLibrary
#Suite Setup       Setup Actions

#Suite Teardown    Teardown Actions

*** Test Cases ***

Configure IP addresses as per the topology
       Ensure that different autonomous systems can communicate with each other
        Configure ip address

Configure loopback interface as per the topology
        Set loopback interface

Configure OSPF within AS2 to advertise the connected networks
        Enable OSPF in devices present in AS2 and set the ospf neighbors

Configure VRFs to PE routers
        Create and Assign VRFs to PE routers

Configure MP-BGP on PE routers
        Enable IBGP and advertise the updates from the loopback interface
        Establish route between R2 and R3
        Enable MP-BGP on PE routers

Enable BGP Synchronisation
       Enable synchronisation between border routers

Configure MPLS on PE and P routers
        Enable MPLS on PE and P routers

Configure EBGP on customer routers
       Enable BGP on customer routers

Configure EBGP towards customers on the PE routers
        Enable EBGP towards customers on the PE routers

Redistribute routes from OSPF into BGP
       Redistribute routes from OSPF into BGP

Redistribute connnected routes into BGP
       Redistribute connnected routes into BGP

Check if ip address is set and interface is up
       Check if ip address is set and interface is up

Check if OSPF neighbors are established
       Check if OSPF neighbors are established

Check if BGP sessions are established
       Check if BGP sessions are established

Ensure that different autonomous systems can communicate with each other
       Ensure that different autonomous systems can communicate with each other

Ensure the VRF reachability between PE routers
       Ensure the VRF reachability between PE routers
