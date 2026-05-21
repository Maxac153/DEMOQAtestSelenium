from src.ui.demoq.selenium.pages.drag_and_drop import DragAndDropPage


class TestsDragAndDrop:
    def test_drag_and_drop(self, driver):
        """Проверка перетаскивания"""

        from_page = DragAndDropPage(driver, 'https://demoqa.com/droppable')
        from_page.open()
        result = from_page.check_drag_and_drop()
        expected_result = 'Dropped!'
        assert expected_result == result
