from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# implicit wait
driver.implicitly_wait(5)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# explicit wait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Top")))
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
sleep(2)

# all actions
# action.double_click()
# action.move_to_element()
# action.context_click()
# action.click_and_hold()
# action.drag_and_drop()