###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###

import os

os.system("clear")


# Creación de listas
print("\nCrear listas")
list1 = [1, 2, 3, 4, 5] # Listas de enteros
list2 = ["Manzanas", "peras", "platanos"] # Lista de cadenas
list3 = [1, "Hola", "3.14", True] # Lista de tipos mixtos

empty_list = []
list_of_lists = [[1, 2], [3, 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(list1)
print(list2)
print(list3)
print(empty_list)
print(list_of_lists)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(list2[0]) #manzanas
print(list2[1]) # peras
print(list2[-1]) # platanos
print(list2[-2])  # peras


print(list_of_lists[1][0])

# Slicing (rebanado) de listas
list1 = [1, 2, 3, 4, 5]
print(list1[1:4]) # [2, 3, 4]
print(list1[:3]) # [1, 2, 3]
print(list1[3:]) # [4, 5]
print(list1[:])

list1 = [1, 2, 3, 4, 5, 6, 7]
# HAY MÁS MAGIA
#print(list1[desde:hasta:paso]) # ????
print(list1[::2]) # Para devolver indices pares
print(list1[::-1]) # Para devolver índices inversas


# Modificar una lista
list1[0] = 16
print(list1)

# Añadir elementos en una lista
list1 = [1, 2, 3]

# Forma larga y menos eficiente
list1 = list1 + [4, 5, 6]
print(list1)

# Forma corta y más eficiente
list1 += [7, 8, 9]
print(list1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(list1))