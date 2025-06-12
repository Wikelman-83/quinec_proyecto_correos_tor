import sqlite3

# Conectar a la base de datos
db_path = r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\base_datos\cuentas.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Consultar las tablas de la base de datos
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

# Verificar que la tabla registros_ip existe
if ('registros_ip',) in tablas:
    print("La tabla 'registros_ip' existe.")
else:
    print("La tabla 'registros_ip' no existe en esta base de datos.")

conn.close()
