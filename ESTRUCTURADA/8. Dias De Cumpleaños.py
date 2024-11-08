if __name__ == '__main__':
    nom = (input("proporciona un nombre: "))
    fecha = ""
    match nom:
        case "Rocio": fecha = "2 de octubre"
        case "Floricela": fecha = "1 de diciembre"
        case "Lucero": fecha = "1 de octubre"
        case "Alejandra": fecha = "22 de noviembre"
        case "Aldair": fecha = "29 de junio"
        case _: fecha = "fecha no valida"
    print(f"la fecha de cumpleaños es: {fecha}")