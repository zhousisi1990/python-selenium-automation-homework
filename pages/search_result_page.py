from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
    def verify_search_result(self,product:str):
        actual_result = self.find_element(self.SEARCH_RESULTS_TEXT).text
        assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'
