from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/login")
print(driver.title)

# lo mas comunes son los id, name y clases
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")

# click login
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

# para verificar 
value = driver.find_element(By.ID, "flash").text
print("Ya esta logeado")

time.sleep(5)

driver.quit()