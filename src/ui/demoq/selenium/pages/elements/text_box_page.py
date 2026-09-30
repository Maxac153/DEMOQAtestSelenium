import allure

from src.ui.demoq.selenium.locators.elements.text_box_page_locators import TextBoxPageLocators
from src.ui.demoq.selenium.modules.elements.text_box import TextBox
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class TextBoxPage(BasePage):
    @allure.step("Отправка формы")
    def submit_form(self, data: TextBox) -> None:
        self.element_is_visible(TextBoxPageLocators.FULL_NAME).send_keys(data.full_name)
        self.element_is_visible(TextBoxPageLocators.EMAIL).send_keys(data.email)
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS).send_keys(data.current_address)
        self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS).send_keys(data.permanent_address)
        self.element_is_visible(TextBoxPageLocators.SUBMIT).click()

    @allure.step("Получение результата")
    def get_result_submit(self, data: TextBox) -> TextBox:
        fields = {
            "full_name": (
                data.full_name,
                TextBoxPageLocators.NAME_RESULT,
            ),
            "email": (
                data.email,
                TextBoxPageLocators.EMAIL_RESULT,
            ),
            "current_address": (
                data.current_address,
                TextBoxPageLocators.CURRENT_ADDRESS_RESULT,
            ),
            "permanent_address": (
                data.permanent_address,
                TextBoxPageLocators.PERMANENT_ADDRESS_RESULT,
            ),
        }

        result = {}

        for field_name, (input_value, locator) in fields.items():
            result[field_name] = (
                self.element_is_visible(locator).text
                if input_value
                else ""
            )

        return TextBox(**result)

    @allure.step("Статус поля email")
    def get_result_email_status(self) -> list[str]:
        return self.element_is_visible(TextBoxPageLocators.EMAIL).get_attribute("class").split()
