import os

import allure
import pytest

from src.ui.demoq.selenium.pages.check_box_page import CheckBoxPage


@allure.feature("Check Box форма")
class TestsCheckBox:
    @allure.story("Проверка выбора check box")
    @allure.title("Тест Check Box с параметризацией")
    @allure.step("Проверка Check Box, выбор случайного значения (run_id = {run_id})")
    @pytest.mark.parametrize("run_id", range(5))
    def test_check_box(self, driver, run_id):
        """Проверка Check Box, выбор случайного значения"""

        with allure.step("Открытие страницы"):
            check_box_page = CheckBoxPage(driver, f"{os.environ.get("DEMOQA_HOST")}/checkbox")
            check_box_page.open()

        with allure.step("Выбор случайного Check Box"):
            select_items, result = check_box_page.select_path()

        with allure.step("Проверка выбранного Check Box"):
            for select_item in select_items:
                assert select_item in result

    @allure.story("Проверка отправки формы")
    @allure.title("Тест Check Box с параметризацией")
    @allure.step("Проверка Check Box, выбор случайного значения (run_id = {run_id})")
    @pytest.mark.parametrize("run_id", range(5))
    def test_check_box_select_item(self, driver, run_id: str):
        """Проверка Check Box, выделение случайного элемента"""

        with allure.step("Открытие страницы"):
            check_box_page = CheckBoxPage(driver, f"{os.environ.get("DEMOQA_HOST")}/checkbox")
            check_box_page.open()

        with allure.step("Выделение случайного элемента Check Box"):
            result, check_box_select = check_box_page.select_item()

        with allure.step("Проверка выделенного элемента"):
            assert result == check_box_select
