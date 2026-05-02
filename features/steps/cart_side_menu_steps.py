from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

# This can only cover the search result which can be picked up
# ADD_TO_CART_BTN = By.CSS_SELECTOR,"[data-test='orderPickupButton']"
ADD_TO_CART_BTN = (By.CSS_SELECTOR,"[data-test='content-wrapper'] button[id*='addToCartButton']")
CLOSE_SIDE_MENU_BTN =  (By.CSS_SELECTOR,"[class*='styles_nonScrollModalContent'] button[aria-label='close']")
ADDED_TO_CART_TEXT = (By.XPATH,"//*[text()='Added to cart']")

@when("Click on Add to cart button from side menu")
def click_on_to_cart_button(context):
    context.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Add to Cart button from side navigation not visible'
    ).click()

@when("Close side menu")
def close_side_menu(context):
    # buttons = context.driver.find_elements(By.CSS_SELECTOR,'button[aria-label="close"]')
    # buttons[1].click()
    context.wait.until(
        EC.visibility_of_element_located(ADDED_TO_CART_TEXT),
        message = "Added to cart text not shown")
    context.wait.until(EC.element_to_be_clickable(CLOSE_SIDE_MENU_BTN),
                       message='Close side menu btn is not visible'
    ).click()

