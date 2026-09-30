from selenium.webdriver.common.by import By


class ModalDialogsLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')