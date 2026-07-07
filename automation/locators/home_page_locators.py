# locators/home_page_locators.py

class HomePageLocators:
    """Locators for the Knihobot home page."""

    # Home page
    LOGO = "a.HeaderLogo_styles_root__2Qyuj"
    NAVIGATION = ".HeaderCategories_styles_root__HuLWi"

    # Main navigation menu
    CATEGORY_MENU_BUTTON = '[id="categories-{}-menu-button"]'
    CATEGORY_MENU = "#categories-{}-menu"

    # IDs of the main navigation buttons
    CATEGORY_MENU_IDS = (
        246,
        247,
        248,
        249,
        250,
    )

    # Links inside the opened mega menu
    SUBCATEGORY_LINKS = "a[href]"