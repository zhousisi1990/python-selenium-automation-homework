from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self,end_url=''):
        self.driver.get(f'https://www.target.com/{end_url}')

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def click(self,locator):
        return self.driver.find_element(*locator).click()

    def input_text(self,text,locator):
        return self.driver.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        )
        return element

    def wait_until_clickable_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_until_appear(self,locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message = f'Element by {locator} not visible'
        )
        return element

    def wait_until_disappear(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still visible on the page'
        )

    def wait_until_url_contains(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected "{expected_partial_url}" not in "{self.driver.current_url}"'
        )

    def wait_until_url_to_be(self, expected_url):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f'Expected "{expected_url}", but got "{self.driver.current_url}"'
        )


    def verify_text(self,expected_result,locator):
        actual_result = self.find_element(locator).text
        assert expected_result == actual_result,\
            f'Expected "{expected_result}", but got"{actual_result}"'

    def verify_partial_text(self,expected_partial_text,locator):
        actual_result = self.find_element(locator).text
        assert expected_partial_text in  actual_result, \
            f'Expected "{expected_partial_text}" not in "{actual_result}"'