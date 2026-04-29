from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ACCOUNT_BTN = (By.ID, 'account-sign-in')
TARGET_CIRCLE_BTN = (By.ID, "utilityNav-circle")
ADS_LINK = (By.CSS_SELECTOR, "a#ad-link")

@when("Search for {search_query}")
def search_product(context,search_query):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    # context.driver.find_element(*SEARCH_BTN).click()
    # context.wait.until(EC.invisibility_of_element_located(ADS_LINK,))
    context.app.header.search_product(search_query)

@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()

@when("Click on Account Button")
def click_sign_in_button(context):
    context.wait.until(EC.element_to_be_clickable(ACCOUNT_BTN),
                       message='Account btn is not visible'
    ).click()

@when("Click on Target Circle button")
def click_target_circle_button(context):
    context.wait.until(EC.element_to_be_clickable(TARGET_CIRCLE_BTN),
                       message='Target circle btn is not visible'
    ).click()