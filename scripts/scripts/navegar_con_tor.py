from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configuración del navegador
options = Options()
options.headless = False  # FORZAR ventana visible
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--start-maximized')
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Ruta real al chromedriver
service = Service(r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\chrome_driver\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

# Abre sitio y espera
driver.get("https://whatismyipaddress.com/")
input("Presiona ENTER para cerrar...")
driver.quit()