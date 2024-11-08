import math

class Autos:
    def __init__(self,v1,v2,v3):
        self.a = v1
        self.b = v2
        self.c = v3
    def raiz(self) -> float:
        return math.sqrt((self.b*self.b)-((4*self.a)*self.c))

    def x1(self) -> float:
        return (-self.b+self.raiz())/(2*self.a)

    def x2(self) -> float:
        return (-self.b-self.raiz())/(2*self.a)

if __name__ == "__main__":
    resultado = Autos(6.0,8.0,2.0)
    print(resultado.x1())
    print(resultado.x2())