import random
import time

import allure

from src.ui.demoq.selenium.locators.widgets.slider_locators import SliderLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class SliderPage(BasePage):
    @allure.step("Изменение значения слайдера")
    def change_slider_value(self):
        value_before = self.element_is_visible(SliderLocators.SLIDER_VALUE).get_attribute("value")
        slider_input = self.element_is_visible(SliderLocators.INPUT_SLIDER)
        # TODO переделать на неявное ожидание, почему он не дожидается изменения значения
        time.sleep(1)
        self.action_drag_and_drop_by_offset(slider_input,random.randint(26, 100),0)
        value_after = self.element_is_visible(SliderLocators.SLIDER_VALUE).get_attribute("value")

        return value_before, value_after
