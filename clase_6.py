print('-'*10)
valor = input('\n ingresa algo: \n\n'.upper())
print(valor *10)

MSG = 'salida: '.upper()
TYPE = 'de tipo: 'upper()
SUM_MATH = 'la suma_concat es: ' .upper()
SUMA_CONCAT = 'la suma_concat es: ' .upper()
DASH = '-'*10

print(DASH)
valor = input('\n ingresa algo: \n\n' .upper())

print('\n' ,MSG, valor)
print('\n' ,TYPE,type(valor))

print(SUM_MATH, int(valor) + 10)
print(SUM_CONCAT, (valor) + str(10))
