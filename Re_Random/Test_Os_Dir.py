# Vamos a realizar un par de pruebas para ver si se entienden los métodos usados.
import os

def listarDir(directorio):
    
    for nombre_iterador in os.listdir(directorio):

        print(f"Nombre de archivo: {nombre_iterador}") # Itero el arreglo

    print(f"Listado total {os.listdir(directorio)}") # Devuelve un arreglo con todos las rutas del directorio


def endsCon(directorio, formato):

    for nombre_iterador in os.listdir(directorio):

        if nombre_iterador.endswith(f".{formato}"): # endswith se vuelve Verdadero cuando hay una coincidencia con el
            # final del archivo, que por defecto es la extensión del archivo (evidentemente podríamos seguir otro patrón)
            # Ejemplo archivos que sean 1_foto.jpg 2_foto.jpg (algo así)
            print(f"El formato de tipo: .{formato}: Devuelve -> {nombre_iterador}")


def lecturaFiles(directorio,formato):
    for files in os.listdir(directorio):

        if files.endswith(f".{formato}"):

            archivo_puntual = os.path.join(directorio,files)
            with open(archivo_puntual, 'r', encoding='utf-8') as input_file: # Veamos la limitante de que esto sirve para leer 
                    # Texto plano, o archivos que sean legible y no estén codificadas.
                    # Por ejemplo para intentar extraer contenido de PDF hay que usar librerías más avanzadas.
                    lines = input_file.readlines() # Esto devuelve un arreglo donde cada posición equivale a una línea
                    # Y el proximo elemento del arreglo es aquel que tiene un salto de línea respecto al primero.
                    print(f"El archivo ha retornado:\n {lines}")


def modTexto(directorio,formato,opc=1):
    for files in os.listdir(directorio):

        if files.endswith(f".{formato}"):

            archivo_puntual = os.path.join(directorio,files)
            with open(archivo_puntual, 'r', encoding='utf-8') as input_file:
                    lines = input_file.readlines()
            
            for line in lines:
                 if opc==1:
                    print(f"La línea contiene : \n {line} devuelve : \n {line.rstrip().endswith('.')}") # con esta combinación obtenemos
                 # Un true si la línea termina con un punto "."
                 elif opc==2:
                      print(f"La línea: \n {line} devuelve : \n {line.rstrip()} ") # Sirve para eliminar espacios, tabulaciones.
                      # es complicado de ver a simple vista
                 elif opc==3:
                    print(f"La línea: \n {line} devuelve : \n {line.strip()} ") # Esto lo hace al principio y final de la línea.
                 elif opc==4:
                    if (line.strip() ==''): # Con esto verífico aquellos saltos de líneas que esten vacíos.
                        print(f"Esta línea : {line} tiene espacios vacíos")
                    else:
                        print(f"Esta línea : {line} no! tiene espacios vacíos")

def arrancaCon(directorio,formato,match):
     for files in os.listdir(directorio):

        if files.endswith(f".{formato}"):

            archivo_puntual = os.path.join(directorio,files)
            with open(archivo_puntual, 'r', encoding='utf-8') as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        if line.strip().startswith(f"{match}"): # Es true cuando coincide con match, el inicio de una línea
                            # strip se usa para eliminar los espacios en blanco que pueden existir para evitar este problema.
                            print(f"El matching {match} se encuentra en: {line}")

def borrarChar(directorio,formato,delete):
     for files in os.listdir(directorio):

        if files.endswith(f".{formato}"):

            archivo_puntual = os.path.join(directorio,files)
            with open(archivo_puntual, 'r', encoding='utf-8') as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                         print(f"Línea normal: {line}")
                         print(f"Línea modificada por izquierda: {line.lstrip(delete)}") # Puedo borrar por derecha (Left)
                         # también podría hacerlo a ambos lados y por derecha probemos ambos lados.
                         print(f"Línea modificada por ambos lados: {line.strip(delete)}")


dir_1 = "C:\\Users\\Nacho\\Downloads"
dir_2 = "./"
#listarDir(dir_1)
#endsCon(dir_1,'pdf')

#print(os.path.join(dir_1,"gilada")) El os.path.join, me agrega la barra de la dirección por argumento
#print(os.path.join(dir_1,"gilada","subgilada")) toma n parámetros *args dicho en python terms

#lecturaFiles(dir_1,'txt')

#modTexto(dir_2,'txt',4)

#arrancaCon(dir_2,'txt',">*")
borrarChar(dir_2,'txt',"+")