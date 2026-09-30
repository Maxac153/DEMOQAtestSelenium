import allure

from src.ui.demoq.selenium.locators.widgets.menu_locators import MenuLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class MenuPage(BasePage):
    @allure.step('check menu item')
    def check_menu(self) -> list[str]:
        menu_item_list = self.elements_are_present(MenuLocators().MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)

        return data
