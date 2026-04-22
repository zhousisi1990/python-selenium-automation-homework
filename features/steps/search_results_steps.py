from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify search results for {product} shown")
def verify_search_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'

@when("Click on the first Add to cart button")
def click_on_first_add(context):

    add_to_cart_btn = context.driver.find_elements(By.CSS_SELECTOR,"button[data-test='chooseOptionsButton']")
    first_btn = add_to_cart_btn[0]
    context.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        first_btn
    )
    first_btn.click()
