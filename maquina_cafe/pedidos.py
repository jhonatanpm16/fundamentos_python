ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elije el café que prefieras")
    print("1. Espresso")
    print("2. Cappuchino")
    print("3. Latte")
    print("4. Americano")
    
    opcion = input("Opcion: ")
    
    cafes = {
        "1": "Espresso",
        "2": "Cappuchino",
        "3": "Latte",
        "4": "Americano"
    }
    
    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Has pedido un " + cafe_elegido + ". Preparando tu cafe")
        
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("La opción no es valida por favor intenta de nuevo")
        