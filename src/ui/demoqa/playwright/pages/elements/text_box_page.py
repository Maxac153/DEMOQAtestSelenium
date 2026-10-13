import allure
from playwright.sync_api import expect

from src.ui.demoqa.__common.models.elements.text_box import TextBox
from src.ui.demoqa.playwright.locators.elements.text_box_locators import TextBoxPageLocators
from src.ui.demoqa.playwright.pages.__common.base_page import BasePage


class TextBoxPage(BasePage):
    @allure.step("Отправка формы")
    def submit_form(self, data: TextBox) -> None:
        self.page.locator(TextBoxPageLocators.FULL_NAME).fill(data.full_name or "")
        self.page.locator(TextBoxPageLocators.EMAIL).fill(data.email or "")
        self.page.locator(TextBoxPageLocators.CURRENT_ADDRESS).fill(
            data.current_address or ""
        )
        self.page.locator(TextBoxPageLocators.PERMANENT_ADDRESS).fill(
            data.permanent_address or ""
        )
        self.page.locator(TextBoxPageLocators.SUBMIT).click()

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
            )
        }

        result = {}
        for field_name, (input_value, selector) in fields.items():
            if not input_value:
                result[field_name] = ""
                continue

            result[field_name] = self.page.locator(selector).inner_text()

        return TextBox(**result)

    @allure.step("Проверка статуса поля email")
    def expect_email_has_error(self) -> None:
        expect(self.page.locator(TextBoxPageLocators.EMAIL)).to_contain_class("field-error")
