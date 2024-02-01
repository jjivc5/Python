import tkinter as tk 

root = tk.Tk()

class Marco:
    def __init__(self, back, x, y, master = None):  
        self.x = x
        self.y = y
        self.back = back

    def create_marco(self, master):
        Marko = tk.Frame()
        Marko.configure(width=100,height=100, background=self.back)
        Marko.grid(row=self.x,column=self.y)


marcos_info = {
    "Marco1": {"color": "red", "x": 0, "y": 0},
    "Marco2": {"color": "blue", "x": 1, "y": 0},
    "Marco3": {"color": "yellow", "x": 2, "y": 0},
    "Marco4": {"color": "green", "x": 0, "y": 1},
    "Marco5": {"color": "black", "x": 1, "y": 1},
    "Marco6": {"color": "orange", "x": 2, "y": 1},
}

marcos = {}

for marco_name, marco_info in marcos_info.items():
    marcos[marco_name] = Marco(marco_info["color"], marco_info["x"], marco_info["y"])
    marcos[marco_name].create_marco(root)

# LAS GRID EN TKINTER POR EJEMPLO AL AVANZAR Y SALTAR COLUMNAS O ROWS
# SE PONEN EN LA MAS CERCANA Y NO SE SALTEAN. 
#Por ejemplo si pongo un marco en la columna 10 se va hacer en la 4.
    
MarcoRelativo = tk.Frame(root)
MarcoRelativo.grid(row=0,column=2) # Notar como aparece en la cuarta y no deja espacios vacios
MarcoRelativo.config(bg="purple", width=100, height=100)

Boton1 = tk.Button(root, 
                   text = "No presiones el boton",
                   padx=10, 
                   pady=10, 
                   state="disabled").grid(row=1,column=2,)



root.mainloop()