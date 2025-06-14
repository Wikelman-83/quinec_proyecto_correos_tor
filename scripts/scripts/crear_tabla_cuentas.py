# Guardar los datos en la base de datos
conn = conectar_db()
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO cuentas (nombre, contrasena, fecha_creacion, fecha_nacimiento) VALUES (?, ?, ?, ?)
''', (nombre_usuario, contrasena, fecha_creacion, fecha_nacimiento))
conn.commit()

# Depuración: Verificar si la inserción fue exitosa
cursor.execute("SELECT * FROM cuentas WHERE nombre = ?", (nombre_usuario,))
registro = cursor.fetchone()
print(f"Registro insertado: {registro}")

conn.close()
