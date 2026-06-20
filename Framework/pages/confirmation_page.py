from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):

    country_input = (By.ID, "country")
    country_suggestions = (By.CSS_SELECTOR, ".suggestions a")
    terms_checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase_button = (By.CSS_SELECTOR, "input[type='submit']")
    success_message = (By.CSS_SELECTOR, ".alert-success")

    def enter_country(self, country):
        self.enter_text(self.country_input, country)

    def select_country_from_suggestions(self, country_name):
        countries = self.find_elements(self.country_suggestions)

        for country in countries:
            if country.text.strip().lower() == country_name.lower():
                country.click()
                return
        raise AssertionError(f"Country suggestion not found: {country_name}")

    def accept_terms_and_conditions(self):
        self.click_element(self.terms_checkbox)

    def click_purchase_button(self):
        self.click_element(self.purchase_button)

    def get_success_message(self):
        return self.get_text(self.success_message)
