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

class Cerchio:
    raggio = 0

    def __init__(self, r):
        self.raggio = r

    def area(self):
        return 3.14 * self.raggio ** 2
    
    def perimetro(self):
        return 2 * 3.14 * self.raggio

class Triangolo:
    base = 0
    altezza = 0


    def __init__(self, b, a):
        self.base = b
        self.altezza = a
  
    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return self.base * 3
        
'''
#Creiamo tre oggetti q1, q2, q3 di tipo Quadrato
q1 = Quadrato(4)
q2 = Quadrato(5)
q3 = Quadrato(100)

print("q1 area: ", q1.area(), " perimetro", q1.perimetro())
print("q2 area: ", q2.area(), " perimetro", q2.perimetro())


r1 = Rettangolo(10, 4)
print("r1 area: ", r1.area(), " perimetro", r1.perimetro())

c = Cerchio(7)

print("cerchio area: ", c.area(), " perimetro", c.perimetro())

tri = Triangolo(8,5)

print("tri area: ", tri.area(), " perimetro", tri.perimetro())
'''

'''
Creare una classe Cellulare che mi consenta di definire gli attributi
batteria e soldi
e creare i metodi chiama, ricaricaBatteria, ricaricaSoldi
Ovviamente per poter chiamare un cellulare deve passargli il numero di tel
e posso chiamare soltanto se la batteria è sufficientemente carica e se ho soldi
ATTENZIONE: ad ogni chiamata si consuma 1euro
implenta il metodo __str__
Fare la simulazione con diversi cellulari che chiamano altri numeri
'''


class Cellulare:
    batteria = 0
    __credito = 0

    def __init__(self, b, c):
        if b > 0 and b < 100 and c > 0:
            self.batteria = b
            self.__credito = c

    def ricaricaBatteria(self):
        self.batteria = 100

        return self.batteria
    
    def ricaricaCredito(self, c):
        if c > 0:
            self.__credito += c
        return self.__credito
    
    def chiamata(self, tel):
        if self.__credito >= 1 and self.batteria >= 10:
            self.__credito -= 1
            self.batteria -= 10
            print(f"Chiamata a {tel} in corso...")
        elif self.__credito < 1:
            print("Questa funzione non è disponibile, ricarica il credito")
        elif self.__batteria < 10:
            print("Batteria esauirita, ricarica!")
        else:
            return 0

    def __str__(self):
        return f"Batteria: {self.batteria} Credito: {self.__credito}"

c4 = Cellulare(-10, 0)
print(c4)
c4.ricaricaBatteria()
c4.ricaricaCredito(30)
print(c4)
c4.chiamata(3471123376)
print(c4)
c4.chiamata(3471123376)
print(c4)
c4.chiamata(3471123376)
print(c4)
c4.ricaricaCredito(-3)
print(c4)
c4.chiamata(3471123376)
print(c4)