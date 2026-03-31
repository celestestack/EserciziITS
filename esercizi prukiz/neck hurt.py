#chiedere all'utente di compiere una serie di operazioni somma differenza moltiplicazione tra diversi elementi di una lista
num = [4, 16, 24, 67]
def somma(lista):
    tot = 0
    for i in range(0, len(lista), 1):
        tot = lista[i] + tot
    return tot 


def differenza(lista):
    tot = lista[0]
    for i in range(1, len(lista), 1):
        tot = tot - lista[i]
    return tot 


def moltiplicazione(lista): 
    tot = 1
    for i in range(0, len(lista), 1):
        tot = lista[i] * tot
    return tot 


def inserimento(num):
    int(input("inserisci valore: "))
    for i in range(5):
       valori = int(input("inserisci valore: "))
       num.append(valori)
    print(num)
inserimento(num)








def menu():
    scelta = -1
    cont = 0
    while scelta < 1 or scelta > 5:
        print("\nMenu:")
        print("1) inserimento dei dati")
        print("2) somma")
        print("3) differenza")
        print("4) moltiplicazione")
        print("5) esci")
        scelta = int(input("inserisci la tu scelta: "))
