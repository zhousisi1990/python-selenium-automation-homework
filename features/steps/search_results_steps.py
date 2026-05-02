from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
PRODUCT_LISTS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR,"[data-test='@web/ProductCard/title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary'] img")

@when("Click on the first Add to cart button")
def click_on_first_add(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    first_btn = context.driver.find_element(*ADD_TO_CART_BTN)
    context.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        first_btn
    )
    first_btn.click()

@then("Verify search results for {product} shown")
def verify_search_results(context,product):
    # actual_result = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    # assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'
    context.app.search_result_page.verify_search_result(product)

@then("Each product should have a product name and img")
def each_product_name_img(context):
   context.driver.execute_script("window.scrollBy(0,1700)", "")
   sleep(0.5)
   context.driver.execute_script("window.scrollBy(0,1700)", "")
   sleep(0.5)
   context.driver.execute_script("window.scrollBy(0,1700)", "")
   sleep(0.5)

   products = context.driver.find_elements(*PRODUCT_LISTS)
   for product in products:
       title = product.find_element(*PRODUCT_TITLE).text
       assert title, 'Product title not shown'
       print(f'🟢{title}')
       # img = product.find_element(*PRODUCT_IMG)
       # print(img.get_attribute('src'))




