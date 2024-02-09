import sqlite3

#conn = sqlite3.connect(':memory:') Si queremos trabajar con algo en memoria

def initial():
    # Connect to database and create if doesn't exist
    conn = sqlite3.connect('customers.db')
    # Crear un cursor
    c = conn.cursor()
    # Crear una tabla
    c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

    # Datatypes:
    # NULL
    # INTEGER
    # REAL
    # TEXT
    # BLOB

    # Hace el commit
    conn.commit()

    # Close our connection

    conn.close()


def insertrows():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
    conn.commit()
    conn.close()

def insertMultirowsByParam(name,lname,email):

    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    many_customers = [(str(name),str(lname),str(email))]
    c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
    conn.commit()
    conn.close()

# Esta es la primera de mis funciones en este caso, use scripts viejos
# De manera de aprovechar el kwargs
def insertMultiRowByKey(*args,**kwargs):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    if "name" in kwargs and "lname" in kwargs and "email" in kwargs:
        many_customers = [(kwargs["name"],kwargs["lname"],kwargs["email"])]
        c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
        conn.commit()
    conn.close()

# Estas es una de mis funciones (Hecha por Chat GPT)
def insertMultiRowByDic(*args, **kwargs):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    
    if args:
        many_customers = [(customer["name"], customer["lname"], customer["email"]) for customer in args]
        c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) # El truco es executemany para ingresar varios
        conn.commit()

    conn.close()

# Aca lo modifique un poquito
    
def QueryFetch(*args,**kwargs):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    if "one" in kwargs:
        print(c.fetchone()[kwargs["one"]]) # hace la request de una fila, como es un tuple también puedo acceder a una posición
    elif "many" in kwargs:
        print(c.fetchmany(kwargs["many"])) # hace la request de 3 filas
    else:
        item = c.fetchall()

        for items in item:
            print(items)
    
    conn.commit()
    conn.close()

def PrimaryKey():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    item = c.fetchall()
    for items in item:
            print(items)
    conn.commit()
    conn.close()

def Filter(lname):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM customers WHERE last_name LIKE '%{lname}%'")
    
    item = c.fetchall()
    
    for items in item:
            print(items)
    conn.commit()
    conn.close()

def Update():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute("""UPDATE customers SET first_name = 'Suar'
              WHERE rowid = 1
              """)

    conn.commit()

    c.execute(f"SELECT * FROM customers")
    
    item = c.fetchall()
    
    for items in item:
            print(items)
    conn.commit()
    conn.close()

def Delete():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute("""DELETE from customers WHERE rowid = 6
              """)

    conn.commit()

    c.execute(f"SELECT rowid,* FROM customers")
    
    item = c.fetchall()
    
    for items in item:
            print(items)
    conn.commit()
    conn.close()
def OrderBY():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    # Query por Order

    c.execute(f"SELECT rowid,* FROM customers ORDER BY rowid DESC") # Ya recordamos este comando de SQL
    
    item = c.fetchall()
    
    for items in item:
            print(items)
    conn.commit()
    conn.close()
def conditionals():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    # Query por Order

    c.execute(f"SELECT rowid,* FROM customers WHERE last_name LIKE 'Vi%' OR first_name LIKE '%Jo%'") # Ya recordamos este comando de SQL
    # Tenemos AND of OR no mucha ciencia
    item = c.fetchall()
    
    for items in item:
            print(items)
    conn.commit()
    conn.close()


def limit():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    # Query por Order

    c.execute(f"SELECT rowid,* FROM customers LIMIT 2") 
    # LIMIT Y el número para que no devuelva tantos resultados
    item = c.fetchall()
    
    for items in item:
            print(items)
    conn.commit()
    conn.close()

def droptable(tablename):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()

    c.execute(f"DROP TABLE {tablename}") 
    # Acá se mata todo.
    conn.commit()
    conn.close()

     

if __name__ == "__main__":
    #initial()
    #insertrows()
    #insertMultiRowByKey(name="Jose", lname="Vivar", email="jvivar@outlook.com")
    # dict_clientes = [
    #     {"name": "Joseu", "lname": "Vcr", "email": "jvcr@outlook.com"},
    #     {"name": "Maria", "lname": "Lopez", "email": "mlopez@gmail.com"},
    #     {"name": "Juan", "lname": "Perez", "email": "jperez@yahoo.com"}
    # ]
    # insertMultiRowByDic(*dict_clientes)
    #QueryFetch()
    #PrimaryKey()
    #Filter("vcr")
    #Delete()
    #OrderBY()
    #conditionals()
    #limit()
    pass