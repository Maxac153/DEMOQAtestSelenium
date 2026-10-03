import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.alerts_frame_windows.modal_dialogs_page import ModalDialogsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.MODAL_DIALOGS.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Model Dialogs")
class TestModalDialogsPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка модальных диалогов")
    @allure.title("Проверка содержимого малого и большого модальных окон")
    def test_modal_dialogs(self, driver: WebDriver):
        modal_dialogs_page = ModalDialogsPage(driver, BASE_URL)
        modal_dialogs_page.open()
        small, large = modal_dialogs_page.get_modal_data()
        small_title, small_text = small
        large_title, large_text = large

        with allure.step("Проверка заголовка малого модального окна"):
            assert small_title == "Small Modal", (
                f"Заголовок малого окна не совпадает. "
                f"Ожидалось: 'Small Modal', получено: '{small_title}'"
            )

        with allure.step("Проверка заголовка большого модального окна"):
            assert large_title == "Large Modal", (
                f"Заголовок большого окна не совпадает. "
                f"Ожидалось: 'Large Modal', получено: '{large_title}'"
            )
