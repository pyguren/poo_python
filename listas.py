# 12/06/2020

# listas = []
# las listas son de tipo (clave, indice) / valor

# nombres = ['aldo', 'anyolita', 'cristofer', 'cesar', 'esteban']

# sirve para insertar un elemento al final de la lista
# nombres.append('hillary')
# nombres.append('juan')
# nombres.append('leopoldo')
# .....................................................................

# sirve para insertar un elemento en un lugar especifico
# nombres.insert(1, 'mishel')
# nombres.insert(7, 'omar')
# ......................................................................

# print(nombres)

# nombres.extend(nombres)  # para agregar en forma masiva
# nombres.pop(2)  # se usa para eliminar un elemento de la lista

# print(nombres)

# .......................................................................

# nombres.remove('juan')  # sirve para eliminar un elemento especifico

# .......................................................................

# nombres.pop()  # sirve para eliminar el ultimo de la lista, parentesis vacio

# .......................................................................

# total_nombres = len(nombres)
# print(nombres)

# ..........................................................................

# clase listas 2
# dia 13/06/2020

# excercise 1

lista_n = [10, 'hola', 20, 'mundo', 30, 'desde', 40]
print(lista_n)
i = 0
total_lista = len(lista_n)
while(i < total_lista):
    if i % 2 != 0:
        print(lista_n[i])
    i += 1
# ......................................................................

# excercise 2

lista_n = [10, 'hola', 20, 'mundo', 30, 'desde', 40]
print(lista_n)
i = 0
total_lista = len(lista_n)
while(i < total_lista):
    if i % 2 == 0:
        print(lista_n[i])
    i += 1

# ........................................................

# excercise 3

lista_n = [10, 'hola', 20, 'mundo', 30, 'desde', 40]
print(lista_n)

for i in range(total_lista):
    print(lista_n[i])

# ........................................................

# excercise 4

    lista_n = [10, 'hola', 20, 'mundo', 30, 'desde', 40]
print(lista_n)

for i in range(total_lista):
    print(f'postion: {i} - valor: {lista_n[i]}')

# ........................................................

# excercise 5

    lista_n = [10, 'hola', 20, 'mundo', 30, 'desde', 40]
print(lista_n)

for i, valor in enumerate(lista_n):
    print(f'postion: {i} - valor: {valor}')

    # ........................................................

# excercise 5

    lista_a = [10, 'hola', 20, 'mundo', 30, 'desde', 40, 'python']
    lista_b = [50, 'somos', 60, 'buenos', 70, 'programadores', 80, 'django']


for valor_a, valor_b in zip(lista_a, lista_b):
    print(f'valor_a: {valor_a}')
    print(f'valor_b: {valor_b}')
    print('-----------')

# ........................................................

# excercise 6

    lista_a = [10, 'hola', 20, 'mundo', 30, 'desde', 40, 'python']


for i in range(len(lista_a)):
    if i % 2 == 0:
        print(lista_a[i])
