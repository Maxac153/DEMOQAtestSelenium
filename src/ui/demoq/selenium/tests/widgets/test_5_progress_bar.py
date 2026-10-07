import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.progress_bar_page import ProgressBarPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.PROGRESS_BAR.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Progress Bar")
class TestProgressBarPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета Progress Bar")
    @allure.title("Проверка изменения значения Progress Bar")
    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, BASE_URL)
        progress_bar_page.open()
        value_before, value_after = (progress_bar_page.change_progress_bar_value())

        with allure.step("Проверка изменения значения Progress Bar"):
            assert value_before != value_after, "Значение Progress Bar не изменилось"
