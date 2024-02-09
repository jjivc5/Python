import re
import csv
import os


def count_lines(input_folder):
    real_total = 0
    for filename in os.listdir(input_folder):
        # Comprobar si el archivo es un archivo Markdown
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_folder, filename)

            with open(input_filepath, 'r', encoding='utf-8') as input_file:
                # Leer todas las líneas del archivo
                lines = input_file.readlines()
                # Contar líneas
                total_lines = len(lines)

                print("Cantidad de líneas en", filename, ":", total_lines)
            
            real_total += total_lines

    print(f"Cantidad total de líneas: {real_total}")

def add_point(input_folder, output_folder):

     for filename in os.listdir(input_folder):
        # Comprobar si el archivo es un archivo Markdown
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.join(output_folder, filename)
            print("Procesando archivo:", input_filepath)

            with open(input_filepath, 'r', encoding='utf-8') as input_file:
                # Leer todas las líneas del archivo
                lines = input_file.readlines()

            modified_lines = []
        
            for line in lines:
                if line.rstrip().endswith('.') or line.strip() == '':
                    modified_lines.append(line)
                else:
                    modified_lines.append(line.rstrip() + '.' + '\n')

        
            with open(output_filepath, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)


def filter_lines_and_save(input_folder, output_folder):
    # Iterar sobre los archivos en la carpeta
    for filename in os.listdir(input_folder):
        # Comprobar si el archivo es un archivo Markdown
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_folder, filename)
            output_filename = "filtered_" + filename
            output_filepath = os.path.join(output_folder, output_filename)

            print("Procesando archivo:", input_filepath)

            with open(input_filepath, 'r', encoding='utf-8') as input_file:
                # Leer todas las líneas del archivo
                lines = input_file.readlines()

                # Filtrar las líneas que comienzan con **
                filtered_lines = [line for line in lines if line.strip().startswith('**') or line.strip().startswith('>**')]

            # Guardar las líneas filtradas en un nuevo archivo en la carpeta de salida
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.writelines(filtered_lines)

def cleanCharacter(input_folder, output_folder):
      
      for filename in os.listdir(input_folder):
        # Comprobar si el archivo es un archivo Markdown
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.join(output_folder, filename)
            print("Procesando archivo:", input_filepath)

            with open(input_filepath, 'r', encoding='utf-8') as input_file:
                # Leer todas las líneas del archivo
                lines = input_file.readlines()

                filtered_lines = [line.lstrip('>') for line in lines]

            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.writelines(filtered_lines)



def parse_md_files(input_folder, output_csv):
    # Lista para almacenar los datos de todos los archivos
    all_data = []

    # Iterar sobre los archivos en la carpeta
    for filename in os.listdir(input_folder):
        # Comprobar si el archivo es un archivo Markdown
        if filename.endswith(".md"):
            filepath = os.path.join(input_folder, filename)
            print("Procesando archivo:", filepath)

            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # Buscar patrones de palabras en negrita con traducción
            pattern = re.compile(r'\*\*([^*]+?)\*\*\s*:\s*([^*]+?)(?=\*\*|$)', re.DOTALL)
            #pattern = re.compile(r'\*\*(.*?)\*\*:\s*(.*?)[\n.]\s*', re.DOTALL)
            matches = pattern.findall(content)

            # Crear lista de diccionarios con las palabras y traducciones
            data = [{'palabra_en_ingles': match[0].strip(), 'traduccion': match[1].strip()} for match in matches]

            # Extender la lista de datos global
            all_data.extend(data)
            # print(data)
            
            # x= input("Seguir ?/n: ")

            # if x=="n":
            #     break

    # Imprimir los datos antes de escribir en el archivo CSV
    #print("Data:", all_data)

    # Guardar los datos en un archivo CSV
    with open(output_csv, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['palabra_en_ingles', 'traduccion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(all_data)

if __name__ == "__main__":
    # Especifica la carpeta de entrada y el archivo de salida
    ruta_ejecucion = os.path.dirname(os.path.realpath(__file__))
    input_folder_path = os.path.join(ruta_ejecucion,"archivosmd")
    # output_csv_path = os.path.join(input_folder_path, 'salida.csv')
    # parse_md_files(input_folder_path, output_csv_path)
    output_carpet = os.path.join(ruta_ejecucion,"filter_archivos_md")
    input_folder_path_1 = os.path.join(ruta_ejecucion,"filter_archivos_md")
    output_carpet_1 = os.path.join(ruta_ejecucion,"filter_archivos_md")
    #cleanCharacter(input_folder_path_1,output_carpet_1)
    #add_point(input_folder_path_1,output_carpet_1)
    parse_md_files(input_folder_path_1,'Devolucion.csv')
    count_lines(input_folder_path_1)