import allure

from src.ui.demoq.selenium.locators.widgets.menu_locators import MenuLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class MenuPage(BasePage):
    @allure.step("Навести курсор на каждый пункт меню и получить их названия")
    def get_menu_items(self) -> list[str]:
        menu_item_list = self.elements_are_present(MenuLocators().MENU_ITEM_LIST)
        menu_items = []

        for item in menu_item_list:
            self.action_move_to_element(item)
            menu_items.append(item.text)

        return menu_items
