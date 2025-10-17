from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("iphone")


# ///////////////////////////////////////////////////////////////////////
# ways to wait for an element
# 1. implicit wait or direct hardcoded wait
driver.implicitly_wait(10)
# sleep(10) not recommended
suggestions = driver.find_elements(By.XPATH, '//li[@class="_3D0G9a"]')
print(f"Found {len(suggestions)} suggestions")

# ///////////////////////////////////////////////////////////////////////
# 2.Manual wait loop until suggestions load
suggestions = None
for i in range(10):  # retry for ~10 seconds
    suggestions = driver.find_elements(By.XPATH, '//li[@class="_3D0G9a"]')
    if len(suggestions) > 0:
        break
    sleep(1)
print(f"Found {len(suggestions)} suggestions")

# ///////////////////////////////////////////////////////////////////////
# 3.using webdriverwait and expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 15)
suggestions = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[@class="_3D0G9a"]'))
)
print(f"Found {len(suggestions)} suggestions")

# ///////////////////////////////////////////////////////////////////////
# 4. Explicit Wait with Custom Lambda (no EC)
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 15)
suggestions = wait.until(
    lambda d: d.find_elements(By.XPATH, '//li[@class="_3D0G9a"]')
)


