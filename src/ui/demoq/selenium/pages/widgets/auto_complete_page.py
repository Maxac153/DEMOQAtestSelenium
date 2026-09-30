import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.generator.generator import generated_color
from src.ui.demoq.selenium.locators.widgets.auto_complete_locators import AutoCompleteLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class AutoCompletePage(BasePage):
    @allure.step("fill multi autocomplete input")
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))

        for color in colors:
            input_multi = self.element_is_clickable(AutoCompleteLocators.MULTI_INPUT)
            input_multi.click()
            input_multi.clear()
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)

        return colors

    @allure.step("remove value form multi autocomplete")
    def remove_value_from_multi(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located(AutoCompleteLocators.MULTI_VALUE))
        count_value_before = len(self.elements_are_present(AutoCompleteLocators.MULTI_VALUE))
        remove_buttons = self.elements_are_visible(AutoCompleteLocators.MULTI_VALUE_REMOVE)
        remove_buttons[0].click()

        count_value_after = len(self.elements_are_present(AutoCompleteLocators.MULTI_VALUE))

        return count_value_before, count_value_after

    @allure.step("check colors in multi autocomplete")
    def check_color_in_multi(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located(AutoCompleteLocators.MULTI_VALUE_LABEL))

        labels = self.elements_are_visible(AutoCompleteLocators.MULTI_VALUE_LABEL)
        return [label.text.strip() for label in labels]

    @allure.step("fill single autocomplete input")
    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)[0]

        input_single = self.element_is_clickable(AutoCompleteLocators.SINGLE_INPUT)
        input_single.click()
        input_single.clear()
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)

        return color

    @allure.step("check color in single autocomplete")
    def check_color_in_single(self):
        wait = WebDriverWait(self.driver, 10)
        single_value = wait.until(
            ec.visibility_of_element_located(AutoCompleteLocators.SINGLE_VALUE)
        )
        return single_value.text.strip()
