import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.sortable_page import SortablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.SORTABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Sortable")
class TestSortablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Сортировка списка")
    @allure.title("Проверить измененный сортируемый список")
    def test_sortable_list(
            self,
            driver: WebDriver
    ):
        sortable_page = SortablePage(driver, BASE_URL)
        sortable_page.open()

        list_before, list_after = sortable_page.change_list_order()

        with allure.step("Проверка изменения порядка списка"):
            assert list_before != list_after, "Порядок списка не был изменен"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Сортировка сетки")
    @allure.title("Проверить измененную сортируемую сетку")
    def test_sortable_grid(
            self,
            driver: WebDriver
    ):
        sortable_page = SortablePage(driver, BASE_URL)
        sortable_page.open()

        grid_before, grid_after = sortable_page.change_grid_order()

        with allure.step("Проверка изменения порядка сетки"):
            assert grid_before != grid_after, "Порядок сетки не был изменен"
