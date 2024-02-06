from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename="cyborg")

root.title("Twelvth Tutorial")
root.geometry("640x600")

# Incremental Function
def increment():
    #my_progress.step(20)
    my_progress['value'] += 15 # Con este método la barra llega a 100 y no arranca de 0.
    my_label.config(text=my_progress['value'])
# Start function
    
def start():
    my_progress.start(10)

def stop():
    my_progress.stop()

def auto():
    for x in range(5):
        my_progress['value'] += 20
        my_label.config(text=my_progress["value"])
        root.update_idletasks() # Update one at a time not all at once porque si no aparece al final del for.
        time.sleep(1) # Gonna give a 1 second delay
# Progress Bar
my_progress = tb.Progressbar(root,
                             bootstyle="danger striped",
                             maximum=100,
                             mode="determinate", # Goes up and down. When mode is indeterminate
                             length=200,
                             value=20,
                            )

my_progress.pack(pady=40)

# Frame

my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Buttons

my_button = tb.Button(my_frame, text="Increment 20",
                      bootstyle="info",
                      command=increment)

my_button.grid(column=0, row=0, padx=10)

my_button1 = tb.Button(my_frame, text="Start",
                      bootstyle="info",
                      command=start)

my_button1.grid(column=1, row=0, padx=10)

my_button2 = tb.Button(my_frame, text="Stop",
                      bootstyle="info",
                      command=stop)

my_button2.grid(column=2, row=0, padx=10)

my_button3 = tb.Button(my_frame, text="Auto",
                      bootstyle="info",
                      command=auto)

my_button3.grid(column=3, row=0, padx=10)


# Create Label 

my_label = tb.Label(root,
                    text="",
                    )

my_label.pack(pady=20)


root.mainloop()