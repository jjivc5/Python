
def default(*args, **kwargs):

    
    if args:
        many_customers = [(customer["name"], customer["lname"], customer["email"]) for customer in args]
        print(many_customers)


dict_clientes = [
        {"name": "Joseu", "lname": "Vcr", "email": "jvcr@outlook.com"},
        {"name": "Maria", "lname": "Lopez", "email": "mlopez@gmail.com"},
        {"name": "Juan", "lname": "Perez", "email": "jperez@yahoo.com"}
    ]

print(*dict_clientes)

default(*dict_clientes)
