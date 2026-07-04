import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.modules.elements.radio_button import RadioButton
from src.ui.demoq.selenium.pages.radio_button_page import RadioButtonPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.RADIO_BUTTON.value}"


@allure.feature("Форма Radio Button")
class TestsRadioButton:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Выбор radio button")
    @allure.title("Проверка Radio Button, кликаем по radio button ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_check_box,expected_result",
        [
            ("Проверка нажатия на Check Box Yes", RadioButton.YES, RadioButton.YES.value),
            ("Проверка нажатия на Check Box Impressive", RadioButton.IMPRESSIVE, RadioButton.IMPRESSIVE.value)
        ]
    )
    def test_check_box(self, driver: WebDriver, test_case_name: str, select_check_box: RadioButton,
                       expected_result: str):
        """Проверка Radio Button, выбор случайного значения"""

        check_box_page = RadioButtonPage(driver, BASE_URL)
        check_box_page.open()
        result = check_box_page.radio_button_click(select_check_box)

        with allure.step("Проверка выбранного Radio Button"):
            assert expected_result == result, f"Ожидался {expected_result}, но получен {result}"
