from pages.login_page import LoginPage
import pytest

# TEST 1: Login success
def test_login_success(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

# TEST 2: Login failure
def test_login_failure(page):
    login = LoginPage(page)
    login.navigate()
    
    # Mandamos cualquier fruta en el pass
    login.login("standard_user", "password_incorrecta_hdp")
    
    # Verificamos que aparezca el mensaje de error
    # Usamos el locator que ya definimos en la clase LoginPage
    assert login.error_message.is_visible()
    assert "Username and password do not match" in login.error_message.text_content()