from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

def instala_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    time.sleep(5)
    return driver

def login(driver):
    driver.get(url)

    input_user = driver.find_element(By.ID, "user-name")
    input_user.send_keys(username)

    input_pass = driver.find_element(By.ID, "password")
    input_pass.send_keys(password)

    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()