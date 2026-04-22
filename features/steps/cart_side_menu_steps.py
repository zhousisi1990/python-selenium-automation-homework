from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when("Click on Add to cart button from side menu")
def click_on_to_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='orderPickupButton']").click()
    sleep(7)



@when("CLose side menu")
def close_side_menu(context):
    # buttons = context.driver.find_elements(By.CSS_SELECTOR,'button[aria-label="close"]')
    # buttons[1].click()
    context.driver.find_element(
    By.CSS_SELECTOR,
    "[class*='styles_nonScrollModalContent'] button[aria-label='close']"
    ).click()

