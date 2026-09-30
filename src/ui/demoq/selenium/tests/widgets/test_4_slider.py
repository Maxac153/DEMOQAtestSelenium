import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.slider_page import SliderPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.SLIDER.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Slider")
class TestSliderPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check moved slider")
    def test_slider(self, driver):
        slider = SliderPage(driver, BASE_URL)
        slider.open()
        before, after = slider.change_slider_value()

        assert before == after, "the slider value has not been changed"
