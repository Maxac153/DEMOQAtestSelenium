import allure

from src.ui.demoqa.__common.models.elements.radio_button import RadioButton
from src.ui.demoqa.selenium.locators.elements.radio_button_locators import RadioButtonLocators
from src.ui.demoqa.selenium.pages.__common.base_page import BasePage


class RadioButtonPage(BasePage):
    @allure.step("Выбор Radio Button")
    def radio_button_click(self, radio_button_enum: RadioButton) -> str:
        if radio_button_enum == RadioButton.YES:
            self.element_is_visible(RadioButtonLocators.RADIO_BUTTON_YES).click()

        if radio_button_enum == RadioButton.IMPRESSIVE:
            self.element_is_visible(RadioButtonLocators.RADIO_BUTTON_IMPRESSIVE).click()

        return self.element_is_visible(RadioButtonLocators.RESULT).text
