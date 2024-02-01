from tkinter import *

root = Tk()

root.title("Ventana Principal")

root.geometry("300x300")

def envia_boton():
    ventana_nueva = Toplevel() # Top Level sirve para crear ventanas nuevas
    ventana_nueva.title("Ventana secundaria")
    ventana_nueva.geometry("400x300")
    valor_entrada = entrada.get()
    etiqueta = Label(ventana_nueva, padx=5, pady=5,
                      text = "El valor introducido en la ventana principal es: " + valor_entrada).grid(row=0)
    cerrar_ventana = Button(root, text="Cerrar la ventana", command = ventana_nueva.destroy).grid(row=2)

entrada = Entry(root, width=20)
entrada.grid(row=0)

envia = Button(root,text="enviar",command=envia_boton).grid(row=1)

cerrar_root = Button(root, text="Cerrar ventana principal", command = root.destroy).grid(row=3)

mainloop()