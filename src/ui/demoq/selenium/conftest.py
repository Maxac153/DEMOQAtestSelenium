import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def _apply_window_size(browser, window_size: str):
    window_size = (window_size or "full").lower()

    sizes = {
        "mobile": (390, 844),
        "fullscreen": None,
        "full": None,
        "2k": (1920, 1080),
        "2.5k": (2560, 1440),
        "4k": (3840, 2160)
    }

    if window_size in sizes:
        size = sizes[window_size]
        if size is None:
            browser.maximize_window()
        else:
            browser.set_window_size(*size)
        return

    if "x" in window_size:
        width, height = window_size.split("x", 1)
        browser.set_window_size(int(width), int(height))
    else:
        browser.maximize_window()


@pytest.fixture(scope='session')
def driver():
    """Инициализация драйвера на основе переменной окружения BROWSER (по умолчанию chrome)"""

    browser_name = os.environ.get("BROWSER", "chrome").lower()
    is_headless = os.environ.get("HEADLESS") == "true"
    window_size = os.environ.get("WINDOW_SIZE", "full")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        if is_headless:
            options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=options)
        _apply_window_size(browser, window_size)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.log.level = "fatal"
        if is_headless:
            options.add_argument("--headless")
        browser = webdriver.Firefox(options=options, service=Service(log_output=os.devnull))
        _apply_window_size(browser, window_size)

    elif browser_name in ["edge", "msedge"]:
        options = webdriver.EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.set_capability("ms:loggingPrefs", {"performance": "ALL"})

        if is_headless:
            options.add_argument("--headless=new")
        browser = webdriver.Edge(options=options)
        _apply_window_size(browser, window_size)

    elif browser_name == "safari":
        options = webdriver.SafariOptions()
        browser = webdriver.Safari(options=options)
        _apply_window_size(browser, window_size)

    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается. Выберите chrome, firefox, edge или safari.")

    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Скриншот и Сетевой лог неуспешных тестов в Allure и локальную папку"""

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver_fixture = item.funcargs.get("driver")
            if driver_fixture:
                if hasattr(driver_fixture, "get_screenshot_as_png"):
                    allure.attach(
                        driver_fixture.get_screenshot_as_png(),
                        name="Screenshot on failure",
                        attachment_type=AttachmentType.PNG
                    )
