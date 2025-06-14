import requests
import sqlite3

# Conectarse a la API de ipinfo usando el proxy Tor (SOCKS5)
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Agregar tu clave API
api_key = 'bf0d4c58b62184'  # Sustituye con tu API token real

# Obtener IP y país desde la API de ipinfo
try:
    response = requests.get(f'https://ipinfo.io/json?token={api_key}', proxies=proxies, timeout=10)

    # Verificar si la respuesta es exitosa
    if response.status_code == 200:
        data = response.json()

        ip = data.get('ip')
        pais = data.get('country')

        if ip and pais:
            print(f"IP detectada: {ip}")
            print(f"País: {pais}")

            # Conectar a la base de datos y almacenar los registros
            conn = sqlite3.connect(r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\base_datos\cuentas.db")
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO registros_ip (ip, pais) VALUES (?, ?)
            ''', (ip, pais))

            conn.commit()
            conn.close()

            print("Registro guardado exitosamente en la base de datos.")
        else:
            print("Error: IP o país no disponibles en la respuesta de la API.")
    else:
        print(f"Error al obtener datos de la API: {response.status_code}")

except Exception as e:
    print("Error al obtener o guardar la IP:", e)
