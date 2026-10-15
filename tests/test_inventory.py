from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Validación del título de la sección de inventario
    assert inventory_page.obtener_titulo_seccion() == "Products"

    # Validación de presencia de productos
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0

    # Validación del primer producto (nombre y precio)
    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    assert inventory_page.obtener_precio_primer_producto() == "$29.99"

    # Validación de componentes de interfaz
    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()