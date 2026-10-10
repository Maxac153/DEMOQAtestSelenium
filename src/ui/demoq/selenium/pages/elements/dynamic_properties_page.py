import allure

from src.ui.demoq.selenium.locators.elements.dynamic_properties_locators import DynamicPropertiesLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    @allure.step("Проверка активации кнопки через 5 секунд")
    def is_enable_button_enabled(self) -> bool:
        button = self.element_is_enabled(DynamicPropertiesLocators.BUTTON_ENABLE_5S, 10)

        return button.is_enabled()

    @allure.step("Получение CSS-классов кнопки с изменяющимся цветом после изменения")
    def get_color_change_button_class(self) -> str | None:
        button = self.element_is_visible(DynamicPropertiesLocators.BUTTON_COLOR_CHANGE, 10)

        # Сохраняем начальный класс
        initial_class = button.get_attribute("class")

        # Ждём изменения класса
        changed_button = self.wait_attribute_changed(
            DynamicPropertiesLocators.BUTTON_COLOR_CHANGE,
            "class",
            initial_class,
            timeout=10
        )

        return changed_button.get_attribute("class")

    @allure.step("Получение текста отображаемой кнопки")
    def get_visible_button_text(self) -> str:
        button = self.element_is_visible(DynamicPropertiesLocators.BUTTON_VISIBLE, 10)

        return button.text
