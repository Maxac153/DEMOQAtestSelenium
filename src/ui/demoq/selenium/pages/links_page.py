from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.demoq.selenium.locators.links_locators import LinksLocators
from src.ui.demoq.selenium.modules.Links import Links
from src.ui.demoq.selenium.pages.base_page import BasePage


class LinksPage(BasePage):
    def open_new_tab(self, select_links: Links) -> str:
        """Открытие новой вкладки"""

        old_handles = self.driver.window_handles

        match select_links:
            case Links.SIMPLE_LINK_LINK:
                self.element_is_visible(LinksLocators.SIMPLE_LINK_LINK).click()
            case Links.DYNAMIC_LINK_LINK:
                self.element_is_visible(LinksLocators.DYNAMIC_LINK_LINK).click()

        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(old_handles))
        new_handle = [h for h in self.driver.window_handles if h not in old_handles][0]
        self.driver.switch_to.window(new_handle)

        return self.driver.title

    def click_links(self, select_links: Links) -> str:
        """Нажатие на ссылку"""

        match select_links:
            case Links.CREATED_LINK:
                self.element_is_visible(LinksLocators.CREATED_LINK).click()
            case Links.NO_CONTENT_LINK:
                self.element_is_visible(LinksLocators.NO_CONTENT_LINK).click()
            case Links.MOVED_LINK:
                self.element_is_visible(LinksLocators.MOVED_LINK).click()
            case Links.BAD_REQUEST_LINK:
                self.element_is_visible(LinksLocators.BAD_REQUEST_LINK).click()
            case Links.UNAUTHORIZED_LINK:
                self.element_is_visible(LinksLocators.UNAUTHORIZED_LINK).click()
            case Links.FORBIDDEN_LINK:
                self.element_is_visible(LinksLocators.FORBIDDEN_LINK).click()
            case Links.INVALID_URL_LINK:
                self.element_is_visible(LinksLocators.INVALID_URL_LINK).click()

        return self.element_is_visible(LinksLocators.RESULT).text
