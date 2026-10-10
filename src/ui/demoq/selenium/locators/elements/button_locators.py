from selenium.webdriver.common.by import By


class ButtonLocators:
    DOUBLE_CLICK_ME_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_ME_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    DOUBLE_CLICK_ME_RESULT = (By.XPATH, "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_ME_RESULT = (By.XPATH, "//p[@id='rightClickMessage']")
    CLICK_ME_RESULT = (By.XPATH, "//p[@id='dynamicClickMessage']")
