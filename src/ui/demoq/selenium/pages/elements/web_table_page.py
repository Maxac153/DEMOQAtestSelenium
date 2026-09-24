from time import sleep

import allure
from selenium.webdriver.common.by import By

from src.ui.demoq.selenium.locators.elements.web_table_locators import WebTableLocators
from src.ui.demoq.selenium.modules.elements.person import Person
from src.ui.demoq.selenium.pages.base_page import BasePage


class WebTablePage(BasePage):
    locators = WebTableLocators()

    @allure.step('Создание нового пользователя')
    def add_new_person(self, person: Person) -> list[str]:
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(person.firstname)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person.age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(person.salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(person.department)
        self.element_is_visible(self.locators.SUBMIT).click()
        self.element_is_invisible(self.locators.REGISTRATION_FORM)

        return [person.firstname, person.lastname, str(person.age), person.email, str(person.salary), person.department]

    @allure.step('Получение всех пользователей')
    def get_persons(self):
        people_list = self.elements_are_visible(self.locators.FULL_PEOPLE_LIST)
        data = []
        # TODO Поправить на объект list[Person(...)]
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('Поиск пользователя')
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Поиск пользователя')
    def get_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text

    @allure.step('Обновить личные данные')
    def update_person_info(self, age: str):
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return age

    @allure.step('Удалить пользователя')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Поиск удалённого пользователя')
    def search_deleted_person(self):
        return self.driver.find_element(*self.locators.NO_ROWS_FOUND).text

    @allure.step('Выбрать до определенного количества строк')
    def select_up_to_some_rows(self):
        count = [10, 20, 30, 40, 50]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('Проверить количество строк')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)
