import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from src.ui.demoqa.__common.models.elements.broken_images import BrokenImages
from src.ui.demoqa.__common.models.elements.broken_links import BrokenLinks
from src.ui.demoqa.selenium.locators.elements.broken_links_and_images_locators import (
    BrokenLinksAndImagesLinksLocators,
)
from src.ui.demoqa.selenium.pages.__common.base_page import BasePage


class BrokenLinksAndImagesPage(BasePage):
    @allure.step("Проверить загрузку изображения ({image})")
    def select_image(self, image: BrokenImages, timeout: int = 10) -> bool:
        """Дождаться завершения загрузки изображения и вернуть True, если оно загрузилось."""
        locator = {
            BrokenImages.VALID_IMAGE: BrokenLinksAndImagesLinksLocators.VALID_IMAGE,
            BrokenImages.BROKEN_IMAGE: BrokenLinksAndImagesLinksLocators.BROKEN_IMAGE,
        }[image]

        image_element = self.element_is_visible(locator)

        self._wait_image_loading_finished(image_element, timeout)

        return self.driver.execute_script(
            "return arguments[0].naturalWidth > 0;",
            image_element,
        )

    def _wait_image_loading_finished(
            self,
            image: WebElement,
            timeout: int = 10,
    ) -> None:
        """Ждёт, пока браузер завершит обработку изображения: success или error."""

        def image_is_completed(driver: WebDriver) -> bool:
            return driver.execute_script(
                "return arguments[0].complete === true;",
                image,
            )

        WebDriverWait(self.driver, timeout).until(image_is_completed)

    @allure.step("Открыть ссылку в новой вкладке ({select_links})")
    def open_new_tab(self, select_links: BrokenLinks) -> str:
        locator = {
            BrokenLinks.VALID_LINK: BrokenLinksAndImagesLinksLocators.VALID_LINK,
            BrokenLinks.BROKEN_LINK: BrokenLinksAndImagesLinksLocators.BROKEN_LINK,
        }[select_links]

        self.element_is_clickable(locator).click()

        return self.driver.title
