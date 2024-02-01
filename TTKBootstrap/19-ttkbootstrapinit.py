from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox


main_window = tb.Window(themename="superhero")

main_window.title("Mensaje de ventana")
main_window.geometry('800x600')

def clicker():
    # create a dialog
    # yesno, te da yes o no
    # después tenes la opción "ok" que devuelve NONE
    # también tenes la opcion okcancel que devuelve 2 estados ok o cancel
    # Messagebox.yesno,ok,okcancel,show_info,show_error, show_question
    # show_warning,yesnocancel, retrycancel
    # Todo esto cambia la lógica del pop up y también a veces las posibilidades de lógica
    # Si o no, dar OK, dar Ok o Cancel.

    # Más información hay en MessageBox ttkbootstrap.

    mb = Messagebox.yesno("Mensaje de muestra", "Titulo de la ventana")

    #Hacer la magia
    #mb puede devolver dos estados yes or no, entonces podes hacer lógica.
    my_etik.config(text=f'La etiqueta devolvió:  {mb}')

El_boton = tb.Button(main_window,
                     text="Clickear!",
                     bootstyle='danger',
                     command=clicker)

El_boton.pack(pady=40)

my_etik = tb.Label(main_window,
                   text='',
                   font=("Helvetica",18)
                   )

my_etik.pack(pady=20)

main_window.mainloop()