from src.ui.demoq.selenium.locators.droppable_page_locators import DroppablePageLocators
from src.ui.demoq.selenium.pages.base_page import BasePage


class DragAndDropPage(BasePage):
    def check_drag_and_drop(self):
        """Проверка перемещения элемента"""

        drop = self.element_is_visible(DroppablePageLocators.DROPPABLE)
        drag = self.element_is_visible(DroppablePageLocators.DROGGABLE)
        self.drag_and_drop(drag, drop)
        return drag.text
