from selenium.webdriver.common.by import By


class DatePickerLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")
