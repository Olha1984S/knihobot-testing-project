from pages.cookie_banner import CookieBanner
from pages.home_page import HomePage
from pages.category_page import CategoryPage


def test_navigation(page):
    """Verify navigation through random menu items."""

    home_page = HomePage(page)
    cookie_banner = CookieBanner(page)
    category_page = CategoryPage(page)

    home_page.open()
    cookie_banner.accept_necessary()
    home_page.verify_page_loaded()

    failures = []

    NAVIGATION_ITERATIONS = 5

    for i in range(NAVIGATION_ITERATIONS):

        try:
            category_id = home_page.hover_random_menu_button()
            selected = home_page.click_random_subcategory(category_id)

            category_page.wait_until_loaded()

            actual = category_page.get_current_breadcrumb()

            expected = selected.removeprefix("Vše z ").removeprefix("Vše ze ")

            if expected not in actual:
                failures.append(
                    f"\n[{i + 1}] Header mismatch\n"
                    f"URL: {page.url}\n"
                    f"Menu:        {selected}\n"
                    f"Expected:    {expected}\n"
                    f"Breadcrumb:  {actual}"
                )

        finally:
            category_page.return_to_home()
            home_page.verify_page_loaded()

    assert not failures, (
        "The following header mismatches were found:\n"
        + "\n".join(failures)
    )