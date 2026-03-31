class ContoBancario:
    __nome: str
    __iban: str
    __saldo: float

    def __init__(self, intestatario, iban):
        self.__nome = intestatario
        self.__iban = iban
        self.__saldo = 0

    def deposita(self, s):
        if s > 0:
            self.__saldo += s

    def prelievo(self, s): #se ho soldi nel mio CB allora posso prelevare
        if self.__saldo > s:
            self.__saldo -= s
            return True
        else:
            return False

    def __prova(self, param1):
        print("prova")

    def __str__(self):
        return f"nome: {self.__nome} iban: {self.__iban} saldo: {self.__saldo}"



class Automobile:
    __benz = 0
    __stato = False #se è False allora il motore è spento, altrimeti è acceso

    def __init__(self):
        self.__benz = 0
        self.__stato = False

    def accendiMotore(self):
        self.__stato = True

    def spegniMotore(self):
        self.__stato = False

    def __èAcceso(self):
        return self.__stato

    def rifornimento(self, b):
        if self.__èAcceso() == False:
            self.__benz = b

    def sposta(self, km):
        if self.__èAcceso() == True and self.__benz > km:
            self.__benz -= km
        
    def __str__(self):
        return f"stato: {self.__stato} benzina: {self.__benz}"





antoConto = ContoBancario("Antonio Lezzi", "12345")
print(antoConto)
antoConto.prelievo(500)
print("stampo le info dopo il prelievo di 500euro")
print(antoConto)
print("Ricevo lo stipendio di 700euro")
antoConto.deposita(700)
print(antoConto)
antoConto.prelievo(200)
print("Prelevo w00euro")
print(antoConto)


pippoConto = ContoBancario("Pippo", "54321")
print(pippoConto)

antoConto.__saldo = 1

print("provo a modificare le variabili del conto di Antonio")
print(antoConto)
#antoConto.__prova()


print("Esempio Auto")
tesla = Automobile()
print("prima di spostarla visualizzo lo stato dell'auto")
print(tesla)
print("voglio spostarmi di 10km")
tesla.sposta(10)
print(tesla)
print("rifornimento di 30l e proviamo a spostarici di 5km")
tesla.accendiMotore()
tesla.rifornimento(30)
tesla.sposta(5)
print(tesla) #NO benz = 25, stato = True
#benz = 30, stato = False


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
# VEDI CLASSECELL.PY
'''
class Cellulare:
    batteria = 0
    soldi = 0

    def __init__(self, b, s):
        self.batteria = b
        self.soldi = s

    def statoCellulare(self):
        return f"batteria rimanente: {self.batteria}, soldi rimanenti: {self.soldi}"
    
    def chiama(self):
        if self.batteria > 10 and self.soldi > 1:
            input("inserire un numero da chiamare: ")
            print("chiamata in corso...")
            self.soldi -= 1
            self.batteria -= 10
        return self.statoCellulare()
    def ricaricaBatteria(self, b):
        self.batteria = b + 30
        return f"batteria +30% {self.batteria}"
    def ricaricaSoldi(self, s):
        self.soldi = s + 10
        return f"soldi +10euro {self.batteria}"

    def __str__(self):
        return f"stato batteria: {self.statoCellulare}"
    

pippoCell = Cellulare(30, 14)
pippoCell.chiama()

'''