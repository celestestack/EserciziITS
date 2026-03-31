'''
Quadrato: lato, perimetro e area
Rettangolo: base altezza, perimetro e area

Implementare classe cerchio e triangolo
Cerchio: raggio,  perimetro e area
Triangolo: lato perimetro e area
'''
#definizione della classe Quadrato, che è una sorta di stampino
class Quadrato:
    lato = 0

    def __init__(self, l):
        self.lato = l

    def perimetro(self):
        return self.lato * 4

    def area(self):
        return self.lato * self.lato


class Rettangolo:
    base = 0
    altezza = 0

    def __init__(self, b, h):
        self.base = b
        self.altezza = h

    def perimetro(self):
        p = (self.base + self.altezza) * 2
        return p

    def area(self):
        a = self.base * self.altezza
        return a


#Creiamo tre oggetti q1, q2, q3 di tipo Quadrato
q1 = Quadrato(4)
q2 = Quadrato(5)
q3 = Quadrato(100)

print("q1 area: ", q1.area(), " perimetro", q1.perimetro())
print("q2 area: ", q2.area(), " perimetro", q2.perimetro())


r1 = Rettangolo(10, 4)
print("r1 area: ", r1.area(), " perimetro", r1.perimetro())



