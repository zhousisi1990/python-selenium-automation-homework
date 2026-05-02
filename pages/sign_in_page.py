from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_FORM_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")
    EXPECTED_RESULT = 'Sign in or create account'
    EMAIL = 'lyakhnikolay1960@weebd.de'
    INPUT_EMAIL = (By.ID, "username")
    CONTINUE_BUTTON = (By.ID, "login")
    FIRST_NAME = (By.ID, "firstname")
    FIRST_NAME_TEXT = 'SISI'
    LAST_NAME = (By.ID, "lastname")
    LAST_NAME_TEXT = 'ZHOU'
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-test='form-submit-button']")
    PASSWORD_CHECKBOX = (By.ID, "password-checkbox")
    PASSWORD_INPUT_TEXT = '*********'
    PASSWORD_INPUT = (By.ID, "password")
    EXPECTED_VERIFY_TEXT = 'Verification code sent'
    VERIFY_TEXT = (By.XPATH, "//span[contains(text(),'Verification code')]")

    def  verify_sign_in_form(self):
         self.verify_text(self. EXPECTED_RESULT,self.SIGN_IN_FORM_TEXT)

    def  input_email_and_password(self):
        #Input email address
         self.input_text(self.EMAIL,self.INPUT_EMAIL)
        #Click continue button
         self.wait_until_clickable_click(self.CONTINUE_BUTTON)
        #Input first_name
         self.input_text(self.FIRST_NAME_TEXT,self.FIRST_NAME)
        #Input last_name
         self.input_text(self.LAST_NAME_TEXT, self.LAST_NAME)
        #Click creat account with password checkbox
         self.wait_until_clickable_click(self.PASSWORD_CHECKBOX)
        #Input password
         self.input_text(self.PASSWORD_INPUT_TEXT,self.PASSWORD_INPUT)
        #Click create account button
         self.wait_until_clickable_click(self.CREATE_ACCOUNT_BUTTON)

    def verify_verification_code_sent(self):
        self.verify_text(self.EXPECTED_VERIFY_TEXT,self.VERIFY_TEXT)



