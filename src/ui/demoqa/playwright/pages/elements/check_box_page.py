import random

import allure

from src.ui.demoqa.playwright.locators.elements.check_box_locators import CheckBoxLocators
from src.ui.demoqa.playwright.pages.__common.base_page import BasePage


class CheckBoxPage(BasePage):
    def _collapse_all_open_nodes(self) -> None:
        """Сворачивает все открытые узлы дерева."""
        close_switches = self.page.locator(CheckBoxLocators.SWITCH_CLOSE)

        while close_switches.count() > 0:
            for switch in close_switches.all():
                switch.click()

    @allure.step("Выбор случайного Check Box")
    def select_path(self) -> tuple[list[str], list[str]]:
        self._collapse_all_open_nodes()
        check_boxes = self.page.locator(CheckBoxLocators.CHECK_BOX)
        check_boxes.nth(random.randint(0, check_boxes.count() - 1)).click()
        selected_names = self.page.locator(CheckBoxLocators.CHECK_BOX_ACTIVE)
        select_result = [
            name.inner_text().split(".")[0].replace(" ", "").lower()
            for name in selected_names.all()
        ]

        result_items = self.page.locator(CheckBoxLocators.RESULT)
        result = [
            item.lower()
            for item in result_items.inner_text().split("\n")
        ]

        return select_result, result

    @allure.step("Выделение случайного элемента Check Box")
    def select_item(self) -> tuple[str, str]:
        self._collapse_all_open_nodes()
        select_items = self.page.locator(CheckBoxLocators.SELECT_ITEMS)
        selected_item = select_items.nth(random.randint(0, select_items.count() - 1))
        expected_item = selected_item.inner_text()
        selected_item.click()
        active_item = self.page.locator(CheckBoxLocators.SELECT_ITEM_ACTIVE)
        result = active_item.inner_text()

        return result, expected_item
