import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.__common.models.elements.broken_images import BrokenImages
from src.ui.demoq.selenium.pages.elements.broken_links_and_images_page import BrokenLinksAndImagesPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.BROKEN_LINKS.value}"


@allure.parent_suite("UI-selenium-test")
@allure.suite("DemoQA")
@allure.feature("Страница Broken Links And Images")
class TestsBrokenLinksAndImages:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка Images")
    @allure.title("Проверка изображения ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,image,is_image_broken",
        [
            ("Проверка VALID_IMAGE", BrokenImages.VALID_IMAGE, False),
            ("Проверка BROKEN_IMAGE", BrokenImages.BROKEN_IMAGE, True),
        ],
    )
    def test_images(
            self,
            driver: WebDriver,
            test_case_name: str,
            image: BrokenImages,
            is_image_broken: bool,
    ) -> None:
        broken_links_page = BrokenLinksAndImagesPage(driver, BASE_URL)
        broken_links_page.open()

        result = broken_links_page.select_image(image)

        with allure.step("Проверка статуса изображения"):
            assert is_image_broken == result, (
                f"Для {image.value}: ожидалось is_broken={is_image_broken}, "
                f"но получено {result}"
            )
