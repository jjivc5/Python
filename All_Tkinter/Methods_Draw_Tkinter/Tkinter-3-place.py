import tkinter

def changetext():
    textochange = cajaTexto.get()
    etiquetaReWrite["text"] = textochange


ventana = tkinter.Tk()

largo = 640
ancho = 480
ventana.geometry(str(largo)+"x"+str(ancho)) 

marco = tkinter.LabelFrame(ventana,
                           text="Marco en la app")

etiqueta = tkinter.Label(ventana, 
                         text = "Super App", 
                         background = "purple1",
                         foreground= "#000000",
                         font = "Helvetica 20", 
                         justify="center",
                         bd=5,
                         relief="ridge"
                         )

boton1 = tkinter.Button(marco,
                        text = "Presiona", 
                        command=changetext, 
                        bg ="purple3", 
                        fg="#000000",
                        font = "Helvetica 20",
                        border=5,
                        )

cajaTexto = tkinter.Entry(marco, 
                          font = "Helvetica 20",
                          width="10", 
                          bg ="purple2",
                          border=5,
                          )

etiquetaReWrite = tkinter.Label(ventana, 
                                text="", 
                                bg="MediumPurple1", 
                                font = "Helvetica 20",
                                border=10,
                                relief="raised",
                                )

Eti2 = tkinter.Label(ventana, 
                     text="Todos los derechos reservados", 
                     bg="MediumPurple2", 
                     font = "Helvetica 20",
                     border=3,
                     relief="groove",
                     )

Eti3 = tkinter.Label(ventana, 
                     text="CopyRight", 
                     bg="MediumPurple3", 
                     font = "Helvetica 8",
                     border=3,
                     relief="groove",
                     )
EtHeight = 80

EtWidth = largo

etiqueta.place(x=largo/2-EtWidth/2, 
               y = 0, 
               width=EtWidth, 
               height = EtHeight
               )

Bt1Height = 100

marco.place(x=0,
            y=EtHeight,
            width=largo,
            height=Bt1Height)

boton1.pack(
            fill="x",
            side="left",
            padx=5)

cajaTexto.pack(
               fill="x",
               side="left",
               padx=5)


EtiReH = 150

etiquetaReWrite.place(x=0, 
                      y=EtHeight+Bt1Height,
                      width=largo,
                      height=EtiReH)

Eti2ReH=75

Eti2.place(x=0, 
           y=EtHeight+Bt1Height+EtiReH, 
           width=largo, 
           height=Eti2ReH
           )

Eti3.place(x=0, 
           y=EtHeight+Bt1Height+EtiReH+75, 
           width=largo, 
           height=75
           )

ventana.mainloop()
