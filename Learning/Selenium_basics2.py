from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.implicitly_wait(1)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Hello@1234")
driver.find_element(By.XPATH, '//button[text()="Save New Password"]').click()
assert driver.title == "Let's Shop"
sleep(2)