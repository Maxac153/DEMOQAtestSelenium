import allure

from src.ui.demoqa.__common.models.elements.radio_button import RadioButton
from src.ui.demoqa.playwright.locators.elements.radio_button_locators import RadioButtonLocators
from src.ui.demoqa.playwright.pages.__common.base_page import BasePage


class RadioButtonPage(BasePage):
    RADIO_BUTTONS = {
        RadioButton.YES: RadioButtonLocators.RADIO_BUTTON_YES,
        RadioButton.IMPRESSIVE: RadioButtonLocators.RADIO_BUTTON_IMPRESSIVE,
    }

    @allure.step("Выбор Radio Button")
    def radio_button_click(self, radio_button: RadioButton) -> str:
        selector = self.RADIO_BUTTONS[radio_button]
        self.page.locator(selector).click()

        return self.page.locator(RadioButtonLocators.RESULT).inner_text()
