def saludo_adicional(func):
    def wrapper(*args, **kwargs):
        mensaje_original = func(*args, **kwargs)
        mensaje_modificado = f"{mensaje_original} ¡Bienvenido! {args}"
        return mensaje_modificado
    return wrapper

@saludo_adicional
def saludar(nombre,*args, **kwargs):
    return f"Hola, {nombre}!"

# Llamas a la función decorada
resultado = saludar("Juan","Pepe","Pedro", Pepe = "Papotero")

print(resultado)