x = 5
y = 3
z = 10

if x > y or x > z:
    print("x es mayor a y y x es menor a z")
elif y > x: 
    print("No se va a cumplir")
elif x == y:
    print("x es mayor a y")
else:
    print("Ninguna de las condiciones anteroriores se cumplio")
    
# Strings
# if anidado

a = "Python"
b = "JavaScript"
c = "Python"

if a == c:
    if a != b:
        print("a es igual a c pero es distinto a b")
    print("a es igual a c")
else:
    print("a no es igual a c")


e = 10
f = 10

if e == f:
    pass # Para ignorar la estructura if hasta tanto definamos que comportamiento se espera

