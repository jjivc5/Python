from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Fifteenth Tutorial")
root.geometry("640x600")


# Frame

my_frame = tb.Frame(root)

my_frame.pack(pady=20)

# Create a Scrollbar

my_scroll = tb.Scrollbar(my_frame,
                         orient='vertical',
                         bootstyle='info')

my_scroll.pack(side=RIGHT, fill=Y)

# Create a Text Widget

my_text = Text(my_frame, width=30, height=25,
               yscrollcommand=my_scroll.set, wrap="none",
               font=(("helvetica"),18))

my_text.pack()

my_scroll.config(command=my_text.yview)





root.mainloop()