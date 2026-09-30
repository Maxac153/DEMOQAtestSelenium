import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.locators.alerts_frame_windows.browser_windows_locators import BrowserWindowsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class WindowsPage(BasePage):

    @allure.step('Открытие новой вкладки')
    def opened_new_tab(self):
        self.element_is_visible(BrowserWindowsLocators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(BrowserWindowsLocators.TITLE_NEW).text

        return text_title

    @allure.step('Открытие нового окна')
    def opened_new_window(self):
        self.element_is_visible(BrowserWindowsLocators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(BrowserWindowsLocators.TITLE_NEW).text

        return text_title

    @allure.step('Открытие нового окна c сообщением')
    def opened_new_window_with_message(self):
        self.element_is_visible(BrowserWindowsLocators.NEW_WINDOW_MESSAGE_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        alert = WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        text = alert.text

        return text
