from behave import given, when, then

# This can only cover the search result which can be picked up
# ADD_TO_CART_BTN = By.CSS_SELECTOR,"[data-test='orderPickupButton']"

@when("Click on Add to cart button from side menu")
def click_on_to_cart_button(context):
   context.app.cart_side_menu_page.click_on_to_cart_button()

@when("Close side menu")
def close_side_menu(context):
    context.app.cart_side_menu_page.close_side_menu()

