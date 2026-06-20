from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShopPage(BasePage):
    product_cards = (By.CSS_SELECTOR, ".card.h-100")
    checkout_button = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")

    def add_product_to_cart(self, product_name):
        products = self.find_elements(self.product_cards)

        for product in products:
            if product_name in product.text:
                product.find_element(By.CSS_SELECTOR, "button").click()
                return
        raise AssertionError(f"Product not found on shop page: {product_name}")

    def add_products_to_cart(self, product_names):
        for product_name in product_names:
            self.add_product_to_cart(product_name)

    def click_checkout(self):
        self.click_element(self.checkout_button)

    def get_checkout_button_text(self):
        return self.get_text(self.checkout_button)
