import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.modules.button import Button
from src.ui.demoq.selenium.pages.button_page import ButtonPage


@allure.feature("Button форма")
class TestsButtons:
    @allure.story("Проверка выбора button")
    @allure.title("Тест Button с параметризацией")
    @allure.step("Проверка Button, кликаем по button ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_button,expected_result",
        [
            (
                    "Проверка нажатия на Button (DOUBLE_CLICK_ME_BUTTON)",
                    Button.DOUBLE_CLICK_ME_BUTTON,
                    Button.DOUBLE_CLICK_ME_BUTTON.value
            ),
            (
                    "Проверка нажатия на Button (RIGHT_CLICK_ME_BUTTON)",
                    Button.RIGHT_CLICK_ME_BUTTON,
                    Button.RIGHT_CLICK_ME_BUTTON.value
            ),
            (
                    "Проверка нажатия на Button (CLICK_ME_BUTTON)",
                    Button.CLICK_ME_BUTTON,
                    Button.CLICK_ME_BUTTON.value
            )
        ]
    )
    def test_check_box(self, driver: WebDriver, test_case_name: str, select_button: Button, expected_result: str):
        """Проверка Radio Button, выбор случайного значения"""

        button_page = ButtonPage(driver, f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.BUTTONS.value}")
        button_page.open()
        result = button_page.button_click(select_button)

        with allure.step("Проверка нажатия на кнопку Button"):
            assert expected_result == result
