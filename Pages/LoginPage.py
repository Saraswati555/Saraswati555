from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebLocators.WebLocators import WebLocators
from TestData.TestData import TestData


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.wait.until(EC.visibility_of_element_located(WebLocators.USERNAME)).send_keys(TestData.USERNAME)
        self.driver.find_element(*WebLocators.PASSWORD).send_keys(TestData.PASSWORD)
        self.driver.find_element(*WebLocators.LOGIN).click()

    def login_invalid(self):
        self.wait.until(EC.visibility_of_element_located(WebLocators.USERNAME)).send_keys(TestData.USERNAME)
        self.driver.find_element(*WebLocators.PASSWORD).send_keys(TestData.INVALID_PASSWORD)
        self.driver.find_element(*WebLocators.LOGIN).click()

    def verify_invalid_login(self):
        error_message = self.wait.until(EC.visibility_of_element_located(WebLocators.INVALID_LOGIN)).text
        return error_message == TestData.INVALID_TEXT
