import time
import random
import string
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime

# Configuración de Selenium con Browserless
api_key = "2SUgwMA2mjrTcs2dc52850194106b52f224de7b71096e6992"  # Tu clave de API de Browserless
browserless_url = "https://chrome.browserless.io/webdriver"  # URL pública de Browserless para WebDriver

options = Options()
options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Incluir la clave de API en los encabezados HTTP de la solicitud
options.add_argument(f'--proxy-server={browserless_url}')
options.add_argument(f'--header=Authorization: Bearer {api_key}')  # Pasar la clave de API correctamente

# Usar Selenium con Browserless
try:
    driver = webdriver.Remote(
        command_executor=browserless_url,
        options=options,
        keep_alive=True  # Mantener la conexión activa
    )
except Exception as e:
    print(f"Error al conectar con Browserless: {e}")
    exit()

# Listas de nombres y apellidos comunes
nombres = ["Juan", "Carlos", "Maria", "Ana", "Pedro", "Luis", "Jose", "Laura", "Jorge", "Sofia"]
apellidos = ["Gomez", "Perez", "Rodriguez", "Martinez", "Lopez", "Gonzalez", "Hernandez", "Diaz", "Sanchez", "Torres"]

# Conectarse a la base de datos
def conectar_db():
    return sqlite3.connect(r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\base_datos\cuentas.db")

# Función para generar una contraseña aleatoria
def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Crear una cuenta de correo
def crear_cuenta():
    try:
        # Generar un nombre y apellido aleatorio
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombre_usuario = f"{nombre.lower()}.{apellido.lower()}"

        # Generar una contraseña aleatoria
        contrasena = generar_contrasena()

        # Generar una fecha de nacimiento aleatoria (usaremos una fecha estándar)
        dia = random.randint(1, 28)  # Asegurar que no haya problemas con el mes
        mes = random.randint(1, 12)
        anio = random.randint(1990, 2000)
        fecha_nacimiento = f"{dia:02d}/{mes:02d}/{anio}"

        # Generar sexo aleatorio
        sexo = random.choice(['Masculino', 'Femenino'])

        # Obtener la fecha de creación
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Acceder a Gmail
        driver.get("https://accounts.google.com/signup/v2/webcreateaccount")  # Gmail URL de creación de cuenta

        # Esperar a que los elementos estén disponibles (aumentamos el tiempo de espera a 30 segundos)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "firstName")))  # Esperar al campo 'firstName'

        # Rellenar el formulario
        driver.find_element(By.ID, "firstName").send_keys(nombre)  # Nombre
        driver.find_element(By.ID, "lastName").send_keys(apellido)  # Apellido

        # Usar 'jsname' para nombre de usuario
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[jsname='L2J9b']")))  # Esperar al campo de usuario
        driver.find_element(By.CSS_SELECTOR, "[jsname='L2J9b']").send_keys(nombre_usuario)  # Nombre de usuario (correo)

        driver.find_element(By.NAME, "Passwd").send_keys(contrasena)  # Contraseña
        driver.find_element(By.NAME, "ConfirmPasswd").send_keys(contrasena)  # Confirmar contraseña

        # Completar la fecha de nacimiento
        driver.find_element(By.ID, "day").send_keys(str(dia))  # Día
        Select(driver.find_element(By.ID, "month")).select_by_value(str(mes))  # Mes
        Select(driver.find_element(By.ID, "year")).select_by_value(str(anio))  # Año

        # Seleccionar el sexo
        if sexo == 'Masculino':
            driver.find_element(By.XPATH, "//div[@class='XY2WNe' and contains(text(),'Masculino')]").click()  # Seleccionar "Masculino"
        else:
            driver.find_element(By.XPATH, "//div[@class='XY2WNe' and contains(text(),'Femenino')]").click()  # Seleccionar "Femenino"

        # Esperar que el formulario sea procesado
        driver.find_element(By.ID, "accountDetailsNext").click()

        # Espera que la página de verificación cargue
        time.sleep(3)

        # Guardar los datos en la base de datos
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO cuentas (nombre, contrasena, fecha_creacion, fecha_nacimiento, sexo) VALUES (?, ?, ?, ?, ?)
        ''', (nombre_usuario, contrasena, fecha_creacion, fecha_nacimiento, sexo))
        conn.commit()

        # Depuración: Verificar si la inserción fue exitosa
        cursor.execute("SELECT * FROM cuentas WHERE nombre = ?", (nombre_usuario,))
        registro = cursor.fetchone()
        if registro:
            print(f"Registro insertado: {registro}")
        else:
            print("No se insertó ningún registro en la base de datos.")

    except Exception as e:
        print(f"Error al crear la cuenta: {e}")

    finally:
        conn.close()
        print(f"Cuenta creada: {nombre_usuario}, Contraseña: {contrasena}, Fecha de Creación: {fecha_creacion}, Fecha de Nacimiento: {fecha_nacimiento}, Sexo: {sexo}")
        driver.quit()  # Cerrar el navegador

# Ejecutar la creación de la cuenta
crear_cuenta()
