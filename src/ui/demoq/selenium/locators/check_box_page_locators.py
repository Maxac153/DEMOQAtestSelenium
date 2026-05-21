from selenium.webdriver.common.by import By


class CheckBoxLocators:
    # Check Box
    SWITCH_CLOSE = (By.XPATH, "//span[@class='rc-tree-switcher rc-tree-switcher_close']")
    CHECK_BOX = (By.XPATH, "//span[@class='rc-tree-checkbox']")
    CHECK_BOX_ACTIVE = (By.XPATH, "//span[contains(@class, 'rc-tree-checkbox-checked')]/following-sibling::span/span[2]")
    RESULT = (By.XPATH, "//div[@id='result']")

    # Select Name Check Box
    SELECT_ITEMS = (By.XPATH, "//span[@class='rc-tree-title']")
    SELECT_ITEM_ACTIVE = (By.XPATH, "//div[contains(@class, 'rc-tree-treenode-selected')]")
