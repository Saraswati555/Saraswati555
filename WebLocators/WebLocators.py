from selenium.webdriver.common.by import By

class WebLocators:
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    LOGIN = (By.XPATH, '//button[@type="submit"]')
    DASHBOARD = (By.XPATH, '//div[1]/span/h6')
    INVALID_LOGIN = (By.XPATH, '//div[1]/p')

    PIM_MODULE = (By.XPATH, '//li[@class="oxd-main-menu-item-wrapper"][2]//a')
    ADD_BUTTON = (By.XPATH, '//div[@class="orangehrm-header-container"]//button')
    EMPLOYEE_SEARCH = (By.XPATH, '//div[contains(@class,"oxd-autocomplete-wrapper")]//input')
    EDIT_BUTTON = (By.XPATH, '//button[contains(@class,"oxd-button--secondary") and contains(text(), "Edit")]')
    EMPLOYEE_FIRSTNAME = (By.XPATH, '//input[@name="firstName"]')
    EMPLOYEE_LASTNAME = (By.XPATH, '//input[@name="lastName"]')
    EMPLOYEE_ID = (By.XPATH, '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]//input[@class="oxd-input oxd-input--active"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
