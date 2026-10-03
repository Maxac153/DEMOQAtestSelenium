import allure

from src.ui.demoq.selenium.locators.alerts_frame_windows.nested_frames_locators import NestedFramesLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class NestedFramesPage(BasePage):
    @allure.step("Получение содержимого вложенных фреймов")
    def check_nested_frame(self) -> tuple[str, str]:
        with allure.step("Переключение на родительский фрейм"):
            parent_frame = self.element_is_present(NestedFramesLocators.PARENT_FRAME)
            self.driver.switch_to.frame(parent_frame)
            parent_text = self.element_is_present(NestedFramesLocators.PARENT_TEXT).text

        with allure.step("Переключение на дочерний фрейм"):
            child_frame = self.element_is_present(NestedFramesLocators.CHILD_FRAME)
            self.driver.switch_to.frame(child_frame)
            child_text = self.element_is_present(NestedFramesLocators.CHILD_TEXT).text

        with allure.step("Возврат в основное содержимое"):
            self.driver.switch_to.default_content()

        return parent_text, child_text
