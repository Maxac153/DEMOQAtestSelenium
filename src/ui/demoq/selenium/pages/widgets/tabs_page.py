import allure

from src.ui.demoq.selenium.locators.widgets.tabs_locators import TabsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class TabsPage(BasePage):
    @allure.step("Открытие вкладки «{tab_name}» и получение её содержимого")
    def open_tab_and_get_content_length(self, tab_name):
        locators = TabsLocators()
        tabs = {
            "what": {
                "title": locators.TABS_WHAT,
                "content": locators.TABS_WHAT_CONTENT,
            },
            "origin": {
                "title": locators.TABS_ORIGIN,
                "content": locators.TABS_ORIGIN_CONTENT,
            },
            "use": {
                "title": locators.TABS_USE,
                "content": locators.TABS_USE_CONTENT,
            },
            "more": {
                "title": locators.TABS_MORE,
                "content": locators.TABS_MORE_CONTENT,
            },
        }

        tab = self.element_is_visible(tabs[tab_name]["title"])
        tab.click()
        content = self.element_is_visible(tabs[tab_name]["content"]).text

        return tab.text, len(content)
