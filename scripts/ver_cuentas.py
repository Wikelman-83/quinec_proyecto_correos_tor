import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect(r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\base_datos\cuentas.db")
cursor = conn.cursor()

# Consultar los registros de la tabla 'cuentas'
cursor.execute("SELECT * FROM cuentas")
registros = cursor.fetchall()

# Mostrar los registros
for registro in registros:
    print(f"ID: {registro[0]} | Nombre: {registro[1]} | Contraseña: {registro[2]} | Fecha de Creación: {registro[3]} | Fecha de Nacimiento: {registro[4]}")

# Cerrar la conexión
conn.close()
