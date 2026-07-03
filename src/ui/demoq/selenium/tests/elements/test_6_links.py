import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.selenium.modules.links import Links
from src.ui.demoq.selenium.pages.links_page import LinksPage


@allure.feature("Links")
class TestsButton:
    @allure.story("Открытие новой вкладки")
    @allure.title("Проверка title новой вкладки для ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_links,expected_result",
        [
            ("Проверка открытия новой вкладки (SIMPLE_LINK_LINK)", Links.SIMPLE_LINK_LINK, Links.SIMPLE_LINK_LINK.value),
            ("Проверка открытия новой вкладки (DYNAMIC_LINK_LINK)", Links.DYNAMIC_LINK_LINK, Links.DYNAMIC_LINK_LINK.value)
        ]
    )
    def test_open_new_tab_title(self, driver: WebDriver, test_case_name: str, select_links: Links, expected_result: str):
        """Проверка Links"""

        with allure.step("Открытие страницы"):
            links_page = LinksPage(driver, f"{os.environ.get("DEMOQA_HOST")}/links")
            links_page.open()

        with allure.step("Нажатие на Links ({select_links})"):
            result = links_page.open_new_tab(select_links)

        assert expected_result == result, "Проверка нажатия на links"

    @allure.story("Проверка выбора links")
    @allure.title("Проверка Links, кликаем по links ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_links,expected_result",
        [
            ("Проверка нажатия на Links (CREATED_LINK)", Links.CREATED_LINK, Links.CREATED_LINK.value),
            ("Проверка нажатия на Links (NO_CONTENT_LINK)", Links.NO_CONTENT_LINK, Links.NO_CONTENT_LINK.value),
            ("Проверка нажатия на Links (MOVED_LINK)", Links.MOVED_LINK, Links.MOVED_LINK.value),
            ("Проверка нажатия на Links (BAD_REQUEST_LINK)", Links.BAD_REQUEST_LINK, Links.BAD_REQUEST_LINK.value),
            ("Проверка нажатия на Links (UNAUTHORIZED_LINK)", Links.UNAUTHORIZED_LINK, Links.UNAUTHORIZED_LINK.value),
            ("Проверка нажатия на Links (FORBIDDEN_LINK)", Links.FORBIDDEN_LINK, Links.FORBIDDEN_LINK.value),
            ("Проверка нажатия на Links (INVALID_URL_LINK)", Links.INVALID_URL_LINK, Links.INVALID_URL_LINK.value)
        ]
    )
    def test_check_links(self, driver: WebDriver, test_case_name: str, select_links: Links, expected_result: str):
        """Проверка Links"""

        with allure.step("Открытие страницы"):
            links_page = LinksPage(driver, f"{os.environ.get("DEMOQA_HOST")}/links")
            links_page.open()

        with allure.step("Нажатие на Links ({select_links})"):
            result = links_page.click_links(select_links)

        with allure.step("Проверка нажатия на links"):
            assert expected_result == result
