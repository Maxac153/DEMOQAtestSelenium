from selenium.webdriver.common.by import By


class LinksLocators:
    SIMPLE_LINK_LINK = (By.XPATH, "//a[@id='simpleLink']")
    DYNAMIC_LINK_LINK = (By.XPATH, "//a[@id='dynamicLink']")

    CREATED_LINK = (By.XPATH, "//a[@id='created']")
    NO_CONTENT_LINK = (By.XPATH, "//a[@id='no-content']")
    MOVED_LINK = (By.XPATH, "//a[@id='moved']")
    BAD_REQUEST_LINK = (By.XPATH, "//a[@id='bad-request']")
    UNAUTHORIZED_LINK = (By.XPATH, "//a[@id='unauthorized']")
    FORBIDDEN_LINK = (By.XPATH, "//a[@id='forbidden']")
    INVALID_URL_LINK = (By.XPATH, "//a[@id='invalid-url']")

    RESULT = (By.XPATH, "//p[@id='linkResponse']")
