from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.dialogs import FontDialog

root = tb.Window(themename="cyborg")

root.title("Mensaje de ventana")
root.geometry('200x200')

def open_font():
    # Define the font
    fd = FontDialog()
    # Show the box
    fd.show()
    # Capture the result fd.result amd update
    my_label.config(font=fd.result)


# Create a labe and button

my_button = tb.Button(root, text = "Open Font Dialog",
                      command=open_font)


my_button.pack(pady=40)


my_label = tb.Label(root, text="Hello World")
my_label.pack(pady=20)

root.mainloop()