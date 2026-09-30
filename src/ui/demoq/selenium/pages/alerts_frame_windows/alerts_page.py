import random

import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.locators.alerts_frame_windows.alerts_frame_windows_locators import AlertsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class AlertsPage(BasePage):
    @allure.step('Получить текст из оповещения')
    def check_see_alert(self):
        self.element_is_visible(AlertsLocators.SEE_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        result = alert.text
        alert.accept()

        return result

    @allure.step('Уведомление появляется через 5 секунд')
    def check_alert_appear_5_sec(self):
        self.element_is_visible(AlertsLocators.APPEAR_ALERT_AFTER_5_Sec_BUTTON).click()
        # TODO Убрать все WebDriverWait из Page в BasePage
        alert = WebDriverWait(self.driver, timeout=10, poll_frequency=0.2).until(ec.alert_is_present())
        alert_text = alert.text
        alert.accept()

        return alert_text

    @allure.step('Проверить, подтвердить, оповестить')
    def check_confirm_alert(self):
        self.element_is_visible(AlertsLocators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        text_result = self.element_is_present(AlertsLocators.CONFIRM_RESULT).text

        return text_result

    @allure.step('Проверить оповещение о запросе')
    def check_prompt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(AlertsLocators.PROMPT_BOX_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        text_result = self.element_is_present(AlertsLocators.PROMPT_RESULT).text

        return text, text_result
