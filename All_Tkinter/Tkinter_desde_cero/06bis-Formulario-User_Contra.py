import tkinter as tk 

root = tk.Tk()

root.configure(bg="lightgray")
def click():
    texto = tk.Label(root, text=f'Hola{Entrada_User.get()} has iniciado sesión',
                     bg = "gray",
                     font="Arial 12")
    texto.grid(row=0,column=0)
    Mensaje.grid_forget()
    root.after(2000, lambda: texto.grid_forget())

Mensaje = tk.Label(root,
                   text="Bienvenido al sistema de inicio de sesión",
                   bg = "gray",
                   font="Arial 12")

Mensaje.grid(row=0,column=0)

Boton1 = tk.Button(root,
                   text="Iniciar Sesión", 
                   bg = "gray",
                   font="Arial 12",
                   command=click)

Boton1.grid(row=3,column=0)

Entrada_User = tk.Entry(root,
                        bg = "gray",
                        font="Arial 12")
Entrada_User.grid(row=1,column=0)


Entrada_Password = tk.Entry(root,
                            bg = "gray",
                            font="Arial 12",
                            show="*")

Entrada_Password.grid(row=2,column=0)




root.mainloop()