import sqlite3 as sql

class Database:
    def __init__(self):
        self.con = sql.connect("dictionary.db")
        self.c = self.con.cursor()
    
    def commit(self):
        self.con.commit()
    
    def end_con(self):
        self.con.close()

    def createTable(self,table_name,*columns):

        self.c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        existing_table = self.c.fetchone()

        if existing_table:
            print(f"La tabla '{table_name}' ya existe.")
            return  # Salir de la función si la tabla ya existe

        columns_definition = ', '.join(columns)

        self.c.execute(f"""CREATE TABLE {table_name} (
                       {columns_definition}
        )""")
        #db_object.createTable('customers', 'first_name TEXT', 'last_name TEXT', 'email TEXT')


    def queryAllDB(self, table):
        self.c.execute(f"SELECT in_english,traduccion,ejemplo FROM {table}")
        return self.c.fetchall()
    
    def query_by_english(self,word):
        
        self.c.execute(f"SELECT in_english,traduccion,ejemplo FROM diccionario WHERE in_english LIKE '%{word}%'")
        result = self.c.fetchall()

        for row in result:
            english_word = row[0]
            self.c.execute("UPDATE diccionario SET contador = contador + 1 WHERE in_english = ?", (english_word,))
            self.con.commit()

        return result
    
    def query_by_spanish(self,word):
        self.c.execute(f"SELECT in_english,traduccion,ejemplo FROM diccionario WHERE traduccion LIKE '%{word}%'")
        result = self.c.fetchall()

        for row in result:
            spanish_word = row[1]
            self.c.execute("UPDATE diccionario SET contador = contador + 1 WHERE traduccion = ?", (spanish_word,))
            self.con.commit()

        return result
    
    def insertWord(self,eng_w,trad,sentence):
        new_word = [(str(eng_w),str(trad),str(sentence))]
        self.c.executemany("INSERT INTO diccionario (in_english, traduccion, ejemplo) VALUES (?,?,?)", new_word)

    # Ejecutar una única vez para agregar el contador con la salvedad (que solo incrementa en busqueda individual)
    def uniqueCreateCounter(self):
        self.c.execute("ALTER TABLE diccionario ADD COLUMN contador INTEGER DEFAULT 0")

    def get10moresearch(self):
        self.c.execute("SELECT in_english,traduccion,ejemplo FROM diccionario ORDER BY contador DESC LIMIT 10")
        top_words = self.c.fetchall()
        return top_words


