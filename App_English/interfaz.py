from tkinter import *
import ttkbootstrap as tkb
from ttkbootstrap.dialogs import Messagebox as MSG 
#from styles import *


class Interface:
    def __init__(self):
        self.main_w = tkb.Window(themename="cyborg")
        self.main_w.title("Mi glosario en Inglés")
        self.main_w.geometry("1024x768")
        self.default_style = {}  # Estilos Nulos de Widget
        self.default_grid = {}  # Estilos Nulos de Grid

    # def getMainW(self):
    #     return self.main_w
    
    def whenCloseWindow(self,object):
        self.main_w.protocol("WM_DELETE_WINDOW",object)

    def finishApp(self):
        self.main_w.destroy()
        
    def addframe(self, style = None, padstyle = None):
         # Los estilos por defecto.
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        # Es necesario realizar una copia para evitar problemas de sobreescritura
        # Actualizar con los estilos proporcionados
        current_style.update(style or {})
        current_grid.update(padstyle or {})
        # La creación del frame
        frame = tkb.Frame(self.main_w,**current_style)
        frame.pack(**current_grid,
                   anchor=CENTER)
        return frame

    def addlabelframe(self,dependency,r,c,style = None, padstyle = None,t="default",rspan=1,cspan=1):
        # Los estilos por defecto.
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        # Es necesario realizar una copia para evitar problemas de sobreescritura
        # Actualizar con los estilos proporcionados
        current_style.update(style or {})
        current_grid.update(padstyle or {})

        labelframe = tkb.LabelFrame(dependency,text=t,**current_style)
        labelframe.grid(row=r,
                        column=c, 
                        rowspan=rspan, 
                        columnspan=cspan,
                        sticky=NSEW,
                        **current_grid)
        
        return labelframe
    
    def addlabelframe_pack(self,dependency,style = None, padstyle = None,t="default"):
        # Los estilos por defecto.
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        # Es necesario realizar una copia para evitar problemas de sobreescritura
        # Actualizar con los estilos proporcionados
        current_style.update(style or {})
        current_grid.update(padstyle or {})

        labelframe = tkb.LabelFrame(dependency,text=t,**current_style,width=1000)
        labelframe.pack(**current_grid)
        
        return labelframe
        
    def addentry(self,dependency,r,c,style = None, padstyle = None):
        # Los estilos por defecto.
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        # Es necesario realizar una copia para evitar problemas de sobreescritura
        # Actualizar con los estilos proporcionados
        current_style.update(style or {})
        current_grid.update(padstyle or {})

        entry = tkb.Entry(dependency,**current_style)
        entry.grid(row=r,
                   column=c,
                   sticky=NSEW,
                   **current_grid)
        return entry
        
    def addlabel(self, dependency, r, c, t="", style = None, padstyle = None):
        # Los estilos por defecto.
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        # Es necesario realizar una copia para evitar problemas de sobreescritura
        # Actualizar con los estilos proporcionados
        current_style.update(style or {})
        current_grid.update(padstyle or {})
        # Definición del Widget y su griding
        label = tkb.Label(dependency,text=t,**current_style)
        label.grid(row=r,column=c,sticky=NSEW,**current_grid)

    def addboton(self,dependency,r,c,t="click", style = None, padstyle = None , obj = None):
        # Los estilos por defecto.
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        # Es necesario realizar una copia para evitar problemas de sobreescritura
        # Actualizar con los estilos proporcionados
        current_style.update(style or {})
        current_grid.update(padstyle or {})

        boton = tkb.Button(dependency,text=t, **current_style,command=obj)
        boton.grid(row=r,
                   column=c,
                   sticky=NSEW,
                   **current_grid)

    def addTree(self,dependency,r,c,name_columns, style = None, padstyle = None,wdt=100):
        
        current_style = self.default_style.copy()
        current_grid = self.default_grid.copy()
        
        current_style.update(style or {})
        current_grid.update(padstyle or {})

        tree = tkb.Treeview(dependency,**current_style,columns=name_columns,show="headings")
        tree.grid(row=r,
                   column=c,
                   sticky=NSEW,
                   **current_grid)
        
        for column_name in name_columns:
            if column_name == 'Oracion':
                tree.column(column_name, width=int(wdt/2))
            else:
                tree.column(column_name, width=wdt)
            tree.heading(column_name, text = column_name)

        return tree

    def run_interface(self):
        self.main_w.mainloop()


# ventana = Interfaz()
# frame_inicial = ventana.addframe(padstyle=sty_pad1)

# frame_1 = ventana.addlabelframe(frame_inicial,0,0,sty_fr_pri,t="Busqueda de Palabras")
# ventana.addentry(frame_1,0,1,sty_entry,padstyle=sty_pad1)
# ventana.addboton(frame_1,0,2,"Realizar Busqueda",sty_entry,padstyle=sty_pad1)
# ventana.addlabel(frame_1,0,0,"Busqueda en Inglés",sty_label,padstyle=sty_pad1)

# ventana.addentry(frame_1,1,1,sty_entry,padstyle=sty_pad1)
# ventana.addboton(frame_1,1,2,"Realizar Busqueda",sty_entry,padstyle=sty_pad1)
# ventana.addlabel(frame_1,1,0,"Busqueda en Español",sty_label,padstyle=sty_pad1)

# frame_2 = ventana.addlabelframe(frame_inicial,1,0,sty_fr_pri,t="Resultados")
# ventana.addlabel(frame_2,1,0,"Texto de la consulta o Ventana de la Consulta",sty_label,padstyle=sty_pad1)

# ventana.run_interface()

