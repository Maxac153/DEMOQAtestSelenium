from selenium.webdriver.common.by import By


class SliderLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")
