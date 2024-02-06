from PIL import Image
Image.CUBIC = Image.BICUBIC
from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Tenth Tutorial")
root.geometry("640x600")


global counter
counter = 0

def up():
    global counter
    if counter<=100:
        my_meter.step(5)
    
def down():
    global counter
    if counter>=0:
        my_meter.step(-5)

def clicker():
    global counter
    if counter <= 100:
        my_meter.configure(amountused=counter)
        counter += 10
        my_button.config(text=f'Click Me {my_meter.amountusedvar.get()}')

my_meter = tb.Meter(root, 
                    bootstyle="danger",
                    subtext="Tkinter Learned",
                    interactive=True,
                    textright="%",
                    #textleft="$"
                    metertype="full", # Can be semi, and you have the half
                    stripethickness=10, # This add sub divisions on the percentage
                    metersize=200, # This change the size of the meter
                    padding=50, #Can also add padding
                    amountused=20, #Default start
                    amounttotal=100, #This define the maximum value
                    subtextstyle="success", # You can change the textstyle

                    ) 

my_meter.pack(pady=20)

my_button = tb.Button(root, text="Click Me 5",
                      command=clicker)

my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Click Up",
                      command=up)

my_button2.pack(pady=20)


my_button3 = tb.Button(root, text="Click Down",
                      command=down)

my_button3.pack(pady=20)

root.mainloop()