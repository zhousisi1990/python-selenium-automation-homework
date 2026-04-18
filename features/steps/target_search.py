from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when("Search for tea")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)


@when("Search for coffee")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)

@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(7)

@then("Verify search results for tea shown")
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'


@then("Verify search results for coffee shown")
def verify_search_results(context):
    expected_result = 'coffee'
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'

@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty_msg(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_result == actual_result, f'Expected "{expected_result}" not actual to"{actual_result}"'