from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Ninth Tutorial")
root.geometry("640x650")

# Create function

def stuff(i):
    my_menu.config(bootstyle=i)
    my_label.config(text=f'You have been selected {i}')


my_menu = tb.Menubutton(root,
                        bootstyle="warning",
                        text="Button Menu")

my_menu.pack(pady=20,padx=20)

# Create basic menu

inside_menu = tb.Menu(my_menu)

# Add Items To Our Inside Menu

item_var = StringVar()

for i in ['primary',
          'secondary','danger',
          'info','outline primary', 
          'outline secondary', 'outline danger', 'outline warning']:
    inside_menu.add_radiobutton(label=i, variable=item_var, 
                                command=lambda i=i: stuff(i))

# Associate the inside menu with the menubutton

my_menu['menu'] = inside_menu

my_label = tb.Label(root,
                    text="Here is where the text go",
                    font=("Helvetica",18))

my_label.pack(pady=20)

root.mainloop()