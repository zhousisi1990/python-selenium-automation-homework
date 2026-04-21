from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when("Search for {search_query}")
def search_product(context,search_query):
    context.driver.find_element(By.ID, 'search').send_keys(search_query)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)


@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(7)

@when("Click on Sign In Button")
def click_sign_in_button(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(7)

@when("Click Sign In from right side navigation menu")
def click_sign_in_from_navigation(context):
     context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
     sleep(7)

@then("Verify search results for {product} shown")
def verify_search_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'



@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty_msg(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_result == actual_result, f'Expected "{expected_result}" not actual to"{actual_result}"'

@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    expected_result = 'Sign in or create account'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert expected_result == actual_result, f'Expected "{expected_result}" not equal to"{actual_result}"'