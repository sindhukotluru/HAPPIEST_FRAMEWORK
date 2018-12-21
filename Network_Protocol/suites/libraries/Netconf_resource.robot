*** Settings ***
Documentation     Resource file containing all the PYTHON API implementations.
Library           Collections
#ibrary           ../../libraries/setup_actions.py
Library           ../../libraries/netconf_config.py
Library           ../../libraries/Netconf_Device.py

Variables         ../../config/variable.py


*** Keywords ***


Configure ip address

    Log To Console            Configuring IP_Address
    ${load_device_R6}=    R6    ${Links_R6}    configure
    ${result}=    Run Keyword and Continue On Failure    start configure     ${load_device_R6}
    Run Keyword If    ${result}==False    FAIL    IP address configuration failed
    Log To Console            IP_Address configured on Netconf Router



Enabling SSH Version 2 Using a Hostname

   Log To Console             Configure Netconf  SSH V2
   ${load_device_R6}=    Create List    R6    ${Links_R6}    configure
   ${result}=    Run Keyword and Continue On Failure    start configure     ${load_device_R6}
   Run Keyword If    ${result}==False    FAIL    Netconf server configuration failed
   Log To Console            Netconf server configured on Router




