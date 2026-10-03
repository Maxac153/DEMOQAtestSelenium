import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.droppable_page import DroppablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DROPPABLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Droppable")
class TestDroppablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check simple droppable")
    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        text = droppable_page.drop_simple()

        with allure.step("Проверка изменения состояния кнопок"):
            assert text == "Dropped!", "the elements has not been dropped"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check accept droppable")
    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        not_accept, accept = droppable_page.drop_accept()

        with allure.step("Проверка изменения состояния кнопок"):
            assert not_accept == "Drop here", "the dropped element has been accepted"
            assert accept == "Dropped!", "the dropped element has not been accepted"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check prevent propogation droppable")
    def test_prevent_propogation_droppable(self, driver):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()

        with allure.step("Проверка изменения состояния кнопок"):
            assert not_greedy == "Dropped!", "the elements texts has not been changed"
            assert not_greedy_inner == "Dropped!", "the elements texts has not been changed"
            assert greedy == "Outer droppable", "the elements texts has been changed"
            assert greedy_inner == "Dropped!", "the elements texts has not been changed"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.feature("Date Picker Page")
    @allure.title("Check revert draggable droppable")
    def test_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        will_after_move, will_after_revert = droppable_page.drop_revert_draggable("will")
        not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable("not_will")

        with allure.step("Проверка изменения состояния кнопок"):
            assert will_after_move != will_after_revert, "the elements has not reverted"
            assert not_will_after_move == not_will_after_revert, "the elements has  reverted"
