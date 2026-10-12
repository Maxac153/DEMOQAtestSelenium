import os

import allure
import pytest
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.__common.generator.generator import create_text_box
from src.ui.demoq.__common.models.elements.text_box import TextBox
from src.ui.demoq.selenium.pages.elements.text_box_page import TextBoxPage

BASE_URL = f"{os.environ.get('DEMOQA_HOST')}{EndpointsDemoq.TEXT_BOX.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Text Box")
class TestsTextBox:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка отправки формы")
    @allure.title("Тест TextBox с параметризацией, позитивные проверки")
    @pytest.mark.parametrize(
        "omit",
        [
            pytest.param((), id="1. Корректные данные"),
            pytest.param(("full_name",), id="2. Пропуск поля name"),
            pytest.param(("email",), id="3. Пропуск поля email"),
            pytest.param(("current_address",), id="4. Пропуск поля current_address"),
            pytest.param(
                ("full_name", "email", "current_address", "permanent_address"),
                id="5. Пропуск всех полей",
            ),
        ],
    )
    def test_text_box(self, driver: WebDriver, fake: Faker, omit: tuple[str, ...]) -> None:
        data = create_text_box(fake, omit=omit)

        text_box_page = TextBoxPage(driver, BASE_URL)
        text_box_page.open()
        text_box_page.submit_form(data)
        result = text_box_page.get_result_submit(data)

        # "Permananet" с опечаткой: именно так подпись выводит сам сайт
        expected_result = TextBox(
            full_name=f"Name:{data.full_name}" if data.full_name else "",
            email=f"Email:{data.email}" if data.email else "",
            current_address=(
                f"Current Address :{data.current_address}" if data.current_address else ""
            ),
            permanent_address=(
                f"Permananet Address :{data.permanent_address}" if data.permanent_address else ""
            ),
        )

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert result.model_dump() == expected_result.model_dump(), (
                "Данные на форме не совпадают с ожидаемыми"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.negative
    @allure.story("Проверка отправки формы")
    @allure.title("Тест TextBox с параметризацией, негативные проверки")
    @pytest.mark.parametrize(
        "invalid_email",
        [
            pytest.param("user1example.com", id="1. Некорректный email, пропуск собаки"),
            pytest.param("user2@examplecom", id="2. Некорректный email, пропуск точки"),
        ],
    )
    def test_text_box_email(self, driver: WebDriver, fake: Faker, invalid_email: str) -> None:
        data = create_text_box(fake, email=invalid_email)

        text_box_page = TextBoxPage(driver, BASE_URL)
        text_box_page.open()
        text_box_page.submit_form(data)
        email_status = text_box_page.get_result_email_status()

        with allure.step("Проверка, что поле email подсвечено как ошибочное"):
            assert "field-error" in email_status, (
                f"Поле email не помечено ошибкой для значения {invalid_email}"
            )
