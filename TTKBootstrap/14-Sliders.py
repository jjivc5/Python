from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Fourtieth Tutorial")
root.geometry("640x600")

def scaler(e):
    my_label.config(text=f'{int(my_scale.get())}')
    if int(my_scale.get()) < 50:
        my_label2.config(text="Menos de la mitad")
    else:
        my_label2.config(text="Más de la mitad")

# Create a Scale/Slider

my_scale = tb.Scale(root, bootstyle ="warning",
                    length=200, # This is the graphical lenght no the maximum number
                    orient = "vertical",
                    from_ = 0, # Minimum Value
                    to=100, # Maximum Value
                    command=scaler,
                    state="normal") # States are disabled an normal
my_scale.pack(pady=50)

# Create a label

my_label = tb.Label(root,text="",
                    font=("Helvetica",18))
my_label.pack()

my_label2 = tb.Label(root,text="",
                    font=("Helvetica",18))
my_label2.pack()

root.mainloop()