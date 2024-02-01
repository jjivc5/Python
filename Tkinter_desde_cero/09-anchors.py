from tkinter import *

root = Tk()

titulo_1 = Label(root,text="Noroeste").pack(anchor=NW)
titulo_2 = Label(root,text="Norte").pack(anchor=N)
titulo_3 = Label(root,text="Noreste").pack(anchor=NE)
titulo_4 = Label(root,text="Oeste").pack(anchor=W)
titulo_5 = Label(root,text="Centro").pack(anchor=CENTER)
titulo_6 = Label(root,text="Este").pack(anchor=E)
titulo_7 = Label(root,text="Sudoeste").pack(anchor=SW)
titulo_8 = Label(root,text="Sur").pack(anchor=S)
titulo_9 = Label(root,text="Sudeste").pack(anchor=SE)


root.mainloop()