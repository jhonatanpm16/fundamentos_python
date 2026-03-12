# Listas: Las listas son ordenadas, modificables y permiten valores duplicados

# Índices     1          2          3            4
frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print("frutas")
print(type(frutas))

frutas[1] = "Banana"

print(frutas[1])
print(frutas)


lista = ['Jhonatan', 5, True]
print(lista)
print(type(lista))

print(len(lista))
print(len(frutas))

print(frutas[1:])

if "Manzana" in frutas:
    print("La manzana esta debtro de las frutas")
# índices     0          1      2
vehiculos = ["Auto", "Moto", "Avión"]

#Metodos
# append (Agregar un elemnto al final de la lista)
vehiculos.append("Barco") # Índice 3
print(vehiculos)

# Insert 
vehiculos.insert(1, "Bicicleta")
print(vehiculos)


# Remove
vehiculos.remove("Auto")
print(vehiculos)

# Pop
vehiculos.pop(1)
print(vehiculos)


# Sort 
vehiculos.sort()
print(vehiculos)

# Reverse
vehiculos.reverse()
print(vehiculos)

#Unir listas
coleccion1 = [1, 3, 4]
coleccion2 = [2, 6, 8]
coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)