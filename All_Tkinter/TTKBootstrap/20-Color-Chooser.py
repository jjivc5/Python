from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

root = tb.Window(themename="superhero")

root.title("Mensaje de ventana")
root.geometry('800x600')

def cc():
    # Create Color Chooser
    my_color = ColorChooserDialog()
    # Show Color Chooser
    my_color.show()
    # Returns Color Chooser Info
    colors = my_color.result
    # Output to the label (.hex .hsl .rgb) # We can get the differents paramaters 
    my_label.config(text=colors.hex)
    # Change background color of the app
    root.configure(background=colors.hex)
    


my_button = tb.Button(root, text="Click Me!",
                      bootstyle="danger",
                      command=cc)
my_button.pack(pady=40)

my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)


root.mainloop()