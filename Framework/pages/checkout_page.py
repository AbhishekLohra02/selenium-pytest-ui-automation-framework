from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from decimal import Decimal
import re


class CheckoutPage(BasePage):
    product_names = (By.CSS_SELECTOR, "h4.media-heading")
    final_checkout_button = (By.CSS_SELECTOR, "button.btn-success")
    product_totals = (By.XPATH, "//tbody/tr/td[4]/strong")
    grand_total = (By.XPATH, "//td/h3/strong")

    def get_product_names_in_cart(self):
        products = self.find_elements(self.product_names)
        product_names = []

        for product in products:
            product_names.append(product.text)
        return product_names

    def click_final_checkout_button(self):
        self.click_element(self.final_checkout_button)


    def get_product_total(self):
        totals = self.find_elements(self.product_totals)
        return [self.convert_price_to_number(total.text) for total in totals]
    
    def convert_price_to_number(self, price_text):
        numeric_value = re.sub(r"\D", "", price_text)
        return Decimal(numeric_value)
    

    def get_grand_total(self):
        return self.convert_price_to_number(self.get_text(self.grand_total))

        
        
