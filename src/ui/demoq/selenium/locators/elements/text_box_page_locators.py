from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT = (By.XPATH, "//button[@id='submit']")
    NAME_RESULT = (By.CSS_SELECTOR, "#name")
    EMAIL_RESULT = (By.CSS_SELECTOR, "#email")
    CURRENT_ADDRESS_RESULT = (By.XPATH, "//p[@id='currentAddress']")
    PERMANENT_ADDRESS_RESULT = (By.XPATH, "//p[@id='permanentAddress']")
