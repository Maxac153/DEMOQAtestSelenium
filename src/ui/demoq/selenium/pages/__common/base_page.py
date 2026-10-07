from typing import List, Tuple

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait

Locator = Tuple[str, str]


class BasePage:
    """Базовый Page Object с общими методами ожидания и действий Selenium."""

    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Дождаться видимости одного элемента")
    def element_is_visible(self, locator: Locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("Дождаться видимости всех элементов")
    def elements_are_visible(self, locator: Locator, timeout: int = 5) -> List[WebElement]:
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step("Дождаться исчезновения элемента")
    def element_is_invisible(self, locator: Locator, timeout: int = 5) -> bool:
        return Wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    @allure.step("Проскроллить страницу к элементу")
    def go_to_element(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Дождаться кликабельности элемента")
    def element_is_clickable(self, locator: Locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    @allure.step("Дождаться присутствия элемента в DOM")
    def element_is_present(self, locator: Locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step("Дождаться присутствия всех элементов в DOM")
    def elements_are_present(self, locator: Locator, timeout: int = 5) -> List[WebElement]:
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    @allure.step("Получить видимый элемент для чтения атрибута class")
    def class_attribute(self, locator: Locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("Перетащить элемент со смещением: x={x_coords}, y={y_coords}")
    def action_drag_and_drop_by_offset(self, element: WebElement, x_coords: int, y_coords: int) -> None:
        ActionChains(self.driver).drag_and_drop_by_offset(element, x_coords, y_coords).perform()

    @allure.step("Перетащить один элемент на другой")
    def action_drag_and_drop_to_element(self, source: WebElement, target: WebElement) -> None:
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Навести курсор на элемент")
    def action_move_to_element(self, element: WebElement) -> None:
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Получить объект ActionChains")
    def action_chains(self) -> ActionChains:
        return ActionChains(self.driver)

    @allure.step("Дождаться видимости вложенного элемента")
    def child_element_is_visible(self, parent_element: WebElement, locator: Locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.visibility_of(parent_element.find_element(*locator)))

    @allure.step("Дождаться присутствия элемента")
    def wait_element_present(self, locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step("Дождаться видимости элемента")
    def wait_element_visible(self, locator, timeout: int = 5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("Дождаться присутствия всех элементов")
    def wait_elements_present(self, locator, timeout: int = 5) -> List[WebElement]:
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    @allure.step("Дождаться видимости всех элементов")
    def wait_elements_visible(self, locator, timeout: int = 5) -> List[WebElement]:
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step("Дождаться изменения атрибута элемента")
    def wait_attribute_change(self, element: WebElement, attribute: str, old_value: str, timeout: int = 5) -> str:
        return Wait(self.driver, timeout).until(lambda _: element.get_attribute(attribute) != old_value)

    @allure.step("Дождаться появления alert")
    def wait_alert_present(self, timeout: int = 5, poll_frequency: float = 0.2) -> Alert:
        return Wait(self.driver, timeout, poll_frequency=poll_frequency).until(ec.alert_is_present())

    @allure.step("Дождаться открытия нового окна или вкладки")
    def wait_new_window(self, current_window: str, timeout: int = 5) -> str:
        return Wait(self.driver, timeout).until(
            lambda driver: next((
                handle
                for handle in driver.window_handles
                if handle != current_window
            ), False))

    @allure.step("Дождаться открытия нового окна или вкладки")
    def wait_new_window(self, current_window: str, timeout: int = 5) -> str:
        return Wait(self.driver, timeout).until(lambda driver: next((
            handle
            for handle in driver.window_handles
            if handle != current_window
        ), False))

    @allure.step("Переключиться на новое окно или вкладку")
    def switch_to_new_window(self, timeout: int = 5) -> str:
        current_window = self.driver.current_window_handle
        new_window = self.wait_new_window(current_window, timeout)
        self.driver.switch_to.window(new_window)

        return new_window
