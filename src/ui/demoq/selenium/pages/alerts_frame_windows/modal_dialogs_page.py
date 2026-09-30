import allure

from src.ui.demoq.selenium.locators.alerts_frame_windows.modal_dialogs_locators import ModalDialogsLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class ModalDialogsPage(BasePage):
    @allure.step('Проверить модальные диалоговые окна')
    def check_modal_dialogs(self):
        self.element_is_visible(ModalDialogsLocators().SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(ModalDialogsLocators().TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(ModalDialogsLocators().BODY_SMALL_MODAL).text
        self.element_is_visible(ModalDialogsLocators().SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(ModalDialogsLocators().LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(ModalDialogsLocators().TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(ModalDialogsLocators().BODY_LARGE_MODAL).text
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]
