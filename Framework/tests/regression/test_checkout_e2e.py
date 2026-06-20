import pytest

from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage
from pages.shop_page import ShopPage


@pytest.mark.regression
def test_user_can_place_order_for_multiple_products(setup):
    home_page = HomePage(setup)
    home_page.click_shop_link()
    shop_page = ShopPage(setup)

    selected_products = ["iphone X", "Samsung Note 8"]
    shop_page.add_products_to_cart(selected_products)
    shop_page.click_checkout()

    checkout_page = CheckoutPage(setup)
    cart_products = checkout_page.get_product_names_in_cart()

    for product in selected_products:
        assert product in cart_products

    checkout_page.click_final_checkout_button()

    confirmation_page = ConfirmationPage(setup)
    confirmation_page.enter_country("India")
    confirmation_page.select_country_from_suggestions("India")
    confirmation_page.accept_terms_and_conditions()
    confirmation_page.click_purchase_button()

    assert "success" in confirmation_page.get_success_message().lower()

@pytest.mark.regression
def test_user_can_complete_purchase_with_correct_cart_total(setup):
    home_page = HomePage(setup)

    home_page.fill_practice_form(
        name= "bhaisaab",
        email= "bhaisaab@gmail.com",
        password= "Bhaisaab123",
        gender= "Male",
        birthday="1901-01-01",
)
    home_page.click_submit()
    assert "success" in home_page.get_success_message().lower()

    home_page.click_shop_link()
    shop_page = ShopPage(setup)


    selected_products = ["Nokia Edge", "Blackberry"]
    shop_page.add_products_to_cart(selected_products)

    assert "Checkout ( 2 )" in shop_page.get_checkout_button_text()

    shop_page.click_checkout()

    checkout_page = CheckoutPage(setup)
        
    calculate_total = sum(checkout_page.get_product_total())
    grand_total = checkout_page.get_grand_total()

    assert calculate_total == grand_total


