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
...                         |         R2      R3         |
...                         |_________|________|_________|
...                                   |        |
...                             ______|__   ___|______
...                            |      AS1| |       AS3|
...                            |    R4   | |   R5     |
...                            |_________| |__________|

...               Testplan Goals:-
...               1. Configure IP addresses as per the topology.
...               2. Each Router should have a loopback0 interface.
...               3. Configure OSPF within AS2 to advertise the loopback0 interfaces.
...                  Don't advertise or run OSPF on the links interconnecting AS1 and AS3.
...               4. Configure IBGP between R2 and R3. Source the BGP updates from the loopback0 interfaces.
...               5. Enable BGP synchronisation.
...               6. Configure EBGP between R2 and R4.
...               7. Configure EBGP between R3 and R5.
...               8. Advertise the loopback0 interfaces on R4 and R5.
...               9. Ensure AS1 and AS3 can communicate with each other without removing the BGP synchronisation command.

Resource         ../libraries/Netconf_resource.robot
Library          DebugLibrary
#Suite Setup     Setup Actions
#Suite Teardown    Teardown Actions

*** Test Cases ***

Configure IP addresses as per the topology
        Configure ip address

#Configure SSH V2
      # Configure SSH V2

Configure Netconf with SSH V2
       Enabling SSH Version 2 Using a Hostname

#Verify Encrypted Session with a Remote Device
 #      Starting Encrypted Session with a Remote Device
 
