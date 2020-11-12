import sqlite3

conexion = sqlite3.connect('tinker_sqlite.db')

cursor = conexion.cursor()

# Creamos un campo matricula como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    matricula VARCHAR(9) PRIMARY KEY,
                    nombre VARCHAR(100), 
                    edad INTEGER)''')

conexion.commit()
conexion.close()