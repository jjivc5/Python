from interfaz import *
from styles import *
from managersql import *


def ender():
    if MSG.yesno("Cerrar aplicación", "¿Está seguro que desea salir?", parent = frame_query_all ) == "Yes":
        db.end_con()
        ventana.finishApp()

def cleantree():
    tree.delete(*tree.get_children())

def addDataTree(datos):
    for it_dato in datos:
        it_dato_ajustado = [value if value is not None else '' for value in it_dato]
        tree.insert('',END,values=it_dato_ajustado)

def query_diccionario():
    cleantree()
    datos=db.queryAllDB("diccionario")
    addDataTree(datos)

def query_word_english():
    cleantree()
    datos=db.query_by_english(english_entry.get())
    addDataTree(datos)

def query_word_spanish():
    cleantree()
    datos=db.query_by_spanish(spanish_entry.get())
    addDataTree(datos)

def query_top_ten():
    cleantree()
    datos=db.get10moresearch()
    addDataTree(datos)

def add_Word():
    if len(english_add_entry.get()) != 0 and len(spanish_add_entry.get()) != 0:
        if MSG.yesno(title="Estas seguro", message="¿Lo que pusiste es correcto?",parent=frame_add_w_main) == "Yes":
            db.insertWord(eng_w=english_add_entry.get(),trad=spanish_add_entry.get(), sentence=sent_add_entry.get())
            db.commit()
        else:
            MSG.show_info(title="Estado",message="Se cancelo el agregado",parent=frame_add_w_main)
    else:
        MSG.show_error(title="Error",message="No se han completado los campos minimos",parent=frame_add_w_main)

if __name__ == "__main__":
    ventana = Interface()
    # Los frames principales
    frame_search = ventana.addframe(padstyle=sty_pad1)
    frame_add_w_main = ventana.addframe(padstyle=sty_pad1)
    frame_query_all = ventana.addframe(padstyle=sty_pad1)
    frame_table_response = ventana.addframe(padstyle=sty_pad1)

    # Frame de busqueda de palabras
    frame_search_1 = ventana.addlabelframe(frame_search,0,0,sty_high,t="Busqueda de Palabras")
    # En inglés + entry + botón
    english_entry = ventana.addentry(frame_search_1,0,1,sty_entry,padstyle=sty_pad1)
    ventana.addboton(frame_search_1,0,2,"Realizar Busqueda",sty_entry,padstyle=sty_pad1,obj=query_word_english)
    ventana.addlabel(frame_search_1,0,0,"Busqueda en Inglés",sty_label,padstyle=sty_pad1)
    # En español + entry + botón
    spanish_entry=ventana.addentry(frame_search_1,1,1,sty_entry,padstyle=sty_pad1)
    ventana.addboton(frame_search_1,1,2,"Realizar Busqueda",sty_entry,padstyle=sty_pad1,obj=query_word_spanish)
    ventana.addlabel(frame_search_1,1,0,"Busqueda en Español",sty_label,padstyle=sty_pad1)

    # Frame de agregar palabras
    frame_add_w_text = ventana.addlabelframe(frame_add_w_main,0,0,sty_high,t="Agregar Nueva Palabra")
    frame_add_w_text_eng = ventana.addlabelframe(frame_add_w_text,0,0,sty_light,t="In English")
    frame_add_w_text_es = ventana.addlabelframe(frame_add_w_text,0,1,sty_light,t="Traduccion")
    frame_add_w_text_sent = ventana.addlabelframe(frame_add_w_text,0,2,sty_light,t="Oración")
    frame_add_button = ventana.addlabelframe(frame_add_w_text,1,1,sty_light,t="Agregar Palabra")
    # Entries
    english_add_entry = ventana.addentry(frame_add_w_text_eng,0,0,sty_entry, padstyle = sty_pad1)
    spanish_add_entry = ventana.addentry(frame_add_w_text_es,0,0,sty_entry, padstyle = sty_pad1)
    sent_add_entry = ventana.addentry(frame_add_w_text_sent,0,0,sty_entry, padstyle = sty_pad1)
    # Boton devolución
    ventana.addboton(frame_add_button,0,0,"Finalizar",sty_entry, padstyle=sty_pad_add, obj=add_Word)

    frame_query_all_1 = ventana.addlabelframe(frame_query_all,0,0,sty_high,t="Devoluciones Especiales")
    ventana.addboton(frame_query_all_1,0,0,"Consultar todos los resultados",style=sty_entry,padstyle=sty_pad_q,obj=query_diccionario)
    ventana.addboton(frame_query_all_1,0,1,"Consultar TOP 10 más consultados",style=sty_warn,padstyle=sty_pad_q, obj=query_top_ten)

    frame_table_1 = ventana.addlabelframe(frame_table_response,0,0,sty_high,t="Consulta Realizada")
    nombres = ('English Word','Significado','Oracion')
    tree=ventana.addTree(frame_table_1,0,0,nombres,padstyle=sty_pad1,wdt=250)


    db = Database()

    # Ya la cree a la tabla (aunque tiene su redundancia)
    # db.createTable('diccionario','in_english text','traduccion text','ejemplo text')
    # db.commit()

    # Agrege estos datos así a manopla, después habrá que ir pensandola a medida que metamos más cosas.
    # db.insertColumn(in_english="Hello",traduccion="Hola",ejemplo="Hello World")
    # db.insertColumn(in_english="Lacked Words",traduccion="Falta de Palabras",ejemplo=" ")
    # db.commit()

    # UNICA Y UNICA VEZ agregada
    #db.uniqueCreateCounter()
    
    ventana.whenCloseWindow(ender)

    ventana.run_interface()

