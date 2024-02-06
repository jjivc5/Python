import tkinter as tk 
import tkinter.messagebox as tkmsg

root = tk.Tk()

root.title("Mensaje de Caja ")
root.iconbitmap("./media/bgs.ico")

def muestra_ventana():
    response = tkmsg.askquestion(message="Debería salir a la calle? ", title = "Titulo de ventana")
    if response == "no":
        tkmsg.showinfo(title="Respuesta correcta", message = "Hace un calor de re contra re mil cagar")
    else:
        response_2=tkmsg.askretrycancel(title="No era por aca", message="No la estas viendo rey, elegi bien")
        # retry da un valor true or false
        if response_2:
            muestra_ventana()
        else:
            tkmsg.showinfo(title="Que tipo boludo", message= " Seguro sos hincha de Racing")


boton1 = tk.Button(root, text="Enviar", command=muestra_ventana, width=75).pack()

root.mainloop()