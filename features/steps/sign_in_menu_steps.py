from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_MENU_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIGN_IN_FORM_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")

@when("Click Sign In from right side navigation menu")
def click_sign_in_from_navigation(context):
     context.wait.until(EC.element_to_be_clickable(SIGN_IN_MENU_BTN)).click()

@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    expected_result = 'Sign in or create account'
    actual_result = context.wait.until(EC.visibility_of_element_located(SIGN_IN_FORM_TEXT),
                                      message='Sign in text not shown'
                    ).text
    assert expected_result == actual_result, f'Expected "{expected_result}" not equal to"{actual_result}"'