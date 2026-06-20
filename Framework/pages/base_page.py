from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config.config import EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def select_dropdown_by_text(self, locator, text):
        dropdown = Select(self.wait.until(EC.visibility_of_element_located(locator)))
        dropdown.select_by_visible_text(text)

    def wait_for_url_contains(self, partial_url):
        return self.wait.until(EC.url_contains(partial_url))
