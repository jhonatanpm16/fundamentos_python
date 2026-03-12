##
# 04 - variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinamico y de tipado fuerte
###

# Asignar una variable
# Solo hace falta poner esto
my_name = "jhonatanpm"
#print(my_name)

age = 32
#print(age)

#age = 34
#print(age)

# Tipado dinamico: el tipo de dato que se asigna a una variable depende del tipo de dato que 
# se asigne a la variable, el tipo de dato se determine en tiempo de ejecución
# que no tienes que declararlo explicitamente


name = "jhonatanpm"
print(type(name))

name = 32
print(type(name))


# Tipado fuerte: Python no realiza conversiones de tipo automaticos
#print(10 + "2")

# f-string (literal de cadena pde formato)
# esto esta desde la versión 3.6
print(f"Hola {my_name}, tengo {age + 5} años")


# No recomndado forma de asignar variiables
name, age, city = "jhonatanpm", 22, "Chicontepec"

# Convenciones de nombre de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

MiNombreDeVariable = "ko" # PascalCase
minobredevariable = "ko" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> contantes

MI_CONSTANTE = 2


# Nombres no validos de variables
# 123123_variable = "ho"
# mi-variable = "ho"
# mi variable = "ho"
#True = False


is_user_logged_in:bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)


name: str = "jhonatanpm"