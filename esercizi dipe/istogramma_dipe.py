'''
Scrivere una funzione che produce un istogramma 
esempio Istrogramma([4,2,6]):
****
**
******'''

def istogramma(lista):
    for numero in lista:
        print("*" * numero) 

print(istogramma([4,2,6]))

