from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

# Close login popup if it appears
try:
    close_btn = driver.find_element(By.CSS_SELECTOR, 'button._2KpZ6l._2doB4z')
    close_btn.click()
except:
    pass


driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("iphone")

wait = WebDriverWait(driver, 15)
suggestions = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[@class="_3D0G9a"]'))
)
print(f"Found {len(suggestions)} suggestions")
for suggestion in suggestions:
    if "iphone 16" in suggestion.text.lower():
        wait.until(EC.element_to_be_clickable(suggestion)).click()
        break

sleep(5)
driver.quit()



