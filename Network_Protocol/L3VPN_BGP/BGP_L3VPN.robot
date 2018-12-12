*** Settings ***

Metadata 	Version           1.0
...	        More Info         For more information about Robot Framework see http://robotframework.org
...             Author            Payal Jain
...             Date              19 Dec 2016
...	        Executed At  	  ${HOST}
...		Test Framework    Robot Framework Python

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


Resource          Resource.robot
Library         DebugLibrary
#Suite Setup       Setup Actions

<<<<<<< HEAD
#Suite Teardown    Teardown Actions

*** Test Cases ***

#Configure IP addresses as per the topology
#        Configure ip address
#
#Configure loopback interface as per the topology
#        Set loopback interface
#
#Configure OSPF within AS2 to advertise the connected networks
#        Enable OSPF in devices present in AS2 and set the ospf neighbors
#
Configure VRFs to PE routers
        Create and Assign VRFs to PE routers
#
#Configure MP-BGP on PE routers
#        Enable MP-BGP on PE routers
#
#Enable BGP Synchronisation
#       Enable synchronisation between border routers
#
#Configure MPLS on P and PE routers
#        Enable MPLS on PE and P routers
#
#Configure EBGP on customer routers
#        Enable EPGP on customer routers
#
#Configure EBGP towards customers on the PE routers
#        Enable EBGP towards customers on the PE routers
#
#Redistribute routes from OSPF into BGP
##            Redistribute routes from OSPF into BGP

#Redistribute connnected routes into BGP
#            Redistribute connnected routes into BGP
#
#Check if ip address is set and interface is up
#       Check if ip address is set and interface is up
#
#Check if OSPF neighbors are established
#       Check if OSPF neighbors are established
#
#Check if BGP sessions are established
#       Check if BGP sessions are established
#
#Ensure that different autonomous systems can communicate with each other
#       Ensure that different autonomous systems can communicate with each other
#
#Ensure the VRF reachability between PE routers
##       Ensure the VRF reachability between PE routers
=======
Suite Teardown    Teardown Actions

*** Test Cases ***

Configure IP addresses as per the topology
        Configure ip address

Configure loopback interface as per the topology
        Set loopback interface

Configure OSPF within AS2 to advertise the connected networks
        Enable OSPF in devices present in AS2 and set the ospf neighbors

Configure VRFs to PE routers
        Create and Assign VRFs to PE routers

Configure MP-BGP on PE routers
        Enable MP-BGP on PE routers

Enable BGP Synchronisation
       Enable synchronisation between border routers

Configure MPLS on P and PE routers
        Enable MPLS on PE and P routers

Configure EBGP on customer routers
        Enable EPGP on customer routers

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
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
