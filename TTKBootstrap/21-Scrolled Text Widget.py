from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

root = tb.Window(themename="cyborg")

root.title("Mensaje de ventana")
root.geometry('800x600')

# Text Widget

my_text = ScrolledText(root, height=20, width=110, wrap=WORD,
                       autohide=False, bootstyle="info",
                       hbar = True) # Wrap allow's to don't cut words in the middle.
                        # We can see more on the documentation
my_text.pack(pady=15)

root.mainloop()