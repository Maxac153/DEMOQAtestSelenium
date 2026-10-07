import random

import allure

from src.ui.demoq.selenium.locators.interactions.selectable_locators import SelectableLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class SelectablePage(BasePage):
    @allure.step("Выбрать случайный элемент из списка")
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step("Открыть вкладку 'List' и выбрать случайный элемент списка")
    def select_list_item(self):
        self.element_is_visible(SelectableLocators().TAB_LIST).click()
        self.click_selectable_item(SelectableLocators().LIST_ITEM)
        active_element = self.element_is_visible(SelectableLocators().LIST_ITEM_ACTIVE)

        return active_element.text

    @allure.step("Открыть вкладку 'Grid' и выбрать случайный элемент сетки")
    def select_grid_item(self):
        self.element_is_visible(SelectableLocators().TAB_GRID).click()
        self.click_selectable_item(SelectableLocators().GRID_ITEM)
        active_element = self.element_is_visible(SelectableLocators().GRID_ITEM_ACTIVE)

        return active_element.text