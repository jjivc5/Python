import tkinter as tk 

root = tk.Tk()


def click_boton():
    texto = tk.Label(root, text = "No vuelvas a presionar el boton! ").grid(row=1,column=2,)


Boton1 = tk.Button(root, 
                   text = "No presiones el boton",
                   padx=10, 
                   pady=10,
                   bg="purple",
                   command=click_boton).grid(row=1,column=1,)


root.mainloop()