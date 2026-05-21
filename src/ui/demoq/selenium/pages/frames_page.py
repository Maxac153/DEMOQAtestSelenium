from src.ui.demoq.selenium.locators.frames_page_locators import FramesPageLocators
from src.ui.demoq.selenium.pages.base_page import BasePage


class FramesPage(BasePage):
    def check_frame(self):
        """Проверка текста"""

        result = self.element_is_visible(FramesPageLocators.HEADING).text
        return result
