# funciones lambda


# def foo(x): return x + 1000


# def foo(n1, n2): return n1 + n2


# v = foo(10)
# print(v)

# /////////////////////////////////////////////////

lista = [100, 200, 300, 400, 500]

v = list(filter(lambda x: x != 300, lista))
v = list(map(lambda x: x + 1, lista))

print(v)

# /////////////////////////////////////////////////


def foo():
    def r(x): return x + 1
    return r


v = foo()(10)
print(v)

# /////////////////////////////////////////////////


# def fn(n): return n


# def fn(): return lambda: print(1)


# print(fn(1))
# print()()

# /////////////////////////////////////////////////
