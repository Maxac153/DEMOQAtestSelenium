import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-тесты")
@allure.suite("BookStore API")
@allure.feature("Книжный магазин")
class TestBookStoreApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.book_store
    @allure.story("Проверка структуры данных книг")
    @allure.title("Проверка обязательных полей у всех книг")
    def test_books_have_required_fields(self, client: DemoQaClient):
        with allure.step("Получение списка книг"):
            response = client.get_books()

        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус-код 200, "
                f"получен {response.status_code}. "
                f"Тело ответа: {response.body}"
            )

        with allure.step("Проверка наличия списка книг"):
            assert "books" in response.body, (
                f"В ответе отсутствует поле 'books': {response.body}"
            )

        books = response.body["books"]

        with allure.step("Проверка обязательных полей книг"):
            required_fields = (
                "isbn",
                "title",
                "author",
                "publisher",
                "pages",
            )

            for index, book in enumerate(books, start=1):
                with allure.step(f"Проверка книги №{index}"):
                    for field in required_fields:
                        assert field in book, (
                            f"У книги №{index} отсутствует поле '{field}': "
                            f"{book}"
                        )

                    assert book["isbn"], (
                        f"У книги №{index} поле 'isbn' пустое"
                    )
                    assert book["title"], (
                        f"У книги №{index} поле 'title' пустое"
                    )
                    assert book["author"], (
                        f"У книги №{index} поле 'author' пустое"
                    )
                    assert book["publisher"], (
                        f"У книги №{index} поле 'publisher' пустое"
                    )
