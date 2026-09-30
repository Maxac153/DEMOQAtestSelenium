import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.locators.widgets.accordian_locators import AccordianLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class AccordianPage(BasePage):
    @allure.step("check accordian widget")
    def check_accordian(self, accordian_num: str):
        accordian = {
            "first": AccordianLocators.SecTION_FIRST,
            "second": AccordianLocators.SecTION_SecOND,
            "third": AccordianLocators.SecTION_THIRD,
        }

        # 1. Находим секцию
        section = self.element_is_visible(accordian[accordian_num])

        # 2. Находим кнопку внутри секции и кликаем
        button = section.find_element(*AccordianLocators.SecTION_BUTTON)
        button.click()

        # 3. Ждём видимости accordion-body ВНУТРИ этой секции
        # TODO Переделать
        wait = WebDriverWait(self.driver, 10)
        body = wait.until(ec.visibility_of(section.find_element(*AccordianLocators.SecTION_BODY)))

        text = body.text.strip()
        return button.text.strip(), bool(text)
