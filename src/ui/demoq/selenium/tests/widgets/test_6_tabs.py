import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.tabs_page import TabsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.TABS.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Tabs")
class TestSliderPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check switched tabs")
    def test_tabs(self, driver):
        tabs = TabsPage(driver, BASE_URL)
        tabs.open()
        what_button, what_content = tabs.check_tabs("what")
        origin_button, origin_content = tabs.check_tabs("origin")
        use_button, use_content = tabs.check_tabs("use")
        more_button, more_content = tabs.check_tabs("more")

        with allure.step("Проверка изменения состояния кнопок"):
            # TODO Переписать на параметризацию
            assert what_button == "What" and what_content != 0, "Вкладка «what» не была нажата, или текст отсутствует"
            assert origin_button == "Origin" and origin_content != 0, "Вкладка «origin» не была нажата, или текст отсутствует"
            assert use_button == "Use" and use_content != 0, "Вкладка «use» не была нажата, или текст отсутствует"
            assert more_button == "More" and what_content != 0, "Вкладка «more» не была нажата, или текст отсутствует"
