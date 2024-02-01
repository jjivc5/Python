import tkinter

def consulta():
    print("Aca el día que realices la consulta")

def texto():
    textovar = cajaTexto.get()
    print(textovar)

def changetext():
    textochange = cajaTexto.get()
    etiquetaReWrite["text"] = textochange
    

ventana = tkinter.Tk()

ventana.geometry("300x300") # Con esto cambio el tamaño de la ventana.

etiqueta = tkinter.Label(ventana, text = "Holiwis", bg = "yellow") # Con esto defino una etiqueta,
#para la ventana.
# Con bg defino el color del fondo

etiqueta2 = tkinter.Label(ventana, text="Texto Vertical", bg="green")


etiqueta.pack(side = tkinter.BOTTOM, fill = tkinter.X) # Pack Acomoda automaticamente mi etiqueta
# Además como argumento le puedo decir la posición donde quiero que se ajuste.
# Con fill = tkinter.X relleno toda la pantalla la etiqueta en el eje X


etiqueta2.pack(side = tkinter.TOP, fill = tkinter.Y, expand = True) #Idem lo anterior pero ahora
# Ajusto sobre el eje "Y", para rellenar además hace falta aclarar con el comando EXPAND
# Si cambio tkinter.Y por tkinter.BOTH obtendría un relleno tanto en X como Y.


boton1 = tkinter.Button(ventana, text = "Presiona", bg="#bb77bb" ,padx=50, pady=50, command=changetext)
boton1.pack(side="top")

cajaTexto = tkinter.Entry(ventana, font="Arial 20")
cajaTexto.pack()

etiquetaReWrite = tkinter.Label(ventana, text="", bg="pink")
etiquetaReWrite.pack()

ventana.mainloop()
