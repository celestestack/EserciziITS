'''
Dati 10 numeri scrivere la loro somma, numeri inseriti ad ogni iterazione
'''

somma = 0
for i in range(10):
    elem = int(input("Inserisci un numero: "))
    somma += elem

print(somma)