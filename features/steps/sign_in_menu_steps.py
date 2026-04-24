from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_MENU_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIGN_IN_FORM_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")

@when("Click Sign In from right side navigation menu")
def click_sign_in_from_navigation(context):
     context.driver.find_element(*SIGN_IN_MENU_BTN).click()
     sleep(7)

@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    expected_result = 'Sign in or create account'
    actual_result = context.driver.find_element(*SIGN_IN_FORM_TEXT).text
    assert expected_result == actual_result, f'Expected "{expected_result}" not equal to"{actual_result}"'