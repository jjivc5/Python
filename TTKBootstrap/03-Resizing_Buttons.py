from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

root.title("Third Tutorial")
root.geometry("640x480")

# Style
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))
# para escribir el estilo correctamente primero hay que escribir el bootstyle.NombreDeEstilo
# Para agregar otro estilo hay que agregar hay que seguir escribiendo bootstyle.parametro1.parametro2


my_button = tb.Button(text="Hello World!",
                      #bootstyle="success", # y este estilo no hace falta ponerlo. Evidentemente.
                      style = "success.Outline.TButton"
                      )

# No existe ni font, ni height como párametros en tb.


my_button.pack(pady=40)


root.mainloop()