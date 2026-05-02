from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInMenu(Page):
    expected_result = 'Sign in or create account'
    SIGN_IN_MENU_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    SIGN_IN_FORM_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")

    def click_sign_in_from_navigation(self):
        self.wait_until_clickable_click(self.SIGN_IN_MENU_BTN)

    def  verify_sign_in_form(self):
         self.verify_text(self.expected_result,self.SIGN_IN_FORM_TEXT)

