import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.selectable_page import SelectablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.SELECTABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Sortable")
class TestSortablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.title("Проверить измененный список и сетку с возможностью выбора")
    def test_selectable(
            self,
            driver: WebDriver
    ):
        selectable_page = SelectablePage(driver, BASE_URL)
        selectable_page.open()
        item_list = selectable_page.select_list_item()
        item_grid = selectable_page.select_grid_item()

        with allure.step("Проверка изменения состояния кнопок"):
            assert len(item_list) > 0, "Не было выбрано ни одного элемента"
            assert len(item_grid) > 0, "Не было выбрано ни одного элемента"
