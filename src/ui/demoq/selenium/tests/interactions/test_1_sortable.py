import os

import allure
import pytest

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
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check changed sortable list and grid")
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, BASE_URL)
        sortable_page.open()
        list_before, list_after = sortable_page.change_list_order()
        grid_before, grid_after = sortable_page.change_grid_order()

        with allure.step("Проверка изменения состояния кнопок"):
            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the grid has not been changed"
