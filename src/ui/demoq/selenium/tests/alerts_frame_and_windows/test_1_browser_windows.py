import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.alerts_frame_windows.browser_windows_page import WindowsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.BROWSER_WINDOWS.value}"

@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Browser Windows")
class TestBrowserWindows:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия нового окна или вкладки")
    @allure.title("Проверка открытия новой вкладки")
    def test_text_box_email(self, driver: WebDriver):
        browser_windows_page = WindowsPage(driver, BASE_URL)
        browser_windows_page.open()
        text_result = browser_windows_page.opened_new_tab()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert text_result == "This is a sample page", "Новая вкладка не открылась или открылась не та вкладка"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия нового окна или вкладки")
    @allure.title("Проверка открытия нового окна")
    def test_text_box_email(self, driver: WebDriver):
        browser_windows_page = WindowsPage(driver, BASE_URL)
        browser_windows_page.open()
        text_result = browser_windows_page.opened_new_window()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert text_result == "This is a sample page", "Новое окно не открылось или открылось неверное окно"

    # TODO Починить тест
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия нового окна или вкладки")
    @allure.title("Проверка открытия нового окна с сообщением")
    def test_text_box_email(self, driver: WebDriver):
        browser_windows_page = WindowsPage(driver, BASE_URL)
        browser_windows_page.open()
        text_result = browser_windows_page.opened_new_window_with_message()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert text_result == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.", "Новое окно не открылось или открылось неверное окно"
