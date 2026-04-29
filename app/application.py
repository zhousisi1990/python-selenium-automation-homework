from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.cart_result_page import CartResultPage

class Application:
    def __init__(self,driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_result_page = CartResultPage(driver)
