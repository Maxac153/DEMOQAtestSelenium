import allure

from src.ui.demoq.selenium.locators.widgets.tool_tips_locators import (
    ToolTipsLocators,
)
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class ToolTipsPage(BasePage):
    @allure.step("Получение текста всплывающей подсказки")
    def get_tooltip_text(self, hover_locator, tooltip_locator):
        element = self.element_is_present(hover_locator)
        self.action_move_to_element(element)
        self.element_is_visible(tooltip_locator)

        tooltip = self.element_is_visible(
            ToolTipsLocators().TOOL_TIPS_INNERS
        )

        return tooltip.text

    def get_tooltip_text_by_type(self, tooltip_type):
        locators = ToolTipsLocators()
        tooltip_locators = {
            "button": (
                locators.BUTTON,
                locators.TOOL_TIP_BUTTON,
            ),
            "field": (
                locators.FIELD,
                locators.TOOL_TIP_FIELD,
            ),
            "contrary": (
                locators.CONTRARY_LINK,
                locators.TOOL_TIP_CONTRARY,
            ),
            "section": (
                locators.SECTION_LINK,
                locators.TOOL_TIP_SECTION,
            ),
        }
        hover_locator, tooltip_locator = tooltip_locators[tooltip_type]

        return self.get_tooltip_text(
            hover_locator,
            tooltip_locator,
        )
