from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
# ADD_TO_CART_BTN = By.CSS_SELECTOR,"button[data-test='chooseOptionsButton']"
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")

@when("Click on the first Add to cart button")
def click_on_first_add(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    first_btn = context.driver.find_element(*ADD_TO_CART_BTN)
    context.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        first_btn
    )
    first_btn.click()

@then("Verify search results for {product} shown")
def verify_search_results(context,product):
    actual_result = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'


