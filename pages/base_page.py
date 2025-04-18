from playwright.sync_api import Page    # Page for browser interactions
import configparser                     # Configparser reads config file
import os                               # For interacting with Operating system
from dotenv import load_dotenv          # To load env variables from a .env file (optional)

load_dotenv()                           # Load env variables from .env if it exists


class BasePage:
    def __init__(self, page: Page):
        """
        Initialize the BasePage with Playwright Page object
        Args:  page (Page):  The PW Object representing the current browser tab
        """
        self.page = page        # Assigns the passed Page to the instance's 'page' attribute, allowing interaction with the browser
        self.config = configparser.ConfigParser()   # Creates an instance of the ConfigParser to handing configuration
        self.config.read('config/config.ini')       # Reads settings from 'config.ini' file
        self.base_url = self.config.get('environment', 'base_url')  # Retrieves url from the '[environment]' section of config file

    def navigate(self, path=""):
        """
        Navigate the browser to the specified path relative to the base URL.
        Args: path (str, optional): The path to navigate to (ex. "/food")
        Defaults to "".
        """
        self.page.goto(f"{self.base_url}/{path}")   # User 'goto' method to navigate to constructed url

    def get_title(self):            # Returns title of the current web page
        return self.page.title()    # 'title' method to return the page title

    def get_url(self):              # Returns the URL of the current web page
        return self.page.url        # 'url' method get the current url

    def is_visible(self, locator):
        """
        Check if an element matching given locator is visible on page
        Args: locator(str): PW locator string to identify the element
        Returns: bool: True if element is visible, otherwise false
        """
        return self.page.is_visible(locator)    # 'is_visible' method to check element visibility

    def get_text(self, locator):
        """
        Retrieves the inner text content of an element matching the given locator.
        Args: locator (str): PW locator string to identify the element.
        Returns: str: The inner text of the element.
        """
        return self.page.inner_text(locator)

    def click(self, locator):
        """
        Clicks on an element matching the given locator.
        Args: locator (str): PW locator string to identify the element.
        """
        self.page.click(locator)

    def fill(self, locator, text):
        """
        Fills an input field or similar element matching the given locator with the provided text.
        Args: locator (str): PW locator string to identify an element.
              text (str): The text to fill into the element.
        """
        self.page.fill(locator, text)

    def wait_for_load_state(self, state="domcontentloaded", timeout=30000):
        """
        Waits for the page to reach a specific load state.
        :param state: (str, optional): Load state to wait for ('domcontentloaded', 'load', 'networkidle')
        :param timeout: (int, optional): The maximum time to wait in milliseconds. Default is 30000
        """
        self.page.wait_for_load_state(state=state, timeout=timeout)
