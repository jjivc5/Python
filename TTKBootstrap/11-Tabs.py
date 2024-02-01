from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="cyborg")

root.title("Elevent Tutorial")
root.geometry("640x600")


my_notebook = tb.Notebook(root, bootstyle="dark") # Dark is the best style for tabs highlighting
# the another ones can be a pretty bit confusing.
my_notebook.pack(pady=20)

tab = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_label = Label(tab, text="A label awesome", font = ("Helvetica", 18))
my_label.pack(pady=20)


my_text = Text(tab, width=70, height=10)
my_text.pack(pady=20,padx=10)

my_button = tb.Button(tab, text="Click Me", bootstyle="warning outline")
my_button.pack(pady=10)

my_label2 = Label(tab2, text="A label 2 Great", font = ("Helvetica", 18))
my_label2.pack(pady=20)

# Add our frames to the notebook

my_notebook.add(tab, text="Tab one")

my_notebook.add(tab2, text="Tab Two")


root.mainloop()