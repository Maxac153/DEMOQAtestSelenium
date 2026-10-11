import allure
from playwright.sync_api import Page


class BasePage:
    """Базовый Page Object с общими методами ожидания и действий Playwright."""

    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url

    @allure.step("Открыть страницу")
    def open(self) -> None:
        self.page.goto(self.url, wait_until="load")
