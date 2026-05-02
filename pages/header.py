from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ACCOUNT_BTN = (By.ID, 'account-sign-in')
    def search_product(self,search_query:str):
        self.input_text(search_query,self.SEARCH_FIELD)
        self.click(self.SEARCH_BTN)
        sleep(8)

    def click_cart_icon(self):
        self.click(self.CART_ICON)

    def click_sign_in(self):
        self.wait_until_clickable_click(self.ACCOUNT_BTN)