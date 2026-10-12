import os

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.demoq.__common.endpoints.endpoints_demoq import EndpointsDemoq
from src.ui.demoq.__common.models.elements.links import Links
from src.ui.demoq.selenium.pages.elements.links_page import LinksPage

BASE_URL = f"{os.environ.get('DEMOQA_HOST')}{EndpointsDemoq.LINKS.value}"


@allure.parent_suite("UI-test")
@allure.suite("DemoQA")
@allure.feature("Страница Links")
class TestsLinks:
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Открытие новой вкладки")
    @allure.title("Проверка открытия новой вкладки ({test_case_name})")
    @pytest.mark.parametrize(
        "test_case_name,select_links,expected_title",
        [
            (
                "SIMPLE_LINK_LINK",
                Links.SIMPLE_LINK_LINK,
                Links.SIMPLE_LINK_LINK.value,
            ),
            (
                "DYNAMIC_LINK_LINK",
                Links.DYNAMIC_LINK_LINK,
                Links.DYNAMIC_LINK_LINK.value,
            ),
        ],
    )
    def test_open_new_tab_title(
        self,
        driver: WebDriver,
        test_case_name: str,
        select_links: Links,
        expected_title: str,
    ) -> None:
        links_page = LinksPage(driver, BASE_URL)
        links_page.open()

        result = links_page.open_new_tab(select_links)

        with allure.step("Проверить title новой вкладки"):
            assert expected_title == result, (
                f"Ожидался title '{expected_title}', но получен '{result}'"
            )

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Проверка HTTP-статуса ссылок")
    @allure.title("Проверка ответа ссылки {select_links.value}")
    @pytest.mark.parametrize(
        "select_links,expected_status_code",
        [
            (Links.CREATED_LINK, 201),
            (Links.NO_CONTENT_LINK, 204),
            (Links.MOVED_LINK, 301),
            (Links.BAD_REQUEST_LINK, 400),
            (Links.UNAUTHORIZED_LINK, 401),
            (Links.FORBIDDEN_LINK, 403),
            (Links.INVALID_URL_LINK, 404),
        ],
    )
    def test_link_response_status(
        self,
        driver: WebDriver,
        select_links: Links,
        expected_status_code: int,
    ) -> None:
        links_page = LinksPage(driver, BASE_URL)
        links_page.open()

        actual_status_code = links_page.get_link_response_status(select_links)

        with allure.step(f"Проверить, что ссылка вернула {expected_status_code}"):
            assert expected_status_code == actual_status_code, (
                f"Для {select_links.value} ожидался статус {expected_status_code}, "
                f"но получен {actual_status_code}"
            )