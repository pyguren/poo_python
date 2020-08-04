# reglas

# - def nombre(): asi se define
# usar formato de netscape: nombre_de_la_persona

# def nombre():
#     print('juan')

# nombre()

# ////////////////////////////////////////////////////////////
# /////////////////imprimir contenido de array///////////////

# def mostrar_perfiles():
#     perfiles = ['juan', 'dan', 'max', 'axel', 'nico']
#     for perfil in perfiles:
#         print(perfil)
#         print('-'*20)


# mostrar_perfiles()

# ////////////////////////////////////////////////////////////
# /////////////funcion con operacion matematica simple///////

# def calcular(tipo_calculo, numero1, numero2):
#     if tipo_calculo == 'sumar':
#         print(numero1 + numero2)

#     if tipo_calculo == 'restar':


# def sumar(numero1, numero2):
#     print(numero1 + numero2)
# sumar(10,20)

# /////////////////////////////////////////////////////////////
# ///////////filtrado en base a edad//////////////////////////


def mayor_de_edad(edad):
    if edad >= 21:
        print('eres mayor de edad')
    else:
        print('eres menor de edad')


edad = 20

mayor_de_edad(20)

# ////////////////////////////////////////////////////////////
# ////////////////imprimir elementos de array////////////////


def listar_valores(lista):
    i = 0
    while(i < len(lista)):
        print(lista[i])
        i = i+1


lista = ['foo', 'bar', 'baz']

listar_valores(lista)

# ////////////////////////////////////////////////////////////
# ///////////////////imprimir pais de residencia/////////////


def donde_estoy(pais):

    print(f'ESTAS EN {pais}')


pais = 'chile'

donde_estoy('chile')

# ///////////////////////////////////////////////////////////////////
# /////cuando se me olvida asignarle un valor puedo ingresarlo//////
# /////despues abajo///////////////////////////////////////////////


def foo(v='se me olvido color un valor'):
    print('soy foo')
    print(v)


foo(1000)

# ///////////////////////////////////////////////////////////////////////
# ///////////////////aqui probamos como print (muestra en pantalla)/////
# ////////y return no, solo asigna el valor////////////////////////////


def foo(e):
    print(e)


def bar(e):
    return e


# foo('valor externo para foo')

# bar('valor externo para bar')

salida_foo = foo('valor externo para foo')
print(salida_foo)

salida_bar = bar('valor externo para bar')
print(salida_bar)


# ///////////////////////////////////////////////////////////////////
# /////validacion de la clave edad//////////////////////////////////
# /////////////////////////////////////////////////////////////////

def validar_perfil(perfil):
    mayor_edad = False
    msg = None
    for clave in perfil:
        if clave == 'edad':
            if perfil['edad'] >= 18:
                mayor_edad = True
                msg = 'es mayor de edad'
            else:
                msg = 'es menor de edad'
        else:
            msg = 'la clave edad no existe'
    return msg, mayor_edad


perfil = {
    "nombre": 'dan',
    "edad": 2
}
m, s = validar_perfil(perfil)
print(f'{m} {s}')
