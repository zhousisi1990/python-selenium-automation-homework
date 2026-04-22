from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("User navigates to target help page")
def open_target_main(context):
    context.driver.get("https://help.target.com/help")
    sleep(2)

@then("Verifies all main UI elements are displayed")
def verify_main_ui_elements(context):
    # Header Help
    expected_help_result = 'Help'
    actual_help_result = context.driver.find_element(By.CSS_SELECTOR,"[class*='PageHeader'] h1").text
    assert  expected_help_result == actual_help_result, f'Expected {expected_help_result} but got {actual_help_result}'

    # Have a question?
    expected_question_result = 'a question'
    actual_question_result = context.driver.find_element(By.CSS_SELECTOR, "[class*='HelpSearch_helpSearchContainer'] span[class*='styles_textSpan']").text
    assert expected_question_result in actual_question_result, f'Expected {expected_question_result} not in {actual_question_result}'

    #Browse all help btn
    expected_btn_text = 'Browse all help'
    button_text = context.driver.find_element(
        By.CSS_SELECTOR, "[class*='HelpSearch_helpSearchHeaderContainer' ] button"
    ).text
    assert expected_btn_text in button_text, f'Expected {expected_btn_text} not in {button_text}'

    #Search button
    expected_search_text_result = 'Search'
    button_search_text = context.driver.find_element(
        By.CSS_SELECTOR, "[class*='HelpSearch_searchButtonContainer'] button"
    ).text
    assert expected_search_text_result == button_search_text, f'Expected {expected_search_text_result} not equal to {button_search_text}'

    #What would you like help with
    expected_text_result = 'What would you like help with?'
    actual_text_result = context.driver.find_element(
        By.CSS_SELECTOR, "[class*=SelfServiceLinks_selfServiceContainer] span[class*='styles_textSpan']"
    ).text
    assert expected_text_result == actual_text_result, f'Expected {expected_text_result}not equal to {actual_text_result}'

    # Verify 9 links displayed
    expected_amount = 9
    actual_amount = len(
        context.driver.find_elements(By.CSS_SELECTOR, "[class*='NavCard_navCardWrapper'] a"))
    print(actual_amount)
    assert actual_amount == expected_amount, f'Expected {expected_amount} links but got {actual_amount}'

    #Popular Page
    expected_pop_text_result = 'Popular Pages'
    actual_pop_text_result = context.driver.find_element(
        By.CSS_SELECTOR, "[class*='LinkCard_titleCard']"
    ).text
    assert expected_pop_text_result == actual_pop_text_result, f'Expected {expected_pop_text_result}not equal to {actual_pop_text_result}'

    # Verify 8 Link item displayed
    expected_pop_section_amount = 8
    actual_pop_section_amount = len(
        context.driver.find_elements(By.CSS_SELECTOR, "[class*='LinkItem_styledLink']"))
    assert actual_pop_section_amount == expected_pop_section_amount, f'Expected {expected_pop_section_amount} items but got {actual_pop_section_amount}'

