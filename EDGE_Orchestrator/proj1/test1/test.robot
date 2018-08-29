*** Settings ***
Documentation     Test EDGE Scenarios
Library           OperatingSystem
Library           Collections
Library           random
Library           add_all_flows.py
Library           ovsconnect.py
Library           dia_test.py
Library           gre_test.py
Library           mpls_test.py
Library           driversetup.py

*** Test Cases ***
OPENSTACK - Validate EDGE Scenarios: Log in test
    [Documentation]    Login Test on EDGE
    Log In

OPENSTACK - Validate EDGE Scenarios: Dia flow test
    [Documentation]    DIA flow Test on EDGE
    Dia Test
    
OPENSTACK - Validate EDGE Scenarios: Gre flow test
    [Documentation]    GRE flow Test on EDGE
    Gre Test
    
OPENSTACK - Validate EDGE Scenarios: MPLS flow test
    [Documentation]    MPLS flow Test on EDGE
    MPLS Test
    
OPENSTACK - Validate EDGE Scenarios: All flows test
    [Documentation]    All Tests Flow Test on EDGE
    Add All Flows
   
OPENSTACK - Validate EDGE Scenarios: Close Driver test
    [Documentation]    Close driver Test on EDGE
    Close Webdriver