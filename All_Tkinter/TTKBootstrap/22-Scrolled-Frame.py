from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="cyborg")

root.title("Mensaje de ventana")
root.geometry('800x600')


# Scrolled frame

my_frame = ScrolledFrame(root, autohide=False)
my_frame.pack(pady=15, padx=15, fill=BOTH, expand=YES)

# Create some buttons

for x in range(21):
    tb.Button(my_frame, bootstyle="info", text=f'Click Me! {x}').pack(pady=10)


root.mainloop()