import tkinter as tk 

root = tk.Tk()
init_row = 0
def actualiza(value):
    opcion_set = tk.Label(root, text = value).grid(row=i+2)

Title = tk.Label(root,text="Seleccionar una opción: ").grid(row=init_row)

opciones = [["Color rojo", "rojo"],["Color azul", "azul"], ["Color amarillo", "amarillo"],
            ["Color verde", "verde"]]

colores = tk.StringVar()

colores.set("rojo")

i = init_row + 1

for opcion, valor in opciones:
    tk.Radiobutton(root, text=opcion, value=valor, variable = colores).grid(row=i)
    i += 1


boton_enviar = tk.Button(root, text="Enviar", command=lambda : actualiza(colores.get())).grid(row=i+1)

root.mainloop()