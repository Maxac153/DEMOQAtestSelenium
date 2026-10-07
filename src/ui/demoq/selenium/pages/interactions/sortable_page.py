import random

import allure

from src.ui.demoq.selenium.locators.interactions.sortable_locators import SortableLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class SortablePage(BasePage):
    @allure.step("Получить текст всех сортируемых элементов")
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)

        return [item.text for item in item_list]

    @allure.step("Открыть вкладку 'List' и изменить порядок элементов перетаскиванием")
    def change_list_order(self):
        self.element_is_visible(SortableLocators().TAB_LIST).click()
        order_before = self.get_sortable_items(SortableLocators().LIST_ITEM)

        item_list = random.sample(self.elements_are_visible(SortableLocators().LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]

        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(SortableLocators().LIST_ITEM)

        return order_before, order_after

    @allure.step("Открыть вкладку 'Grid' и изменить порядок элементов сетки перетаскиванием")
    def change_grid_order(self):
        self.element_is_visible(SortableLocators().TAB_GRID).click()
        order_before = self.get_sortable_items(SortableLocators().GRID_ITEM)

        item_list = random.sample(self.elements_are_visible(SortableLocators().GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]

        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(SortableLocators().GRID_ITEM)

        return order_before, order_after
