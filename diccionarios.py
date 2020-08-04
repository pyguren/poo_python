# listas = ['elem_1', 'elem_2', 'elem_3'] //inician en 0 el indice
# tuplas = ('elem_1', 'elem_2', 'elem_3') //inician en 0 el indice

# {
# 'clave':valor
# }

# perfil = {
#     'nombre': 'juan',
#     'correo': 'juan@gmail.com',
#     'edad': 35,
#     'sexo': 'm',
#     'estado_civil': 'soltero'
# }
# print(perfil)

# si se repite una clave solo mostrará el valor de la ultima clave, es decir no muestra claves repetidas
# en caso de querer mostrar varios correos (por ejemplo) tendria que con una sola clave abrir una lista (array) e introducirlos todos adentro

# correosFacebook = {
#     'correo_1': 'jc@gmail.com',
#     'correo_2': 'jose@gmail.com',
#     'correo_3': 'jcar@gmail.com',
#     'correo_4': 'jpablo@gmail.com',
#     'correo_5': 'juan@gmail.com',
#     'correo_6': 'john@gmail.com',
#     'correo_7': 'julio@gmail.com',
#     'correo_8': 'jonas@gmail.com'
# }
# totalCorreos = len(correosFacebook)
# print(f' total de correos {totalCorreos}')
# print(correosFacebook.keys())
# print(correosFacebook.values())
# print(correosFacebook['correo_4'])


# correosFacebook['correo_9'] = 'kim@gmail.com'
# aqui se esta agregando una clave y valor a la lista
# correos = correosFacebook.values()
# for correo in correos:
#     print(correo)
# for correo in correos:
#     if correo == 'dan@gmail.com':
#         print(f' existe: {correo}')
#     else:
#         print(None)


# clase diccionario 20-06-2020


lista = [
    {'dni': 100, 'nombre': 'juan', 'correo': 'juan@gmail.com'},
    {'dni': 101, 'nombre': 'frank', 'correo': 'carlos@gmail.com'},
    {'dni': 102, 'nombre': 'gian', 'correo': 'pedro@gmail.com'},
]
print(lista)
print('='*50)


# lista.pop(2)

# persona = {
#     'dni': 103,
#     'nombre': 'max',
#     'correo': 'max@gmail.com',
#     'ciudad': 'tokyo'
# }

# persona.pop('ciudad')
# lista.append('persona')

for k, v in enumerate(lista):
    if lista[k]['nombre'] == 'juan':
        print(f'el esta en la posicion {k+1}')
        lista.pop(0)
print(lista)

#    print(lista[k]['nombre'])
