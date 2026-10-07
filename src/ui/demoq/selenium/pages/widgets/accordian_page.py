import allure
from _pytest.mark import ParameterSet

from src.ui.demoq.selenium.locators.widgets.accordian_locators import AccordianLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class AccordionPage(BasePage):
    @allure.step("Открыть секцию аккордеона и получить её заголовок и текст")
    def open_accordion_section(self, accordion_num: ParameterSet):
        accordian = {
            "first": AccordianLocators.SECTION_FIRST,
            "second": AccordianLocators.SECTION_SECOND,
            "third": AccordianLocators.SECTION_THIRD,
        }

        section = self.element_is_visible(accordian[accordion_num])
        button = section.find_element(*AccordianLocators.SECTION_BUTTON)
        button.click()
        body = self.child_element_is_visible(section, AccordianLocators.SECTION_BODY)
        text = body.text.strip()

        return button.text.strip(), bool(text)