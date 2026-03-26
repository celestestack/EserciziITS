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
    
    def __init__(self, b, s):
        self.batteria = b
        self.soldi = s

    def statoCellulare(self):
        return f"batteria rimanente: {self.batteria}%, soldi rimanenti: {self.soldi}€"
    
    def chiama(self, numero):
        if type(numero) == int:
            if self.batteria < 10 or self.soldi < 1:
                print("batteria o credito insufficiente per effettuare la chiamata!")
            else:
                print(f"sto chiamando il numero {numero}...")
                self.batteria -= 10
                self.soldi -= 1
                print(f"chiamata terminata. {self.statoCellulare()}\n")
        else:
            print("valore non valido.\n")

    def ricaricaBatteria(self, quantita):
        if quantita > 0:
            self.batteria += quantita
        if self.batteria > 100:
            self.batteria = 100
        print(f"batteria ricaricata. {self.statoCellulare()}")

    def ricaricaSoldi(self, quantita):
        if quantita > 0:
            self.soldi += quantita
        print(f"soldi ricaricati. {self.statoCellulare()}")

    def __str__(self):
        return self.statoCellulare()
    


pippo = Cellulare(100, 15)
print(pippo)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama("ciao")
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
pippo.chiama(387473829)
print(pippo)
pippo.ricaricaBatteria(20)
pippo.ricaricaSoldi(5)
