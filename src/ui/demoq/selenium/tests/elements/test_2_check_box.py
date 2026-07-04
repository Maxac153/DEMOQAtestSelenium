import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.check_box_page import CheckBoxPage

BASE_URL = f"{os.environ.get('DEMOQA_HOST')}{EndpointsDemoq.CHECKBOX.value}"
RUN_IDS = [f"Проверка выделения случайного чекбокса ({i})" for i in range(5)]


@allure.feature("Форма Check Box")
class TestsCheckBox:

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Выбор чекбоксов по путям")
    @allure.title("Проверка случайного выбора путей чекбоксов ({run_id})")
    @pytest.mark.parametrize("run_id", RUN_IDS, ids=RUN_IDS)
    def test_check_box_random_paths(self, driver: WebDriver, run_id: str):
        """Проверка выбора чекбоксов по случайным путям."""

        check_box_page = CheckBoxPage(driver, BASE_URL)
        check_box_page.open()
        select_items, result = check_box_page.select_path()

        with allure.step("Проверить отображение элементов в результате"):
            for select_item in select_items:
                assert select_item in result, f"Элемент '{select_item}' отсутствует в результате"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Выделение отдельного элемента")
    @allure.title("Проверка выделения случайного чекбокса ({run_id})")
    @pytest.mark.parametrize("run_id", RUN_IDS, ids=RUN_IDS)
    def test_check_box_select_item(self, driver: WebDriver, run_id: str):
        """Проверка выделения одного случайного чекбокса."""

        check_box_page = CheckBoxPage(driver, BASE_URL)
        check_box_page.open()
        result, check_box_select = check_box_page.select_item()

        with allure.step("Проверить равенство выделенного элемента и результата"):
            assert result == check_box_select, f"Ожидался '{check_box_select}', но получен '{result}'"
