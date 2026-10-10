import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.tool_tips_page import ToolTipsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.TOOL_TIPS.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Tool Tips")
class TestToolTips:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "tooltip_type, expected_text",
        [
            pytest.param("button", "You hovered over the Button", id="button-tooltip"),
            pytest.param("field", "You hovered over the text field", id="field-tooltip"),
            pytest.param("contrary", "You hovered over the Contrary", id="contrary-tooltip"),
            pytest.param("section", "You hovered over the 1.10.32", id="section-tooltip"),
        ],
    )
    @allure.story("Проверка всплывающих подсказок")
    @allure.title("Проверка текста подсказки: {tooltip_type}")
    def test_tooltip_text(
            self,
            driver: WebDriver,
            tooltip_type: str,
            expected_text: str,
    ):
        tool_tips_page = ToolTipsPage(driver, BASE_URL)
        tool_tips_page.open()
        actual_text = tool_tips_page.get_tooltip_text_by_type(tooltip_type)

        with allure.step(f"Проверка текста подсказки для элемента «{tooltip_type}»"):
            assert actual_text == expected_text, (
                f"Ожидался текст «{expected_text}», но получен «{actual_text}»"
            )
