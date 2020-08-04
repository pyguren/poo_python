tupla_a = 'hola', 10, 'mundo', 20, 'desde', 40, 'python'
tupla_b = ('hola', 10, 'mundo', 20, 'desde', 40, 'python')

print(tupla_a)
print(tupla_b)
print(tupla_a[0])
print(tupla_a.count('mundo'))
print(tupla_a.count('python'))
print(tupla_a.count('mundo'))
print('mund' in tupla_a)

i = 0
total_tupla_a = len(tupla_a)

while(i < total_tupla_a):
    print(tupla_a[i])
    i += 1
