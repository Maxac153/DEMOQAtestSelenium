import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.dynamic_properties_page import DynamicPropertiesPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DYNAMIC_PROPERTIES.value}"


@allure.feature("Форма Dynamic Properties")
class TestsDynamicProperties:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка выбора Dynamic Properties")
    @allure.title("Проверка Dynamic Properties, изменение состояние button")
    def test_dynamic_properties(self, driver: WebDriver) -> None:
        """Проверка Dynamic Properties, выбор случайного значения"""

        dynamic_properties_page = DynamicPropertiesPage(driver, BASE_URL)
        dynamic_properties_page.open()
        button_enable, button_color_change, button_visible = dynamic_properties_page.button_click()

        with allure.step("Проверка изменения состояния кнопок"):
            assert button_enable == True
            assert button_color_change == "mt-4 text-danger btn btn-primary"
            assert button_visible == "Visible After 5 Seconds"
