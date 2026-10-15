from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_producto_al_carrito(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Guardar el nombre del producto que se va a agregar
    nombre_esperado = inventory_page.obtener_nombre_primer_producto()

    # Agregar primer producto y verificar incremento en el badge
    inventory_page.agregar_primer_producto_al_carrito()
    assert inventory_page.obtener_contador_carrito() == "1"

    # Navegar al carrito
    inventory_page.ir_al_carrito()

    # Validaciones en la página del carrito
    assert "/cart.html" in driver.current_url
    assert cart_page.obtener_titulo() == "Your Cart"
    assert cart_page.contar_productos_en_carrito() == 1
    assert cart_page.obtener_nombre_producto_en_carrito() == nombre_esperado