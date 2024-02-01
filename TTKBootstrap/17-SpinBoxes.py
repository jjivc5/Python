from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Sixteenth Tutorial")
root.geometry("640x600")


def buttonfun():
    my_label.config(text=my_spin.get())

# Spinbox
stuff = ['John', 'Joseph', 'Mary']
my_spin = tb.Spinbox(root, bootstyle="info",
                     font=("Arial",18),
                     from_=0,
                     to=10,
                     values = stuff,
                     state="readonly",
                     command=buttonfun)
my_spin.pack(pady=20)

# Set spinbox default
my_spin.set("John")

my_label = tb.Label(root,
                    text="Textito",
                    font=("Arial",18),
                    bootstyle="success")
my_label.pack(pady=20)


my_button = tb.Button(root,
                      text="Tocar",
                      bootstyle="success",
                      command=buttonfun)

my_button.pack(pady=20)

root.mainloop()