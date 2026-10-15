from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores
    _TITULO_CARRITO = (By.CLASS_NAME, "title")
    _ITEMS_CARRITO = (By.CLASS_NAME, "cart_item")
    _NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")

    def obtener_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self._TITULO_CARRITO)).text

    def obtener_nombre_producto_en_carrito(self):
        return self.wait.until(EC.visibility_of_element_located(self._NOMBRE_PRODUCTO)).text

    def contar_productos_en_carrito(self):
        return len(self.driver.find_elements(*self._ITEMS_CARRITO))