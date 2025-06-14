from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta completa al chromedriver
chromedriver_path = "C:/Users/wrmuela/Quinec/proyectoPythonCEA/proyecto_correos/chrome_driver/chromedriver.exe"  # Actualiza con la ruta correcta

# Configurar las opciones de Chrome
options = Options()
options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Crear el servicio con el chromedriver
service = Service(executable_path=chromedriver_path)

# Usar el servicio y las opciones para iniciar el navegador
driver = webdriver.Chrome(service=service, options=options)

# Ir a la página de creación de cuenta de Outlook
driver.get("https://signup.live.com/")

# Esperar a que el campo del nombre de usuario esté disponible
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "memberName")))

# Rellenar los campos del formulario (esto es solo un ejemplo)
driver.find_element(By.NAME, "memberName").send_keys("nuevo_usuario@outlook.com")  # Nombre de usuario
driver.find_element(By.NAME, "password").send_keys("ContraseñaSegura123")  # Contraseña

# Otros campos de registro pueden ser completados de forma similar...

# Esperar un poco para ver el resultado
time.sleep(5)

# Cerrar el navegador
driver.quit()
