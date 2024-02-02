import re
import csv
import os

ruta_principal = os.path.dirname(os.path.realpath(__file__))
# Para hacer un join de las rutas
ruta_archivo = os.path.join(ruta_principal,"Glosario-23.12.29.md")

ruta_archivo_modificado = os.path.join(ruta_principal, "Glosario-23.12.29_modificado.md")

# Eliminar el carácter ">" al principio de cada línea y guardar el resultado
with open(ruta_archivo, 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines = [line.lstrip('>') for line in lines]

with open(ruta_archivo_modificado, 'w', encoding='utf-8') as file:
    file.writelines(lines)



def parse_md_file(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Eliminar el carácter ">" al principio de cada línea

    # Buscar patrones de palabras en negrita con traducción
    pattern = re.compile(r'\*\*(.*?)\*\*:\s*(.*?)[\n.]\s*', re.DOTALL)
    matches = pattern.findall(content)

    # Imprimir las coincidencias
    print("Matches:", matches)

    # Crear lista de diccionarios con las palabras y traducciones
    data = [{'palabra_en_ingles': match[0].strip(), 'traduccion': match[1].strip()} for match in matches]

    # Imprimir los datos antes de escribir en el archivo CSV
    print("Data:", data)

    # Guardar los datos en un archivo CSV
    with open(output_csv, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['palabra_en_ingles', 'traduccion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    output_csv_path = os.path.join(ruta_principal, 'salida.csv')
    parse_md_file(ruta_archivo_modificado, output_csv_path)

