from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify {expected_amount} story cards under 'Unlock added value'")
def verify_under_unlock_added_value_amount(context,expected_amount):
    expected_amount = int(expected_amount)
    actual_amount = len(context.driver.find_elements(By.CSS_SELECTOR,"div[data-test='@web/SlingshotComponents/Storyblocks'] a"))
    print(actual_amount)
    assert actual_amount == expected_amount,f'Expected {expected_amount} story cards but got {actual_amount}'
