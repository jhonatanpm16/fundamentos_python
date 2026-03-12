###
# 05 - Entrada de usuario (input) - Version simplificada
# La función input() permite obtener datos del usuario a través de la consola
###

nombre = input("Hola, ¿Como te llamas?\n")


print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuantos años tienes?\n")
age = int(age)

print(f"Dentro de 20 años tendrás {age + 20}")


print("Obtener multiples valores a la vez")
country, city = input("¿En que país y ciudad vives?\n").split()
print(f"Hola {nombre}, tengo {age} años y vivo en {country}, {city}")

print(f"Vives en {country}, {city}")