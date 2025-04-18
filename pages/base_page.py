from playwright.sync_api import Page    #Page for browser interactions
import configparser                     #Configparser reads config file
import os                               #for interacting with Operating system
from dotenv import load_dotenv          #to load env variables from a .env file (optional)

load_dotenv()                           #Load env variables from .env if it exists


class BasePage:
    def __init__(self, page: Page):
        """
        Initialize the BasePage with Playwright Page object
        Args:  page (Page):  The PW Object representing the current browser tab
        """
        self.page = page