
# *******************Claves primarias ***************
import sqlite3

conexion = sqlite3.connect('usuarios2.db')

cursor = conexion.cursor()

# Creamos un campo dni como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    dni VARCHAR(9) PRIMARY KEY,
                    nombre VARCHAR(100), 
                    edad INTEGER,
                    email VARCHAR(100))''')

usuarios = [('A01252368', 'Alejandro ', 18, 'alejandro@ejemplo.com'),
            ('A01252421', 'Paola', 18, 'paola@ejemplo.com'),
            ('A01252717', 'Saúl', 18, 'saul@ejemplo.com'),
            ('A01252708', 'Mariana', 19, 'mariana@ejemplo.com')]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

conexion.commit()
conexion.close()


# *******************Campos autoincrementales ***************

import sqlite3

conexion = sqlite3.connect('productos.db')

cursor = conexion.cursor()

# Las cláusulas not null indican que no puede ser campos vacíos
cursor.execute('''CREATE TABLE productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')

# *******************Campos autoincrementales ***************
cursor = conexion.cursor()

productos = [('Teclado', 'Logitech', 19.95),
             ('Pantalla 19"' 'LG', 89.95),]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

conexion.commit()
conexion.close()

# *******************Claves únicas ***************

import sqlite3

conexion = sqlite3.connect('usuarios3.db')

cursor = conexion.cursor()

# Creamos un campo matricula como clave primaria
cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY,
                    matricula VARCHAR(9) UNIQUE,
                    nombre VARCHAR(100), 
                    edad INTEGER(3),
                    email VARCHAR(100))''')

usuarios = [('A01252368', 'Alejandro ', 18, 'alejandro@ejemplo.com'),
            ('A01252421', 'Paola', 18, 'paola@ejemplo.com'),
            ('A01252717', 'Saúl', 18, 'saul@ejemplo.com'),
            ('A01252708', 'Mariana', 19, 'mariana@ejemplo.com')]

cursor.executemany("INSERT INTO usuarios VALUES (null, ?,?,?,?)", usuarios)

conexion.commit()


# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)
conexion.close()