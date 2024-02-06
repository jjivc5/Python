import tkinter as tk
from Constantes import style
from Screens import Home, Game

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(" Yo nunca : Juegardium")
        self.mode = "Normal"
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1) # Weight es una especie de multiplicador respecto de otros elementos
        container.grid_rowconfigure(0, weight = 1)

        self.frames = {}
        for F in (Home, Game ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky= tk.NSEW)  # Diccionario de Clases :@
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()