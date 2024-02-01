# Me gusta la combinación de marcos más celdas, puede ser por ahí.
import tkinter as tkb

ventana_main = tkb.Tk()

ventana_main.title("Ventana de Prueba SQL English Knowledge")

width_main = 800

height_main = 600

ventana_main.configure(background="gray58")

ventana_main.geometry(str(width_main)+"x"+str(height_main))

# Marco de Consulta

marco_consulta=tkb.LabelFrame(ventana_main,
                              text="Ingrese su consulta: ",
                              font="Arial 20",
                              padx=5,
                              pady=5,
                              background="gray63",
                              relief="groove",
                              border=5
                              )
marco_consulta.grid(row=0,
                    column=0,
                    padx=15,
                    pady=15,)

marco_buscar=tkb.LabelFrame(ventana_main,
                            text="Realizar Consulta",
                            font="Arial 20",
                            padx=5,
                            pady=5,
                            background="gray63",
                            relief="groove",
                            border=5)

marco_buscar.grid(row=1,
                    column=0,
                    padx=15,
                    pady=15,)

marco_resultado = tkb.LabelFrame(ventana_main,
                                 text="Resultado Consulta",
                                 font="Arial 20",
                                 padx=5,
                                 pady=5,
                                 background="gray63",
                                 relief="groove",
                                 border=5)

marco_resultado.grid(row=0,
                     column=1,
                     padx=15,
                     pady=15,)

consulta = tkb.Entry(marco_consulta,
                 background="gray33",
                 foreground="lightskyblue",
                 border=5,
                 width = 20,
                 font="Arial 16",
                 relief="solid")

consulta.pack()
consulta.insert(0,"Ingrese consulta..") # Esto es un texto por default, para que se vea mejor
consulta.bind("<Button-1>", lambda e: consulta.delete(0, tkb.END)) # Esto al clickear borra ese texto.

# Acá se realizaría la consulta

resultado =  tkb.Label(marco_resultado,
              text="",
              background="gray33",
              foreground="lightskyblue",
              border=5,
              width = 20,
              font="Arial 16",
              relief="solid")

resultado.pack()
marco_resultado.grid_remove()

def efectuar_consulta():
    valor_retornado_consulta = consulta.get()
    resultado.config(text=f"{valor_retornado_consulta}")
    consulta.delete(0, tkb.END)
    consulta.insert(0,"Ingrese consulta..")
    marco_resultado.grid()


# Acá defino el boton que ejecuta la consulta

boton_consultador = tkb.Button(marco_buscar,
                               text="Realizar Consulta",
                               background="gray33",
                               foreground="lightskyblue",
                               border=5,
                               width = 20,
                               font="Arial 16",
                               relief="solid",
                               command=efectuar_consulta)

boton_consultador.pack()


ventana_main.mainloop()