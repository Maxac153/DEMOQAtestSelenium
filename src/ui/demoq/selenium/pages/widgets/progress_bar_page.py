import random
import time

import allure

from src.ui.demoq.selenium.locators.widgets.progress_bar_locators import ProgressBarLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class ProgressBarPage(BasePage):
    @allure.step("change progress bar value")
    def change_progress_bar_value(self):
        value_before = self.element_is_present(ProgressBarLocators().PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(ProgressBarLocators().PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(4, 6))
        progress_bar_button.click()
        value_after = self.element_is_present(ProgressBarLocators().PROGRESS_BAR_VALUE).text

        return value_before, value_after