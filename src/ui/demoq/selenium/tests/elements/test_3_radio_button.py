import os

import allure
import pytest
from webdriver_manager.core.driver import Driver

from src.ui.demoq.selenium.modules.radio_button import RadioButton
from src.ui.demoq.selenium.pages.radio_button_page import RadioButtonPage


@allure.feature("Radio Button форма")
class TestsRadioButton:
    @allure.story("Проверка выбора radio button")
    @allure.title("Тест Radio Button с параметризацией")
    @allure.step("Проверка Radio Button, кликаем по radio button ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_check_box,expected_result",
        [
            ("Проверка нажатия на Check Box Yes", RadioButton.YES, RadioButton.YES.value),
            ("Проверка нажатия на Check Box Impressive", RadioButton.IMPRESSIVE, RadioButton.IMPRESSIVE.value)
        ]
    )
    def test_check_box(self, driver: Driver, test_case_name: str, select_check_box: RadioButton, expected_result: str):
        """Проверка Radio Button, выбор случайного значения"""

        with allure.step("Открытие страницы"):
            check_box_page = RadioButtonPage(driver, f"{os.environ.get("DEMOQA_HOST")}/radio-button")
            check_box_page.open()

        with allure.step("Выбор Radio Button ({})"):
            result = check_box_page.radio_button_click(select_check_box)

        with allure.step("Проверка выбранного Radio Button"):
            assert expected_result == result
