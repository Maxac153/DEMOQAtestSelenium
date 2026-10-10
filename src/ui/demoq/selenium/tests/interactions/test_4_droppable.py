import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.interactions.droppable_page import DroppablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.DROPPABLE.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Droppable")
class TestDroppablePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Простое перетаскивание элемента")
    @allure.title("Проверка простого перетаскивания элемента")
    def test_simple_droppable(
            self,
            driver: WebDriver
    ):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        text = droppable_page.drop_simple()

        with allure.step("Проверка результата перетаскивания"):
            assert text == "Dropped!", f"После перетаскивания текст целевой области должен измениться на 'Dropped!', фактическое значение: {text!r}"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Перетаскивание только разрешенного элемента")
    @allure.title("Проверка приема и отклонения элемента")
    def test_accept_droppable(
            self,
            driver: WebDriver
    ):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        not_accept, accept = droppable_page.drop_accept()

        with allure.step("Проверка приема и отклонения элементов"):
            assert not_accept == "Drop here", f"Область, которая не принимает элемент, не должна изменять текст. Фактическое значение: {not_accept!r}"
            assert accept == "Dropped!", f"Область, которая принимает элемент, должна изменить текст на 'Dropped!', фактическое значение: {accept!r}"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Предотвращение всплытия события перетаскивания")
    @allure.title("Проверка поведения вложенных областей при перетаскивании")
    def test_prevent_propagation_droppable(
            self,
            driver: WebDriver
    ):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        (not_greedy, not_greedy_inner, greedy, greedy_inner) = droppable_page.drop_prevent_propagation()

        with allure.step("Проверка поведения вложенных областей"):
            assert not_greedy == "Dropped!", f"Внешняя область not greedy должна изменить текст на 'Dropped!', фактическое значение: {not_greedy!r}"
            assert not_greedy_inner == "Dropped!", f"Вложенная область not greedy должна изменить текст на 'Dropped!', фактическое значение: {not_greedy_inner!r}"
            assert greedy == "Outer droppable", f"Внешняя greedy-область не должна изменить текст. Фактическое значение: {greedy!r}"
            assert greedy_inner == "Dropped!", f"Вложенная greedy-область должна изменить текст на 'Dropped!', фактическое значение: {greedy_inner!r}"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Возврат элемента после перетаскивания")
    @allure.title("Проверка возврата draggable-элементов")
    def test_revert_draggable_droppable(
            self,
            driver: WebDriver
    ):
        droppable_page = DroppablePage(driver, BASE_URL)
        droppable_page.open()
        will_after_move, will_after_revert = (droppable_page.drop_revert_draggable("will"))
        not_will_after_move, not_will_after_revert = (droppable_page.drop_revert_draggable("not_will"))

        with allure.step("Проверка возврата элементов после перетаскивания"):
            assert will_after_move == will_after_revert, "Элемент с настройкой возврата должен вернуться в исходное состояние"
            assert not_will_after_move != "0px", "Элемент без настройки возврата не должен изменять состояние после завершения перетаскивания"
            assert not_will_after_revert != "0px", "Элемент без настройки возврата не должен изменять состояние после завершения перетаскивания"
