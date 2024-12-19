*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Email}    wasim.shaikh@cctech.co.in
${ErrorMessageLoginLocator}    xpath://span[text()="Invalid email"]

*** Test Cases ***
Validate Unsuccessful Login
    Open the browser with simulation hub url
    Click login button and add email
    Wait until it checks EmailID and display error
    Verify error message

*** Keywords ***
Open the browser with simulation hub url
    Open Browser    https://webapp.simulationhub.com/simulation-gallery    Chrome
    Maximize Browser Window
    Title Should Be    Simulation Gallery | simulationHub

Click login button and add email
    Click Button    xpath:(/l'/button[contains(@class, 'btn-materia)])[1]
    Wait Until Element Is Visible    xpath://*[@class='ui header']    timeout=10s
    Input Text    id:l_email    ${Email}
    Click Button    id:btn_get_user

Wait until it checks EmailID and display error
    Wait Until Element Is Visible    ${ErrorMessageLoginLocator}

Verify error message
    Element Text Should Be    ${ErrorMessageLoginLocator}    Invalid email