import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.alerts_frame_windows.frames_page import FramesPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.FRAMES.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Frames")
class TestFramesPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "frame_name, expected_result",
        [
            pytest.param(
                "frame1",
                ["This is a sample page", "500px", "350px"],
                id="frame1",
            ),
            pytest.param(
                "frame2",
                ["This is a sample page", "100px", "100px"],
                id="frame2",
            ),
        ],
    )
    @allure.story("Проверка iframe")
    @allure.title("Проверка отображения данных в {frame_name}")
    def test_frames(self, driver: WebDriver, frame_name: str, expected_result: list[str]):
        frames_page = FramesPage(driver, BASE_URL)
        frames_page.open()
        actual_result = frames_page.frame(frame_name)

        with allure.step(f"Проверка содержимого {frame_name}"):
            assert actual_result == expected_result, (
                f"Некорректные данные в {frame_name}. "
                f"Ожидалось: {expected_result}, "
                f"получено: {actual_result}"
            )
