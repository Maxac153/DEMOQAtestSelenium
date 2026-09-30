import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.alerts_frame_windows.nested_frames_page import NestedFramesPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.NESTED_FRAMES.value}"

@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Nested Frames")
class TestNestedFramesPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия алерта")
    @allure.title("Проверьте страницу с вложенными фреймами")
    def test_nested_frames(self, driver):
        nested_frame_page = NestedFramesPage(driver, BASE_URL)
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frame()

        assert parent_text == "Parent frame", "Вложенный фрейм не существует"
        assert child_text == "Child Iframe", "Вложенный фрейм не существует"
