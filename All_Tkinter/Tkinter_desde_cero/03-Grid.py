import tkinter as tk

root = tk.Tk()


# marco.pack()
# texto.pack()
# El orden del método pack, también es el orden en que aparecen las etiquetas
# Esto lo sabía intuitivamente.

# Marcos
marco = tk.Frame()
marco.configure(width=100,height=100,bg="white")
marco.grid(row=0, column=0)

marco1 = tk.Frame()
marco1.configure(width=100,height=100,bg="black")
marco1.grid(row=0, column=1)

marco2 = tk.Frame()
marco2.configure(width=100,height=100,bg="white")
marco2.grid(row=1, column=1)

marco3 = tk.Frame()
marco3.configure(width=100,height=100,bg="black")
marco3.grid(row=1, column=0)

marco4 = tk.Frame()
marco4.configure(width=100,height=100,bg="white")
marco4.grid(row=0, column=2)

marco5 = tk.Frame()
marco5.configure(width=100,height=100,bg="black")
marco5.grid(row=1, column=2)

class Marco:
    def __init__(self, x, y, master = None):  
        self.x = x
        self.y = y

    def create_marco(self, back, master):
        Marko = tk.Frame()
        Marko.configure(width=100,height=100, background=back)
        Marko.grid(row=self.x,column=self.y)
    
    def create_marco_black(self, master):
        Marko = tk.Frame()
        Marko.configure(width=100,height=100, background="black")
        Marko.grid(row=self.x,column=self.y)
    
    def create_marco_white(self, master):
        Marko = tk.Frame()
        Marko.configure(width=100,height=100, background="white")
        Marko.grid(row=self.x,column=self.y)


marco6 = Marco(3,3,master=root)
marco7 = Marco(3,4,master=root)

marco6.create_marco("black",root)
marco7.create_marco_black(root)





root.mainloop()