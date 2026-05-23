from selenium.webdriver.common.by import By


class DynamicPropertiesLocators:
    BUTTON_ENABLE_5S = (By.XPATH, "//button[@id='enableAfter']")
    BUTTON_COLOR_CHANGE = (By.XPATH, "//button[@id='colorChange']")
    BUTTON_VISIBLE = (By.XPATH, "//button[@id='visibleAfter']")
