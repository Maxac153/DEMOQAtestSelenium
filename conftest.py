import os

import allure
import faker
import pytest
from allure_commons.types import AttachmentType
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver

env_file = find_dotenv(".env", raise_error_if_not_found=False)
if env_file:
    load_dotenv(env_file)

FAKE = faker.Faker(os.environ.get("FAKER_LOCALE", "ru_RU"))


def pytest_configure(config):
    """Хук инициализации конфигурации Pytest."""

    pass

@pytest.fixture(scope='session')
def driver():
    """Инициализация драйвера на основе переменной окружения BROWSER (по умолчанию chrome)"""

    browser_name = os.environ.get("BROWSER", "chrome").lower()
    is_headless = os.environ.get("HEADLESS") == "true"

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        if is_headless:
            options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        if not is_headless:
            browser.maximize_window()

    elif browser_name in ["edge", "msedge"]:
        options = webdriver.EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        if is_headless:
            options.add_argument("--headless=new")
        browser = webdriver.Edge(options=options)

    elif browser_name == "safari":
        options = webdriver.SafariOptions()
        browser = webdriver.Safari(options=options)
        browser.maximize_window()

    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается. Выберите chrome, firefox, edge или safari.")

    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Скриншот неуспешных тестов в Allure"""

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver_fixture = item.funcargs.get("driver")
            if driver_fixture and hasattr(driver_fixture, "get_screenshot_as_png"):
                allure.attach(
                    driver_fixture.get_screenshot_as_png(),
                    name="Screenshot on failure",
                    attachment_type=AttachmentType.PNG
                )
