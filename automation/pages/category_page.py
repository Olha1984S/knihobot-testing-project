from playwright.sync_api import Page, expect

from locators.category_page_locators import CategoryPageLocators
from locators.home_page_locators import HomePageLocators


class CategoryPage:
    """Page Object for a category page."""

    def __init__(self, page: Page):
        self.page = page

    def wait_until_loaded(self) -> None:
        """Wait until the category page is loaded."""

        breadcrumb = self.page.locator(
            CategoryPageLocators.CURRENT_BREADCRUMB
        )

        expect(breadcrumb).to_be_visible()

    def get_current_breadcrumb(self) -> str:
        """Return the current breadcrumb text."""

        return (
            self.page.locator(
                CategoryPageLocators.CURRENT_BREADCRUMB
            )
            .inner_text()
            .strip()
        )

    def return_to_home(self) -> None:
        logo = self.page.locator(HomePageLocators.LOGO)
        logo.scroll_into_view_if_needed()
        logo.click()