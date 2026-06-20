import pytest

from pages.home_page import HomePage


@pytest.mark.regression
def test_name_field_shows_validation_for_single_character(setup):
    home_page = HomePage(setup)

    home_page.enter_name("A")
    home_page.enter_email("tester@example.com")

    assert "minimum" in home_page.get_name_error_message().lower()
