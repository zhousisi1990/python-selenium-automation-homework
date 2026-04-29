from pages.base_page import Page
from time import sleep

class MainPage(Page):

    def open_main_page(self):
        self.open_url()
        sleep(2)
