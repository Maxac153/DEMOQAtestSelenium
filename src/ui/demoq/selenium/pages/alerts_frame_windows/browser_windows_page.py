import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.locators.alerts_frame_windows.browser_windows_locators import BrowserWindowsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class WindowsPage(BasePage):
    @allure.step("Переключиться на новое окно или вкладку")
    def switch_to_new_window(self, timeout: int = 5) -> str:
        current_window = self.driver.current_window_handle
        new_window = self.wait_new_window(current_window, timeout)
        self.driver.switch_to.window(new_window)

        return new_window

    @allure.step("Переключиться на новое окно или вкладку")
    def _switch_to_new_window(self) -> str:
        return self.switch_to_new_window()

    def _return_to_original_window(self, original_handle: str):
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
