from PIL import Image
Image.CUBIC = Image.BICUBIC
from tkinter import *
from ttkbootstrap.dialogs import Messagebox as MSG
import ttkbootstrap as tb 
import time
from ttkbootstrap.toast import ToastNotification
import pygame
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
ruta_audio = os.path.join(script_directory, "media", "audio.wav")

root = tb.Window(themename="cyborg")
root.title("Temporizador APP")
root.geometry("650x600")


temporizador_en_ejecucion = False
total_t = 0
destroyer = False
# Sonido función
def reproducir_sonido(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()
# Funciones
def carga_hora():
    global temporizador_en_ejecucion, total_t
    try:
        if entry_hour.get():
            hour = int(entry_hour.get())
        else:
            hour = 0
        if entry_minute.get():
            minute = int(entry_minute.get())
        else:
            minute = 0
        if entry_sec.get():
            sec = int(entry_sec.get())
        else:
            sec = 0
        if hour*3600 + minute*60 + sec > 0:
            total_t = hour*3600 + minute*60 + sec
            # Bucle que ocurre solo si el tiempo total es mayor a 0
            ToastNotification(title="Carga de Valores",
                            message="La carga se efectuó",
                            duration=3000, # Without time doesn't disappear if you don't click
                            alert=True,
                            position=(20,50,'sw')
                            ).show_toast()
        
    except:
        MSG.show_error(title="Error", message="Formato de hora erronea")
        
    

def ejecutar_temporizador():
    global temporizador_en_ejecucion, total_t, destroyer
    temporizador_en_ejecucion = True
    total_start = total_t
    try:
        while total_t>=0:
            clock.configure(amountused=int((total_start-total_t)/total_start * 100))
            horas, remainder = divmod(total_t, 3600)
            minutos, segundos = divmod(remainder, 60)
            clock.configure(subtext=f'{horas}:{minutos}:{segundos}')
            root.update()
            time.sleep(1)
            total_t -= 1
            if destroyer:
                break
        
        
        if total_t == -1 and temporizador_en_ejecucion == True :
            reproducir_sonido(ruta_audio)

        if not temporizador_en_ejecucion:
            clock.configure(amountused=0)
            clock.configure(subtext="00:00:00")
        else:
            temporizador_en_ejecucion = False
    except:
        MSG.show_error(title="Error", message="No ha cargado los valores")

def detener_temporizador():
    global temporizador_en_ejecucion
    temporizador_en_ejecucion = False

def reanudar_temporizador():
    global temporizador_en_ejecucion
    if not temporizador_en_ejecucion:
        ejecutar_temporizador()

def reset_temporizador():
    global temporizador_en_ejecucion, total_t
    temporizador_en_ejecucion = False
    total_t = 0
    clock.configure(amountused=0)
    clock.configure(subtext="00:00:00")

def rean_para():
    if temporizador_en_ejecucion:
        detener_temporizador()
    else:
        reanudar_temporizador()

def reset():
    reset_temporizador()
    #MSG.show_info("En progreso", "Aun no funciona")

def salir():
    global destroyer
    try:
        mb = MSG.yesno("Fin del Programa","Quiere Salir?")
        if mb == "Yes":
            destroyer=True
            root.destroy()
            
    except Exception as e:
        print(f'Error al salir {e}')


frame_prin = tb.Frame(root)
frame_prin.pack(pady=40,padx=5, anchor=CENTER)
# Frame reloj
frame_clock = tb.LabelFrame(frame_prin, bootstyle="info", text="Cuadro de Timer")
frame_clock.grid(padx=2, pady=2, row=0, column=0,sticky=NSEW)
frame_clock.rowconfigure(0,weight=1)
frame_clock.columnconfigure(0, weight=1)
# Reloj
clock = tb.Meter(frame_clock, 
                 bootstyle="info",
                 padding=30,
                 #subtext= "HH:MM:SS",
                 subtextstyle="success",
                 stripethickness=10,
                 amounttotal=100,
                 metersize=150,
                 textright="%",
                )

clock.grid(pady=10,padx=10, column=0, row=0, sticky=NSEW)
# Frame tiempo
frame_input_time = tb.LabelFrame(frame_prin, bootstyle="info", text="Ingreso del tiempo")
frame_input_time.grid(padx=2, pady=2, row=1, column=0,sticky=NSEW)
# Hora
label_hour = tb.Label(frame_input_time,font=("Arial",12), bootstyle="success", text="Ingrese Horas")
label_hour.grid(pady=10,padx=10, column=0, row=0,sticky=NSEW)

entry_hour = tb.Entry(frame_input_time, bootstyle="success", width=10, font=("Arial",12))
entry_hour.grid(pady=10,padx=10, column=1, row=0,sticky=NSEW)
# Minuto
label_minute = tb.Label(frame_input_time,font=("Arial",12), bootstyle="success", text="Ingrese Minutos")
label_minute.grid(pady=10,padx=10, column=0, row=1,sticky=NSEW)

entry_minute = tb.Entry(frame_input_time, bootstyle="success", width=10, font=("Arial",12))
entry_minute.grid(pady=10,padx=10, column=1, row=1,sticky=NSEW)
# Segundos
label_sec = tb.Label(frame_input_time,font=("Arial",12), bootstyle="success", text="Ingrese Segundos")
label_sec.grid(pady=10,padx=10, column=0, row=2,sticky=NSEW)

entry_sec = tb.Entry(frame_input_time, bootstyle="success", width=10, font=("Arial",12))
entry_sec.grid(pady=10,padx=10, column=1, row=2,sticky=NSEW)

# Frame botones
frame_buttons = tb.LabelFrame(frame_prin, bootstyle="info", text="Acciones",)
frame_buttons.grid(padx=2, pady=2, row=0, column=1,rowspan=2,sticky=NSEW)
# Ajuste de las columnas y rows para ocupar espacio equitativamente
frame_buttons.columnconfigure(0, weight=1)
frame_buttons.rowconfigure(0, weight=1)
frame_buttons.rowconfigure(1, weight=1)
frame_buttons.rowconfigure(2, weight=1)
# Envíar Tiempo e Iniciar
enviar_button = tb.Button(frame_buttons,text="Cargar Valores", bootstyle="info", command=carga_hora)
enviar_button.grid(pady=20, padx=20, row=0, column=0,sticky=NSEW)
# Reanudar / Parar
rean_button = tb.Button(frame_buttons,text="Iniciar/Reanudar/Parar", bootstyle="info", command=rean_para)
rean_button.grid(pady=20, padx=20, row=1, column=0,sticky=NSEW)
# Reiniciar
reset_button = tb.Button(frame_buttons,text="Reset", bootstyle="info", command=reset)
reset_button.grid(pady=20, padx=20, row=2, column=0,sticky=NSEW)

OFF_button = tb.Button(frame_buttons,text="Apagar", bootstyle="warning", command=salir)
OFF_button.grid(pady=20, padx=20, row=3, column=0,sticky=NSEW)



root.mainloop()