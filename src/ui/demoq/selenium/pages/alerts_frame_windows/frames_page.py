import allure

from src.ui.demoq.selenium.locators.alerts_frame_windows.frames_locators import FramesLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class FramesPage(BasePage):
    @allure.step('check frame')
    def frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(FramesLocators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(FramesLocators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == 'frame2':
            frame = self.element_is_present(FramesLocators.SecOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(FramesLocators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
