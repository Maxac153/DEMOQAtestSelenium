import random

from selenium.common import TimeoutException

from src.ui.demoq.selenium.locators.check_box_page_locators import CheckBoxLocators
from src.ui.demoq.selenium.pages.base_page import BasePage


class CheckBoxPage(BasePage):
    def __switch_open(self) -> None:
        """Открываем все Check Box"""

        while True:
            try:
                close_switches = self.elements_are_visible(CheckBoxLocators.SWITCH_CLOSE)
            except TimeoutException:
                close_switches = []

            close_switches = [el for el in close_switches if el.is_displayed()]

            if not close_switches:
                break

            for el in close_switches:
                el.click()

    def select_path(self) -> tuple[list[str], list[str]]:
        """Проверка пути"""

        self.__switch_open()
        check_boxes = self.elements_are_visible(CheckBoxLocators.CHECK_BOX)
        random.choice(check_boxes).click()
        check_boxes_active = self.elements_are_visible(CheckBoxLocators.CHECK_BOX_ACTIVE)
        select_result = [i.text.split(".")[0].replace(" ", "").lower() for i in check_boxes_active]
        result = [i.lower() for i in self.element_is_visible(CheckBoxLocators.RESULT).text.split("\n")]
        return select_result, result

    def select_item(self) -> tuple[str, str]:
        """Проверка выделения элемента"""

        self.__switch_open()
        check_boxes = self.elements_are_visible(CheckBoxLocators.SELECT_ITEMS)
        check_box = random.choice(check_boxes)
        check_box.click()
        result = self.element_is_visible(CheckBoxLocators.SELECT_ITEM_ACTIVE).text
        return result, check_box.text
