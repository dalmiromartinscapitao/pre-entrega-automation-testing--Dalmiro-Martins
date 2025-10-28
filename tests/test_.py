import pytest
from selenium.webdriver.common.by import By
from auxiliares.funciones_auxiliares import login


def test_login(driver):
    login(driver)
    
    assert "/inventory.html" in driver.current_url
    driver.save_screenshot('Esta en la pagina correcta.jpg')
    
    boton_de_producto = driver.find_element(By.CSS_SELECTOR, ".header_secondary_container .title").text
    assert boton_de_producto == "Products"


def test_catalogo(driver):
   
    login(driver)
    
    titulo = driver.find_element(By.CSS_SELECTOR, ".header_label .app_logo").text
    assert titulo == "Swag Labs"
    driver.save_screenshot('Esta el titulo.jpg')

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()
    driver.save_screenshot('Esta el filtro.jpg')


def test_carrito(driver):
    login(driver)
    
    boton_comprar_bolso = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    boton_comprar_bolso.click()
  
    contador_de_carrito = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert int(contador_de_carrito.text) > 0
    driver.save_screenshot('contador de carrito es 1.jpg')

    carrito = driver.find_element(By.ID, "shopping_cart_container")
    carrito.click()

    carrito_agregado = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    assert carrito_agregado == "Sauce Labs Backpack"
    driver.save_screenshot('Se agrego al carrito.jpg')