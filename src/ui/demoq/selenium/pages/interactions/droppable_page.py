import allure

from src.ui.demoq.selenium.locators.interactions.droppable_locators import DroppableLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class DroppablePage(BasePage):
    @allure.step("Открыть вкладку 'Simple' и перетащить элемент в зону сброса")
    def drop_simple(self):
        self.element_is_visible(DroppableLocators().SIMPLE_TAB).click()
        drag_div = self.element_is_visible(DroppableLocators().DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(DroppableLocators().DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)

        return drop_div.text

    @allure.step("Открыть вкладку 'Accept' и проверить перетаскивание допустимого и недопустимого элементов")
    def drop_accept(self):
        self.element_is_visible(DroppableLocators().ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(DroppableLocators().ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(DroppableLocators().NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(DroppableLocators().DROP_HERE_ACCEPT)

        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text

        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text

        return drop_text_not_accept, drop_text_accept

    @allure.step("Открыть вкладку 'Prevent Propogation' и перетащить элемент во внутренние зоны сброса")
    def drop_prevent_propagation(self):
        self.element_is_visible(DroppableLocators().PREVENT_TAB).click()
        drag_div = self.element_is_visible(DroppableLocators().DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(DroppableLocators().NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(DroppableLocators().GREEDY_INNER_BOX)

        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(DroppableLocators().NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text

        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(DroppableLocators().GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text

        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    @allure.step("Открыть вкладку 'Revert Draggable' и перетащить элемент в зону сброса")
    def drop_revert_draggable(self, type_drag):
        drags = {
            "will": {
                "revert": DroppableLocators().WILL_REVERT,
            },
            "not_will": {
                "revert": DroppableLocators().NOT_REVERT
            },
        }
        self.element_is_visible(DroppableLocators().REVERT_TAB).click()
        revert = self.element_is_visible(drags[type_drag]["revert"])
        drop_div = self.element_is_visible(DroppableLocators().DROP_HERE_REVERT)

        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute("style")
        position_after_revert = self.wait_attribute_change(
            element=revert,
            attribute="style",
            old_value=position_after_move,
        )

        return position_after_move, position_after_revert
