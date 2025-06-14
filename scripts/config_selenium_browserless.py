from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuración de Browserless
browserless_url = "https://chrome.browserless.io"
options = Options()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Conectar a Browserless a través de WebDriver
service = Service(executable_path="path_to_your_local_chromedriver")
driver = webdriver.Remote(
    command_executor=browserless_url,
    options=options
)

driver.get("https://www.google.com")
print(driver.title)  # Mostrar el título de la página

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuración de Browserless
browserless_url = "https://chrome.browserless.io"
options = Options()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Conectar a Browserless a través de WebDriver
service = Service(executable_path="path_to_your_local_chromedriver")
driver = webdriver.Remote(
    command_executor=browserless_url,
    options=options
)

driver.get("https://www.google.com")
print(driver.title)  # Mostrar el título de la página

driver.quit()
