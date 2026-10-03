import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.locators.alerts_frame_windows.browser_windows_locators import BrowserWindowsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class WindowsPage(BasePage):
    def _switch_to_new_window(self):
        """Переключение на новое окно/вкладку с ожиданием."""
        current_window = self.driver.current_window_handle
        # TODO переделать
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        for handle in self.driver.window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                return handle
        raise RuntimeError("Новое окно не открылось")

    def _return_to_original_window(self, original_handle: str):
        """Закрытие текущего окна и возврат к исходному."""
        self.driver.close()
        self.driver.switch_to.window(original_handle)

    @allure.step("Открытие новой вкладки")
    def opened_new_tab(self):
        original_window = self.driver.current_window_handle
        self.element_is_visible(BrowserWindowsLocators.NEW_TAB_BUTTON).click()
        self._switch_to_new_window()
        text_title = self.element_is_present(BrowserWindowsLocators.TITLE_NEW).text
        self._return_to_original_window(original_window)

        return text_title

    @allure.step("Открытие нового окна")
    def opened_new_window(self):
        original_window = self.driver.current_window_handle
        self.element_is_visible(BrowserWindowsLocators.NEW_WINDOW_BUTTON).click()
        self._switch_to_new_window()
        text_title = self.element_is_present(BrowserWindowsLocators.TITLE_NEW).text
        self._return_to_original_window(original_window)

        return text_title

    @allure.step("Открытие окна с алертом")
    def opened_new_window_with_message(self):
        original_window = self.driver.current_window_handle
        self.element_is_visible(BrowserWindowsLocators.NEW_WINDOW_MESSAGE_BUTTON).click()
        self._switch_to_new_window()
        alert = WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        text = alert.text
        self._return_to_original_window(original_window)

        return text
