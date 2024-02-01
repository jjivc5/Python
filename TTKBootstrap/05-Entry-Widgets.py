from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

root.title("Fifth Tutorial")
root.geometry("640x480")

def speak():
    my_label.config(text=f'You Typed: {my_entry.get()}')


# La entry
my_entry = tb.Entry(root, bootstyle="success",
                     font=("Helvetica", 18),
                     foreground="green",
                     width=10,
                     show = "*") # El width son el número de carácteres acá.
my_entry.pack(pady=50)

# El botón
my_button = tb.Button(root, bootstyle = "danger outline", 
                      text="Click Me",
                      command=speak)
my_button.pack(pady=20)

# La Label
my_label = tb.Label(root, text ="")
my_label.pack(pady=20)


root.mainloop()