if __name__ == '_main_':
    num = int(input("dame un numero: "))
    poten = int(input("dame la potencia: "))
    i=1
    while i < poten:
        num = num * num
        i=i+1
    print(f"la ´potencia es: {num}")