import sqlite3
import os

# Ruta absoluta
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'base_datos'))
os.makedirs(base_dir, exist_ok=True)  # Crea la carpeta si no existe
db_path = os.path.join(base_dir, 'cuentas.db')

# Crear y conectar
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cuentas_google (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insertar datos
cuentas = [
    ('ejemplo1@gmail.com', 'Password123'),
    ('ejemplo2@gmail.com', 'Clave456'),
    ('ejemplo3@gmail.com', 'MiPass789')
]
cursor.executemany('INSERT INTO cuentas_google (email, password) VALUES (?, ?)', cuentas)

# Cerrar
conn.commit()
conn.close()

print("Base de datos creada y poblada con éxito.")
