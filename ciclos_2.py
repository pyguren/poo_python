# for

for i in range(0, 10):
    print(i)

inicio = 0
limite = 10
for i in range(inicio, limite):
    print(i)

inicio = 0
limite = 10
for i in range(inicio, limite):
    print(f'itera en {i}')

inicio = 0
limite = 10
for i in range(inicio, limite, 2):
    print(f'itera en {i}')

inicio = 10
limite = 0
print('0...9')
for i in range(inicio, limite, -1):
    print(f'itera en {i}')

inicio = 10
limite = 0
salto = -1
print('.....')
for i in range(inicio, limite, salto):
    print(f'{i} itera en {i+1}')


inicio = 10
limite = 0
salto = -1
print('.....')
for i in range(inicio, limite, salto):
    if(i % 2 == 0):
        print(f'PAR {i}')
    else:
        print(f'IMPAR {i}')

inicio = 1
limite = 11

print('.....')
for i in range(inicio, limite):
    if(i % 2 == 0):
        print(f'PAR {i}')
    else:
        print(f'IMPAR {i}')


nombre = "Esteban Sologuren"
# longitud = len
print(f"el nombre a recorrer es: {nombre}")
for i in nombre:
    print(i)
