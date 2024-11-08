import math

if  __name__ == "__main__":
    Suma = lambda x,y:x+y
    print(f"La suma es: {Suma(2,6)}")

    Potencia = lambda x:x ** 2
    print(f"La potencia es: {Potencia(9)}")

    x1 = lambda a,b,c:(-b+math.sqrt((b**2)*((4*a)*c)))/(2*a)
    x2 = lambda a,b,c:(-b-math.sqrt((b**2)*((4*a)*c)))/(2*a)

    print(f"x1 es: {x1(6,8,6)}")
    print(f"x2 es: {x2(6,8,6)}")