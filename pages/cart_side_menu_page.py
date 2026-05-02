from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartSideMenuPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButton']")
    CLOSE_SIDE_MENU_BTN = (By.CSS_SELECTOR, "[class*='styles_nonScrollModalContent'] button[aria-label='close']")

    def click_on_to_cart_button(self):
        self.wait_until_clickable_click(self.ADD_TO_CART_BTN)

    def close_side_menu(self):
        self.wait_until_clickable_click(self.CLOSE_SIDE_MENU_BTN)