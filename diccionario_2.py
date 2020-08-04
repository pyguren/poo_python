# https://pypi.org/project/colorama/
# pip install colorama

import os
from colorama import init
init(autoreset=True)

lista_personas = [
    {'dni': 100, 'nombre': 'juan', 'correo': 'juan@gmail'},
    {'dni': 101, 'nombre': 'frank', 'correo': 'grank@gmail'},
    {'dni': 102, 'nombre': 'gian', 'correo': 'gian@gmail'}
]

colores = {
    'rojo': '\033[31m',
    'azul': '\033[34m',
    'verde': '\033[32m',
    'fondo_azul': '\033[44m'
}

OPCIONES = ('1', '2', '3', '4')

top_mensaje = 'control de personal'.upper()
mensaje = '1) para leer - 2) para agregar - 3)para eliminar - 4) salir \n'.upper(
)
dash = '='*50
PRESIONAR_PARA_CONTINUAR = ':: presione cualquier tecla para continuar'


while(True):
    print(dash)
    print('{} {}'.format(colores['fondo_azul'], top_mensaje))
    print('{} {}'.format(colores['azul'], mensaje))
    r = input()

    # leer
    if r == OPCIONES[0]:
        for key, persona in enumerate(lista_personas):
            print(
                '{} - {} - {}'.format(persona['dni'], persona['nombre'], persona['correo']))
        print('{} {}'.format(colores['verde'], PRESIONAR_PARA_CONTINUAR))
        input()
        os.system('cls')

    # agregar
    if r == OPCIONES[1]:
        persona = dict()
        dni = input('ingresar dni \n'.upper())
        nombre = input('ingresar nombre \n'.upper())
        correo = input('ingresar correo \n'.upper())

        persona['dni'] = dni
        persona['nombre'] = nombre
        persona['correo'] = correo
        lista_personas.append(persona)
        print('registro guardado...')

        print(':: presione cualquier tecla para continuar')
        input()
        os.system('cls')

    # eliminar
    if r == OPCIONES[2]:
        dni = input('ingresar el dni \n')
        for k, v in enumerate(lista_personas):
            if lista_personas[k]['dni'] == int(dni):
                lista_personas.pop(k)
                print(f'este {dni} fue eliminado...')
        print(':: presione cualquier tecla para continuar')
        input()
        os.system('cls')

    # salida
    if r == OPCIONES[3]:
        break

print('el sistema se ha cerrado'.upper())
