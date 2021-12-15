.. code:: robotframework

    *** Settings ***
    Library  lib/ConfigureLibrary.py

    *** Variables ***
    ${USERNAME}  kelaves
    ${VYOS2}     192.168.56.101
    ${VYOS1}     192.168.56.102
    ${COMMANDS}  set interfaces ethernet eth0 description tchutchucao     
    
    *** Test Cases ***
    Valid host and user should connect
        Check Connection  ${VYOS1}  ${USERNAME}
        Check Connection  ${VYOS2}  ${USERNAME}

    Configure network adapters in connected vyos
        Send Configuration      ${VYOS1}    ${USERNAME}    ${COMMANDS}
        Send Configuration      ${VYOS2}    ${USERNAME}    ${COMMANDS}


       
    
        



