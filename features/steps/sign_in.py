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