import os

import allure
import pytest
from playwright.sync_api import Page

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.__common.models.elements.radio_button import RadioButton
from src.ui.demoq.playwright.pages.elements.radio_button_page import RadioButtonPage

BASE_URL = f"{os.environ.get('DEMOQA_HOST')}{EndpointsDemoq.RADIO_BUTTON.value}"


@allure.parent_suite("UI-playwright-test")
@allure.suite("DemoQA")
@allure.feature("Страница Radio Button")
class TestsRadioButton:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Выбор radio button")
    @allure.title("Проверка Radio Button, кликаем по radio button ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_radio_button,expected_result",
        [
            (
                "Проверка нажатия на Radio Button Yes",
                RadioButton.YES,
                RadioButton.YES.value,
            ),
            (
                "Проверка нажатия на Radio Button Impressive",
                RadioButton.IMPRESSIVE,
                RadioButton.IMPRESSIVE.value,
            ),
        ],
    )
    def test_radio_button(
        self,
        page: Page,
        test_case_name: str,
        select_radio_button: RadioButton,
        expected_result: str,
    ) -> None:
        radio_button_page = RadioButtonPage(page, BASE_URL)
        radio_button_page.open()
        result = radio_button_page.radio_button_click(select_radio_button)

        with allure.step("Проверка выбранного Radio Button"):
            assert expected_result == result, (
                f"Ожидался {expected_result}, но получен {result}"
            )