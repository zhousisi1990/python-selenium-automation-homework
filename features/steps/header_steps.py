from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("Search for {search_query}")
def search_product(context,search_query):
    context.driver.find_element(By.ID, 'search').send_keys(search_query)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)

@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(7)

@when("Click on Account Button")
def click_sign_in_button(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(7)