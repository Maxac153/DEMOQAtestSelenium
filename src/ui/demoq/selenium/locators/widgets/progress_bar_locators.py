from selenium.webdriver.common.by import By


class ProgressBarLocators:
    PROGRESS_BAR_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[role='progressbar']")
