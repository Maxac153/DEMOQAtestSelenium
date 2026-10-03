from selenium.webdriver.common.by import By


class AccordianLocators:
    # Контейнер аккордеона
    ACCORDION_CONTAINER = (By.CSS_SELECTOR, "div.accordion")

    # Элементы секций
    SECTION_FIRST = (By.CSS_SELECTOR, "div.accordion-item:nth-of-type(1)")
    SECTION_SECOND = (By.CSS_SELECTOR, "div.accordion-item:nth-of-type(2)")
    SECTION_THIRD = (By.CSS_SELECTOR, "div.accordion-item:nth-of-type(3)")

    # Кнопка заголовка внутри секции
    SECTION_BUTTON = (By.CSS_SELECTOR, "button.accordion-button")

    # Контент внутри открытой секции
    SECTION_BODY = (By.CSS_SELECTOR, "div.accordion-body")
