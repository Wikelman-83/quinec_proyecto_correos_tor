import sqlite3

def obtener_credenciales():
    conn = sqlite3.connect('../base_datos/cuentas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM cuentas_google")
    cuentas = cursor.fetchall()
    conn.close()
    return cuentas

# Probar lectura
for email, password in obtener_credenciales():
    print(f"Email: {email}, Password: {password}")
