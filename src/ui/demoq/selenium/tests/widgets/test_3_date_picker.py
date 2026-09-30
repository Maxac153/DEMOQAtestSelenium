import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.date_picker_page import DatePickerPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DATE_PICKER.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Accordian")
class TestAccordianPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check change date")
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, BASE_URL)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()

        assert value_date_before != value_date_after, "the date has not been changed"

    @allure.title("Check change date and time")
    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, BASE_URL)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()

        assert value_date_before != value_date_after, "the date and time have not been changed"
