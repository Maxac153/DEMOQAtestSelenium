from selenium.webdriver.common.by import By


class SliderPageLocators:
    SLIDER = (By.XPATH, "//input[contains(@class, 'range-slider')]")
    SLIDER_VALUE = (By.XPATH, "//input[@id='sliderValue']")
