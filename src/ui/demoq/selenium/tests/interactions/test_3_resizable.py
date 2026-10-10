import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.resizable_page import ResizablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.RESIZABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Resizable")
class TestResizablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Изменение размера resizable box")
    @allure.title("Проверить изменение размера resizable box")
    def test_resizable_box(
            self,
            driver: WebDriver
    ):
        resizable_page = ResizablePage(driver, BASE_URL)
        resizable_page.open()

        max_box, min_box = resizable_page.change_size_resizable_box()

        with allure.step("Проверка размера resizable box"):
            assert ("200px", "200px") == max_box, "Максимальный размер не равен '200px', '200px'"
            assert ("150px", "150px") == min_box, "Минимальный размер не равен '150px', '150px'"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Изменение размера resizable")
    @allure.title("Проверить изменение размера resizable")
    def test_resizable(
            self,
            driver: WebDriver
    ):
        resizable_page = ResizablePage(driver, BASE_URL)
        resizable_page.open()

        max_resize, min_resize = resizable_page.change_size_resizable()

        with allure.step("Проверка изменения размера resizable"):
            assert min_resize != max_resize, "Resizable не был изменен"
