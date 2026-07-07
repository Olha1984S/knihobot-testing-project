import random
from playwright.sync_api import Locator, Page, expect

from locators.home_page_locators import HomePageLocators


class HomePage:
    """Page Object for the Knihobot home page."""

    URL = "https://knihobot.cz/"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        """Open the home page."""

        self.page.goto(
            self.URL,
            wait_until="domcontentloaded",
            timeout=60000,
        )

    def verify_page_loaded(self) -> None:
        """Verify that the home page has loaded successfully."""

        logo = self.page.locator(HomePageLocators.LOGO)
        expect(logo).to_be_visible()

    def get_main_menu_buttons(self) -> list[Locator]:
        """Return locators for all main navigation buttons."""

        return [
            self.page.locator(
                HomePageLocators.CATEGORY_MENU_BUTTON.format(category_id)
            )
            for category_id in HomePageLocators.CATEGORY_MENU_IDS
        ]

    def hover_random_menu_button(self) -> int:
        """Hover over a randomly selected main navigation button."""

        category_id = random.choice(HomePageLocators.CATEGORY_MENU_IDS)

        menu_button = self.page.locator(
            HomePageLocators.CATEGORY_MENU_BUTTON.format(category_id)
        )

        menu_button.hover()

        return category_id

    def get_menu_button_text(self, category_id: int) -> str:
        """Return the text of the selected main menu button."""

        menu_button = self.page.locator(
            HomePageLocators.CATEGORY_MENU_BUTTON.format(category_id)
        )

        return menu_button.inner_text().strip()

    def click_random_subcategory(self, category_id: int) -> str:
        """Click a random subcategory from the opened menu and return its name."""

        menu_button = self.page.locator(
            HomePageLocators.CATEGORY_MENU_BUTTON.format(category_id)
        )

        category_menu = self.page.locator(
            HomePageLocators.CATEGORY_MENU.format(category_id)
        )

        # Reopen the menu in case it has already closed.
        menu_button.hover()
        expect(category_menu).to_be_visible()

        links = category_menu.locator(
            HomePageLocators.SUBCATEGORY_LINKS
        )

        expect(links.first).to_be_visible()

        random_index = random.randrange(links.count())
        subcategory = links.nth(random_index)

        # subcategory.scroll_into_view_if_needed()
        # expect(subcategory).to_be_visible()

        subcategory_name = subcategory.inner_text().strip()

        print(f"Selected subcategory: {subcategory_name}")

        subcategory.click()
        print(f"After click URL: {self.page.url}")

        return subcategory_name
    

