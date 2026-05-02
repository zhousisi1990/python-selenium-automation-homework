from behave import given, when, then

@when("Click Sign In from right side navigation menu")
def click_sign_in_from_navigation(context):
     context.app.sign_in_menu_page.click_sign_in_from_navigation()

@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    context.app.sign_in_menu_page.verify_sign_in_form()