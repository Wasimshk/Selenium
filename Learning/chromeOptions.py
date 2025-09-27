from selenium import webdriver
from selenium.webdriver.common.by import By

# customize chrome automation execution
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless") #will run automation in headless mode
chrome_option.add_argument("--ignore-certificate-errors") #by passing this flag script will handle the restrictions

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
