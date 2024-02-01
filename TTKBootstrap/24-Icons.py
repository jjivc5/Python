from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon

root = tb.Window(themename="cyborg")

root.title("Mensaje de ventana")
root.geometry('200x200')

# Icons : warning

iconyto = PhotoImage(data=Icon.warning)  # You also can change this with your own image.

# You can have : warning, icon, error, question, info

# Label to attach

my_label = tb.Label(image=iconyto)

my_label.pack(pady=20)

root.mainloop()