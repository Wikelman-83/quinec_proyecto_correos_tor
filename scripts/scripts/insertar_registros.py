import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect(r"C:\Users\wrmuela\Quinec\proyectoPythonCEA\proyecto_correos\base_datos\cuentas.db")
cursor = conn.cursor()

# Insertar registros de ejemplo si no están
registros_ejemplo = [
    ('185.220.101.1', 'NL'),
    ('192.168.0.1', 'US'),
    ('203.0.113.5', 'IN')
]

cursor.executemany('INSERT INTO registros_ip (ip, pais) VALUES (?, ?)', registros_ejemplo)

# Confirmar cambios
conn.commit()

# Verificar que los registros fueron insertados
cursor.execute("SELECT * FROM registros_ip")
registros = cursor.fetchall()

# Cerrar la conexión
conn.close()

# Mostrar los registros insertados
print("Registros insertados:")
for registro in registros:
    print(f"ID: {registro[0]} | IP: {registro[1]} | País: {registro[2]} | Fecha: {registro[3]}")
