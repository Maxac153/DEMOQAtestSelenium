import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.form.form_page import FormPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.AUTOMATION_PRACTICE_FORM.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Practice Form")
class TestFormPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Заполнение формы регистрации")
    @allure.title("Проверка успешного заполнения формы регистрации")
    def test_form(
            self,
            driver: WebDriver
    ):
        form_page = FormPage(driver, BASE_URL)
        form_page.open()
        person = form_page.fill_form_fields(rf"input/img/test_file.txt")
        result = form_page.form_result()

        with allure.step("Проверка заполненных данных формы"):
            assert [f"{person.firstname} {person.lastname}", person.email] == [
                result[0],
                result[1],
            ], f"Данные формы заполнены некорректно: ожидалось={[person.firstname + ' ' + person.lastname, person.email]!r}, получено={result[:2]!r}"
