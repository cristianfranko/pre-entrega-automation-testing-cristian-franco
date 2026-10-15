from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Localizadores
    _PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    _TITULO_SECCION = (By.CLASS_NAME, "title")
    _BURGER_MENU = (By.ID, "react-burger-menu-btn")
    _FILTRO = (By.CLASS_NAME, "product_sort_container")
    _BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    _LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")

    def obtener_titulo_seccion(self):
        return self.wait.until(EC.visibility_of_element_located(self._TITULO_SECCION)).text

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTOS)

    def obtener_nombre_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    def obtener_precio_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    def agregar_primer_producto_al_carrito(self):
        productos = self.obtener_productos()
        boton_agregar = productos[0].find_element(By.TAG_NAME, "button")
        boton_agregar.click()

    def obtener_contador_carrito(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self._BADGE_CARRITO))
        return elemento.text

    def ir_al_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._LINK_CARRITO)).click()

    def menu_visible(self):
        menu = self.driver.find_element(*self._BURGER_MENU)
        return menu.is_displayed()

    def filtro_visible(self):
        filtro = self.driver.find_element(*self._FILTRO)
        return filtro.is_displayed()