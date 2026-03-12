day = 4

match day:
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miercoles")
    case _:
        print("No coincide con ninguna de las anteriores opciones")
        
colors = "azul"

match colors:
    case "amarillo":
        print("es un color amarillo")
    case "rojo":
        print("Es un color rojo")
    case "azul":
        print("Es un color azul")
    case "verde":
        print("Es un color verde")