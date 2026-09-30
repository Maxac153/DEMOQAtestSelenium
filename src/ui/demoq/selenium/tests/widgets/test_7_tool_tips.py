import os

import allure
import pytest

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
    @allure.story("Проверка всплывающих подсказок")
    @allure.title("Проверка текста всплывающих подсказок")
    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, BASE_URL)
        tool_tips_page.open()

        (
            button_text,
            field_text,
            contrary_text,
            section_text,
        ) = tool_tips_page.check_tool_tips()

        assert button_text == "You hovered over the Button", "Всплывающая подсказка над кнопкой отсутствует или содержит некорректный текст"
        assert field_text == "You hovered over the text field", "Всплывающая подсказка над текстовым полем отсутствует или содержит некорректный текст"
        assert contrary_text == "You hovered over the Contrary", "Всплывающая подсказка над элементом Contrary отсутствует или содержит некорректный текст"
        assert section_text == "You hovered over the 1.10.32", "Всплывающая подсказка над элементом 1.10.32 отсутствует или содержит некорректный текст"
