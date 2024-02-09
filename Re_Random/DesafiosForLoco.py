def printer(func):
    def wrapper(*args,**kwargs):
        print(f"El resultado de la operación es : {func(*args,**kwargs)}")
    return wrapper

@printer
def cuadradoListas(lista):
    resultado = [iterador**2 for iterador in lista]
    return resultado


cuadradoListas([1,2,3,4,5])

@printer
def creaTuplas(eldic):
        new_dic = {clave:valor for clave,valor in eldic.items() if valor>18}
        return new_dic

dicExample = {"Juan": 20, "María": 15, "Pedro": 25, "Laura": 18}
creaTuplas(dicExample)