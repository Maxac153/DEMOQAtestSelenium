import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.alerts_frame_windows.modal_dialogs_page import ModalDialogsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.MODAL_DIALOGS.value}"

@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Model Dialogs")
class TestNestedFramesPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия алерта")
    @allure.title("Проверьте страницу с модальными диалогами")
    def test_modal_dialogs(self, driver):
        modal_dialogs_page = ModalDialogsPage(driver, BASE_URL)
        modal_dialogs_page.open()
        small, large = modal_dialogs_page.check_modal_dialogs()

        assert small[1] < large[1], "Текст из большого диалогового окна короче текста из маленького диалогового окна"
        assert small[0] == "Small Modal", "Заголовок не является 'Small modal'"
        assert large[0] == "Large Modal", "Заголовок не является 'Large modal'"
