from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# switch to frame
driver.switch_to.frame("courses-iframe") #pass the id of the iframe tag
driver.find_element(By.LINK_TEXT, "Courses").click()

# switch back to main page
driver.switch_to.default_content()
driver.find_element(By.ID, "alertbtn").click()
alertbox = driver.switch_to.alert
print(alertbox.text)
alertbox.accept()
sleep(1)



