import random

import allure

from src.ui.demoq.selenium.locators.interactions.resizable_locators import ResizableLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class ResizablePage(BasePage):
    @allure.step("Получить значения ширины и высоты в пикселях из атрибута style")
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].replace(" ", "")
        height = value_of_size.split(";")[1].split(":")[1].replace(" ", "")

        return width, height

    @allure.step("Получить текущий размер элемента из атрибута style")
    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute("style")

        return size_value

    @allure.step("Открыть вкладку 'Resizable Box' и изменить размер блока до максимального и минимального")
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(
            self.element_is_present(ResizableLocators().RESIZABLE_BOX_HANDLE),
            400,
            200
        )
        max_size = self.get_px_from_width_height(self.get_max_min_size(ResizableLocators().RESIZABLE_BOX))

        self.action_drag_and_drop_by_offset(
            self.element_is_present(ResizableLocators().RESIZABLE_BOX_HANDLE),
            -500,
            -300
        )
        min_size = self.get_px_from_width_height(self.get_max_min_size(ResizableLocators().RESIZABLE_BOX))

        return max_size, min_size

    @allure.step("Изменить размер элемента 'Resizable' в случайную сторону")
    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(
            self.element_is_visible(ResizableLocators().RESIZABLE_HANDLE),
            random.randint(1, 300),
            random.randint(1, 300)
        )
        max_size = self.get_px_from_width_height(self.get_max_min_size(ResizableLocators().RESIZABLE))

        self.action_drag_and_drop_by_offset(
            self.element_is_visible(ResizableLocators().RESIZABLE_HANDLE),
            random.randint(-200, -1),
            random.randint(-200, -1)
        )
        min_size = self.get_px_from_width_height(self.get_max_min_size(ResizableLocators().RESIZABLE))

        return max_size, min_size