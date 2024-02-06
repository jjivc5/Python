from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

root.title("Second Tutorial")
root.geometry("640x480")

def checker():
    if var1.get() == 1:
        my_label.config(text="Checked")
    else:
        my_label.config(text="Unchecked")

# Label First
my_label = tb.Label(text = "Click the button",
                    font = ("Helvetica",18))

my_label.pack(pady=(40,10))

# Check Button
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", 
                          text="Check Me Out!",
                          variable=var1,
                          onvalue=1,
                          offvalue=0,
                          command=checker)
my_check.pack(pady=10)

# Toolbutton

var2 = IntVar()
my_check2 = tb.Checkbutton(text="the button checker",bootstyle = "danger, toolbutton",
                           variable=var2,
                           onvalue=1,
                           offvalue=0,
                           command=checker)

my_check2.pack(pady=10)


# Outlines toolbutton

var3 = IntVar()
my_check3 = tb.Checkbutton(text="the button outliner",bootstyle = "danger, toolbutton, outline",
                           variable=var3,
                           onvalue=1,
                           offvalue=0,
                           command=checker)

my_check3.pack(pady=10)

# Round toggle butto

var4 = IntVar()
my_check4 = tb.Checkbutton(text="Text Round Toggle",bootstyle = "success, round-toggle",
                           variable=var4,
                           onvalue=1,
                           offvalue=0,
                           command=checker)

my_check4.pack(pady=10)

# Square Toggle Button
var5 = IntVar()

my_check5 = tb.Checkbutton(bootstyle="warning , square-toggle",
                           text="Square Toggle!!",
                           variable=var5,
                           onvalue=1,
                           offvalue=0,
                           command=checker)

my_check5.pack(pady=10)

root.mainloop()