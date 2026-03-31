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

class cellulare:
    def __init__(self, batteria, soldi):
        self.batteria = batteria
        self.soldi = soldi
    
    def chiama(self, numero: str):
       if self.batteria < 10 and self.soldi < 1:
           print("impossibile eseguire la chiamata, batteria scarica o saldo insufficiente")
       elif self.batteria >=10 and self.soldi >=1:
           self.batteria -=10
           self.soldi -=1
           print("chiamata eseguita con successo")

    def ricaricaBatteria(self, quantita: int):
        if quantita > 0 and self.batteria <=100:
            self.batteria += quantita
            print("batteria ricaricata")
        if self.batteria > 100:
            self.batteria = 100
        else:
            print("impossibile la quantità ricaricata non può essere negativa")
    

    def ricaricaSoldi(self,quantita: int):
        if quantita > 0:
            self.soldi += quantita
            print("ricarica monetaria effettuata con successo")
        else: 
            print("impossibile la quantità di soldi ricaricata non può essere negativa ")

    

    def __str__(self):
        return f"Cellulare: (Batteria: {self.batteria}%, Soldi: €{self.soldi:})"
    
cell1 = cellulare(batteria=50, soldi=5)
cell2 = cellulare(batteria=0, soldi=0.5)

print("Stato iniziale dei cellulari:")
print(cell1)
print(cell2)

cell2.chiama("3333333333")
    
cell2.ricaricaBatteria(150)
cell2.ricaricaSoldi(3)

print("Stato iniziale dei cellulari:")
print(cell1)
print(cell2)

cell2.chiama("33333333333")