import allure
from selenium.webdriver.support.select import Select

from src.ui.demoq.selenium.generator.generator import generated_date
from src.ui.demoq.selenium.locators.widgets.date_picker_locators import DatePickerLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class DatePickerPage(BasePage):
    @allure.step('change date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(DatePickerLocators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(DatePickerLocators.DATE_SELecT_MONTH, date.month)
        self.set_date_by_text(DatePickerLocators.DATE_SELecT_YEAR, date.year)
        self.set_date_item_from_list(DatePickerLocators.DATE_SELecT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('change select date and time')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(DatePickerLocators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(DatePickerLocators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(DatePickerLocators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(DatePickerLocators.DATE_SELecT_DAY_LIST, date.day)
        self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(DatePickerLocators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('select date by text')
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('select date item form list')
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
