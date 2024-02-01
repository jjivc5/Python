import tkinter as tk 

root = tk.Tk()

entrada = tk.Entry(root, 
                   width=50, 
                   bg="mediumpurple4", 
                   borderwidth=5,
                   fg="skyblue",
                   font="Arial 14",
                   #show="*"
                   )

entrada.insert(0,"Gilada")

entrada.grid(row=2,column=0)

def click_boton():
    texto = tk.Label(root, text = f'Se almaceno {entrada.get()} ', font = "Arial 14").grid(row=1,column=0,)


Boton1 = tk.Button(root, 
                   text = "Enviar",
                   padx=10, 
                   pady=10,
                   height=1,
                   width=5,
                   bg="mediumpurple",
                   borderwidth=5,
                   fg="skyblue",
                   font="Arial 14",
                   command=click_boton).grid(row=0,column=0,)


root.mainloop()