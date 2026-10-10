import random
from typing import List

import allure
from selenium.webdriver.common.keys import Keys

from src.ui.demoq.__common.generator.generator import generated_color
from src.ui.demoq.selenium.locators.widgets.auto_complete_locators import AutoCompleteLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class AutoCompletePage(BasePage):
    @allure.step("Заполнить multi autocomplete случайными цветами")
    def fill_input_multi(self) -> List[str]:
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))

        for color in colors:
            input_multi = self.element_is_clickable(AutoCompleteLocators.MULTI_INPUT)
            input_multi.click()
            input_multi.clear()
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)

        return colors

    @allure.step("Удалить первое значение из multi autocomplete")
    def remove_value_from_multi(self) -> tuple[int, int]:
        self.wait_element_present(AutoCompleteLocators.MULTI_VALUE)
        count_before = len(self.wait_elements_present(AutoCompleteLocators.MULTI_VALUE))
        remove_buttons = self.wait_elements_visible(AutoCompleteLocators.MULTI_VALUE_REMOVE)
        remove_buttons[0].click()
        count_after = len(self.wait_elements_present(AutoCompleteLocators.MULTI_VALUE))

        return count_before, count_after

    @allure.step("Получить выбранные цвета из multi autocomplete")
    def check_color_in_multi(self) -> List[str]:
        self.wait_element_present(AutoCompleteLocators.MULTI_VALUE_LABEL)
        labels = self.wait_elements_visible(AutoCompleteLocators.MULTI_VALUE_LABEL)

        return [label.text.strip() for label in labels]

    @allure.step("Заполнить single autocomplete случайным цветом")
    def fill_input_single(self) -> str:
        color = random.sample(next(generated_color()).color_name, k=1)[0]
        input_single = self.element_is_clickable(AutoCompleteLocators.SINGLE_INPUT)
        input_single.click()
        input_single.clear()
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)

        return color

    @allure.step("Получить выбранный цвет из single autocomplete")
    def get_color_in_single(self) -> str:
        single_value = self.wait_element_visible(AutoCompleteLocators.SINGLE_VALUE)

        return single_value.text.strip()
