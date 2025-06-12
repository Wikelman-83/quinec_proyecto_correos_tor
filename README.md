# Proyecto Correos Tor

Este proyecto automatiza la creación y gestión de cuentas de correo electrónico utilizando **Tor** y **Selenium**. El sistema se conecta a través de la red Tor para garantizar el anonimato al realizar tareas automáticas, como la obtención de direcciones IP y la creación de cuentas.

## Tecnologías utilizadas

- **Python 3.10+**: Lenguaje de programación.
- **Selenium**: Para la automatización de navegador web.
- **Tor Expert Bundle**: Para ocultar la IP y navegar de forma anónima.
- **ChromeDriver**: Necesario para usar Selenium con Google Chrome.
- **SQLite**: Para almacenar los registros de IP y país.

## Requisitos

Este proyecto depende de las siguientes librerías de Python:

- `selenium`
- `requests`
- `PySocks` (para usar el proxy Tor)
  
Para instalar todas las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt


##Autor

Wikelman([@Wikelman-83](https://github.com/Wikelman-83))