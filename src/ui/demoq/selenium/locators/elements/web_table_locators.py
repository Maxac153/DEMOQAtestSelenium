from selenium.webdriver.common.by import By


class WebTableLocators:
    # Add person form
    REGISTRATION_FORM = (By.XPATH, "//div[@class='modal-dialog modal-lg']")
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Table
    FULL_PEOPLE_LIST = (By.XPATH, "//tbody/tr")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = (By.XPATH, './ancestor::tr[1]')
    NO_ROWS_FOUND = (By.XPATH, '//tbody')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[class="form-control"]')

    # Update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
