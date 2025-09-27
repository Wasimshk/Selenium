from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# #//////////////// Old\with driver exe: ////////////////////////////////////////////////////
# # chrome driver
# from selenium.webdriver.chrome.service import Service
# serviceobj = Service("path/to/chrome/driver.exe")
# driver = webdriver.chrome(service=serviceobj)
#
# # edge driver
# from selenium.webdriver.edge.service import Service
# serviceobj = Service("path/to/msedge/driver.exe")
# driver = webdriver.edge(service=serviceobj)
#
# # firefox
# from selenium.webdriver.firefox.service import Service
# serviceobj = Service("path/to/gecko/driver.exe")
# driver = webdriver.firefox(service=serviceobj)


# //////////////// New\without driver exe: ///////////////////////////////////////////////////
driver = webdriver.Chrome() #this will invoke the browser
# driver = webdriver.Edge()
# driver = webdriver.Firefox()

# //////////////// goto url and validate title and url ///////////////////////////////////////////////////
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title) #gets the page title
print(driver.current_url) #gets the current url


# //////////////// locators ///////////////////////////////////////////////////
# ID, NAME, CLASS_NAME, TAG_NAME, XPATH, CSS_SELECTOR, LINK_TEXT, PARTIAL_LINK_TEXT
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.NAME, "name").send_keys("Wasim")

# Static Dropdown
selectObj = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
selectObj.select_by_visible_text("Female")
selectObj.select_by_index(0)
# selectObj.select_by_value()

driver.find_element(By.CLASS_NAME, "btn-success").click()
message = driver.find_element(By.XPATH, '//*[@class="alert alert-success alert-dismissible"]').text
assert "Success!" in message
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys("Wasim Shaikh")
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()


















sleep(2)
driver.close()