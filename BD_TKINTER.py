from tkinter import *
from tkinter import messagebox as MessageBox
import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('tinker_sqlite.db')

# Creamos el cursor
cursor = conexion.cursor()

# Configuración de la raíz
root = Tk()
root.title("Ejemplo de base de datos con Tkinter")
root.resizable(1,1)
root.iconbitmap('python.ico')
root.config(bd=30) #añadirle un borde

def insertar():
	m=tmatricula.get()
	n=tnombre.get()
	e=tedad.get()

	cursor.execute("INSERT INTO usuarios VALUES ('{}', '{}', '{}')".format(m,n,e))
	# Guardamos los cambios haciendo un commit
	conexion.commit()
	MessageBox.showinfo("¡Agregado!","Agregado a la base de datos")
	borrar()

def buscar():
	m=tmatricula.get()

	# Recuperamos un registro de la tabla de usuarios
	cursor.execute("SELECT matricula, nombre, edad FROM usuarios WHERE matricula=?",m)
	usuario = cursor.fetchone()
	#print(usuario) esta línea la use para comprobar que existia el registro
	tnombre.set(usuario[1])
	tedad.set(usuario[2])

def eliminar():
	buscar()
	m=tmatricula.get()
	resultado = MessageBox.askyesno("Salir","¿Está seguro que desea borrar?")
	if resultado:
		cursor.execute("DELETE FROM usuarios WHERE matricula=?",m)
		MessageBox.showinfo("¡Eliminado!","Registro Eliminado")
		borrar()


def borrar():
	tmatricula.set("")
	tnombre.set("")
	tedad.set("")
	


#variables para  manipular los datos
tmatricula = StringVar()
tnombre = StringVar()
tedad = StringVar()

#labels y etiquetas
Label(root, text="Matrícula").pack()
Entry(root, justify="center", textvariable=tmatricula).pack() # primer numero

Label(root, text="Nombre").pack()
Entry(root, justify="center", textvariable=tnombre).pack() # segundo numero

Label(root, text="Edad").pack()
Entry(root, justify="center", textvariable=tedad).pack() # resultado

Label(root, text="").pack() #hacer un espacio entre los entry y los botones

#botones a usar
Button(root, text="Insertar", command=insertar).pack(side="left")
Button(root, text="Buscar", command=buscar).pack(side="left")
Button(root, text="eliminar", command=eliminar).pack(side="left")


# Finalmente bucle de la aplicación
root.mainloop()

