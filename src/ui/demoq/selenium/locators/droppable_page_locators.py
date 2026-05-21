from selenium.webdriver.common.by import By


class DroppablePageLocators:
    DROGGABLE = (By.XPATH, "//div[@id='draggable']")
    DROPPABLE = (By.XPATH, "//div[@id='droppable']")
