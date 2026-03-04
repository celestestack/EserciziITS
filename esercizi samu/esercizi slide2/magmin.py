'''
Dati due numeri, scrivere il maggiore (verificare anche se sono uguali)
'''
n1 = int(input("Inserisci un numero: "))
n2 = int(input("Inserisci un numero: "))
if n1 > n2:
    print("Il primo è maggiore")
elif n2 > n1:
    print("Il secondo è più grande")
else:
    print("I numeri sono uguali")