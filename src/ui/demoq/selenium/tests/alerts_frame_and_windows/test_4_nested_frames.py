import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

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
    @pytest.mark.parametrize(
        "expected_parent, expected_child",
        [
            pytest.param(
                "Parent frame",
                "Child Iframe",
                id="standard_texts",
            ),
        ],
    )
    @allure.story("Проверка вложенных фреймов")
    @allure.title("Проверка содержимого родительского и дочернего фреймов")
    def test_nested_frames(
            self,
            driver: WebDriver,
            expected_parent: str,
            expected_child: str,
    ):
        nested_frame_page = NestedFramesPage(driver, BASE_URL)
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frame()

        with allure.step(f"Проверка текста родительского фрейма: '{parent_text}'"):
            assert parent_text == expected_parent, (
                f"Текст родительского фрейма не совпадает. "
                f"Ожидалось: '{expected_parent}', получено: '{parent_text}'"
            )

        with allure.step(f"Проверка текста дочернего фрейма: '{child_text}'"):
            assert child_text == expected_child, (
                f"Текст дочернего фрейма не совпадает. "
                f"Ожидалось: '{expected_child}', получено: '{child_text}'"
            )
