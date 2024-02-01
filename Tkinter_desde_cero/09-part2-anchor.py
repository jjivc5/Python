from tkinter import *

root = Tk()

titulo_1 = Label(root,text="Este texto esta").pack(anchor=NW)
titulo_2 = Label(root,text="Puesto").pack(anchor=NW)
titulo_3 = Label(root,text="En dirección").pack(anchor=NW)
titulo_4 = Label(root,text="Al Noroeste").pack(anchor=NW)

titulo_4 = Label(root,text="ESTE NO").pack(anchor=SE)



root.mainloop()