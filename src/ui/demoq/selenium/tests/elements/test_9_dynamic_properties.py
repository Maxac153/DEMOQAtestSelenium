import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.elements.dynamic_properties_page import DynamicPropertiesPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DYNAMIC_PROPERTIES.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Dynamic Properties")
class TestDynamicProperties:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка активации кнопки")
    @allure.title("Проверка активации кнопки через 5 секунд")
    def test_button_becomes_enabled(
            self,
            driver: WebDriver
    ):
        dynamic_properties_page = DynamicPropertiesPage(driver, BASE_URL)
        dynamic_properties_page.open()
        is_enabled = dynamic_properties_page.is_enable_button_enabled()

        with allure.step("Проверка активности кнопки"):
            assert is_enabled, "Кнопка «Enable After 5 Seconds» должна быть активной"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка изменения цвета кнопки")
    @allure.title("Проверка изменения цвета кнопки")
    def test_button_color_changes(
            self,
            driver: WebDriver
    ):
        dynamic_properties_page = DynamicPropertiesPage(driver, BASE_URL)
        dynamic_properties_page.open()
        button_class = dynamic_properties_page.get_color_change_button_class()

        with allure.step("Проверка CSS-классов кнопки"):
            assert button_class == "mt-4 text-danger btn btn-primary", "CSS-классы кнопки не соответствуют ожидаемым. Фактические CSS-классы: {button_class!r}"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка отображения кнопки")
    @allure.title("Проверка отображения кнопки через 5 секунд")
    def test_button_becomes_visible(
            self,
            driver: WebDriver
    ):
        dynamic_properties_page = DynamicPropertiesPage(driver, BASE_URL)
        dynamic_properties_page.open()
        button_text = dynamic_properties_page.get_visible_button_text()

        with allure.step("Проверка текста отображаемой кнопки"):
            assert button_text == "Visible After 5 Seconds", "Кнопка должна стать видимой через 5 секунд. Фактический текст кнопки: {button_text!r}"
