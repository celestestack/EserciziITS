'''
Dati due numeri scrivere il loro quoziente, se il divisore è diverso da
0 allora stampare la divisione altrimenti “impossibile” se il divisore = 0
'''
n1 = int(input("Inserisci il dividendo: "))
n2 = int(input("Inserisci un divisore: "))

if n2 > 0:
    print(int(n1/n2))
else:
    print("COGLIONE è impossibile questa divisione")