.. code:: robotframework

    *** Settings ***
    Library     lib/VyosLibrary.py

    *** Variables ***
    ${VYOS1}                192.168.56.102
    ${VYOS2}                192.168.56.101
    ${UNREACHABLE_HOST1}    192.168.56.103
    ${UNREACHABLE_HOST2}    google.com
    ${USER}                 kelaves

    *** Test Cases ***
    Vyos should be reachable from host
        Host Vyos Ping      ${VYOS1}
        Host Vyos Ping      ${VYOS2}   
    
    Vyos should be able to reach each other
        Vyos Ping       ${VYOS1}    ${USER}    ${VYOS2}
        Vyos Ping       ${VYOS2}    ${USER}    ${VYOS1}

    Vyos should not connect to out of reach host
        Run Keyword And Expect Error    *   Vyos Ping       ${VYOS1}    ${USER}   ${UNREACHABLE_HOST1}
        Run Keyword And Expect Error    *   Vyos Ping       ${VYOS1}    ${USER}   ${UNREACHABLE_HOST2}
        Run Keyword And Expect Error    *   Vyos Ping       ${VYOS2}    ${USER}   ${UNREACHABLE_HOST1}
        Run Keyword And Expect Error    *   Vyos Ping       ${VYOS2}    ${USER}   ${UNREACHABLE_HOST2}