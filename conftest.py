import os

import pytest
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Загрузка переменных из .env (если файл есть) + fallback на системные переменные"""

    env_file = find_dotenv(".env", raise_error_if_not_found=False)

    if env_file:
        load_dotenv(env_file)


@pytest.fixture(scope='session')
def driver():
    """Инициализация драйвера"""

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    if os.environ.get("HEADLESS") == "true":
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Скриншот неуспешных тестов"""
#
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         # Если есть драйвер, сделай скриншот
#         if "driver" in rep.fixturenames:
#             driver = item.funcargs.get("driver")
#             if hasattr(driver, "get_screenshot_as_png"):
#                 allure.attach(
#                     driver.get_screenshot_as_png(),
#                     name="Screenshot on failure",
#                     attachment_type=AttachmentType.PNG
#                 )
