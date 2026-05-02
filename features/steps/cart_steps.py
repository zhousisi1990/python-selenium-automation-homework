from behave import given, when, then

# item 1 can't assert directly with 11.99 subtotal1 item
# CART_ITEM_AMOUNT = By.CSS_SELECTOR, "[class*='styles_cart-summary-span']"

@then("Verify “Your cart is empty” message is shown")
def verify_cart_empty_msg(context):
  context.app.cart_result_page.verify_cart_empty_msg()

@then("Verify cart has {item_amount} item(s)")
def verify_cart_item(context,item_amount):
   context.app.cart_result_page.verify_cart_item(item_amount)
