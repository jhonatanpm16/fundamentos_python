print("hola 'Mundo'")
print('hola "mundo"')


ingles = "I'm Jhonatan"

multiples = """ Hola
Mundo
desde
las comillas
triples"""

print(ingles)
print(multiples)

palabra = "Murcielago"

print(len(palabra))

texto = "Este curso es de Fundamentos de Python"
estaIncluida = "Python" in texto
noEstaIncluida = "JavaScript" not in texto
print(estaIncluida)

print(noEstaIncluida)

mayuscula = texto.upper()
minuscula = texto.lower()

print(mayuscula)
print(minuscula)

texto2 = texto.upper()
texto2 = texto.lower()

print(texto2)


espacios = "      Este es el texto        "
sinEspacios = espacios.strip()

print(sinEspacios)