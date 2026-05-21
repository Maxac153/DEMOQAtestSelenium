from src.ui.demoq.selenium.pages.slider_page import SliderPage


class TestsCheckTextSlider:
    def test_check_text_slider(self, driver):
        """Проверка слайдера"""

        from_page = SliderPage(driver, 'https://demoqa.com/slider')
        from_page.open()

        from_page.slider_move(60)
        result_text = from_page.slider_value()
        extends_result = '59'
        assert result_text == extends_result
