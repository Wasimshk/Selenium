from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# driver.get("https://www.redbus.in/")
# driver.find_element(By.CLASS_NAME, "doj___e69938").click()

driver.get("https://formy-project.herokuapp.com/datepicker")
driver.find_element(By.XPATH, '//*[@id="datepicker"]').click()
driver.implicitly_wait(1)
driver.find_element(By.XPATH, '//td[@class="today active day"]').click()
sleep(5)

