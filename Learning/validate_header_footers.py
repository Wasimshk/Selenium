'''
Scenario - validate header and footers in every page of the web application

the best practice approach — creating a Base Page class (following the Page Object Model) that contains reusable validations.
This way, every page object you create will inherit from the base class, and before/after performing page-specific validations, you can automatically check the header and footer.
🏗️ How It Works
BasePage class
Keeps common methods like validate_header(), validate_footer(), and utility wrappers (click, is_visible, etc.).
Child Page classes (HomePage, AboutPage, etc.)
Inherit from BasePage.
When initialized, they automatically call header/footer validations.
Tests
Your test just creates a HomePage(driver) or ContactPage(driver).
The constructor runs header/footer validation behind the scenes.

'''



from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.validate_header()
        self.validate_footer()

    # ---- Locators ----
    HEADER_LOGO = (By.CSS_SELECTOR, "header .logo")
    HEADER_NAV = (By.CSS_SELECTOR, "header nav")
    FOOTER_COPYRIGHT = (By.CSS_SELECTOR, "footer .copyright")
    FOOTER_LINKS = (By.CSS_SELECTOR, "footer a")

    # ---- Common Validations ----
    def validate_header(self):
        assert self.driver.find_element(*self.HEADER_LOGO).is_displayed(), "Header logo missing"
        assert self.driver.find_element(*self.HEADER_NAV).is_displayed(), "Header navigation missing"
        print("✅ Header validated")

    def validate_footer(self):
        assert self.driver.find_element(*self.FOOTER_COPYRIGHT).is_displayed(), "Footer copyright missing"
        links = self.driver.find_elements(*self.FOOTER_LINKS)
        assert len(links) > 0, "No footer links found"
        print("✅ Footer validated")


# Example: Home Page inheriting from BasePage
class HomePage(BasePage):
    WELCOME_TEXT = (By.CSS_SELECTOR, ".welcome-text")

    def __init__(self, driver):
        super().__init__(driver)  # ✅ validates header & footer
        assert self.driver.find_element(*self.WELCOME_TEXT).is_displayed(), "Welcome text missing"
        print("✅ Home Page specific validation done")


# Example Test
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

home = HomePage(driver)  # automatically validates header, footer, and page-specific element

driver.quit()