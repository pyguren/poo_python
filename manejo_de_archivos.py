import shutil
import os
f = open('archivo.txt', 'w')
f.write('soy un mensaje secreto simple')
f.write('\n')
f.write('continuacion de mensaje secreto')
f.write('\n')
f.write('final de mensaje secreto')
f.close()

# ////////////////para leer el archivo.txt en consola////////////////

f = open('archivo.txt', 'r')
print(f.read())
f.close()

# /////////////modificar y crear txt, borrar y crear/////////////////

existe = os.path.exists('prueba')
path_dir_nmame = 'prueba'

if existe:
    # os.rmdir(path_dir_name)
    shutil.rmtree('prueba')
    print('existe')
else:
    os.mkdir('prueba')
    os.mkdir('prueba/interno')
    print('no existe')


# 1 path / ruta
# 2 parametros w, r
# open(path, type)

# os
# open - w / r
# mkdir - make directory (crear el archivo)
# rmdir - este cuando esta vacio (eliminar el archivo)
# rename - cambiar el nombre
# path.exists - verificar la ruta
# shutil -> rmtree - no esta vacio
# shutil -> copy / copyfile - clonar el archivo


# /////////////ejercisio 1////////////////////////////////////

# crear una funcion que me permita mostrar una multiplicacion de 5 numeros
# y enviar el resultado dentro de una archivo llamado operaciones.txt.


def foo():
    def r(x): return x * 10 * 3 * 8 * 2 * 1
    return r


v = foo()(10)
os.rmdir


os.mkdir('operaciones.txt')
print('existe')
existe = os.path.exists('operaciones.txt')
print(v)

f = open('operaciones.txt')
print(f.read())
f.close()


def multiplicacion(n1, n2, n3, n4, n5): return n1*n2*n3*n4*n5


resultado = multiplicacion(1, 2, 3, 4, 5)

existe = os.path.exists('prueba/resultados.txt')

if existe:

    f = open('prueba/resultados.txt', 'w')
    f.write(f'\n{resultado}')
    f.close()

else:

    os.mkdir('prueba')
    f = open('prueba/resultados.txt', 'w')

    f.write(f'\n {resultado}')
    f.close()
    print('no existe, lo creo')

    # /////////////ejercisio 2////////////////////////////////////

    import os
    import shutil

    paths = {
        'operaciones': 'operaciones.txt',
        'dir_prueba_dir_interno': 'prueba/interno'

        existeOperaciones = os.path.exists(path['operaciones'])
        copiar_operaciones = lambda: shutil.copy(
            'operaciones.txt', paths['dir_prueba_dir_interno'])

        ifexisteOperaciones:
        copiar_operaciones()
        else:
            f= open(paths['operaciones'], 'w')
            f.write('contenido base')
            f.close()
            copiar_operaciones()
    }
