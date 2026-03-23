"""
Page Object Model: LoginPage
Description: Encapsulates UI locators and interaction logic for the Authentication module.
"""

class LoginPage:
    def __init__(self, page):
        """
        Initialize the Page Object with Playwright locators.
        Think of these as the 'test points' or 'pins' of the UI component.
        """
        self.page = page
        
        # UI Element Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        
        # Error validation component (Attribute-based selector)
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """
        Navigate to the application's primary login endpoint.
        """
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """
        Execute the authentication workflow.
        Input: user credentials.
        Action: Populate fields and trigger the login event.
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()