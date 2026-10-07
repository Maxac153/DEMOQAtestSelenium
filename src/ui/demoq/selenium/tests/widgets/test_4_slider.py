import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.slider_page import SliderPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.SLIDER.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Slider")
class TestSliderPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета слайдера")
    @allure.title("Проверка изменения значения слайдера")
    def test_slider(
            self,
            driver: WebDriver
    ):
        slider_page = SliderPage(driver, BASE_URL)
        slider_page.open()
        value_before, value_after = slider_page.change_slider_value()

        with allure.step("Проверка изменения значения слайдера"):
            assert value_before != value_after, "Значение слайдера не изменилось"
