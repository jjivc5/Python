from tkinter import *
import ttkbootstrap as tb
import time as t
import mariadb


root = tb.Window(themename="cyborg")
root.title("Ventana Principal")
root.geometry("400x480")

def registrar():
    nombre = EtName.get()
    apellido = EtSurN.get()
    tel = EtTel.get()
    dir = EtDir.get()
    try:
        cursor.execute("INSERT INTO clientes"
                       "(nombre, apellidos, telefono, direccion) VALUES (?,?,?,?)",(nombre,apellido,tel,dir))
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


# Funciones
    

# Interfaz gráfica
    
LB1=tb.Label(root, text=" Registro para nuevos clientes ",
         font = "calibri 18", bootstyle="info")
LB1.grid(row=0,columnspan=2, pady=10, padx = 10)



LBName=tb.Label(root, text=" Nombre ",
         font = "calibri 18", bootstyle="info")
LBName.grid(row=1,column=0,pady=10 , padx = 10)

EtName = tb.Entry(root, bootstyle="info")
EtName.grid(row=1,column=1, pady=10 , padx = 10)



LBSurN=tb.Label(root, text=" Apellidos ",
         font = "calibri 18", bootstyle="info")
LBSurN.grid(row=2,column=0,pady=10 , padx = 10)

EtSurN = tb.Entry(root, bootstyle="info")
EtSurN.grid(row=2,column=1, pady=10 , padx = 10)



LBTel=tb.Label(root, text=" Teléfono ",
         font = "calibri 18", bootstyle="info")
LBTel.grid(row=3,column=0,pady=10 , padx = 10)

EtTel = tb.Entry(root, bootstyle="info")
EtTel.grid(row=3,column=1, pady=10 , padx = 10)



LBDir=tb.Label(root, text=" Dirección ",
         font = "calibri 18", bootstyle="info")
LBDir.grid(row=4,column=0,pady=10 , padx = 10)

EtDir = tb.Entry(root, bootstyle="info")
EtDir.grid(row=4,column=1, pady=10 , padx = 10)


Butt_Send = tb.Button(root, text="Agregar Campos",
                      command=registrar, bootstyle="success")

Butt_Send.grid(row=5,column=0, pady=20 , padx = 10, columnspan=2)

root.mainloop()