import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.pages.elements.upload_and_download_page import UploadAndDownloadPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.UPLOAD_DOWNLOAD.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Upload And Download")
class TestsUploadAndDownload:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Скачивание картинки")
    @allure.title("Проверка скачивания картинки ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,file_path",
        [
            ("Проверка скачивания картинки", rf"input/img/file_test.jpeg")
        ]
    )
    def test_download_file(self, driver: WebDriver, test_case_name: str, file_path: str):
        upload_download_page = UploadAndDownloadPage(driver, BASE_URL)
        upload_download_page.open()
        result = upload_download_page.download_file(file_path)

        with allure.step("Проверка скачивания картинки"):
            assert result is True, "Картинка не была скачена"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Загрузка файла")
    @allure.title("Проверка загрузки файла ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,file_path",
        [
            ("Проверка загрузки файла", rf"input/img/test_file.txt")
        ]
    )
    def test_upload_file(self, driver: WebDriver, test_case_name: str, file_path: str):
        upload_download_page = UploadAndDownloadPage(driver, BASE_URL)
        upload_download_page.open()
        file_name, result = upload_download_page.upload_file(file_path)

        with allure.step("Проверка загрузки файла"):
            assert file_name == result, "Файл не был загружен"
