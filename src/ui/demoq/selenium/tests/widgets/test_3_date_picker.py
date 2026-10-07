import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.date_picker_page import DatePickerPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DATE_PICKER.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Date Picker")
class TestDatePickerPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка выбора даты")
    @allure.title("Проверка изменения даты")
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, BASE_URL)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()

        with allure.step("Проверка изменения даты"):
            assert value_date_before != value_date_after, "Дата не была изменена"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка выбора даты и времени")
    @allure.title("Проверка изменения даты и времени")
    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, BASE_URL)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()

        with allure.step("Проверка изменения даты и времени"):
            assert value_date_before != value_date_after, "Дата и время не были изменены"
