from src.ui.demoq.selenium.locators.radio_button_locators import RadioButtonLocators
from src.ui.demoq.selenium.modules.radio_button import RadioButton
from src.ui.demoq.selenium.pages.base_page import BasePage


class RadioButtonPage(BasePage):
    def radio_button_click(self, radio_button_enum: RadioButton) -> str:
        """Нажатие на определённый radio button"""

        if radio_button_enum == RadioButton.YES:
            self.element_is_visible(RadioButtonLocators.RADIO_BUTTON_YES).click()

        if radio_button_enum == RadioButton.IMPRESSIVE:
            self.element_is_visible(RadioButtonLocators.RADIO_BUTTON_IMPRESSIVE).click()

        return self.element_is_visible(RadioButtonLocators.RESULT).text
