from playwright.sync_api import Page  # Importing the Page object from Playwright.
from pages.base_page import BasePage  # Importing the BasePage class, which this class inherits from.


class HomePage(BasePage):
    def __init__(self, page: Page):
        """
        Initializes the HomePage object, inheriting from BasePage.
        :param page:  (Page): The Playwright Page object.
        """
        super().__init__(page)  # Calls the __init__ method of the parent class (BasePage), passing the Page object.
        self.logo_locator = "a[aria-label='Oprah.com']"  # Defines a locator for the Oprah.com logo using a CSS selector.
        self.navigation_links_locator = "ul[role='menubar'] li a"  # Defines a locator for the main navigation links (adjust if needed).

    def navigate_to_homepage(self):
        """
        Navigates the browser to the homepage using the navigate method from the BasePage.
        """
        self.navigate()  # Calls the 'navigate' method inherited from BasePage (which uses the base_url).

    def is_logo_visible(self):
        """
        Checks if the Oprah.com logo is visible on the page.

        Returns:
            bool: True if the logo is visible, False otherwise.
        """
        return self.is_visible(self.logo_locator)  # Calls the 'is_visible' method inherited from BasePage, using the logo locator.

    def get_navigation_links_text(self):
        """
        Retrieves the text content of all the main navigation links.

        Returns:
            list: A list of strings, where each string is the text of a navigation link.
        """
        links = self.page.locator(self.navigation_links_locator).all_inner_texts()  # Uses Playwright's 'locator' to find all matching elements and then extracts their inner text.
        return links  # Returns the list of link texts.
