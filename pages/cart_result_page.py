from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartResultPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    def verify_cart_empty_msg(self):
          expected_result = 'Your cart is empty'
          self.verify_text(expected_result,self.CART_EMPTY_MSG)