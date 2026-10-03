import os
import platform
import shutil

import faker
from dotenv import find_dotenv, load_dotenv

env_file = find_dotenv(".env", raise_error_if_not_found=False)
if env_file:
    load_dotenv(env_file)

FAKE = faker.Faker(os.environ.get("FAKER_LOCALE", "ru_RU"))
os.makedirs("output", exist_ok=True)


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
