import requests

api_key = "2SUgwMA2mjrTcs2dc52850194106b52f224de7b71096e6992"  # Tu clave de API de Browserless
browserless_url = "https://chrome.browserless.io/health"  # Endpoint de salud para probar la conexión

# Hacer una solicitud GET para verificar si la clave de API funciona
headers = {
    'Authorization': f'Bearer {api_key}'  # Pasar la clave de API en los encabezados
}

response = requests.get(browserless_url, headers=headers)

# Verificar la respuesta
if response.status_code == 200:
    print("La autenticación con Browserless fue exitosa.")
else:
    print(f"Error de autenticación con Browserless: {response.status_code}, {response.text}")
