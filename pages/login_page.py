from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _APP_LOGO = (By.CLASS_NAME, "app_logo")

    def ingresar_usuario(self, usuario):
        self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT)).send_keys(usuario)

    def ingresar_password(self, password):
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys(password)

    def hacer_click_login(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()

    def login(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_click_login()

    def obtener_texto_logo(self):
        return self.wait.until(EC.visibility_of_element_located(self._APP_LOGO)).text