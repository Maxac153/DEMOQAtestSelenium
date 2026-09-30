from selenium.webdriver.common.by import By


class SortableLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//div[@class="list-group"]/div[@class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//div[@class="create-grid"]/div[@class="list-group-item list-group-item-action"]')
