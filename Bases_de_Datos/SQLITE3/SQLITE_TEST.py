import sqlite3 as sql


def createDB():
    con = sql.connect("streamers.db")
    con.commit()
    con.close()

def createTable():
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer
        )"""
    )
    con.commit()
    con.close()

def insertRow(nombre, followers, subs):
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO streamers VALUES('{nombre}',{followers},{subs})"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def readData():
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    con.commit()
    con.close()
    print(datos)
    return datos

def insertRows(streamerList):
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamerList)
    con.commit()
    con.close()

def readOrder(field):
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    con.commit()
    con.close()
    print(datos)
    
def search():
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name LIKE 'alexelcapo'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    con.commit()
    con.close()
    print(datos)

def buscar_similar(frase):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()

    # Utiliza FREETEXT para buscar frases similares
    query = "SELECT * FROM streamers WHERE name LIKE ?"
    cursor.execute(query, ('%'+frase+'%',))

    # Obtén los resultados
    resultados = cursor.fetchall()

    # Muestra los resultados
    for resultado in resultados:
        print(resultado)

    conn.close()

def updateFields():
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"UPDATE streamers SET followers = 1200000 WHERE name LIKE 'El Xokas'"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def deleteRow():
    con = sql.connect("streamers.db")
    cursor = con.cursor()
    instruccion = f"DELETE FROM streamers WHERE name LIKE 'Rubius'"
    cursor.execute(instruccion)
    con.commit()
    con.close()

if __name__ == "__main__": # Esto hace que al exportarlo desde otro archivo
     # Solo se obtengan los métodos que esten por fuera
    # Evitando que se ejecute cualquier cosa de esté código.
    #createDB()
    #createTable()
    #insertRow("Ibai",700000,2500)
    #insertRow("AlexElCapo", 800000,10000)
    #readData()
    # streamers = [
    #     ("El Xokas", 1000000, 9500), # Cada tupla corresponde a una fila
    #     ("Cuqita", 5400000, 23330),  # Las filas de una base de datos en sqlite3 se devuelve en una lista
    #     ("Rubius", 14500000, 95400)
    # ]
    # insertRows(streamers)
    #readOrder("name")
    #search()
    #buscar_similar("") Esto lo metí yo
    #updateFields()
    deleteRow()