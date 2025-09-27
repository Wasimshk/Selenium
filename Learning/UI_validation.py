from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("Ber")

products = driver.find_elements(By.XPATH, '//div[@class="product"]')

for product in products:
    product.find_element(By.XPATH, 'div/button').click()

#    to check if the added item in card matches
# print(driver.find_element(By.XPATH, '//tr/td[text()="Items"]/following-sibling::td/strong').text)

driver.find_element(By.CSS_SELECTOR, '[alt="Cart"]').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

sleep(2)
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 15)

assert wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[contains(text(), "Code applied")]')))

# find the total column and sum the total amount and match with the actual total amount
columns = driver.find_elements(By.XPATH, "//thead/tr/td")

index = 1
for column in columns:
    if column.text == "Total":
        break
    index += 1

items = driver.find_elements(By.XPATH, "//tbody/tr")

calculated_sum = 0
for item in items:
    price_text = item.find_element(By.XPATH, f"./td[{index}]").text
    price = int(price_text)
    calculated_sum += price

print(calculated_sum)
actual_sum = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
print(actual_sum)

assert actual_sum == calculated_sum
