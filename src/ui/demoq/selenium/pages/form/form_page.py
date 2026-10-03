import os

import allure
from selenium.webdriver import Keys

from src.ui.demoq.selenium.generator.generator import generated_person, generated_file
from src.ui.demoq.selenium.locators.form.form_page_locators import FormLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class FormPage(BasePage):
    @allure.step("Заполните все поля")
    def fill_form_fields(self, file_path: str):
        person = next(generated_person())
        file_name, path = generated_file(file_path)
        self.element_is_visible(FormLocators().FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(FormLocators().LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(FormLocators().EMAIL).send_keys(person.email)
        self.element_is_visible(FormLocators().GENDER).click()
        self.element_is_visible(FormLocators().MOBILE).send_keys(person.mobile)
        self.element_is_visible(FormLocators().SUBJECT).send_keys("Math")
        self.element_is_visible(FormLocators().SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(FormLocators().HOBBIES).click()
        self.element_is_present(FormLocators().FILE_INPUT).send_keys(path)

        os.remove(path)

        self.element_is_visible(FormLocators().CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(FormLocators().SELECT_STATE).click()
        self.element_is_visible(FormLocators().STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(FormLocators().SELECT_STATE).click()
        self.element_is_visible(FormLocators().CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(FormLocators().SUBMIT).click()

        return person

    @allure.step("Получить результат формы")
    def form_result(self):
        result_list = self.elements_are_visible(FormLocators().RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)

        return data
