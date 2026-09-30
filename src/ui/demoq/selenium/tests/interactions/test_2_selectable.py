import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.selectable_page import SelectablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.SELecTABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Tabs")
class TestSortablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check changed selectable list and grid")
    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, BASE_URL)
        selectable_page.open()
        item_list = selectable_page.select_list_item()
        item_grid = selectable_page.select_grid_item()

        assert len(item_list) > 0, "no elements were selected"
        assert len(item_grid) > 0, "no elements were selected"
