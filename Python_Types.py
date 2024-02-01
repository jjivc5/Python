lista_nombres = ['John', 'James', 'Mandy']
print(lista_nombres[1])
lista_nombres[2] = 'Robert'

# En una lista en python podemos acceder tanto como a sus valores
# Y modificarlos

print(lista_nombres)

lista_par = [lista_nombres[i] for i in range(0, len(lista_nombres),2)]

#range(start,stop,step)


tupla_lista = ['John', 'James', 'Mandy']

print(tupla_lista[2])

# en caso de queerer modificar 
# tupla_lista[0] = 'Algo'
# recibiriamos error en esto.
# los tuples son más efectivos en temas de memoria
# es una constant list en python
# es más segura de nos er modificada

set_nombres = {'John', 'James', 'Mandy'}

# En una estructura tipo set, una colección de datos se cumple que:

# Elementos únicos no se almacenan valores iguales

# No ordenados no se pueden llamar por índice

# Mutables se pueden agregar o quitar elmeentos después de su creación

set_nombres.add('Alexihno')



diccionario_nombres = {
    'CEO' : 'Ruphert',
    'STO' : 'William',
    'Lead Developer' : 'Mandy'
}

print(diccionario_nombres['STO'])