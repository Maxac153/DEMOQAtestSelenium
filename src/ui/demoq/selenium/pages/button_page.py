import allure
from selenium.webdriver import ActionChains

from src.ui.demoq.selenium.locators.button_locators import ButtonLocators
from src.ui.demoq.selenium.modules.button import Button
from src.ui.demoq.selenium.pages.base_page import BasePage


class ButtonPage(BasePage):
    @allure.step("Нажатие на Button")
    def button_click(self, button_enum: Button) -> str:
        """Нажатие на определённый button"""

        result = ""
        if button_enum == Button.DOUBLE_CLICK_ME_BUTTON:
            element = self.element_is_visible(ButtonLocators.DOUBLE_CLICK_ME_BUTTON)
            ActionChains(self.driver).move_to_element(element).double_click(element).perform()
            result = self.element_is_visible(ButtonLocators.DOUBLE_CLICK_ME_RESULT).text

        if button_enum == Button.RIGHT_CLICK_ME_BUTTON:
            element = self.element_is_visible(ButtonLocators.RIGHT_CLICK_ME_BUTTON)
            ActionChains(self.driver).move_to_element(element).context_click(element).perform()
            result = self.element_is_visible(ButtonLocators.RIGHT_CLICK_ME_RESULT).text

        if button_enum == Button.CLICK_ME_BUTTON:
            self.element_is_visible(ButtonLocators.CLICK_ME_BUTTON).click()
            result = self.element_is_visible(ButtonLocators.CLICK_ME_RESULT).text

        return result
