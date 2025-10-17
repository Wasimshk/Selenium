from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() #close the focused window
driver.switch_to.window(opened_windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
sleep(2)

# open a new window (blank window)
driver.switch_to.new_window()
driver.get("https://the-internet.herokuapp.com")
sleep(2)
driver.close()
sleep(1)