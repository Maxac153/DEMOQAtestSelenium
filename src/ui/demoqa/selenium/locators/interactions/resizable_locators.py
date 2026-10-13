from selenium.webdriver.common.by import By


class ResizableLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR,
        "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']"
    )
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR,
        "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']"
    )
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
