# Estas librerías las necesitamos para el METER
from PIL import Image
Image.CUBIC = Image.BICUBIC
# Esto lo necesitamos para la interfaz gráfica
from tkinter import *
import ttkbootstrap as tb 
from ttkbootstrap.dialogs import Messagebox as MSG
from ttkbootstrap.toast import ToastNotification
# Esto lo necesitamos para el sleep() y contar el tiempo
import time
# Esto lo necesitamos para reproducir el sonido
import pygame
# Esto lo necesitamos para encontrar el path, y lograr que se encuentre
# La ruta del archivo
import os


# Para obtener la ruta desde donde corremos
script_directory = os.path.dirname(os.path.realpath(__file__))
# Para hacer un join de las rutas
ruta_audio = os.path.join(script_directory, "media", "audio.wav")
print(ruta_audio)