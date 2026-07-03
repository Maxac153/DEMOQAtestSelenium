import allure
import requests

from src.ui.demoq.selenium.locators.elements.broken_links_and_images_locators import BrokenLinksAndImagesLinksLocators
from src.ui.demoq.selenium.modules.elements.broken_images import BrokenImages
from src.ui.demoq.selenium.modules.elements.broken_links import BrokenLinks
from src.ui.demoq.selenium.pages.base_page import BasePage


class BrokenLinksAndImagesPage(BasePage):
    @classmethod
    def _is_broken_image(cls, url: str) -> bool:
        try:
            r = requests.get(url, timeout=10)
            return not (r.status_code == 200 and r.headers.get("Content-Type", "").startswith("image/"))
        except requests.RequestException:
            return True

    @allure.step("Нажатие на Links ({image})")
    def select_image(self, image: BrokenImages) -> bool:
        """Проверка images"""

        img = ""
        match image:
            case BrokenImages.VALID_IMAGE:
                img = self.element_is_visible(BrokenLinksAndImagesLinksLocators.VALID_IMAGE)
            case BrokenImages.BROKEN_IMAGE:
                img = self.element_is_visible(BrokenLinksAndImagesLinksLocators.BROKEN_IMAGE)

        return self.driver.execute_script("return arguments[0].naturalWidth > 0", img)

    @allure.step("Нажатие на Links ({select_links})")
    def open_new_tab(self, select_links: BrokenLinks) -> str:
        """Нажатие на ссылку"""

        match select_links:
            case BrokenLinks.VALID_LINK:
                self.element_is_visible(BrokenLinksAndImagesLinksLocators.VALID_LINK).click()
            case BrokenLinks.BROKEN_LINK:
                self.element_is_visible(BrokenLinksAndImagesLinksLocators.BROKEN_LINK).click()

        return self.driver.title
