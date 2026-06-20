import pytest
from pages.home_page import HomePage


@pytest.mark.smoke
def test_home_page_load_name_feild_visible(setup):
    driver = setup
    home_page = HomePage(driver)

    assert home_page.is_element_visible(home_page.name_feild)

