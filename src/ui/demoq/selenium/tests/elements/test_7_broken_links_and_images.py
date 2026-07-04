import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.selenium.modules.elements.broken_images import BrokenImages
from src.ui.demoq.selenium.modules.elements.broken_links import BrokenLinks
from src.ui.demoq.selenium.pages.elements.broken_links_and_images_page import BrokenLinksAndImagesPage

BASE_URL = f"{os.environ.get("DEMOQA_HOST")}{EndpointsDemoq.BROKEN_LINKS.value}"


@allure.feature("Форма Broken Links")
class TestsBrokenLinksAndImages:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка Images")
    @allure.title("Проверка Images ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,image,broken_images",
        [
            ("Проверка нажатия на Links (VALID_IMAGE)", BrokenImages.VALID_IMAGE, False),
            ("Проверка нажатия на Links (BROKEN_IMAGE)", BrokenImages.BROKEN_IMAGE, True)
        ]
    )
    def test_images(self, driver: WebDriver, test_case_name: str, image: BrokenImages, broken_images: bool):
        """Проверка Images"""

        broken_links_page = BrokenLinksAndImagesPage(driver, BASE_URL)
        broken_links_page.open()
        result = broken_links_page.select_image(image)

        with allure.step("Проверка image (True, False)"):
            assert broken_images == result, f"Ожидался {broken_images}, но получен {result}"

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.negative
    @allure.story("Открытие новой вкладки")
    @allure.title("Проверка title новой вкладки для ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_links,expected_result",
        [
            ("Проверка нажатия на Links (CLICK VALID LINK)", BrokenLinks.VALID_LINK, BrokenLinks.VALID_LINK.value),
            ("Проверка нажатия на Links (CLICK BROKEN LINK)", BrokenLinks.BROKEN_LINK, BrokenLinks.BROKEN_LINK.value)
        ]
    )
    def test_links(self, driver: WebDriver, test_case_name: str, select_links: BrokenLinks, expected_result: str):
        """Проверка Links"""

        broken_links_page = BrokenLinksAndImagesPage(driver, BASE_URL)
        broken_links_page.open()
        result = broken_links_page.open_new_tab(select_links)

        with allure.step("Проверка нажатия на links"):
            assert expected_result == result, f"Ожидался {expected_result}, но получен {result}"
