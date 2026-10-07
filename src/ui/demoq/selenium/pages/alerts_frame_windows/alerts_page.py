import random

import allure

from src.ui.demoq.selenium.locators.alerts_frame_windows.alerts_frame_windows_locators import AlertsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class AlertsPage(BasePage):
    @allure.step("Получить текст из оповещения")
    def check_see_alert(self) -> str:
        self.element_is_visible(AlertsLocators.SEE_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        result = alert.text
        alert.accept()

        return result

    @allure.step("Проверить появление уведомления через 5 секунд")
    def check_alert_appear_5_sec(self) -> str:
        self.element_is_clickable(AlertsLocators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()

        with allure.step("Дождаться появления alert"):
            alert = self.wait_alert_present()

        alert_text = alert.text

        with allure.step("Закрыть alert"):
            alert.accept()

        return alert_text

    @allure.step("Проверить, подтвердить, оповестить")
    def check_confirm_alert(self) -> str:
        self.element_is_visible(AlertsLocators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        text_result = self.element_is_present(AlertsLocators.CONFIRM_RESULT).text

        return text_result

    @allure.step("Проверить оповещение о запросе")
    def check_prompt_alert(self) -> [str, str]:
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(AlertsLocators.PROMPT_BOX_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        text_result = self.element_is_present(AlertsLocators.PROMPT_RESULT).text

        return text, text_result
