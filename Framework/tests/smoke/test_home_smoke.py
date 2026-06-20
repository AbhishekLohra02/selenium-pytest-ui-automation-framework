import pytest
from pages.home_page import HomePage


@pytest.mark.smoke
def test_home_page_loads(setup):
    driver = setup
    home_page = HomePage(driver)

    assert home_page.is_element_visible(home_page.name_input)


@pytest.mark.smoke
def test_shop_page_navigation(setup):
    driver = setup
    home_page = HomePage(driver)

    home_page.click_shop_link()
    home_page.wait_for_url_contains("shop")

    assert "shop" in driver.current_url.lower()
