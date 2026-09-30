import allure

from src.ui.demoq.selenium.locators.widgets.tabs_locators import TabsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class TabsPage(BasePage):
    @allure.step("check tabs")
    def check_tabs(self, name_tab):
        tabs = {
            "what": {
                "title": TabsLocators().TABS_WHAT,
                "content": TabsLocators().TABS_WHAT_CONTENT
            },
            "origin": {
                "title": TabsLocators().TABS_ORIGIN,
                "content": TabsLocators().TABS_ORIGIN_CONTENT
            },
            "use": {
                "title": TabsLocators().TABS_USE,
                "content": TabsLocators().TABS_USE_CONTENT
            },
            "more": {
                "title": TabsLocators().TABS_MORE,
                "content": TabsLocators().TABS_MORE_CONTENT
            }
        }

        button = self.element_is_visible(tabs[name_tab]["title"])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]["content"]).text

        return button.text, len(what_content)
