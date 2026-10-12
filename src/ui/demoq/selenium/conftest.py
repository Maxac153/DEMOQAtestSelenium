import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, UnexpectedAlertPresentException, WebDriverException, \
    NoAlertPresentException
from selenium.webdriver.firefox.service import Service


def _apply_window_size(browser, window_size: str) -> None:
    window_size = (window_size or "full").lower()

    sizes = {
        "mobile": (390, 844),
        "fullscreen": None,
        "full": None,
        "2k": (1920, 1080),
        "2.5k": (2560, 1440),
        "4k": (3840, 2160),
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


@pytest.fixture(scope="session")
def driver():
    """Один браузер на pytest-воркера, с обязательной очисткой после каждого теста."""

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

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.log.level = "fatal"

        if is_headless:
            options.add_argument("--headless")

        browser = webdriver.Firefox(
            options=options,
            service=Service(log_output=os.devnull),
        )

    elif browser_name in ("edge", "msedge"):
        options = webdriver.EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.set_capability("ms:loggingPrefs", {"performance": "ALL"})

        if is_headless:
            options.add_argument("--headless=new")

        browser = webdriver.Edge(options=options)

    elif browser_name == "safari":
        options = webdriver.SafariOptions()
        browser = webdriver.Safari(options=options)

    else:
        raise ValueError(
            f"Браузер '{browser_name}' не поддерживается. "
            "Выберите chrome, firefox, edge или safari."
        )

    _apply_window_size(browser, window_size)

    yield browser

    try:
        browser.quit()
    except WebDriverException:
        pass


@pytest.fixture(autouse=True)
def _isolate_browser_state(driver):
    """
    Гарантирует одинаковое стартовое состояние браузера для каждого теста.

    Выполняется после каждого теста: успешно завершённого, упавшего
    или прерванного на teardown.
    """
    yield

    if driver is None:
        return

    _dismiss_alert(driver)
    _close_extra_windows(driver)
    _clear_browser_state(driver)


def _dismiss_alert(browser: webdriver.Remote) -> None:
    """Закрывает неподтверждённый alert, чтобы он не блокировал следующие команды."""
    try:
        alert = browser.switch_to.alert
        alert.dismiss()
    except (NoAlertPresentException, NoSuchWindowException, WebDriverException):
        pass


def _close_extra_windows(browser: webdriver.Remote) -> None:
    """Оставляет только первое окно и переключается на него."""
    try:
        handles = browser.window_handles
        if not handles:
            return

        for handle in handles[1:]:
            browser.switch_to.window(handle)
            browser.close()

        browser.switch_to.window(handles[0])
    except (NoSuchWindowException, WebDriverException):
        pass


def _clear_browser_state(browser: webdriver.Remote) -> None:
    """Сбрасывает cookies, localStorage и sessionStorage в текущем origin."""
    try:
        browser.switch_to.default_content()
        browser.delete_all_cookies()

        browser.execute_script("window.localStorage.clear();")
        browser.execute_script("window.sessionStorage.clear();")
    except (UnexpectedAlertPresentException, NoSuchWindowException, WebDriverException):
        pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Прикладывает скриншот к Allure при любом неуспехе: setup, call или teardown."""
    outcome = yield
    report = outcome.get_result()

    if report.when not in ("setup", "call", "teardown") or not report.failed:
        return

    browser = item.funcargs.get("driver")
    if not browser:
        return

    _dismiss_alert(browser)

    try:
        allure.attach(
            browser.get_screenshot_as_png(),
            name=f"Снимок экрана при сбое ({report.when})",
            attachment_type=AttachmentType.PNG,
        )
    except (UnexpectedAlertPresentException, NoSuchWindowException, WebDriverException):
        pass
