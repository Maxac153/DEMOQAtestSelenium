import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.selectable_page import SelectablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.SELECTABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Selectable")
class TestSelectablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Выбор элементов списка")
    @allure.title("Проверить выбор элемента в списке")
    def test_selectable_list(
            self,
            driver: WebDriver
    ):
        selectable_page = SelectablePage(driver, BASE_URL)
        selectable_page.open()

        item_list = selectable_page.select_list_item()

        with allure.step("Проверка выбора элемента списка"):
            assert len(item_list) > 0, "Не было выбрано ни одного элемента списка"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Выбор элементов сетки")
    @allure.title("Проверить выбор элемента в сетке")
    def test_selectable_grid(
            self,
            driver: WebDriver
    ):
        selectable_page = SelectablePage(driver, BASE_URL)
        selectable_page.open()

        item_grid = selectable_page.select_grid_item()

        with allure.step("Проверка выбора элемента сетки"):
            assert len(item_grid) > 0, "Не было выбрано ни одного элемента сетки"
