import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.accordian_page import AccordianPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.ACCORDIAN.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Accordian")
class TestAccordianPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.title("Проверьте виджет-аккордеон")
    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver, BASE_URL)
        accordian_page.open()

        first_title, first_has_content = accordian_page.check_accordian("first")
        second_title, second_has_content = accordian_page.check_accordian("second")
        third_title, third_has_content = accordian_page.check_accordian("third")

        with allure.step("Проверка изменения состояния кнопок"):
            assert first_title == "What is Lorem Ipsum?" and first_has_content, "Неверный заголовок или отсутствует текст"
            assert second_title == "Where does it come form?" and second_has_content, "Неверный заголовок или отсутствует текст"
            assert third_title == "Why do we use it?" and third_has_content, "Неверный заголовок или отсутствует текст"
