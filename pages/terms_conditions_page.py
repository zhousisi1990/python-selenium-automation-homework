from pages.base_page import Page

class TermsAndConditionsPage(Page):

 def verify_terms_and_conditions_page_opened(self):
    self.wait_until_url_contains('terms-conditions')