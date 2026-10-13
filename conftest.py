import os
import platform
import random
import re
import shutil
import subprocess
from importlib.metadata import version, PackageNotFoundError

import allure
import pytest
from dotenv import find_dotenv, load_dotenv
from faker import Faker

env_file = find_dotenv(".env", raise_error_if_not_found=False)
if env_file:
    load_dotenv(env_file)


def _get_package_version(package_name: str) -> str:
    try:
        return version(package_name)
    except PackageNotFoundError:
        return "unknown"


_BROWSER_BINARIES = {
    "chrome": [
        "google-chrome", "google-chrome-stable", "chrome",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ],
    "chromium": ["chromium", "chromium-browser"],
    "firefox": [
        "firefox",
        "/Applications/Firefox.app/Contents/MacOS/firefox",
    ],
    "edge": [
        "microsoft-edge", "microsoft-edge-stable", "msedge",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ],
}

_WINDOWS_REGISTRY = {
    "chrome": r"HKCU\Software\Google\Chrome\BLBeacon",
    "edge": r"HKCU\Software\Microsoft\Edge\BLBeacon",
}


def _get_browser_version(browser: str | None) -> str:
    """Версия браузера: из BROWSER_VERSION, иначе определяется по установленному браузеру."""
    explicit = os.environ.get("BROWSER_VERSION")
    if explicit:
        return explicit

    browser = (browser or "chrome").lower()

    # Windows: бинарники не отвечают на --version, читаем из реестра
    if platform.system() == "Windows" and browser in _WINDOWS_REGISTRY:
        try:
            out = subprocess.run(
                ["reg", "query", _WINDOWS_REGISTRY[browser], "/v", "version"],
                capture_output=True, text=True, timeout=10,
            ).stdout
            match = re.search(r"(\d+\.\d+\.\d+\.\d+)", out)
            if match:
                return match.group(1)
        except (OSError, subprocess.SubprocessError):
            pass

    for binary in _BROWSER_BINARIES.get(browser, []):
        path = shutil.which(binary) or (binary if os.path.isfile(binary) else None)
        if not path:
            continue
        try:
            out = subprocess.run(
                [path, "--version"], capture_output=True, text=True, timeout=10
            ).stdout
            match = re.search(r"(\d+(?:\.\d+)+)", out)
            if match:
                return match.group(1)
        except (OSError, subprocess.SubprocessError):
            continue

    return "unknown"


@pytest.fixture(scope="session")
def faker_seed() -> int:
    return int(os.environ.get("FAKER_SEED", random.randrange(2 ** 32)))


@pytest.fixture
def fake(faker_seed: int, request) -> Faker:
    fake = Faker(os.environ.get("FAKER_LOCALE", "ru_RU"))
    fake.seed_instance(faker_seed)
    allure.dynamic.parameter("faker_seed", faker_seed)
    return fake


def pytest_configure(config):
    """Хук инициализации конфигурации Pytest и подготовки истории Allure."""
    browser = os.environ.get("BROWSER")
    env_data = {
        "System execution": platform.platform(),
        "Environment": os.environ.get("ENVIRONMENT", "QA"),
        "BROWSER": browser,
        "BROWSER_VERSION": _get_browser_version(browser),
        "HEADLESS": os.environ.get("HEADLESS"),
        "DEMOQA_HOST": os.environ.get("DEMOQA_HOST"),
        "FAKER_LOCALE": os.environ.get("FAKER_LOCALE"),
        "WINDOW_SIZE": os.environ.get("WINDOW_SIZE"),
        "SELENIUM_VERSION": _get_package_version("selenium"),
        "PYTEST_VERSION": _get_package_version("pytest"),
        "ALLURE_PYTEST_VERSION": _get_package_version("allure-pytest"),
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
