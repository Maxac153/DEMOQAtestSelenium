from src.ui.demoq.selenium.locators.book_page_locators import BookPageLocators
from src.ui.demoq.selenium.pages.base_page import BasePage


class BookPage(BasePage):
    def search_book(self, string):
        """Поиск книги"""

        self.element_is_visible(BookPageLocators.SEARCH_BOOK).send_keys(string)
        result_search = self.elements_are_visible(BookPageLocators.TABLE)
        result_text = [i.text for i in result_search]
        return result_text

    def all_books(self):
        """Все книги"""

        self.element_is_visible(BookPageLocators.SEARCH_BOOK).clear()
        covers = self.elements_are_visible(BookPageLocators.IMAGES)
        covers = [i.get_attribute("src") for i in covers]
        titles_author_publisher = self.elements_are_visible(BookPageLocators.TABLE)
        titles_author_publisher = [i.text for i in titles_author_publisher]

        books = []
        for i in range(len(covers)):
            books.append(covers[i] + titles_author_publisher[i])

        return books

    def set_rows(self, number):
        """Изменение количества отражаемых книг"""

        self.element_is_visible(BookPageLocators.SELECT_ROWS).send_keys(f'{number} rows')

    def pagination_right(self):
        """Переход на следующие страницу"""

        self.element_is_visible(BookPageLocators.NEXT).click()

    def pagination_left(self):
        """Переход на предыдущую страницу"""

        self.element_is_visible(BookPageLocators.PREVIOUS).click()
