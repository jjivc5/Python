from tkinter import *

root = Tk()
root.title("Ventana principal")
root.geometry("250x200")


def seleccion():
    etiqueta = Label(root,text=control.get()).pack()
    etiqueta1 = Label(root,text=control1.get()).pack()

control = StringVar()

opcion_1 = Checkbutton(root, text="Opción 1", variable=control,onvalue="Opc 1 On", offvalue="Opc 1 Off")
opcion_1.pack() # Esto me permite modificar el valor de la variable de control si esta
# En check o no.
# El valor onvalue y offvalue pueden ser string también.
opcion_1.deselect()




control1 = StringVar()

opcion_2 = Checkbutton(root, text="Opción 2", variable=control1,onvalue ="Opc 2 On", offvalue = "Opc 2 Off")
opcion_2.pack()
opcion_2.deselect()

muestra_seleccion = Button(root, text="Mostrar selección", command=seleccion).pack()

mainloop()