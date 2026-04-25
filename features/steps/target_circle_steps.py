from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

UNDER_ADD_VALUE_AMOUNT = (By.CSS_SELECTOR,"div[data-test='@web/SlingshotComponents/Storyblocks'] a")
UNLOCK_ADDED_VALUE =(By.XPATH,"//h2[text()='Unlock added value']")

@then("Verify {expected_amount} story cards under 'Unlock added value'")
def verify_under_unlock_added_value_amount(context,expected_amount):
    context.wait.until(EC.visibility_of_element_located(UNLOCK_ADDED_VALUE),
                       message='Unlock added value is not visible')
    expected_amount = int(expected_amount)
    actual_amount = len(context.driver.find_elements(*UNDER_ADD_VALUE_AMOUNT))
    print(actual_amount)
    assert actual_amount == expected_amount,f'Expected {expected_amount} story cards but got {actual_amount}'
