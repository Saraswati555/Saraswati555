from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from WebLocators.WebLocators import WebLocators
from TestData.TestData import TestData


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(WebLocators.PIM_MODULE)).click()

    def add_employee(self):
        self.wait.until(EC.element_to_be_clickable(WebLocators.ADD_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(WebLocators.EMPLOYEE_FIRSTNAME)).send_keys(TestData.FIRST_NAME)
        self.driver.find_element(*WebLocators.EMPLOYEE_LASTNAME).send_keys(TestData.LAST_NAME)

        employee_id_field = self.driver.find_element(*WebLocators.EMPLOYEE_ID)
        employee_id_field.send_keys(Keys.CONTROL + "a")
        employee_id_field.send_keys(Keys.DELETE)
        employee_id_field.send_keys(TestData.EMPLOYEE_ID_NO)

        self.driver.find_element(*WebLocators.SAVE_BUTTON).click()

    def search_employee(self, employee_name):
        employee_search = self.wait.until(EC.visibility_of_element_located(WebLocators.EMPLOYEE_SEARCH))
        employee_search.send_keys(employee_name)
        time.sleep(2)  # Allow time for search results to populate

    def click_edit_button(self):
        try:
            edit_button = self.wait.until(EC.element_to_be_clickable(WebLocators.EDIT_BUTTON))
            edit_button.click()
        except Exception as e:
            edit_button = self.wait.until(EC.presence_of_element_located(WebLocators.EDIT_BUTTON))
            self.driver.execute_script("arguments[0].click();", edit_button)

    def edit_employee_id(self):
        employee_id_field = self.wait.until(EC.visibility_of_element_located(WebLocators.EMPLOYEE_ID))
        employee_id_field.send_keys(Keys.CONTROL + "a")
        employee_id_field.send_keys(Keys.DELETE)
        employee_id_field.send_keys(TestData.UPDATED_EMPLOYEE_ID_NO)

        self.driver.find_element(*WebLocators.SAVE_BUTTON).click()

    def verify_employee_id_update(self):
        updated_id = self.wait.until(EC.visibility_of_element_located(WebLocators.EMPLOYEE_ID)).get_attribute("value")
        return updated_id == TestData.UPDATED_EMPLOYEE_ID_NO
