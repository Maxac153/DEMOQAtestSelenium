from selenium.webdriver.common.by import By


class LinksLocators:
    SIMPLE_LINK_LINK = (By.CSS_SELECTOR, "a#simpleLink")
    DYNAMIC_LINK_LINK = (By.CSS_SELECTOR, "a#dynamicLink")

    CREATED_LINK = (By.CSS_SELECTOR, "a#created")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a#no-content")
    MOVED_LINK = (By.CSS_SELECTOR, "a#moved")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a#bad-request")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a#unauthorized")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a#forbidden")
    INVALID_URL_LINK = (By.CSS_SELECTOR, "a#invalid-url")

    RESULT = (By.CSS_SELECTOR, "p#linkResponse")