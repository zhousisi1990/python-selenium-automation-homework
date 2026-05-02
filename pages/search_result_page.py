from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    DD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_result(self,product:str):
        self.verify_partial_text(product,self.SEARCH_RESULTS_TEXT,)

    def click_on_first_add(self):
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.wait_until_clickable_click(self.DD_TO_CART_BTN)

