from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# handle Checkbox
checkboxes = driver.find_elements(By.CSS_SELECTOR, 'fieldset input[type="checkbox"]')
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        checkbox.is_selected()
        break

# handle radiobutton
radioButtons = driver.find_elements(By.CSS_SELECTOR, "fieldset input[class='radioButton']")
for button in radioButtons:
    if button.get_attribute("value") == "radio2":
        button.click()
        button.is_selected()
        break

# visibility checks
driver.find_element(By.XPATH, '//*[@value="Hide"]').click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.XPATH, '//*[@value="Show"]').click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()


# handle alert boxes
# accept the dialog
driver.find_element(By.ID, "name").send_keys("Wasim")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# dismiss(click on cancel button)
driver.find_element(By.ID, "confirmbtn").click()
confirmDialog = driver.switch_to.alert
print(confirmDialog.text)
confirmDialog.dismiss()


