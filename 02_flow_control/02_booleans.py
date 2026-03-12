###
# 02 -booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la logica en programación.
###

import os

os.system("clear")

# Los valores booelanos representan valores de verdad: True o False
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: Devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3", 5 > 3) # True
print("5 < 3", 5 < 3) #False
print("5 == 5", 5 == 5) # True (igualdad)
print("5 != 3", 5 != 3) # True (desigualdad)
print("5 >= 5", 5 >= 5) # True (Mayor o igual que)
print("5 <= 3", 5 <= 3) # False (Menor o igual que)


print("\nComparación de textos:")
print("manzana < mora", "manzana" < "mora")
print("'hola' == 'Hola'", "hola" == "Hola")


# Operadores lógicos: and, or, not
print("\nOperadores logicos:")
print("True and True:", True and True) # True
print("True and False:", True and False) # False
print("True or False:", True or False) #True
print("False or False:", False or False) # False
print("not True:", not True) # False
print("not False:", not False) # True


# Tablas de verdad (para referencia) :
print("\nTablas de verdad:")
print("and:")
print("A     B     A and B")
print("True  True ",True and True)
print("True  False ",True and False)
print("False  True ", False and True)
print("False  False ", False and False)


print("or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False ", True or False)
print("False  True ", False or True)
print("False  False ", False or False)

print("not:")
print("A  not  A")
print("True:", not True)
print("False:", not False)