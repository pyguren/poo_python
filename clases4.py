# class A:

#     def __init__(self, nombre_a):
#         self.nombre_a = nombre_a

#     def get_nombre_a(self):
#         return self.nombre_a


# class B:

#     def __init__(self, nombre_b):
#         self.nombre_b = nombre_b

#     def get_nombre_b(self):
#         return self.nombre_b


# class C(A, B):
#     def __init__(self, nombre_a, nombre_b, nombre_c):
#         A.__init__(self, nombre_a)
#         B.__init__(self, nombre_b)
#         self.nombre_c = nombre_c

#     def get_todos(self):
#         nom_a = self.get_nombre_a()
#         nom_b = self.nombre_b
#         nom_c = self.nombre_c
#         print('{} {} {}'.format(nom_a, nom_b, nom_c))

#     def get_nombre_c(self):
#         return self.nombre_c


# claseC = C('soy a', 'soy b', 'soy c')
# print(claseC.get_nombre_a())
# print(claseC.get_nombre_b())
# print(claseC.get_nombre_c())
# claseC.get_todos()


# ////////////////////////////ejersicio 1///////////////////////
# crear 3 clases una llamada TipoAvion, Motor, Avion
# en la clase TipoAvion especificar el tipo del avion
# teniendo en cuenta tres clases de aviones ['transporte', 'turismo', 'guerra']
# En la clase Motor tener un diccionario con 2 tipos de motores {motor jet, motor subsonico}
# en la clase Avion requiere el nombre del avion por init y con las bases armar un avion


# class TipoAvion:

#     tipos_aviones = ['transporte', 'turismo', 'militar']

#     def getTipoAvion(self, nombre):
#         for tipo in tipos_aviones:
#             if tipo == nombre:
#                r = nombre
#         return nombre

# class Motores:

#     tipos_motores  = {
#         "motor_jet":"motor jet",
#         "motor_subsonico":"motor subsonico"
#     }

#    def getTipoMotor(self, nombre):
#        for tipo in tipos_motores:
#            if tipo == nombre:
#               r = nombre
#         return r

# class Avion(TipoAvion, Motores):

#     def __init__(self, nombre):
#         TipoAvion.__init__(self)
#         self.nombre = nombre


# a = Avion('f-18')
# avion = a.getTipoAvion('militar')
# motor = a.getTipoMotor('motor_jet')
# print('{} - {}'.format(avion, motor))

# #1
# avionMilitar = Avion('f35', 'guerra', 'motor jet')
# avionMilitar.get_nombreAvion()
# avionMilitar.get_tipo()
# avionMilitar.get_motor()

# #2
# avionMilitar = Avion('f35')
# avionMilitar.get_tipo_avion('guerra')
# avionMilitar.get_tipo_motor('motor jet')


class Persona:

    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    def public_nombre(self):
        return self.__get_nombre()

    def __get_nombre(self):
        return self.__nombre

    def __get_correo(self):
        return self.__correo

    def __set_nombre(self, nombre):
        self.__nombre = nombre

    def __set_correo(self, correo):
        self.__correo = correo

    nombre = property(
        fget=__get_nombre,
        fset=__set_nombre
    )
    correo = property(
        fget=__get_correo,
        fset=__set_correo
    )


p = Persona('jc', 'jc@gmail.com')
print(p.nombre)
print(p.public_nombre())
print(p.correo)
p.nombre = 'foo'
p.correo = 'foo@domain.com'
print(p.nombre)
print(p.correo)

# print(p.get_nombre())
# p.set_nombre('foo')
# print(p.get_nombre())
