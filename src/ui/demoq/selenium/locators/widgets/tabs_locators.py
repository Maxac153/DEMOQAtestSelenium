from selenium.webdriver.common.by import By


class TabsLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'button[id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'button[id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TABS_USE = (By.CSS_SELECTOR, 'button[id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TABS_MORE = (By.CSS_SELECTOR, 'button[id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')