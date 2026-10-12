import re

import allure
from selenium.webdriver.remote.webelement import WebElement

from src.ui.demoq.__common.models.elements.links import Links
from src.ui.demoq.selenium.locators.elements.links_locators import LinksLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class LinksPage(BasePage):
    @allure.step("Открыть ссылку в новой вкладке: {select_links}")
    def open_new_tab(self, select_links: Links, timeout: int = 10) -> str:
        """Открывает ссылку в новой вкладке и возвращает её title."""
        locator = self._new_tab_link_locators()[select_links]

        self.element_is_clickable(locator).click()
        self.switch_to_new_window(timeout)

        return self.driver.title

    @allure.step("Получить HTTP-статус ответа для ссылки ({link})")
    def get_link_response_status(self, link: Links, timeout: int = 10) -> int:
        """Кликает по ссылке и возвращает HTTP-статус из блока с результатом."""
        locator = self._response_link_locators()[link]

        self.element_is_clickable(locator).click()

        response_element: WebElement = self.element_is_visible(
            LinksLocators.RESULT,
            timeout=timeout,
        )
        response_text = response_element.text

        match = re.search(r"\b(\d{3})\b", response_text)
        if not match:
            raise AssertionError(
                f"Не удалось извлечь HTTP-статус из ответа: '{response_text}'"
            )

        return int(match.group(1))

    def _new_tab_link_locators(self) -> dict[Links, tuple[str, str]]:
        """Возвращает локаторы ссылок, открывающихся в новой вкладке."""
        return {
            Links.SIMPLE_LINK_LINK: LinksLocators.SIMPLE_LINK_LINK,
            Links.DYNAMIC_LINK_LINK: LinksLocators.DYNAMIC_LINK_LINK,
        }

    def _response_link_locators(self) -> dict[Links, tuple[str, str]]:
        """Возвращает локаторы ссылок с HTTP-ответом на странице."""
        return {
            Links.CREATED_LINK: LinksLocators.CREATED_LINK,
            Links.NO_CONTENT_LINK: LinksLocators.NO_CONTENT_LINK,
            Links.MOVED_LINK: LinksLocators.MOVED_LINK,
            Links.BAD_REQUEST_LINK: LinksLocators.BAD_REQUEST_LINK,
            Links.UNAUTHORIZED_LINK: LinksLocators.UNAUTHORIZED_LINK,
            Links.FORBIDDEN_LINK: LinksLocators.FORBIDDEN_LINK,
            Links.INVALID_URL_LINK: LinksLocators.INVALID_URL_LINK,
        }