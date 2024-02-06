from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

root.title("Sixth Tutorial")
root.geometry("640x480")

def starter():
    my_gauge.start()

def stopper():
    my_gauge.stop()

def incrementer():
    my_gauge.step(10) 
    my_label.config(text=f"Position: {my_gauge.variable.get()}") # Este valor es un número. 
    # Para tener en cuenta las posibilidades que se consiguen.


my_gauge = tb.Floodgauge(root, bootstyle="success",
                         font=("Helvetica",18),
                         mask="Pos: {}%",
                         maximum=80,
                         #orient="horizontal"
                         value=0,
                         mode = "determinate"
                         )

my_gauge.pack(pady=55, fill=X, padx=50)


start_button = tb.Button(root, text="Start",
                         bootstyle="danger outline",
                         command=starter)
start_button.pack(pady=20,padx=10)

stop_button = tb.Button(root, text="Stop",
                         bootstyle="danger outline",
                         command=stopper)
stop_button.pack(pady=20,padx=10)

inc_button = tb.Button(root, text="Increment",
                         bootstyle="danger outline",
                         command=incrementer)
inc_button.pack(pady=20,padx=10)


my_label = tb.Label(root, text="Position: ")

my_label.pack(pady=20,padx=10)

root.mainloop()