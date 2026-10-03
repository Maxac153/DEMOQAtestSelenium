import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.auto_complete_page import AutoCompletePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.AUTO_COMPLETE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Auto Complete")
class TestAutoCompletePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Multi autocomplete")
    @allure.title("Check the autocomplete is filled")
    def test_fill_multi_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, BASE_URL)
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()

        with allure.step("Проверка изменения состояния кнопок"):
            assert colors == colors_result, "the added colors are missing in the input"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Multi autocomplete")
    @allure.title("Check deletions form the multi autocomplete")
    def test_remove_value_from_multi(self, driver):
        autocomplete_page = AutoCompletePage(driver, BASE_URL)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()

        with allure.step("Проверка изменения состояния кнопок"):
            assert count_value_before != count_value_after, "value was not deleted"
            assert count_value_after == count_value_before - 1, "more than one value was deleted"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Single autocomplete")
    @allure.title("Check single autocomplete is filled")
    def test_fill_single_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, BASE_URL)
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()

        with allure.step("Проверка изменения состояния кнопок"):
            assert color == color_result, "the added color is missing in the input"
