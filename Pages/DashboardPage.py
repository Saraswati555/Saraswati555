from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebLocators.WebLocators import WebLocators

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def verify_dashboard(self):
        dashboard_text = self.wait.until(EC.visibility_of_element_located(WebLocators.DASHBOARD)).text
        return dashboard_text == "Dashboard"
