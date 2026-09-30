from selenium.webdriver.common.by import By


class AccordianLocators:
    # Контейнер аккордеона
    ACCORDION_CONTAINER = (By.CSS_SELECTOR, "div.accordion")

    # Элементы секций
    SecTION_FIRST = (By.CSS_SELECTOR, "div.accordion-item:nth-of-type(1)")
    SecTION_SecOND = (By.CSS_SELECTOR, "div.accordion-item:nth-of-type(2)")
    SecTION_THIRD = (By.CSS_SELECTOR, "div.accordion-item:nth-of-type(3)")

    # Кнопка заголовка внутри секции
    SecTION_BUTTON = (By.CSS_SELECTOR, "button.accordion-button")

    # Контент внутри открытой секции
    SecTION_BODY = (By.CSS_SELECTOR, "div.accordion-body")
