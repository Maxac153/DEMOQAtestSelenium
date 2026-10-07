import os
import random

import allure
import pytest
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.modules.elements.person import Person
from src.ui.demoq.selenium.pages.elements.web_table_page import WebTablePage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.WEB_TABLES.value}"

faker_ru = Faker("ru_RU")
fake_en = Faker("En")
Faker.seed()


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Web Tables")
class TestsButton:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Добавление пользователя")
    @allure.title("Проверка добавление пользователя ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,person",
        [
            ("Проверка открытия новой вкладки (SIMPLE_LINK_LINK)",
             Person(
                 full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
                 firstname=faker_ru.first_name(),
                 lastname=faker_ru.last_name(),
                 age=random.randint(10, 80),
                 salary=random.randint(10000, 100000),
                 department=faker_ru.job(),
                 email=faker_ru.email(),
                 current_address=faker_ru.address(),
                 permanent_address=faker_ru.address(),
                 mobile=faker_ru.msisdn(),
             )),
        ]
    )
    def test_add_new_person(
            self,
            driver: WebDriver,
            test_case_name: str,
            person: Person
    ):
        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()
        new_person = web_table_page.add_new_person(person)
        result = web_table_page.get_persons()

        with allure.step("Проверка добавления нового person"):
            assert [" ".join(new_person)] in result, ""

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Поиск person")
    @allure.title("Проверьте наличие человека в результатах поиска в таблице ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,person",
        [
            ("Проверка открытия новой вкладки (SIMPLE_LINK_LINK)",
             Person(
                 full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
                 firstname=faker_ru.first_name(),
                 lastname=faker_ru.last_name(),
                 age=random.randint(10, 80),
                 salary=random.randint(10000, 100000),
                 department=faker_ru.job(),
                 email=faker_ru.email(),
                 current_address=faker_ru.address(),
                 permanent_address=faker_ru.address(),
                 mobile=faker_ru.msisdn(),
             )),
        ]
    )
    def test_web_table_search_person(
            self,
            driver: WebDriver,
            test_case_name: str,
            person: Person
    ):
        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()
        key_word = web_table_page.add_new_person(person)[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.get_search_person()

        with allure.step("Проверка поиска пользователя в таблице"):
            assert key_word in table_result, "Пользователь не был найден в таблице"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Добавление пользователя")
    @allure.title("Проверка для обновления информации о человеке в таблице")
    @pytest.mark.parametrize(
        "test_case_name,person",
        [
            ("Проверка открытия новой вкладки (SIMPLE_LINK_LINK)",
             Person(
                 full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
                 firstname=faker_ru.first_name(),
                 lastname=faker_ru.last_name(),
                 age=random.randint(10, 80),
                 salary=random.randint(10000, 100000),
                 department=faker_ru.job(),
                 email=faker_ru.email(),
                 current_address=faker_ru.address(),
                 permanent_address=faker_ru.address(),
                 mobile=faker_ru.msisdn(),
             )),
        ]
    )
    def test_web_table_update_person_info(
            self,
            driver: WebDriver,
            test_case_name: str,
            person: Person
    ):
        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()
        lastname = web_table_page.add_new_person(person)[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info("20")
        row = web_table_page.get_search_person()

        with allure.step("Карточка пользователя не была изменена"):
            assert age in row, "Карточка пользователя не была изменена"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Удаление пользователя")
    @allure.title("Удаление пользователя ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,person",
        [
            ("Проверка открытия новой вкладки (SIMPLE_LINK_LINK)",
             Person(
                 full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
                 firstname=faker_ru.first_name(),
                 lastname=faker_ru.last_name(),
                 age=random.randint(10, 80),
                 salary=random.randint(10000, 100000),
                 department=faker_ru.job(),
                 email=faker_ru.email(),
                 current_address=faker_ru.address(),
                 permanent_address=faker_ru.address(),
                 mobile=faker_ru.msisdn(),
             )),
        ]
    )
    @allure.title("Проверка возможности удаления человека из таблицы")
    def test_web_table_delete_person(
            self,
            driver: WebDriver,
            test_case_name: str,
            person: Person
    ):
        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()
        email = web_table_page.add_new_person(person)[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.search_deleted_person()

        with allure.step("Проверка удаления пользователя"):
            assert text == "", "Пользователей не удалён"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверьте изменение количества строк в таблице")
    @allure.title("Проверьте изменение количества строк в таблице ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,person",
        [
            ("Проверка открытия новой вкладки (SIMPLE_LINK_LINK)",
             Person(
                 full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
                 firstname=faker_ru.first_name(),
                 lastname=faker_ru.last_name(),
                 age=random.randint(10, 80),
                 salary=random.randint(10000, 100000),
                 department=faker_ru.job(),
                 email=faker_ru.email(),
                 current_address=faker_ru.address(),
                 permanent_address=faker_ru.address(),
                 mobile=faker_ru.msisdn(),
             )),
        ]
    )
    def test_web_table_change_count_row(
            self,
            driver: WebDriver,
            test_case_name: str,
            person: Person
    ):
        web_table_page = WebTablePage(driver, BASE_URL)
        web_table_page.open()
        count = web_table_page.select_up_to_some_rows()

        with allure.step("Строки не найдены"):
            assert count == [10, 20, 30, 40, 50], "Количество строк в таблице не изменилось или изменилось некорректно"
