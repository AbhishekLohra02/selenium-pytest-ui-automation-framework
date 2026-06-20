import pytest

from pages.home_page import HomePage


@pytest.mark.sanity
def test_user_can_submit_practice_form(setup):
    home_page = HomePage(setup)

    home_page.fill_practice_form(
        name="Automation Tester",
        email="tester@example.com",
        password="Password123",
        gender="Female",
        birthday="1998-08-14",
    )
    home_page.click_submit()

    assert "success" in home_page.get_success_message().lower()
