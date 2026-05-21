from behave import given, when, then

@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()

@when("Input email and password on SignIn page")
def input_email_and_password(context):
    context.app.sign_in_page.input_email_and_password()

@then("Verify the verification code sent shown")
def verify_verify_code_sent(context):
    context.app.sign_in_page.verify_verification_code_sent()

@given("Open sign in page")
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when("Click on Target terms and conditions link")
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_on_target_terms_and_conditions_link()

@then("Verify Terms and Conditions page is opened")
def verify_terms_and_conditions_page_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page_opened()



