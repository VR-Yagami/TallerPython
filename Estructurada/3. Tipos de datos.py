if __name__ == '__main__':

    entero = 42
    decimal = 3.14
    complejo = 2 + 3j
    booleano = True
    cadena = "Hola, Python!"
    binario = bytes([50, 100, 150])

    # Estructura
    print("Tipos básicos: ")
    print("Entero: ", entero)
    print("Decimal: ", decimal)
    print("Complejo: ", complejo)
    print("Booleano: ", booleano)
    print("Cadena: ", cadena)
    print("binario: ", binario, "\n")

    lista = [1, 2, 3, "cuatro"]
    tupla = (5, 6, 7, "ocho")
    conjunto = {9, 10, "once", "doce"}
    diccionario = {"clave1": "valor1", "clave2": 20}

    # Especiales
    print("Estructuras avanzadas: ")
    print("Lista: ", lista)
    print("Tupla: ", tupla)
    print("Conjunto: ", conjunto)
    print("Diccionario: ", diccionario, "\n")

    nulo = None
    rango = range(3)

    print("Tipos especiales: ")
    print("Nulo: ", nulo)
    print("Rango: ", list(rango))

    # Ejemplo de iteracion con el tipo range
    print("\nIterando sobre el rango: ")

    # Esta es la manera mas corta de recorrer un rango
    for numero in rango:
        print(numero)