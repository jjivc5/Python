import tkinter as tk

from tkinter import font

import tkinter.messagebox as tkmsg

from Constants import style

# Inminente declaración y configuración de la interfaz principal
root = tk.Tk()
root.title("Calculadora básica")
root.iconbitmap("./media/bgs.ico")
root.resizable(0,0)
root.geometry("450x600")
root.configure(bg="black",padx=30,pady=20)


# Clase calculadora
class Calculadora():
    def __init__(self):
        self.screen = None
        self.num1 = None
        self.num2 = None
        self.operador = None

    def envia_boton(self, valor):
        anterior = self.screen.get()
        self.screen.delete(0, tk.END)
        self.screen.insert(0, str(anterior) + str(valor))
       
    
    def create_screen(self, belong):
        self.screen = tk.Entry(belong,**style.SCREEN_STYLE)
        self.screen.grid(row=0,padx=10,pady=10,columnspan=4)

   
    def create_botton(self, row_pos, col_pos, char, belong):
        normal_button=tk.Button(belong,
        text = char,
        **style.BUTTON_STYLE,
        command = lambda : (self.envia_boton(char))
        )
        normal_button.grid(row=row_pos,column=col_pos, **style.PAD_BUTTON)
    
    
    def create_botton_special(self, row_pos, col_pos, char, belong, order):
        special_button = tk.Button(belong,
        text = char,
        **style.SP_BUT_STYLE,
        command = order)

        special_button.grid(row=row_pos,column=col_pos, **style.PAD_BUTTON)
    
    
    def create_botton_clear(self, row_pos, col_pos, char, belong):
        clear_button = tk.Button(belong,
                                 text=char,
                                 **style.SP_BUT_STYLE,
                                 command=lambda : (self.screen.delete(0,tk.END)))
        clear_button.grid(row=row_pos, column=col_pos, **style.CLEAR_STYLE)
    
    def suma(self):
        self.num1 = self.screen.get()
        self.num1 = float(self.num1)
        self.screen.delete(0, tk.END)
        self.operador = "+"
   
    def rest(self):
        self.num1 = self.screen.get()
        self.num1 = float(self.num1)
        self.screen.delete(0, tk.END)
        self.operador = "-"
    
    def mult(self):
        self.num1 = self.screen.get()
        self.num1 = float(self.num1)
        self.screen.delete(0, tk.END)
        self.operador = "*"
    
    def div(self):
        self.num1 = self.screen.get()
        self.num1 = float(self.num1)
        self.screen.delete(0, tk.END)
        self.operador = "/"
    
    def eq(self):
        try:
            self.num2 = self.screen.get()
            self.num2 = float(self.num2)
            self.screen.delete(0,tk.END)
            
            if self.operador == "+":
                resultado = self.num1+self.num2
            elif self.operador == "-":
                resultado = self.num1-self.num2
            elif self.operador == "*":
                resultado = self.num1*self.num2
            elif self.operador == "/":
                if self.num2==0:
                    tkmsg.showerror(title="Operación No realizada", message="No se puede dividir por cero")
                    resultado = "Inf"
                else:
                    resultado = self.num1/self.num2
            
            self.screen.insert(0, str(resultado))
        except:
            tkmsg.showerror(title="Operación No realizada", message="No se ha realizado ninguna operación valida")
        

# Creación de la instancia de la calculadora
calc = Calculadora()
# Creación de la pantalla
calc.create_screen(root)
# Diccionario de Botones Comunes
but_dict = {
    "Boton 1" : {"row" : "1", "col" : "0", "char" : "1"},
    "Boton 2" : {"row" : "1", "col" : "1", "char" : "2"},
    "Boton 3" : {"row" : "1", "col" : "2", "char" : "3"},
    "Boton 4" : {"row" : "2", "col" : "0", "char" : "4"},
    "Boton 5" : {"row" : "2", "col" : "1", "char" : "5"},
    "Boton 6" : {"row" : "2", "col" : "2", "char" : "6"},
    "Boton 7" : {"row" : "3", "col" : "0", "char" : "7"},
    "Boton 8" : {"row" : "3", "col" : "1", "char" : "8"},
    "Boton 9" : {"row" : "3", "col" : "2", "char" : "9"},
    "Boton 0" : {"row" : "4", "col" : "0", "char" : "0"},
    "Boton point" : {"row" : "4", "col" : "1", "char" : "."},    
}

sp_dict = {
    "Boton sum" : {"row" : "1", "col" : "3", "char" : "+", "command" : calc.suma},
    "Boton rest" : {"row" : "2", "col" : "3", "char" : "-", "command" : calc.rest},
    "Boton mult" : {"row" : "3", "col" : "3", "char" : "*", "command" : calc.mult},
    "Boton div" : {"row" : "4", "col" : "3", "char" : "/", "command" : calc.div},
    "Boton equal" : {"row" : "4", "col" : "2", "char" : "=", "command" : calc.eq},
}
# Definición de botones comunes
for button_index, but_dict in but_dict.items():
    calc.create_botton(but_dict["row"], but_dict["col"], but_dict["char"], root)

# Definición 
for button_index, sp_dict in sp_dict.items():
    calc.create_botton_special(sp_dict["row"], sp_dict["col"], sp_dict["char"], root, sp_dict["command"] )

# Definir botón de borrado.

calc.create_botton_clear(5,0,"CLC",root)

# Definición de pantalla


root.mainloop()