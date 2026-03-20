from pages.login_page import LoginPage
import pytest

def test_login_success(page):
    # 1. Instanciamos la página
    login = LoginPage(page)
    
    # 2. Ejecutamos las acciones
    login.navigate()
    login.login("standard_user", "secret_sauce")
    
    # 3. Verificamos que todo esté OK
    assert page.url == "https://www.saucedemo.com/inventory.html"