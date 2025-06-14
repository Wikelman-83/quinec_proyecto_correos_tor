import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect(r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\base_datos\cuentas.db")
cursor = conn.cursor()

# Consultar registros de IP y país
cursor.execute("SELECT * FROM registros_ip")
registros = cursor.fetchall()

# Mostrar los registros
if registros:
    for registro in registros:
        print(f"ID: {registro[0]} | IP: {registro[1]} | País: {registro[2]} | Fecha: {registro[3]}")
else:
    print("No hay registros en la base de datos.")

conn.close()
