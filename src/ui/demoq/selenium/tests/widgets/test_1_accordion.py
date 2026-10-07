import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.accordian_page import AccordionPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.ACCORDIAN.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Accordion")
class TestAccordionPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "section_name, expected_title",
        [
            pytest.param(
                "first",
                "What is Lorem Ipsum?",
                id="first-section",
            ),
            pytest.param(
                "second",
                "Where does it come from?",
                id="second-section",
            ),
            pytest.param(
                "third",
                "Why do we use it?",
                id="third-section",
            ),
        ],
    )
    @allure.story("Проверка виджета-аккордеона")
    @allure.title("Проверка секции аккордеона: {expected_title}")
    def test_accordion_section(self, driver, section_name, expected_title):
        accordion_page = AccordionPage(driver, BASE_URL)
        accordion_page.open()
        actual_title, has_content = accordion_page.open_accordion_section(section_name)

        with allure.step(f"Проверка секции «{expected_title}»"):
            assert actual_title == expected_title, f"Ожидался заголовок «{expected_title}», получен «{actual_title}»"
