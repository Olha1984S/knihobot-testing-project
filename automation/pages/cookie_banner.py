from playwright.sync_api import Page

from locators.cookie_banner_locators import CookieBannerLocators


class CookieBanner:
    """Page Object for the cookie consent banner."""

    def __init__(self, page: Page):
        self.page = page

    def accept_necessary(self):
        """Accept only necessary cookies."""

        banner = self.page.locator(CookieBannerLocators.BANNER)
        accept_button = self.page.locator(
            CookieBannerLocators.ACCEPT_NECESSARY_BUTTON
        )

        if banner.is_visible():
            accept_button.click()
            banner.wait_for(state="hidden")
