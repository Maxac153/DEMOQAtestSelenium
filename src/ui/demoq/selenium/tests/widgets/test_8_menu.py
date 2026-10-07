import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.menu_page import MenuPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.MENU.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Menu")
class TestMenuPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка пунктов меню")
    @allure.title("Проверка всех пунктов меню")
    def test_menu_items(self, driver):
        menu_page = MenuPage(driver, BASE_URL)
        menu_page.open()
        result = menu_page.get_menu_items()

        with allure.step("Проверка изменения состояния кнопок"):
            assert result == [
                "Main Item 1",
                "Main Item 2",
                "Sub Item",
                "Sub Item",
                "SUB SUB LIST »",
                "Sub Sub Item 1",
                "Sub Sub Item 2",
                "Main Item 3",
            ], "Пункты меню отсутствуют или выбраны некорректно"
