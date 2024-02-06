import tkinter as tk
root = tk.Tk()

x = tk.IntVar()
x.set(value=1)

def actualiza(value):
    opcion_set = tk.Label(root, text=value).grid(row=3)


titulo = tk.Label(root, text="Seleccione la respuesta correcta").grid(row=0)

opcion_1 = tk.Radiobutton(root, text="Primer opción", value=1, variable=x).grid(row=1)

opcion_2 = tk.Radiobutton(root, text= "Segunda opción", value=2, variable=x).grid(row=2)


boton_envia = tk.Button(root, text="Enviar", command=lambda : actualiza(x.get())).grid(row=4)

root.mainloop()

