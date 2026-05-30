import os

import allure
import pytest
from faker import Faker
from webdriver_manager.core.driver import Driver

from src.ui.demoq.selenium.modules.TextBox import TextBox
from src.ui.demoq.selenium.pages.text_box import TextBoxPage


class TestsTextBox:
    FAKE = Faker('ru_RU')
    EMAIL = FAKE.email()

    @allure.feature("Text Box форма")
    @allure.story("Проверка отправки формы")
    @allure.title("Тест TextBox с параметризацией")
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
                    "2. Создание пользователя с одинаковым email",
                    TextBox(
                        full_name=FAKE.name(),
                        email=EMAIL,
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "3. Некорректный email, пропуск @",
                    TextBox(
                        full_name=FAKE.name(),
                        email="user1example.com",
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "4. Некорректный email, пропуск .",
                    TextBox(
                        full_name=FAKE.name(),
                        email="user2@examplecom",
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "5. Пропуск поля name",
                    TextBox(
                        email=FAKE.email(),
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "6. Пропуск поля email",
                    TextBox(
                        full_name=FAKE.name(),
                        current_address=FAKE.address(),
                        permanent_address=FAKE.address(),
                    )
            ),
            (
                    "7. Пропуск поля current_address",
                    TextBox(
                        full_name=FAKE.name(),
                        email=FAKE.email(),
                        permanent_address=FAKE.address()
                    )
            ),
            (
                    "8. Пропуск всех полей",
                    TextBox()
            )
        ],
    )
    @allure.step("Открытие страницы и отправка формы ({test_case_name})")
    def test_text_box(self, driver: Driver, test_case_name: str, data: TextBox):
        """Проверка формы ввода с разными данными и ожидаемым результатом"""

        with allure.step("Открытие страницы"):
            text_box_page = TextBoxPage(driver, f"{os.environ.get("DEMOQA_HOST")}/text-box")
            text_box_page.open()

        with allure.step("Отправка формы"):
            text_box_page.submit_form(data)
            result = text_box_page.get_result_submit()

        expected_result = TextBox(
            full_name=f"Name:{data.full_name}",
            email=f"Email:{data.email}",
            current_address=f"Current Address :{data.current_address}",
            permanent_address=f"Permananet Address :{data.permanent_address}",
        )

        with allure.step("Проверка отправленных данных"):
            assert result.model_dump() == expected_result.model_dump()
