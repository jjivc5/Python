import tkinter as tk

root = tk.Tk()

x = tk.IntVar()

x.set(value=1)

def actualiza(value):
    opcion_set= tk.Label(root, text=value)
    opcion_set.grid(row=3)

titulo =tk.Label(root, 
                 text = "Ingrese la respuesta")

titulo.grid(row=0)

opc_1 = tk.Radiobutton(root,
                       text="Primera opción",
                       value = 1,
                       variable = x,
                       command=lambda: actualiza(x.get()))

opc_1.grid(row=1)

opc_2 = tk.Radiobutton(root,
                       text="Segunda opción",
                       value = 2,
                       variable = x,
                       command=lambda: actualiza(x.get()))

opc_2.grid(row=2)

root.mainloop()