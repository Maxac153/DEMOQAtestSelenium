import allure

from src.ui.demoq.selenium.locators.widgets.tool_tips_locators import ToolTipsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class ToolTipsPage(BasePage):
    @allure.step("get text form tool tip")
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(ToolTipsLocators().TOOL_TIPS_INNERS)
        text = tool_tip_text.text

        return text

    @allure.step("check tool tip")
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(
            ToolTipsLocators().BUTTON, ToolTipsLocators().TOOL_TIP_BUTTON
        )
        tool_tip_text_field = self.get_text_from_tool_tips(
            ToolTipsLocators().FIELD, ToolTipsLocators().TOOL_TIP_FIELD
        )
        tool_tip_text_contrary = self.get_text_from_tool_tips(
            ToolTipsLocators().CONTRARY_LINK,
            ToolTipsLocators().TOOL_TIP_CONTRARY
        )
        tool_tip_text_section = self.get_text_from_tool_tips(
            ToolTipsLocators().SECTION_LINK,
            ToolTipsLocators().TOOL_TIP_SecTION
        )

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
