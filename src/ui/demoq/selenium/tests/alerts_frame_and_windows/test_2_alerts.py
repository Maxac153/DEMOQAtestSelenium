import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.alerts_frame_windows.alerts_page import AlertsPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.ALERTS.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Alerts")
class TestAlertsPage:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия алерта")
    @allure.title("Проверка открытия оповещения")
    def test_text_box_email(self, driver: WebDriver):
        alert_page = AlertsPage(driver, BASE_URL)
        alert_page.open()
        alert_text = alert_page.check_see_alert()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert alert_text == "You clicked a button", "Уведомление не появилось"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия алерта")
    @allure.title("Проверка открытия оповещения через 5 секунд")
    def test_alert_appear_5_sec(self, driver: WebDriver):
        alert_page = AlertsPage(driver, BASE_URL)
        alert_page.open()
        alert_text = alert_page.check_alert_appear_5_sec()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert alert_text == "This alert appeared after 5 seconds", "Уведомление не появилось"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия алерта")
    @allure.title("Проверка срабатывания оповещения с подтверждением")
    def test_confirm_alert(self, driver: WebDriver):
        alert_page = AlertsPage(driver, BASE_URL)
        alert_page.open()
        alert_text = alert_page.check_confirm_alert()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert alert_text == "You selected Ok", "Вы нажали «ОК», но оповещение не появилось"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка открытия алерта")
    @allure.title("Проверка открытия оповещения с запросом")
    def test_prompt_alert(self, driver: WebDriver):
        alert_page = AlertsPage(driver, BASE_URL)
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()

        with allure.step("Проверка соответствия отправленных и отображаемых данных"):
            assert text in alert_text, "Уведомление не появилось"
