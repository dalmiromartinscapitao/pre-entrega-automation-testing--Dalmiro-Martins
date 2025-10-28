from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


url = "https://www.saucedemo.com/"
username ="standard_user"
password ="password"

# Crear opciones de Chrome
chrome_options = Options()

# Oculta los mensajes "DevTools listening" y otros logs internos
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Crear el driver usando ChromeDriver desde el PATH del sistema
driver = webdriver.Chrome(options=chrome_options)


def instala_driver():

    #instala el driver
    service = Service(ChromeDriverManager.install())
    driver = webdriver.Chrome(service=service)
    time.sleep(5)
    return(driver)

def login( driver ):
    # Ir a la página web
    
    driver.get(url)

    driver.find_element(By.ID, "user-name")
    driver.send_keys(username)

    driver.find_element(By.ID, "password")
    driver.send_keys(password)
    driver.send_keys(Keys.RETURN)

