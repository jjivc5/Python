from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

root.title("Fourth Tutorial")
root.geometry("640x480")


# Function button

def clicker():
    my_label.config(text=f'You Clicked On {my_combo.get()} !')

# Function binding selection list

def click_bind(e): # Hay que pasar un evento que viene con información extra
    # Aunque no se use esta información hay que pasarla para evitar problemas
    my_label.config(text=f'You Clicked On {my_combo.get()} !')


my_label = tb.Label(root, text="Hello World", font = ("Helvetica", 18))
my_label.pack(pady=30)

# Create Dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)


# Set Combo Default

my_combo.current(0)


# Button Controller

my_button = tb.Button(root, text="Click me",
                      command=clicker,
                      bootstyle="danger")

my_button.pack(pady=10)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)
root.mainloop()