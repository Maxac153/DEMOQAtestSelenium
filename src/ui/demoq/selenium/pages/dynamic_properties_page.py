import allure

from src.ui.demoq.selenium.locators.dynamic_properties_locators import DynamicPropertiesLocators
from src.ui.demoq.selenium.pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    @allure.step("Ожидание изменение состояний кнопок")
    def button_click(self) -> tuple[bool, str | None, str]:
        button_visible = self.element_is_visible(DynamicPropertiesLocators.BUTTON_VISIBLE, 10).text
        button_enable = self.element_is_visible(DynamicPropertiesLocators.BUTTON_ENABLE_5S).is_enabled()
        button_color_change = self.element_is_visible(DynamicPropertiesLocators.BUTTON_COLOR_CHANGE).get_attribute("class")

        return button_enable, button_color_change, button_visible
