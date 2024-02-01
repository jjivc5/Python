from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification


root = tb.Window(themename="cyborg")

root.title("Mensaje de ventana")
root.geometry('800x600')
def clicker():
    toast.show_toast()

toast = ToastNotification(title="My Toast Title",
                          message="This is a Toast Mesage!! WOOHOO!!",
                          duration=3000, # Without time doesn't disappear if you don't click
                          alert=True,
                          position=(20,50,'sw')
                          )



my_button = tb.Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=40)
root.mainloop()