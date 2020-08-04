# reglas

# - def nombre(): asi se define
# usar formato de netscape: nombre_de_la_persona

# ej:

def nombre():
    print('juan')
    nombre()


def mostrar_perfiles():
    perfiles = ['juan', 'dan', 'max', 'axel', 'nico']
    for perfil in perfiles:
        print(perfil)
        print('-'*20)

    mostrar_perfiles()
