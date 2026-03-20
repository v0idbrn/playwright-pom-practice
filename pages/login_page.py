class LoginPage:
    def __init__(self, page):
        self.page = page
        
        # Definimos los "componentes" (Locators)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        # Ajuste: Agregamos los corchetes [] para que reconozca el atributo
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """Va a la URL de la página de login"""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """Carga los datos y hace clic. El 'workflow' del login."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()