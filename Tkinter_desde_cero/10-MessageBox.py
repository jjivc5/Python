import tkinter as tk 
import tkinter.messagebox as tkmsg

root = tk.Tk()

root.title("Mensaje de Caja ")
root.iconbitmap("./media/bgs.ico")

def muestra_ventana():
    #tkmsg.showinfo(title="Cuadro de dialogo", message="Que onda loco?")
    #tkmsg.showwarning(title="Cuadro de dialogo", message="Que onda loco?")
    #tkmsg.showerror(title="Cuadro de dialogo", message="Que onda loco?")
    # Cambian los iconos
    #tkmsg.askquestion(message="Debería salir a la calle? ", title = "Titulo de ventana")
    #tkmsg.askyesno(message="Debería salir a la calle? ", title = "Titulo de ventana")
    #tkmsg.askyesnocancel(message="Debería salir a la calle? ", title = "Titulo de ventana")
    tkmsg.askretrycancel(message="Debería salir a la calle? ", title = "Titulo de ventana")
    # Cambian las preguntas


boton1 = tk.Button(root, text="Enviar", command=muestra_ventana, width=75).pack()

root.mainloop()