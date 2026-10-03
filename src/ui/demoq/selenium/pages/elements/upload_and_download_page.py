import base64
import os

import allure

from src.ui.demoq.selenium.generator.generator import generated_file
from src.ui.demoq.selenium.locators.elements.upload_and_download_locators import UploadAndDownloadLocators
from src.ui.demoq.selenium.pages.__common.base_page import BasePage


class UploadAndDownloadPage(BasePage):
    @allure.step("Загрузить картинку")
    def upload_file(self, file_path: str):
        file_name, path = generated_file(os.path.abspath(file_path))
        self.element_is_visible(UploadAndDownloadLocators().UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_visible(UploadAndDownloadLocators().UPLOADED_RESULT).text

        return file_name.split("/")[-1], text.split("\\")[-1]

    @allure.step("Скачать картинку")
    def download_file(self, file_path: str):
        link = self.element_is_visible(UploadAndDownloadLocators().DOWNLOAD_FILE).get_attribute("href")
        link_b = base64.b64decode(link)
        with open(file_path, "wb+") as f:
            offset = link_b.find(b"\xff\xd8")
            f.write(link_b[offset:])
            check_file = os.path.exists(file_path)
            f.close()

        return check_file
