from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    def verify_search_result(self,product:str):
        self.verify_partial_text(product,self.SEARCH_RESULTS_TEXT,)