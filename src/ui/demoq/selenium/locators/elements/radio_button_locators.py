from selenium.webdriver.common.by import By


class RadioButtonLocators:
    RADIO_BUTTON_YES = (By.XPATH, "//label[@for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.XPATH, "//label[@for='impressiveRadio']")
    RESULT = (By.XPATH, "//span[@class='text-success']")
