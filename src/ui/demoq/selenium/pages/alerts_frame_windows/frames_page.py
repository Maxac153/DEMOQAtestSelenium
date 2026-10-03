import allure
from selenium.webdriver.remote.webelement import WebElement

from src.ui.demoq.selenium.locators.alerts_frame_windows.frames_locators import FramesLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class FramesPage(BasePage):
    def _get_frame_data(self, frame_element: WebElement) -> list[str]:
        """Получение данных фрейма: текст заголовка, ширина, высота."""

        width = frame_element.get_attribute("width")
        height = frame_element.get_attribute("height")

        self.driver.switch_to.frame(frame_element)
        text = self.element_is_present(FramesLocators.TITLE_FRAME).text
        self.driver.switch_to.default_content()

        return [text, width, height]

    @allure.step("Получение данных фрейма {frame_num}")
    def frame(self, frame_num: str) -> list[str]:
        if frame_num == "frame1":
            with allure.step("Поиск первого фрейма"):
                frame = self.element_is_present(FramesLocators.FIRST_FRAME)
            return self._get_frame_data(frame)

        if frame_num == "frame2":
            with allure.step("Поиск второго фрейма"):
                frame = self.element_is_present(FramesLocators.SECOND_FRAME)
            return self._get_frame_data(frame)

        raise ValueError(f"Неизвестный фрейм: {frame_num}. Допустимые значения: frame1, frame2")
