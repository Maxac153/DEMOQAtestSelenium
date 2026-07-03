from selenium.webdriver.common.by import By


class BrokenLinksAndImagesLinksLocators:
    VALID_IMAGE = (By.XPATH, "//p[contains(text(), 'Valid image')]/following-sibling::img[1]")
    BROKEN_IMAGE = (By.XPATH, "//p[contains(text(), 'Broken image')]/following-sibling::img[1]")

    VALID_LINK = (By.XPATH, "//a[contains(text(), 'Click Here for Valid Link')]")
    BROKEN_LINK = (By.XPATH, "//a[contains(text(), 'Click Here for Broken Link')]")
