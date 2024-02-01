from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="cyborg")

root.title("Eighth Tutorial")
root.geometry("640x650")


def  thing():
    my_label.config(text=f'Hiciste Click!')

def thing2():
    my_label2.config(text=f'Hiciste Click!')


# If you want you can also use the regular frame from tkinter.
# When you do that the frame don't gonna have a style therefore you can use it for make the frame invisibly
    
my_frame = tb.Frame(root, bootstyle="success")
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, 
                      text="CLICK ME!",
                      bootstyle = "success outline",
                      command = thing
)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Hello There", font = ("Helvetica", 18), bootstyle="success inverse")

my_label.pack(pady=20)


my_frame2 = Frame(root)
my_frame2.pack(pady=40)

my_entry2 = tb.Entry(my_frame2, font=("Helvetica", 18))
my_entry2.pack(pady=20, padx=20)

my_button2 = tb.Button(my_frame2, 
                      text="CLICK ME!",
                      bootstyle = "success outline",
                      command = thing2
)
my_button2.pack(pady=20, padx=20)

my_label2 = tb.Label(my_frame2, text="Hello There", font = ("Helvetica", 18), bootstyle="success inverse")

my_label2.pack(pady=20)


root.mainloop()