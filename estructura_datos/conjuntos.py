# Conjunto (set): Colección no ordenada de elementos únicos (no se puede acceder por índice)

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))

print(len(frutas))


for item in frutas:
    print(item)
    
conjunto = {"Python", 122, True}
print(conjunto)
print("Manzana" in frutas)
print("Pera" not in frutas)

#Agregar
# add
frutas.add("Pera")
print(frutas)

#update
frutas_tropicales = {"Piña", "Mango"}
frutas.update(frutas_tropicales) # agregar listas, tuplas, conjuntos
print(frutas)

#Eliminarlos
#Remove
frutas.remove("Mango")  # Ok si "Mango" esta; error si no
print(frutas)
#Discard
frutas.discard("Banana") # Ok esté o no esté "Banana"
print(frutas)
#Pop
frutas.pop()
print(frutas)
#eliminado = frutas.pop() # Elemento al azar
#print(eliminado)
#Clear
frutas.clear()
print(frutas) # set()

print("-------------")
a = {"A", "B", "C"}
b = {"C", "D", "E"}

C_union = a.union(b)  # {"A", "B", "C", "D", "E"}
I_inter = a.intersection(b) # {"C"}
D_diff = a.difference(b) # {"A", "B"}

print(C_union)
print(I_inter)
print(D_diff)


numeros = {1, 2, 2, 3, 3, 3}
unicos = list(set(numeros))
print(unicos) # [1, 2, 3] El orden puede variar