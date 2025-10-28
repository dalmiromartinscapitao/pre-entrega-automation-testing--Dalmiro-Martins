import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from auxiliares.funciones_auxiliares import instala_driver, login

@pytest.fixture
def driver():
    driver = instala_driver
    yield driver
    driver.quit()

def test_login(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url()
    boton_de_producto = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container ,title').text
    assert boton_de_producto == "Products"

def test_catalogo():
     login(driver)
     titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_label ,app_logo').text
     assert titulo == "Swag Labs"
     productos = driver.find_elements(By.CLASS_NAME, "inventory_list")
     assert productos.len() > 0
     filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')
     assert filtro in driver.current_url()


def test_carrito():
    login(driver)
    boton_comprar_bolso = driver.find_element(By.NAME "add-to-cart-sauce-labs-backpack")
    boton_comprar_bolso.click()
    contador_de_carrito = driver.find_element(By.CSS_SELECTOR, 'shopping_cart_badge ,shopping-cart-badge').int
    assert contador_de_carrito > 0
    carrito = driver.find_element(By.ID, 'shopping_cart_container')
    carrito.click()
    carrito_agregado = driver.find_element(By.CSS_SELECTOR, 'inventory_item_name ,inventory-item-name').text
    assert carrito_agregado == "Sauce Labs Backpack"
