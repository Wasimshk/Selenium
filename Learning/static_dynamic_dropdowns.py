from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.CSS_SELECTOR, "input#autosuggest").send_keys("ind")
driver.implicitly_wait(1)
countries = driver.find_elements(By.XPATH, '//li[@class="ui-menu-item"]')


# handle dynamic drop down
for country in countries:
    if country.text == 'India':
        country.click()
        break
# get value of the filled text box
assert driver.find_element(By.CSS_SELECTOR, "input#autosuggest").get_attribute("value") == "India"
sleep(2)


# # handle static dropdown
# selectObj = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# selectObj.select_by_visible_text("Female")
# selectObj.select_by_index(0)
# # selectObj.select_by_value()