import random
import re

import allure

from src.ui.demoq.selenium.locators.interactions.draggable_locators import DraggableLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class DraggablePage(BasePage):
    @allure.step("get before and after positions")
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute("style")
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute("style")
        
        return before_position, after_position

    @allure.step("simple drag and drop")
    def simple_drag_box(self):
        self.element_is_visible(DraggableLocators().SIMPLE_TAB).click()
        drag_div = self.element_is_visible(DraggableLocators().DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        
        return before_position, after_position

    @allure.step("get top position")
    def get_top_position(self, positions):
        return re.findall(r"\d[0-9]|\d", positions.split(";")[2])

    @allure.step("get left position")
    def get_left_position(self, positions):
        return re.findall(r"\d[0-9]|\d", positions.split(";")[1])

    @allure.step("drag only_x")
    def axis_restricted_x(self):
        self.element_is_visible(DraggableLocators().AXIS_TAB).click()
        only_x = self.element_is_visible(DraggableLocators().ONLY_X)
        position_x = self.get_before_and_after_position(only_x)
        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])
        
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    @allure.step("drag only_y")
    def axis_restricted_y(self):
        self.element_is_visible(DraggableLocators().AXIS_TAB).click()
        only_y = self.element_is_visible(DraggableLocators().ONLY_Y)
        position_x = self.get_before_and_after_position(only_y)
        top_y_before = self.get_top_position(position_x[0])
        top_y_after = self.get_top_position(position_x[1])
        left_y_before = self.get_left_position(position_x[0])
        left_y_after = self.get_left_position(position_x[1])
        
        return [top_y_before, top_y_after], [left_y_before, left_y_after]
