from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty_msg(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_result == actual_result, f'Expected "{expected_result}" not actual to"{actual_result}"'