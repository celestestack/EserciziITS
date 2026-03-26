class Bottiglia:

    def __init__(self):
        self.open = False
        self.full = 100
        self.color = "verde"

    def __str__(self):
        return f"La bottiglia è aperta? {self.open}, quantità presente: {self.full}, è di colore: {self.color}"
    
    def openb(self):
        self.open = True
        return self.open
    
    def closeb(self):
        self.open = False
        return self.open

    def sip(self, quantita):
        if type(quantita) == int and self.open == True:
          if self.full >= quantita:
            self.full -= quantita
            return self.full
                    

borra = Bottiglia()

print(borra)
borra.openb()
borra.sip(80)
print(borra)
