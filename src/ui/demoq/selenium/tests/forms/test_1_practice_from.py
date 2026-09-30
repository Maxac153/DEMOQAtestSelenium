import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.form.form_page import FormPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.AUTOMATION_PRACTICE_FORM.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Practice Form")
class TestFormPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка формы")
    @allure.title("Проверка формы")
    def test_form(self, driver):
        form_page = FormPage(driver, BASE_URL)
        form_page.open()
        p = form_page.fill_form_fields()
        result = form_page.form_result()
        assert [p.firstname + " " + p.lastname, p.email] == [result[0], result[1]], "Форма не заполнена"
