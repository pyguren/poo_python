nombre = 'Esteban'
apellido = 'Sologuren'
edad = 41
hola = 20
formato_plus = 'texto_triple_quotes' + 'nombre' + 'FLAG_SPACE' + 'apellido'
FLAG_SPACE = ' '
texto_triple_quotes = """ tus datos son necesarios
             para realizar un buen
            ejemplo de cadenas """

formato_plus_pure = nombre + ' ' + apellido
formato_plus_ext = nombre + FLAG_SPACE + apellido
formato_plus_ext = 'tus datos son: '+nombre + FLAG_SPACE + apellido
formato_param_1 = 'tus datos son: {} {} {} '.format(nombre, FLAG_SPACE, apellido) 
formato_param_2 = 'tus datos son: {} {}' .format (nombre, apellido)
formato_param_3 = 'tus datos son 0 1: {0} {1}'.format (nombre, apellido)
formato_parm_4 = 'tus datos son 1 1: {1} {1}'.format (nombre, apellido)
formato_param_5 = 'tus datos son 1 0: {1} {0}'.format (nombre, apellido)
formato_param_6 = '{} ese es mi nombre y este es mi apellido {}'.format (nombre, apellido)

template_string = f'tus datos son: {nombre} {apellido}'

upper_text = f'upper: mi npombre es : {nombre}'.upper()
lower_text = f'lower: MI NOMBRE ES : {nombre}'.lower()
capital_text = f'capitalize : mI nOmbrE eS: {nombre}'.capitalize()
title_text = f'title: mI nOmbrE eS {nombre}'.title()

print(edad)
print(edad+2)
print(edad +int('4'))
print(str (edad) +'2')
print(hola*5)
print(2*5)
print('2'*5)
print(5 + 55)
print('5' + '55')
print('hola'*5)
print(edad+int('4'))
print(str(edad)+'2')
print('mis datos'+str(edad))
print(formato_plus_pure)
print(formato_plus)
print(formato_plus_ext)
print(formato_param_1)
print(formato_param_2)
print(template_string)
print(texto_triple_quotes)
print(upper_text)
print(lower_text)
print(capital_text)
print(title_text)



#upper
#lower
#capitalize
