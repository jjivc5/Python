import tkinter as tk

root = tk.Tk()

root.title("Moment Frames")

buscador = tk.LabelFrame(root, text = "Buscador", padx=30, pady=30)

buscador.grid(row=0,column=0, padx=50, pady=50)

barra = tk.Entry(buscador, text = "¿ Buscas algo ?").grid(row=0,column=0)

boton = tk.Button(buscador, text=" buscar").grid(row=0,column=1)

buscador1 = tk.LabelFrame(root, text = "Buscador", padx=30, pady=30)

buscador1.grid(row=1,column=0, padx=50, pady=50)

barra1 = tk.Entry(buscador1, text = "¿ Buscas algo ?").grid(row=0,column=0)

boton1 = tk.Button(buscador1, text=" buscar").grid(row=0,column=1)



root.mainloop()