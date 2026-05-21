from src.ui.demoq.selenium.pages.book_page import BookPage


class TestsSearchBook:
    def test_search_book_by_name(self, driver):
        """Проверка поиска (По названию книги)"""

        from_page = BookPage(driver, 'https://demoqa.com/books')
        from_page.open()
        books = from_page.search_book('Java')
        expected_result = [
            "Learning JavaScript Design Patterns\nAddy Osmani\nO'Reilly Media",
            "Speaking JavaScript\nAxel Rauschmayer\nO'Reilly Media",
            "Programming JavaScript Applications\nEric Elliott\nO'Reilly Media",
            'Eloquent JavaScript, Second Edition\nMarijn Haverbeke\nNo Starch Press'
        ]
        assert expected_result == books[:-6]

    def test_search_book_by_name_author(self, driver):
        """Проверка поиска (По названию автору)"""

        from_page = BookPage(driver, 'https://demoqa.com/books')
        from_page.open()
        books = from_page.search_book('Eric')
        expected_result = "Programming JavaScript Applications\nEric Elliott\nO'Reilly Media"
        assert expected_result == books[0]

    def test_search_book_by_name_publisher(self, driver):
        """Проверка поиска (По названию издателя)"""

        from_page = BookPage(driver, 'https://demoqa.com/books')
        from_page.open()
        books = from_page.search_book("O'Reilly Media")
        expected_result = [
            "Git Pocket Guide\nRichard E. Silverman\nO'Reilly Media",
            "Learning JavaScript Design Patterns\nAddy Osmani\nO'Reilly Media",
            "Designing Evolvable Web APIs with ASP.NET\nGlenn Block et al.\nO'Reilly Media",
            "Speaking JavaScript\nAxel Rauschmayer\nO'Reilly Media",
            "You Don't Know JS\nKyle Simpson\nO'Reilly Media",
            "Programming JavaScript Applications\nEric Elliott\nO'Reilly Media"
        ]
        assert expected_result == books[:-4]

    def test_check_img(self, driver):
        """Проверка соответствия картинки и текста"""

        from_page = BookPage(driver, 'https://demoqa.com/books')
        from_page.open()

        books = from_page.all_books()
        from_page.search_book('Java')
        search_book = from_page.all_books()

        for book in search_book:
            if book not in books:
                assert book in books, 'Картинка не соответствует книге!'

    def test_pagination(self, driver):
        """Проверка пагинации страницы"""

        from_page = BookPage(driver, 'https://demoqa.com/books')
        from_page.open()

        from_page.set_rows(5)
        from_page.pagination_right()
        from_page.pagination_left()
