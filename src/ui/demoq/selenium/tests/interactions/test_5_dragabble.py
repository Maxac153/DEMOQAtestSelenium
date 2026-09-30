import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.draggable_page import DraggablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DRAGABBLE.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Droppable")
class TestDraggablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.title("Check simple draggable")
    def test_simple_draggable(self, driver):
        draggable_page = DraggablePage(driver, BASE_URL)
        draggable_page.open()
        before, after = draggable_page.simple_drag_box()

        assert before != after, "the position of the box has not been changed"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка виджета-аккордеона")
    @allure.title("Check axis restricted draggable")
    def test_axis_restricted_draggable(self, driver):
        draggable_page = DraggablePage(driver, BASE_URL)
        draggable_page.open()
        top_x, left_x = draggable_page.axis_restricted_x()
        top_y, left_y = draggable_page.axis_restricted_y()

        assert top_x[0][0] == top_x[1][0] and int(
            top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
        assert left_x[0][0] != left_x[1][0] and int(
            left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
        assert top_y[0][0] != top_y[1][0] and int(
            top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
        assert left_y[0][0] == left_y[1][0] and int(
            left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"
