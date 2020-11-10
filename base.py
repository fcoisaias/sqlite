#en este archivo crearemos todo lo requerido para
#la base de datos

# Importamos el módulo
import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('base.db')


#crearemos una tabla para trabajar
# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Guardamos los cambios haciendo un commit
conexion.commit()
# Cerramos la conexión, si no la cerramos se mantendrá en uso y no podremos gestionar el fichero
conexion.close()