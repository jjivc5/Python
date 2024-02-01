from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

#root = Tk()
root.title("First tutorial")

root.geometry("640x480")

counter = 0

def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text=f'Holis el número es par : {counter}')
    else:
        my_label.config(text=f'Holis el número es impar : {counter}')

# Colors

# Default, primary, secondary, success, info, warning, danger,

# light, dark

# Label 

my_label = tb.Label(text="Hello Mundo", font =("Arial",28), bootstyle = "primary, inverse") 
# Puedo usar las constantes así porque las importamos onda bootstyle = DANGER.

my_label.pack(pady=20)
# Si agregamos el color, inverse. genera un efecto de subrayado.

my_button = tb.Button(text="Click me!", bootstyle = "success, outline", command=changer)

# Al agregar el estilo outline conseguimos el efecto de que se sombree cuando acercamos el mouse.

# también existe el estilo link, que lo vuelve como un link (literal)
my_button.pack(pady=50)


root.mainloop()