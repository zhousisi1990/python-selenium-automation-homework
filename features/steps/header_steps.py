from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ACCOUNT_BTN = (By.ID, 'account-sign-in')
TARGET_CIRCLE_BTN = (By.ID, "utilityNav-circle")

@when("Search for {search_query}")
def search_product(context,search_query):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)

@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(7)

@when("Click on Account Button")
def click_sign_in_button(context):
    context.driver.find_element(*ACCOUNT_BTN).click()
    sleep(7)

@when("Click on Target Circle button")
def click_target_circle_button(context):
    context.driver.find_element(*TARGET_CIRCLE_BTN).click()
    sleep(7)