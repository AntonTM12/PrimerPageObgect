from pages.ya_pages import SearchHelper
from pages.serch_page import SerchPageHelper

def test_serch(browsser):
    ya_main = SearchHelper(browsser)
    ya_serch = SerchPageHelper(browsser)
    ya_main.go_to_site()
    ya_main.enter_word('privet')
    ya_main.click_on_poisk()
    elements = ya_serch.check_navi_bar()
    assert "Картинка" and "Видео" in elements


