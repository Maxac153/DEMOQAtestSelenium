import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.progress_bar_page import ProgressBarPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.PROGRESS_BAR.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Progress Bar")
class TestSliderPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check changed progress bar")
    def test_progress_bar(self, driver):
        progress_bar = ProgressBarPage(driver, BASE_URL)
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()

        with allure.step("Проверка изменения состояния кнопок"):
            assert before != after, "the progress bar value has not been changed"
