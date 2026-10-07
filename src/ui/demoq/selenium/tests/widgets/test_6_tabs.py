import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.tabs_page import TabsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.TABS.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Tabs")
class TestTabsPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "tab_name, expected_title",
        [
            pytest.param("what", "What", id="what"),
            pytest.param("origin", "Origin", id="origin"),
            pytest.param("use", "Use", id="use"),
            pytest.param("more", "More", id="more"),
        ],
    )
    @allure.story("Переключение вкладок")
    @allure.title("Проверка вкладки «{expected_title}»")
    def test_tabs(
            self,
            driver: WebDriver,
            tab_name: str,
            expected_title: str
    ):
        tabs = TabsPage(driver, BASE_URL)
        tabs.open()
        actual_title, content_length = tabs.open_tab_and_get_content_length(tab_name)

        with allure.step("Проверка названия вкладки"):
            assert actual_title == expected_title, f"Ожидалось название «{expected_title}», получено «{actual_title}»"

        with allure.step("Проверка наличия содержимого вкладки"):
            assert content_length > 0, f"Содержимое вкладки «{tab_name}» отсутствует"
