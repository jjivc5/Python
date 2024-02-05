# Así lo hice yo
def OperarConPares(func):
    def interna(*args,**kwargs):
        soloPares = list(filter(lambda num: num%2 == 0, args))
        resultado = func(*soloPares, **kwargs)
        
        if kwargs != {}:
            if resultado > kwargs['max']:
                print(f'El resultado obtenido es {kwargs["max"]}')
            else:
                print(f'El resultado obtenido es {resultado}')
        else:
            print(f'El resultado obtenido es {resultado}')

        return resultado
    return interna


@OperarConPares
def multiplicar(*args, **kwargs):
    acc = 1
    for num in args:
        acc *= num
    return acc


multiplicar(4,6,max=50)

# Así me pego el baile el dumas
def OperarConPares1(func):

    def interna(*args,**kwargs):
        soloPares = list(filter(lambda num: num%2 == 0, args))
        resultado = func(*soloPares, **kwargs)
        print(f'El resultado obtenido es {resultado}')
        return resultado
    
    return interna


@OperarConPares1
def multiplicar1(*args, **kwargs):
    acc = 1
    
    for num in args:
        acc *= num
    
    if "max" in kwargs.keys():
        return min(acc,kwargs["max"])
    
    return acc

multiplicar1(4,8,2,max=63)