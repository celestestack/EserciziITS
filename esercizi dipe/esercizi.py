# chiedere all'utente di compiere una serie di operazioni: somma, differenza, moltiplicazione, 
# tra i diversi elementi di una lista

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
        scelta = int(input("inserisci la tua scelta: "))
        if scelta < 1 or scelta > 5:
            print("riprova")
            cont += 1
            if cont == 3:
                print("hai sbagliato 3 volte, programma terminato")
                return 0
    return scelta

def inserisci():
    risultato = []
    n = int(input("quanti numeri vuoi inserire? "))
    for i in range(n):
        num = int(input("inserisci un numero: "))
        risultato.append(num)
    return risultato

def somma(lista):
    s = 0
    for i in lista:
        s += i
    return s

def differenza(lista):
    d = 0
    for i in lista:
        d -= i
    return d

def moltiplicazione(lista):
    m = 1
    for i in lista:
        m *= i
    return m

def main():
    lista = []
    scelta = menu()
    while scelta != 5:
        if scelta == 0:
            break
        elif scelta == 1:
            lista = inserisci()
            print("lista:", lista)
        elif scelta == 2:
            print("somma:", somma(lista))
        elif scelta == 3:
            print("differenza:", differenza(lista))
        elif scelta == 4:
            print("moltiplicazione:", moltiplicazione(lista))
        scelta = menu()

main()