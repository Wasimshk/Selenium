from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
dropdown = Select(driver.find_element(By.ID, "page-menu"))
driver.find_element(By.ID, "page-menu").click()
dropdown.select_by_value("20")
driver.find_element(By.XPATH, '//*[text() ="Veg/fruit name"]').click()


# check the sort functionality of a web table
items = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
item_list = []
for item in items:
    item_list.append(item.text)
assert item_list == sorted(item_list)