import tkinter as tk

from Constantes import style,config

class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value="Normal")

        self.init_widgets()

    def move_to_game(self):
        self.controller.mode = self.gameMode.get()
        self.controller.show_frame(Game)

    def init_widgets(self):
        tk.Label(
            self,
            text = "Yo nunca: THE GAME",
            justify = tk.CENTER,
            **style.STYLE # Aca tengo un diccionar desempaquetado con varios argumentos, probar después
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11
            )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background= style.BACKGROUND)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx=22,
            pady=11
        )

        tk.Label(
            optionsFrame,
            text = "Elegir el modo de juego",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )

        for (key, values) in config.MODES.items():
            tk.Radiobutton(
                optionsFrame,
                text = key + (" C: " if key == "ATREVIDO" else ""),
                variable = self.gameMode,
                value = values,
                activebackground = style.BACKGROUND,
                activeforeground = style.TEXT,
                **style.STYLE
            ).pack(
                side = tk.LEFT,
                fill = tk.BOTH,
                expand = True,
                padx = 5,
                pady = 5
            )

        tk.Button(
            self,
            text = "Comenzar",
            command = self.move_to_game,
            **style.STYLE,
            relief = tk.FLAT,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,

        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )



class Game(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.currentQuestion = tk.StringVar(self, value = "Preparados, Listos, Dale Mi Rey")
        self.fichero = None
        self.init_widgets()

    def update_question(self):
        self.mode = self.controller.mode
        if (self.fichero == None) or (self.controller.mode.lower() not in self.fichero.name.lower()):
            self.fichero = open(f'./ficheros/{self.mode}.txt'
, 'r', encoding="utf-8")
        tmp = self.fichero.readline()

        if tmp != "":
            self.currentQuestion.set(tmp)
        else:
            self.currentQuestion.set("Ya hemos leído todas las preguntas, volvemos a empezar")
            self.fichero.close()
            self.fichero = open(f'.ficheros/{self.mode}.txt', 'r', encoding="utf-8")


    def init_widgets(self):
        tk.Label(
            self,
            text = "Yo nunca ....",
            justify = tk.CENTER,
            **style.STYLE # Aca tengo un diccionar desempaquetado con varios argumentos, probar después
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11
            )
       

        tk.Label(
            self,
            text = "",
            textvar = self.currentQuestion,
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )

      

        tk.Button(
            self,
            text = "Siguiente Pregunta --> ",
            command = self.update_question,
            **style.STYLE,
            relief = tk.FLAT,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,

        ).pack(
            side = tk.TOP,
            fill = tk.X,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Button(
            self,
            text = "Volver a pantalla inicial",
            command = lambda: self.controller.show_frame(Home),
            **style.STYLE,
            relief = tk.FLAT,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,

        ).pack(
            side = tk.TOP,
            fill = tk.X,
            expand = True,
            padx = 22,
            pady = 11
        )