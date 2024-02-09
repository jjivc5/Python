import sqlite3
import csv

# Función para leer los datos del CSV y agregarlos a la base de datos
def add_csv_to_database(csv_file, db_file):
    # Conecta con la base de datos SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Abre el archivo CSV y lee sus datos
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        # Itera sobre cada fila del CSV
        for row in csvreader:
            # Inserta los datos en la base de datos
            cursor.execute('INSERT INTO diccionario (in_english, traduccion) VALUES (?, ?)', (row[0], row[1])) # Ajusta el nombre de la tabla y las columnas según tu base de datos

    # Guarda los cambios en la base de datos
    conn.commit()

    # Cierra la conexión
    conn.close()

# Llama a la función para agregar el CSV a la base de datos
add_csv_to_database('Devolucion.csv', 'dictionary.db')
