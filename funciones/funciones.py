#Definir

def mi_funcion():
    print("Hola mundo desde una función")
    #invocar (se ejecuta cada vez que se llama)
    
mi_funcion()
mi_funcion()

# un agumento
def saludar(nombre):
    print("Hola", nombre)

saludar("Pedro")
saludar("Ana")

# Varios argumentos y oder estricto
def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")

saludar("Pedro", "Sánchez")
saludar("María", "Gutiérrez")

#Valores por defecto
def saludar(nombre, apellido="", nacionalidad="Colombia"):
    # Ejemplo de perzonalización con valores por defecto
    if apellido:
        print(f"Hola, {nombre} {apellido} de {nacionalidad}")
    else:
        print(f"Hola {nombre} de {nacionalidad}")
        
saludar("Pedro", "Sanchez", "España") # Hola, Pedro Sánchez de españa
saludar("Maria", "Gutierrez")  # Hola, Maria Gutierrez de Colombia
saludar("Ana") # Hola, Ana de colombia

# Devolver un valor
def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
print(resultado) # 5

def funcion():
    pass # evita error mientras decides la lógica
