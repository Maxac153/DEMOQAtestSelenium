from typing import List

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    @allure.step("Открытие страницы")
    def open(self):
        """Открытие страницы"""

        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout: int = 5) -> WebElement:
        """Найти один элемент на странице"""

        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout: int = 5) -> List[WebElement]:
        """Найти все элементы на странице"""

        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_invisible(self, locator, timeout: int = 5) -> bool:
        """Дождаться исчезновения элемента со страницы."""

        return Wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    #TODO исправить на рус
    @allure.step('Go to specified element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Find clickable elements')
    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    @allure.step('Найдите присутствующий элемент')
    def element_is_present(self, locator, timeout=5) -> WebElement:
        """Найдите присутствующий элемент"""

        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def class_attribute(self, locator, timeout: int = 5) -> WebElement:
        """Параметры атрибута"""

        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))


    @allure.step('Drag and drop by offset')
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step('Drag and drop element to element')
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step('Move cursor to element')
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_chains(self):
        """Возврат объект ActionChains движения мыши"""

        return ActionChains(self.driver)
