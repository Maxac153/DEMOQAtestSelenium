from selenium.webdriver.common.by import By


class BookPageLocators:
    BOOK_STORE_APPLICATION = (By.XPATH, '//div[6]/span')
    BOOK_STORE = (By.XPATH, '//div[6]/div/ul/li[2]')
    SEARCH_BOOK = (By.XPATH, '//input')
    IMAGES = (By.XPATH, "//img[@alt='image']")
    TABLE = (By.XPATH, '//div[@class="rt-tbody"]/div')
    TITLE = (By.XPATH, "//div[@role='gridcell']/div/span/a")
    AUTHOR = (By.XPATH, "//div[@role='gridcell']/div/span/a")
    PUBLISHER = (By.XPATH, "//div[@role='gridcell']/div/span/a")
    PREVIOUS = (By.XPATH, "//button[text()='Previous']")
    SELECT_ROWS = (By.XPATH, "//select[@aria-label='rows per page']")
    NEXT = (By.XPATH, "//button[text()='Next']")
