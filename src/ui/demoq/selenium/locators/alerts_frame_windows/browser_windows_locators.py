from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE_BUTTON = (By.XPATH, "//button[@id='messageWindowButton']")
    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    MESSAGE_NEW = (By.TAG_NAME, "body")
