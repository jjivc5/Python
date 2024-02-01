import tkinter as tk

from tkinter import font

import tkinter.messagebox as tkmsg

root = tk.Tk()
root.title("Calculadora básica")
root.iconbitmap("./media/bgs.ico")
root.resizable(0,0)
root.geometry("450x600")
root.configure(bg="black",padx=30,pady=20)

pantalla = tk.Entry(width=20,
                    bg="gray",
                    fg="skyblue",
                    borderwidth=0,
                    font=('arial',20,'bold'),
                    )

pantalla.grid(row=0,padx=10,pady=10,columnspan=4)

def envia_boton(valor):
    anterior = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, str(anterior) + str(valor))

def suma():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "+"

def resta():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "-"

def mult():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "*"

def dividir():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "/"

def clear():
    pantalla.delete(0,tk.END)

    

def igual():
    try:
        global num2
        num2 = pantalla.get()
        num2 = float(num2)
        pantalla.delete(0,tk.END)
        
        if operacion == "+":
            resultado = num1+num2
        elif operacion == "-":
            resultado = num1-num2
        elif operacion == "*":
            resultado = num1*num2
        elif operacion == "/":
            if num2==0:
                tkmsg.showerror(title="Operación No realizada", message="No se puede dividir por cero")
                resultado = "Inf"
            else:
                resultado = num1/num2
        
        
        pantalla.insert(0, str(resultado))
    except:
        tkmsg.showerror(title="Operación No realizada", message="No se ha realizado ninguna operación valida")

boton_suma = tk.Button(
    text = '+',
    width = 9 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command=suma
)

boton_suma.grid(row=1,column=3, padx=1, pady=15)

boton_resta = tk.Button(
    text = '-',
    width = 9 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command=resta
)
boton_resta.grid(row=2,column=3, padx=1, pady=15)

boton_mult = tk.Button(
    text = '*',
    width = 9 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command = mult
)
boton_mult.grid(row=3,column=3, padx=1, pady=15)

boton_div = tk.Button(
    text = '/',
    width = 9 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command=dividir
)
boton_div.grid(row=4,column=3, padx=1, pady=15)


boton_1 = tk.Button(
    text = '1',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(1))
)
boton_1.grid(row=1,column=0, padx=1, pady=15)



boton_2 = tk.Button(
    text = '2',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(2))
)
boton_2.grid(row=1,column=1, padx=1, pady=15)

boton_3 = tk.Button(
    text = '3',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(3))
)
boton_3.grid(row=1,column=2, padx=1, pady=15)

boton_4 = tk.Button(
    text = '4',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(4))
)
boton_4.grid(row=2,column=0, padx=1, pady=15)

boton_5 = tk.Button(
    text = '5',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(5))
)
boton_5.grid(row=2,column=1, padx=1, pady=15)

boton_6 = tk.Button(
    text = '6',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(6))
)
boton_6.grid(row=2,column=2, padx=1, pady=15)

boton_7 = tk.Button(
    text = '7',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(7))
)
boton_7.grid(row=3,column=0, padx=1, pady=15)

boton_8 = tk.Button(
    text = '8',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(8))
)

boton_8.grid(row=3,column=1, padx=1, pady=15)

boton_9 = tk.Button(
    text = '9',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(9))
)

boton_9.grid(row=3,column=2, padx=1, pady=15)

boton_0 = tk.Button(
    text = '0',
    width = 9 ,
    height = 3 ,
    bg = "gray",
    fg = "skyblue",
    borderwidth = 0,
    cursor = "hand2",
    command = lambda : (envia_boton(0))
)

boton_0.grid(row=4,column=0, padx=1, pady=15)

boton_point = tk.Button(
    text = '.',
    width = 9 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command= lambda : (envia_boton("."))
)

boton_point.grid(row=4,column=1, padx=1, pady=15)

boton_equal = tk.Button(
    text = '=',
    width = 9 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command=igual
)

boton_equal.grid(row=4,column=2, padx=1, pady=15)

boton_clear = tk.Button(
    text = 'CLEAR',
    font = "Arial, 12",
    width = 10 ,
    height = 3 ,
    bg = "blue",
    fg = "white",
    borderwidth = 0,
    cursor = "hand2",
    command=clear
)

boton_clear.grid(row=5,column=0,padx=1, pady=15,columnspan=4)


root.mainloop()