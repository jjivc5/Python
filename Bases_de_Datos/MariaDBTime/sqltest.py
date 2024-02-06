from tkinter import *
import ttkbootstrap as tb
import time as t
import mariadb


root = tb.Window(themename="cyborg")
root.title("Ventana Principal")
root.geometry("450x350")

try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port = 3306,
        database="test"
    )
    cursor = conexion.cursor()

    eti=tb.Label(root, text= "La conexión a la base de datos fue correcta; base:" + conexion.database +" ."
                 , wraplength=200,
                 bootstyle="success")
except mariadb.Error as error:
    eti=tb.Label(root, text=f'Error al conectarse {error}',
                 bootstyle="warning")
    root.after(3000, lambda: exit(1))
    


    
def crea_tabla():
    try:
        cursor.execute("CREATE TABLE clientes (id INT NOT NULL AUTO_INCREMENT,"
                        "nombre VARCHAR(32) NOT NULL,"
                        "apellidos VARCHAR(64) NOT NULL," 
                        "telefono VARCHAR(9) NOT NULL, direccion VARCHAR(256), PRIMARY KEY (id))")
        conexion.commit()
        eti.config(text="Tabla Creada")
    except mariadb.Error as error:
        print(f'El error fue: {error}')


eti.pack(padx=10,pady=10,expand=True,fill=X)

boton = tb.Button(root, text="Realizar Tabla", width=20, command=crea_tabla)
boton.pack(pady=20)

root.mainloop()