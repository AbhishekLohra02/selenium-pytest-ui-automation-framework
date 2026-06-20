import pytest

from pages.home_page import HomePage
from pages.shop_page import ShopPage


@pytest.mark.sanity
def test_user_can_add_single_product_to_cart(setup):
    home_page = HomePage(setup)
    home_page.click_shop_link()
    shop_page = ShopPage(setup)

    shop_page.add_product_to_cart("iphone X")

    assert "Checkout ( 1 )" in shop_page.get_checkout_button_text()


@pytest.mark.sanity
def test_user_can_add_more_than_one_product_to_cart(setup):
    
    home_page = HomePage(setup)
    home_page.click_shop_link()

    shop_page = ShopPage(setup)

    shop_page.add_products_to_cart(["iphone X", "Samsung Note 8"])
    assert "Checkout ( 2 )" in shop_page.get_checkout_button_text()

