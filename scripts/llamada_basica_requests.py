import requests

browserless_url = "https://production-sfo.browserless.io?token=TU_TOKEN_AQUI"
response = requests.get(browserless_url)

print(response.text)  # Debería devolver información o confirmar el acceso
