from selenium.webdriver import Keys

from src.ui.demoq.selenium.locators.form_page_locators import FormPageLocators
from src.ui.demoq.selenium.pages.base_page import BasePage


class FormPage(BasePage):
    def fill_fields_and_submit(self):
        """Заполнение формы"""

        first_name = 'Hello'
        last_name = 'World'
        email = 'hello@world.com'
        self.remove_footer()
        self.element_is_visible(FormPageLocators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(FormPageLocators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(FormPageLocators.EMAIL).send_keys(email)
        self.element_is_visible(FormPageLocators.GENDER).click()
        self.element_is_visible(FormPageLocators.MOBILE).send_keys('5323542565')
        subject = self.element_is_visible(FormPageLocators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(FormPageLocators.CURRENT_ADDRESS).send_keys('City, 1231, USA')
        self.element_is_visible(FormPageLocators.SUBMIT).click()
        return first_name, last_name, email

    def form_result(self):
        """Проверка формы"""

        result_list = self.elements_are_visible(FormPageLocators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text
