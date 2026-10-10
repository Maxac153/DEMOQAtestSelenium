import allure

from src.ui.demoq.selenium.locators.widgets.progress_bar_locators import ProgressBarLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class ProgressBarPage(BasePage):
    @allure.step("Запустить прогресс-бар, дождаться 100% и получить значения до и после")
    def change_progress_bar_value(self) -> tuple[str, str]:
        value_before = self.element_is_present(ProgressBarLocators().PROGRESS_BAR_VALUE).text
        self.element_is_clickable(ProgressBarLocators().PROGRESS_BAR_BUTTON).click()
        self.wait_for_attribute_value(
            locator=ProgressBarLocators().PROGRESS_BAR_VALUE,
            attribute="aria-valuenow",
            expected_value="100",
            timeout=60,
        )
        value_after = self.element_is_present(ProgressBarLocators().PROGRESS_BAR_VALUE).text

        return value_before, value_after
