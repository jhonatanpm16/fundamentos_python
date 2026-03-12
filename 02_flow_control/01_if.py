###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo solo si cumplen ciertas condiciones
###
import os

os.system("clear")


print("\n Sentencia simple condicional")

age = 18

if age >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
    
age = 16

if age >= 18:
    print("Eres mayor de edad")
    print("Felicidades")



print("\n Sentencia simple condicional")
age = 16

if age >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
else:
    print("Eres menor de edad")


print("\n Sentencia condicional con elif")
note = 7
if note >= 9:
    print("¡Sobresaliente!")
elif note >= 7:
    print("Notable!")
elif note >= 5:
    print("aprobado")
    
    
print("\n Condiciones Multiples")
age = 12
has_card = False

# Un pueblo de Valencia
if age >= 18 and has_card:
    print("Puedes conducir")
else:
    print("POLICIA!!!")
    
    
# Un pueblo de Isla Margarita
if age >= 18 or has_card:
    print("Puedes conducir en la Isla Margarita")
else:
    print("Paga al policia y te deja conducir!!!")
    
its_weekend = False
if not its_weekend:
    print("¡Venga, hay que estudiar!")
    
    
print("\n Anidar condicionales")
age = 20
has_money = True
if age >= 18:
    if has_money:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")

# Mas facil
#if age <= 18:
#    print("No puedes entrar a la disco")
#elif has_money:
#    print("Puedes ir a la discoteca")
#else:
#    print("Quédate en casa")

number = 0
if number: # False
    print("Aqui no entrara nunca")
    
name = ""
if name:
    print("El nombre no es vacio")
    

number = 3 # asiganación
it_is_the_three = number == 3  # comparación
if it_is_the_three: 
    print("El numero es 3")
    
print("\nLa condición terniaria")
# Es una forma concisa de un if-else en una linea de codigo
# [Codigo si cumple una condición] if [condición] else [codigo si no cumple]

age = 17
message = "Es mayor de edad" if age >= 18 else "Es menor de edad"
print(message)

