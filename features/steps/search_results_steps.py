from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify search results for {product} shown")
def verify_search_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'