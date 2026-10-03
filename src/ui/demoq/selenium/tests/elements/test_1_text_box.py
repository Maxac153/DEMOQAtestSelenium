import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from conftest import FAKE
from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.modules.elements.text_box import TextBox
from src.ui.demoq.selenium.pages.elements.text_box_page import TextBoxPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.TEXT_BOX.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Text Box")
class TestsTextBox:
    EMAIL = FAKE.email()

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка отправки формы")
    @allure.title("Тест TextBox с параметризацией, позитивные проверки")
    @pytest.mark.parametrize(
        "test_case_name,data",
        [
            (
                    "1. Корректные данные",
                    TextBox(
                        full_name=FAKE.name(),
                        email=EMAIL,
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    ),

            ),
            (
                    "2. Пропуск поля name",
                    TextBox(
                        email=FAKE.email(),
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "3. Пропуск поля email",
                    TextBox(
                        full_name=FAKE.name(),
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "4. Пропуск поля current_address",
                    TextBox(
                        full_name=FAKE.name(),
                        email=FAKE.email(),
                        permanent_address=FAKE.address()
                    )
            ),
            (
                    "5. Пропуск всех полей",
                    TextBox()
            )
        ],
    )
    def test_text_box(self, driver: WebDriver, test_case_name: str, data: TextBox):
        text_box_page = TextBoxPage(driver, BASE_URL)
        text_box_page.open()
        text_box_page.submit_form(data)
        result = text_box_page.get_result_submit(data)

        expected_result = TextBox(
            full_name=(
                f"Name:{data.full_name}"
                if data.full_name
                else ""
            ),
            email=(
                f"Email:{data.email}"
                if data.email
                else ""
            ),
            current_address=(
                f"Current Address :{data.current_address}"
                if data.current_address
                else ""
            ),
            permanent_address=(
                f"Permananet Address :{data.permanent_address}"
                if data.permanent_address
                else ""
            ),
        )

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert result.model_dump() == expected_result.model_dump(), "Данные на форме не совпадают с ожидаемыми"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.negative
    @allure.story("Проверка отправки формы")
    @allure.title("Тест TextBox с параметризацией, негативные проверки")
    @pytest.mark.parametrize(
        "test_case_name,data",
        [
            (
                    "1. Некорректный email, пропуск собаки",
                    TextBox(
                        full_name=FAKE.name(),
                        email="user1example.com",
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "2. Некорректный email, пропуск точки",
                    TextBox(
                        full_name=FAKE.name(),
                        email="user2@examplecom",
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            )

        ],
    )
    def test_text_box_email(self, driver: WebDriver, test_case_name: str, data: TextBox):
        text_box_page = TextBoxPage(driver, BASE_URL)
        text_box_page.open()
        text_box_page.submit_form(data)
        email_status = text_box_page.get_result_email_status()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert "field-error" in email_status, "Email не совпадают с ожидаемыми"
