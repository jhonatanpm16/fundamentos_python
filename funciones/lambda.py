x = lambda a: a + 10
print(x(5))


x = lambda a,b: a + b
print(x(2,3)) # 5

def mi_funcion(n):
    return lambda a: a * n

duplicador = mi_funcion(2)
triplicador= mi_funcion(3)

print(duplicador(5))
print(triplicador(5))

quintuplicador = mi_funcion(5)
print(quintuplicador(5))