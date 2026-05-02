from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TARGET_CIRCLE_BTN = (By.ID, "utilityNav-circle")

@when("Search for {search_query}")
def search_product(context,search_query):
    context.app.header.search_product(search_query)

@when("Click on Cart icon")
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@when("Click on Account Button")
def click_sign_in_button(context):
    context.app.header.click_sign_in()

@when("Click on Target Circle button")
def click_target_circle_button(context):
    context.wait.until(EC.element_to_be_clickable(TARGET_CIRCLE_BTN),
                       message='Target circle btn is not visible'
    ).click()