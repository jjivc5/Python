from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox


root = tb.Window(themename="cyborg")

root.title("Seventh Tutorial")
root.geometry("640x480")

def datef():
    my_label.config(text=f'You picked: {my_date.entry.get()}')

def thing():
    cal = Querybox()
    my_label.config(text=f'You picked: {cal.get_date()}')

my_date = tb.DateEntry(root,
                        bootstyle = "danger",
                        startdate=date(2023,2,14), # the start date is adate object
                        firstweekday=0) # You can assign the day of start. Monday belongs to '0' position
my_date.pack(pady=50)

my_button = tb.Button(root, text = 'Get Date',
                      bootstyle="danger outline",
                      command=datef)
my_button.pack(pady=20)


my_button2 = tb.Button(root, text = 'Get Calendar',
                      bootstyle="succes outline",
                      command=thing)
my_button2.pack(pady=20)

my_label = tb.Label(root, text="You Picked: ")
my_label.pack(pady=20)

root.mainloop()