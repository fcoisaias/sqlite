
import sqlite3
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('base.db')

# *******************Agregar datos***************
# Creamos el cursor
cursor = conexion.cursor()

#agregar usuarios
nombre=input("Ingresa el nombre del usuario: ")
edad=int(input("Ingresa la edad: "))
email=input("Ingresa el correo electrónico")

cursor.execute("INSERT INTO usuarios VALUES ('{}', '{}', '{}')".format(nombre,edad,email))
# Guardamos los cambios haciendo un commit
conexion.commit()


# *******************Agregar de una lista***************
#agregar usuarios de una lista de datos
# Creamos una lista con varios usuarios
usuarios = [('Alina', 18, 'alina@ejemplo.com'),
            ('Jordan', 18, 'jordan@ejemplo.com'),
            ('Andrés', 17, 'andres@ejemplo.com'),
            ]

# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

# Guardamos los cambios haciendo un commit
conexion.commit()


# *******************Consultar datos ***************
#Todos los registros
# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)


#Buscar un registro o condición en específico
# Recuperamos un registro de la tabla de usuarios
cursor.execute("SELECT nombre, edad, email FROM usuarios WHERE nombre='Alina'")
print("Muestra los de 18 años")
usuario = cursor.fetchone()
print(usuario)

# *******************Actualizar datos ***************

# Actualizamos un registro
cursor.execute("UPDATE usuarios SET edad=17 WHERE nombre='Alina'")

# Ahora lo consultamos de nuevo
cursor.execute("SELECT * FROM usuarios WHERE nombre='Alina'")
usuario = cursor.fetchone()
print(usuario)

conexion.commit()


# *******************Borrar datos ***************

# como borrar
cursor.execute("DELETE FROM usuarios WHERE nombre='Isaias'")

# Consultamos de nuevo los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)

conexion.commit()

#Cerrar conexión de base de datos si no usarás más la tabla
conexion.close()