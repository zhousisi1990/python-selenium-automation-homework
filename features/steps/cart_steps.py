from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
import re

CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
# item 1 can't assert directly with 11.99 subtotal1 item
# CART_ITEM_AMOUNT = By.CSS_SELECTOR, "[class*='styles_cart-summary-span']"
CART_ITEM_AMOUNT = (By.XPATH,"//h2[./span[contains(text(),'subtotal')]]")

@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty_msg(context):
    expected_result = 'Your cart is empty'
    actual_result = context.wait.until(
        EC.visibility_of_element_located(CART_EMPTY_MSG),
        message="Your cart is empty text not shown").text
    assert expected_result == actual_result, f'Expected "{expected_result}" not actual to"{actual_result}"'

@then("Verify cart has {item_amount} item(s)")
def verify_cart_item(context,item_amount):
    actual_result = context.driver.find_element(*CART_ITEM_AMOUNT).text
    # actual_result = re.search(r'\d+ items?', actual_result).group()
    # assert expected_result == actual_result, f'Expected "{expected_result}" not equal to "{actual_result}"'
    assert f'{item_amount}' in actual_result, f'Expected "{item_amount}" items but got "{actual_result}"'
