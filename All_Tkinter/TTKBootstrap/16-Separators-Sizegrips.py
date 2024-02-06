from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Sixteenth Tutorial")
root.geometry("640x600")

label1 = tb.Label(root,
                  text="Label 1",
                  bootstyle="info")

label1.pack(pady=40)

my_sep = tb.Separator(root,
                      bootstyle="light",
                      orient="horizontal"
                      )

my_sep.pack(fill=X,padx=20)

# Separator

label2 = tb.Label(root,
                  text="Label 2",
                  bootstyle="info")

label2.pack(pady=40)

# Sizegrip

my_sizegrip = tb.Sizegrip(root,
                          bootstyle="info")

my_sizegrip.pack(anchor=SE, fill=BOTH, expand=True)


from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Sixteenth Tutorial")
root.geometry("640x600")