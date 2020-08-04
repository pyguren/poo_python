# Programación orientada a objetos bajo clases

# la clase va a hacer un esquema
# la clase va a hacer un diseño
# la clase es un plano de posibles funciones - acciones

class Persona:

    def saluda(self, saludo):
        print(f'hola {saludo}')


juan = Persona()
carmen = Persona()
Hillary = Persona()
Omar = Persona()
Juanjo = Persona()
Esteban = Persona()

juan.saluda('son juan')
carmen.saluda('soy carmen')
Hillary.saluda('soy Hillary')
Omar.saluda('soy Omar')
Juanjo.saluda('soy Juanjo')
Esteban.saluda('soy Esteban')


class Persona:

    def __init__(self, nombre, correo, dni):
        self.nombre = nombre
        self.correo = correo
        self.dni = dni

    def saluda(self):
        print(f'hola soy {self.nombre}')

    def despide(self):
        print(f'adios')

    def info(self):
        print(
            f'nombre: {self.nombre} - correo: {self.correo} - dni: {self.dni}')


print('bienvenido al consultorio')

nombre = input('dime tú nombre \n')
correo = input('dime tú correo \n')
dni = input('dime tú dni \n')

usuario = Persona(nombre, correo, dni)
usuario.info()

# ////////////////////////////codigo para un chatbot//////////////////////////


class Telefono:

    def__init__(self, nombre, modelo, marca, color, peso)

    class ChatBot:

    def__init__(self, alias, saludo, mensaje):
        self.alias = alias
        self.saludo = saludo
        self.mensaje = mensaje

    def mensaje_de_bienvenida(self):
        print(f' hola soy {self.alias} {self.saludo} {self.mensaje}')

    def opciones_del_chat(self):
        print("""
         1) atención al cliente
         2) ventas
         3) faq
         4) ninguna de las anteriores
        """)

    def mensaje_base_opciones(self):
        print(f'gracias por seleccionar, en breve será atendido')

    def opcion_seleccionada(self, opcion):
        if opcion == '1':
            print("""
           1) Entidad Buenos Aires
           2) Entidad Colombia
           3) Entidad Chile
           4) Entidad Venezuela
           """)
        if opcion == '2':
            print("""
           1) Entidad Buenos Aires
           2) Entidad Colombia
           3) Entidad Chile
           4) Entidad Venezuela
           """)
        if opcion == '3':
            print("""
            1_ solo ventas al mayor y no al detal
            2_ solo pagos en USD
            3_ no se acepta efectivo
            4_ se recibe los canales de pagos tales como: (paypal / zelle / transferencia bancaria"""
                  )
        if opcion == '4':
            print("""
             en breve será atendido por otro operador
           """)


def publicidad():
    print('='*30)
    print('='*30)
    print('gracias por elegirnos dentro del mercado de ventas al mayor de hamburguesas - fabrica wendy')
    print('='*30)
    print('='*30)


carga_inicial_chatbot = {
    "alias": ['hillary', 'maria', 'sandra'],
    "mensaje_dia": 'buenos día, bienvenido a nuestra plataforma',
    "mensaje_tarde": 'buenas tardes, bienvenido a nuestra plataforma',
    "mensaje_noche": 'buenas noches, bienvenido a nuestra plataforma',
    "mensaje_opciones": 'abajo tienes varias opciones elige una de ellas'
}

cb = ChatBot(
    carga_inicial_chatbot['alias'][0],
    carga_inicial_chatbot['mensaje_noche'],
    carga_inicial_chatbot['mensaje_opciones']
)

cb.mensaje_de_bienvenida()
cb.opciones_del_chat()
opcion = input('\n')
cb.opcion_seleccionada(opcion)
publicidad()

# ////////////////////////////continuación clases//////////////////////////


class Alumno:

    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase

    def get_clase(self):
        return self.clase


a1 = Alumno('anyolita', 'python')
a2 = Alumno('esteban', 'js')
a3 = Alumno('hillary', 'go')
a4 = Alumno('juanjo', 'c#')
a5 = Alumno('maria', 'scala')

lista = []
lista.append(a1)
lista.append(a2)
lista.append(a3)
lista.append(a4)
lista.append(a5)

for alumno in lista:
    if alumno.nombre == 'esteban':
        print(alumno.nombre)
        print(alumno.get_clase())
