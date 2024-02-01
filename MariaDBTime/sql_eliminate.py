from tkinter import *
import ttkbootstrap as tb
import time as t
import mariadb


root = tb.Window(themename="cyborg")
root.title("Ventana Principal")
root.geometry("700x480")

def eliminar_tabla():
    tabla = EtTable.get()
    try:
        cursor.execute(f"DROP TABLE {tabla}")
        conexion.commit()
    except mariadb.Error as error:
        print(f'Error al conectarse {error}')        
        root.after(3000, lambda: exit(1))

def eliminar_base():
    base = EtB.get()
    try:
        cursor.execute(f"DROP DATABASE {base}")
        conexion.commit()
    except mariadb.Error as error:
        print(f'Error al conectarse {error}')        
        root.after(3000, lambda: exit(1))

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



LB1=tb.Label(root, text=" Borrado de tablas y bases de datos ",
         font = "calibri 18", bootstyle="info")
LB1.grid(row=0,columnspan=2, pady=10, padx = 10)



LBB=tb.Label(root, text=" Nombre de Base de Datos ",
         font = "calibri 18", bootstyle="info")
LBB.grid(row=1,column=0,pady=10 , padx = 10)

EtB = tb.Entry(root, bootstyle="info")
EtB.grid(row=1,column=1, pady=10 , padx = 10)



LBTable=tb.Label(root, text=" Nombre de Tabla ",
         font = "calibri 18", bootstyle="info")
LBTable.grid(row=2,column=0,pady=10 , padx = 10)

EtTable = tb.Entry(root, bootstyle="info")
EtTable.grid(row=2,column=1, pady=10 , padx = 10)

B1 = tb.Button(root, text="Borrar DB", bootstyle="success", command=eliminar_base)
B1.grid(row=3,column=0, pady=20,padx=20)

B2 = tb.Button(root, text="Borrar Tabla", bootstyle="success", command=eliminar_tabla)
B2.grid(row=3,column=1, pady=20,padx=20)

root.mainloop()