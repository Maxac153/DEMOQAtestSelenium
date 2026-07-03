import allure

from src.ui.demoq.selenium.locators.text_box_page_locators import TextBoxPageLocators
from src.ui.demoq.selenium.modules.elements.text_box import TextBox
from src.ui.demoq.selenium.pages.base_page import BasePage


class TextBoxPage(BasePage):
    def __filling_fields(self, data: TextBox):
        """Заполнение формы"""

        self.element_is_visible(TextBoxPageLocators.FULL_NAME).send_keys(data.full_name)
        self.element_is_visible(TextBoxPageLocators.EMAIL).send_keys(data.email)
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS).send_keys(data.current_address)
        self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS).send_keys(data.permanent_address)
        self.element_is_visible(TextBoxPageLocators.SUBMIT).click()

    @allure.step("Отправка формы")
    def submit_form(self, data: TextBox) -> None:
        """Отправка формы"""

        self.__filling_fields(data)

    @allure.step("Получение результата")
    def get_result_submit(self) -> TextBox:
        """Проверка на отправку"""

        return TextBox(
            full_name=self.element_is_visible(TextBoxPageLocators.NAME_RESULT).text,
            email=self.element_is_visible(TextBoxPageLocators.EMAIL_RESULT).text,
            current_address=self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS_RESULT).text,
            permanent_address=self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS_RESULT).text
        )
