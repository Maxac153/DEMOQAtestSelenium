import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.resizable_page import ResizablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.RESIZABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Resizable")
class TestResizablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check changed resizable boxes")
    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, BASE_URL)
        resizable_page.open()
        max_box, min_box = resizable_page.change_size_resizable_box()
        max_resize, min_resize = resizable_page.change_size_resizable()

        assert ("200px", "200px") == max_box, "maximum size not equal to '200px', '200px'"
        assert ("150px", "150px") == min_box, "minimum size not equal to '150px', '150px'"
        assert min_resize != max_resize, "resizable has not been changed"
