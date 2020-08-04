# crear 2 clases
# 1 clase base llamada pc
# 2 clase llamada notebook
# 3 notebook hereda de pc
# 4 la clase pc contiene (cpu, ram, disco)
# 5 notebook contiene (peso, pulgadas)

class Padre:

    def __init__(self, nombre_padre):
        self.nombre_padre = nombre_padre

    def get_nombre_padre(self):
        return self.nombre_padre


class Hijo(Padre):

    lugar_de_nacimiento = 'latino america'

    def __init__(self, nombre_padre, nombre_hijo):
        Padre.__init__(self, nombre_padre)
        self.nombre_hijo = nombre_hijo

    def get_nacionalidad_padre(self):
        return self.lugar_de_nacimiento

    def cambiar_nacionalidad(self, lugar):
        self.lugar_de_nacimiento = lugar

    def get_nombre_hijo(self):
        return self.nombre_hijo


h = Hijo('nombre padre bar', 'nombre hijo foo')
print(h.get_nombre_padre())
print(h.get_nombre_hijo())
print(h.get_nacionalidad_padre())
h.cambiar_nacionalidad('brasil')
print(h.get_nacionalidad_padre())


class Pc:

    def __init__(self, cpu, ram, disco):
        self.cpu = cpu
        self.ram = ram
        self.disco = disco

    def get_cpu(self):
        return self.cpu

    def get_ram(self):
        return self.ram

    def get_disco(self):
        return self.disco


class Notebook(Pc):

    def __init__(self, cpu, ram, disco, peso, pulgadas):
        Pc.__init__(self, cpu, ram, disco)
        self.peso = peso
        self.pulgadas = pulgadas

    def get_peso(self):
        return self.peso

    def get_pulgadas(self):
        return self.pulgadas


notebook = Notebook('pc_cpu', 'pc_ram', 'pc_disco', 'not_peso', 'not_pulgadas')
print(notebook.get_cpu())
print(notebook.get_ram())
print(notebook.get_disco())
print(notebook.get_peso())
print(notebook.get_pulgadas())
