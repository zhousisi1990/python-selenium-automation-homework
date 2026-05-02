from pages.base_page import Page
from pages.cart_side_menu_page import CartSideMenuPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.cart_result_page import CartResultPage
from pages.sign_in_page import SignInPage
from pages.sign_in_menu_page import SignInMenu


class Application:
    def __init__(self,driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_result_page = CartResultPage(driver)
        self.sign_in_menu_page = SignInMenu(driver)
        self.cart_side_menu_page = CartSideMenuPage(driver)
        self.sign_in_page = SignInPage(driver)