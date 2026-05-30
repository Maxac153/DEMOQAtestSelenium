from src.ui.demoq.selenium.pages.frames_page import FramesPage


class TestsCheckTextFrame:
    def test_check_text_frame(driver):
        """Проверка рамки"""

        from_page = FramesPage(driver, 'https://demoqa.com/sample')
        from_page.open()
        result_text = from_page.check_frame()
        expected_result = 'This is a sample page'
        assert expected_result == result_text
