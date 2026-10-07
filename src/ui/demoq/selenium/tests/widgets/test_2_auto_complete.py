import os

import allure
import pytest

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.widgets.auto_complete_page import AutoCompletePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.AUTO_COMPLETE.value}"


@allure.parent_suite("UI-тесты")
@allure.suite("DemoQA")
@allure.feature("Страница Auto Complete")
class TestAutoCompletePage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Множественный автозаполнитель")
    @allure.title("Проверка заполнения поля множественного автозаполнения")
    def test_fill_multi_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, BASE_URL)
        autocomplete_page.open()

        expected_colors = autocomplete_page.fill_input_multi()
        actual_colors = autocomplete_page.check_color_in_multi()

        with allure.step(
            "Проверка выбранных значений в поле автозаполнения"
        ):
            assert expected_colors == actual_colors, (
                "Добавленные цвета отсутствуют в поле автозаполнения"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Множественный автозаполнитель")
    @allure.title("Проверка удаления значения из автозаполнения")
    def test_remove_value_from_multi(self, driver):
        autocomplete_page = AutoCompletePage(driver, BASE_URL)
        autocomplete_page.open()

        autocomplete_page.fill_input_multi()

        count_before, count_after = (
            autocomplete_page.remove_value_from_multi()
        )

        with allure.step(
            "Проверка удаления одного значения"
        ):
            assert count_before != count_after, (
                "Значение не было удалено"
            )

            assert count_after == count_before - 1, (
                "Было удалено более одного значения"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Одиночный автозаполнитель")
    @allure.title("Проверка заполнения одиночного автозаполнения")
    def test_fill_single_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, BASE_URL)
        autocomplete_page.open()

        expected_color = autocomplete_page.fill_input_single()
        actual_color = autocomplete_page.get_color_in_single()

        with allure.step(
            "Проверка выбранного значения в одиночном автозаполнении"
        ):
            assert expected_color == actual_color, (
                "Добавленный цвет отсутствует в поле автозаполнения"
            )