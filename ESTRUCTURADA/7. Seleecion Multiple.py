if __name__ == '__main__':
    dia=int(input("proporciona un numero de la semana"))
    nomdia=""
    match dia:
        case 1: nomdia = "lunes"
        case 2: nomdia = "martes"
        case 3: nomdia = "miercoles"
        case 4: nomdia = "jueves"
        case 5: nomdia = "viernes"
        case 6: nomdia = "sabado"
        case 7: nomdia = "domingo"
        case _: nomdia = "dia no valido"
    print(f"el dia de la semana es {nomdia}")