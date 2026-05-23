import os

import allure
from webdriver_manager.core.driver import Driver

from src.ui.demoq.selenium.pages.dynamic_properties_page import DynamicPropertiesPage


@allure.feature("Dynamic Properties форма")
class TestsDynamicProperties:
    @allure.story("Проверка выбора Dynamic Properties")
    @allure.title("Тест Dynamic Properties с параметризацией")
    @allure.step("Проверка Dynamic Properties, изменение состояние button")
    def test_dynamic_properties(self, driver: Driver) -> None:
        """Проверка Dynamic Properties, выбор случайного значения"""

        with allure.step("Открытие страницы"):
            dynamic_properties_page = DynamicPropertiesPage(driver, f"{os.environ.get("DEMOQA_HOST")}/dynamic-properties")
            dynamic_properties_page.open()

        with allure.step("Ожидание изменение состояние кнопки"):
            button_enable, button_color_change, button_visible = dynamic_properties_page.button_click()

        with allure.step("Проверка изменения состояния кнопок"):
            assert button_enable == True
            assert button_color_change == "mt-4 text-danger btn btn-primary"
            assert button_visible == "Visible After 5 Seconds"
