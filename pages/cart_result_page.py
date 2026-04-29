from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartResultPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    def verify_cart_empty_msg(self):
          expected_result = 'Your cart is empty'
          actual_result = self.find_element(self.CART_EMPTY_MSG).text
          assert expected_result == actual_result, f'Expected "{expected_result}" not actual to"{actual_result}"'