import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.draggable_page import DraggablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DRAGABBLE.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Draggable")
class TestDraggablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Простое перетаскивание элемента")
    @allure.title("Проверка простого перетаскивания элемента")
    def test_simple_draggable(
            self,
            driver: WebDriver
    ):
        draggable_page = DraggablePage(driver, BASE_URL)
        draggable_page.open()
        before, after = draggable_page.simple_drag_box()

        with allure.step("Проверка изменения состояния кнопок"):
            assert before != after, "the position of the box has not been changed"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Перетаскивание элемента по заданной оси")
    @allure.title("Проверка ограничения перетаскивания по горизонтальной и вертикальной оси")
    def test_axis_restricted_draggable(
            self,
            driver: WebDriver
    ):
        draggable_page = DraggablePage(driver, BASE_URL)
        draggable_page.open()
        top_x, left_x = draggable_page.axis_restricted_x()
        top_y, left_y = draggable_page.axis_restricted_y()

        with allure.step("Проверка изменения состояния кнопок"):
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, "Положение коробки не изменилось или произошло смещение y-axis"
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, "Положение коробки не изменилось или произошло смещение y-axis"
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, "Положение коробки не изменилось или произошло смещение x-axis"
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, "Положение коробки не изменилось или произошло смещение x-axis"
