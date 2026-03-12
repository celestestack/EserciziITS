'''
Scrivete un programma che chieda due numeri. Se la somma dei due numeri supera 100,
stampate “Numero troppo grande”
'''
while True:
    a = input("Inserisci un numero: ")
    b = input("Inserisci un numero: ")
    if(a.isdigit() == True and b.isdigit() == True):
        n1, n2 = int(a), int(b)
        sum = n1 + n2
        if(sum >= 100):
            print("Hai sforato! Numero troppo grande")
        else: print("OK")
    break