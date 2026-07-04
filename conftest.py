import os
import platform
import shutil

import allure
import faker
import pytest
from allure_commons.types import AttachmentType
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

env_file = find_dotenv(".env", raise_error_if_not_found=False)
if env_file:
    load_dotenv(env_file)

FAKE = faker.Faker(os.environ.get("FAKER_LOCALE", "ru_RU"))
os.makedirs("output", exist_ok=True)


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


def pytest_configure(config):
    """Хук инициализации конфигурации Pytest и подготовки истории Allure."""
    env_data = {
        "System execution": platform.platform(),
        "Environment": os.environ.get("ENVIRONMENT", "QA"),
        "BROWSER": os.environ.get("BROWSER"),
        "HEADLESS": os.environ.get("HEADLESS"),
        "DEMOQA_HOST": os.environ.get("DEMOQA_HOST"),
        "FAKER_LOCALE": os.environ.get("FAKER_LOCALE"),
        "WINDOW_SIZE": os.environ.get("WINDOW_SIZE"),
        "BROWSER_VERSION": os.environ.get("BROWSER_VERSION"),
        "OS_SYSTEM": platform.system(),
        "OS_RELEASE": platform.release(),
        "OS_VERSION": platform.version(),
        "MACHINE": platform.machine(),
        "PROCESSOR": platform.processor(),
        "PYTHON_VERSION": platform.python_version(),
    }

    # Пути к директориям результатов и отчетов
    results_dir = os.path.join("output", "allure-results")
    report_history_dir = os.path.join("output", "allure-report", "history")
    results_history_dir = os.path.join(results_dir, "history")

    # 1. ПЕРЕНОС ИСТОРИИ ДЛЯ ТРЕНДОВ:
    # Если прошлый отчет существует, копируем его историю в новую папку результатов
    if os.path.exists(report_history_dir):
        # Удаляем старую историю в results, если она осталась от предыдущих локальных запусков
        if os.path.exists(results_history_dir):
            shutil.rmtree(results_history_dir)

        # Копируем историю из allure-report/history в allure-results/history
        shutil.copytree(report_history_dir, results_history_dir)

    # 2. Создание папки результатов, если её не было
    os.makedirs(results_dir, exist_ok=True)

    # 3. Запись environment.properties
    with open(os.path.join(results_dir, "environment.properties"), "w", encoding="utf-8") as f:
        for key, value in env_data.items():
            f.write(f"{key}={value}\n")


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
