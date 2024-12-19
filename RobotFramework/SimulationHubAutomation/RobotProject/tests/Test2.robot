*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem

*** Test Cases ***
Clean Up Screenshots
    Remove Files    selenium-screenshot-*.png

Test Airline Support Office
    Open the browser with simulation hub url
    view HVAC CFD gallery
    Validate Simulations Display
    Open Airline Support Office
#    Validate the flow chart
#    Select charts
#    Validate the other workflows

*** Keywords ***
Open the browser with simulation hub url
    Open Browser    https://webapp.simulationhub.com/simulation-gallery    Chrome
    Maximize Browser Window
    Title Should Be    Simulation Gallery | simulationHub

view HVAC CFD gallery
    Sleep    5
    Click Element    xpath://a[contains(@href, 'simulation-gallery')]

Validate Simulations Display
    Wait Until Element Is Visible    css:.aspectRatio169    timeout=10s
    @{expectedList}=    Create List    Washington DC Cooling I Cooling Simulation    simulationHub Office    Burger Joint Case Study    ASHRAE Global Headquarters    Office Workspace HVAC Cooling Simulation    High School Pune HVAC Cooling Simulations    Manhattan Commercial Space    Airline Support Office    Crimson Anisha Global School    Commercial Bank    CCTech Office Pune    Conference Room study
    ${CardElements}=    Get Webelements    css:.aspectRatio169
    @{actualList}=    Create List

    FOR    ${element}    IN    @{CardElements}
        ${altText}=    Get Element Attribute    ${element}    alt
        Log    ${altText}
        Append To List    ${actualList}    ${altText}
    END
    Log    ${actualList}
    Lists Should Be Equal    ${expectedList}    ${actualList}

Open Airline Support Office
    Click Element    id:BLiEh8P
    sleep    5

#Validate the flow chart
#Select charts
#Validate the other workflows

