from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInMenu(Page):
    SIGN_IN_MENU_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def click_sign_in_from_navigation(self):
        self.wait_until_clickable_click(self.SIGN_IN_MENU_BTN)



