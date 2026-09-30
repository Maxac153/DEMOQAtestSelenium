import allure

from src.ui.demoq.selenium.locators.alerts_frame_windows.nested_frames_locators import NestedFramesLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class NestedFramesPage(BasePage):
    @allure.step('Проверить вложенный фрейм')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(NestedFramesLocators().PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(NestedFramesLocators().PARENT_TEXT).text
        child_frame = self.element_is_present(NestedFramesLocators().CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(NestedFramesLocators().CHILD_TEXT).text

        return parent_text, child_text
