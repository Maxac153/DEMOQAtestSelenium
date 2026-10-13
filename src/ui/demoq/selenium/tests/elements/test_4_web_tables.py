import os

import allure
import pytest
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.__common.models.elements.person import Person
from src.ui.demoq.selenium.pages.elements.web_table_page import WebTablePage

BASE_URL = f"{os.environ.get('DEMOQA_HOST')}{EndpointsDemoq.WEB_TABLES.value}"


def _create_person(fake: Faker) -> Person:
    """Создаёт тестовые данные пользователя."""
    first_name = fake.first_name()
    last_name = fake.last_name()

    return Person(
        full_name=f"{first_name} {last_name} {fake.middle_name()}",
        firstname=first_name,
        lastname=last_name,
        age=fake.random_int(min=10, max=80),
        salary=fake.random_int(min=10_000, max=100_000),
        department=fake.job(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
        mobile=fake.msisdn(),
    )


@allure.parent_suite("UI-selenium-test")
@allure.suite("DemoQA")
@allure.feature("Страница Web Tables")
class TestsWebTable:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Добавление пользователя")
    @allure.title("Проверка добавления пользователя")
    def test_add_new_person(self, driver: WebDriver, fake: Faker) -> None:
        person = _create_person(fake)

        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()

        new_person = web_table_page.add_new_person(person)
        table_persons = web_table_page.get_persons()

        with allure.step("Проверить, что пользователь добавлен в таблицу"):
            assert " ".join(new_person) in table_persons, (
                f"Пользователь {person.email} не был добавлен в таблицу"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Поиск пользователя")
    @allure.title("Проверка поиска пользователя по email")
    def test_web_table_search_person(self, driver: WebDriver, fake: Faker) -> None:
        person = _create_person(fake)

        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()

        web_table_page.add_new_person(person)
        web_table_page.search_some_person(person.email)

        search_result = web_table_page.get_search_person()

        with allure.step("Проверить, что пользователь найден по email"):
            assert person.email in search_result, (
                f"Пользователь с email {person.email} не был найден"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Обновление пользователя")
    @allure.title("Проверка обновления возраста пользователя")
    def test_web_table_update_person_info(self, driver: WebDriver, fake: Faker) -> None:
        person = _create_person(fake)

        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()

        web_table_page.add_new_person(person)
        web_table_page.search_some_person(person.email)

        updated_age = web_table_page.update_person_info("20")
        search_result = web_table_page.get_search_person()

        with allure.step("Проверить, что возраст пользователя обновился"):
            assert updated_age in search_result, (
                f"Возраст {updated_age} не появился в строке пользователя"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Удаление пользователя")
    @allure.title("Проверка удаления пользователя")
    def test_web_table_delete_person(self, driver: WebDriver, fake: Faker) -> None:
        person = _create_person(fake)

        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()

        web_table_page.add_new_person(person)
        web_table_page.search_some_person(person.email)
        web_table_page.delete_person()

        search_result = web_table_page.search_deleted_person()

        with allure.step("Проверить, что пользователь удалён"):
            assert search_result == "", (
                f"Пользователь с email {person.email} не был удалён"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Размер страницы таблицы")
    @allure.title("Проверка доступных размеров страницы таблицы")
    def test_web_table_change_count_row(self, driver: WebDriver) -> None:
        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()

        available_row_counts = web_table_page.select_up_to_some_rows()

        with allure.step("Проверить доступные размеры страницы"):
            assert available_row_counts == [10, 20, 30, 40, 50], (
                f"Ожидались размеры страницы [10, 20, 30, 40, 50], "
                f"но получены {available_row_counts}"
            )