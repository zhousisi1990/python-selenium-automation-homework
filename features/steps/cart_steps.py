from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
import re

CART_EMPTY_MSG = By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1"
CART_ITEM_AMOUNT = By.CSS_SELECTOR, "[class*='styles_cart-summary-span']"

@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty_msg(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_result == actual_result, f'Expected "{expected_result}" not actual to"{actual_result}"'

@then("Verify cart has {item_amount} item")
def verify_cart_item(context,item_amount):
    expected_result = f'{item_amount} item'
    actual_result = context.driver.find_element(*CART_ITEM_AMOUNT).text
    actual_result = re.search(r'\d+ items?', actual_result).group()
    assert expected_result == actual_result, f'Expected "{expected_result}" not equal to "{actual_result}"'
