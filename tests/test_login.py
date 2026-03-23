import pytest
from pages.login_page import LoginPage

"""
Test Suite: Authentication Flow
Description: Verifies the login functionality for the SauceDemo application.
Pattern: Page Object Model (POM)
"""

def test_login_success(page):
    """
    Test Case: Successful Login
    Objective: Verify that a user can log in with valid credentials.
    Expected Result: Redirection to the inventory page.
    """
    login = LoginPage(page)
    
    login.navigate()
    login.login("standard_user", "secret_sauce")
    
    # Assert redirection to the correct endpoint
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_login_failure(page):
    """
    Test Case: Login Failure (Negative Testing)
    Objective: Verify that the system displays an error message for invalid credentials.
    Expected Result: Error message visibility and correct error text.
    """
    login = LoginPage(page)
    
    login.navigate()
    
    # Testing with invalid credentials to trigger validation
    login.login("standard_user", "invalid_password_test")
    
    # Assert error message properties
    assert login.error_message.is_visible(), "Error message should be visible on failed login"
    
    expected_error = "Username and password do not match"
    assert expected_error in login.error_message.text_content(), f"Expected error message: '{expected_error}'"