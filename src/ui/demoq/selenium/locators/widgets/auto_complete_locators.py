from selenium.webdriver.common.by import By


class AutoCompleteLocators:
    # Инпуты
    MULTI_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteMultipleInput')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteSingleInput')

    # Выбранные значения (чипы) в мульти-режиме
    MULTI_VALUE = (By.CSS_SELECTOR, '.auto-complete__multi-value')
    MULTI_VALUE_LABEL = (By.CSS_SELECTOR, '.auto-complete__multi-value .auto-complete__multi-value__label')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, '.auto-complete__multi-value .auto-complete__multi-value__remove svg')

    # Выбранное значение в сингл-режиме
    SINGLE_VALUE = (By.CSS_SELECTOR, '.auto-complete__single-value')