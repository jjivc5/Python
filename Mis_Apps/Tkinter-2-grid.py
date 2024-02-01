import tkinter

def changetext():
    textochange = cajaTexto.get()
    etiquetaReWrite["text"] = textochange


ventana = tkinter.Tk()

largo = 400
ancho = 400
ventana.geometry(str(largo)+"x"+str(ancho)) 

etiqueta = tkinter.Label(ventana, text = "Holiwis")

boton1 = tkinter.Button(ventana, text = "Presiona", command=changetext)

cajaTexto = tkinter.Entry(ventana, font="Arial 20",width="10")

etiquetaReWrite = tkinter.Label(ventana, text="")



#etiqueta
etiqueta.grid(row=0, column=0, padx=10,pady=10)
etiqueta.config(width="15",height="5")
etiqueta.config(bg="#dd77dd")
#boton1
boton1.grid(row=1,column=0, padx=10,pady=10)
boton1.config(width="15",height="5")
boton1.config(bg="#bb77bb")
#CajaTexto
cajaTexto.grid(row=1,column=1,padx=30) # Para las cajas de texto tipo Entry solo se puede modificar el width
                               # En su creación únicamente.

#EtiquetaReWrite
etiquetaReWrite.grid(row=2,column=0, padx=10,pady=10)
etiquetaReWrite.config(width="15",height="5")
etiquetaReWrite.config(bg="#cc77cc")

ventana.mainloop()
