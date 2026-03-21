lista = []

def mostraMenu():
    scelta = 1
    cont = 0

    while scelta != 0 and cont < 3:
        print("Menù calcolatrice\n1)Inserimento dati\n2)somma\n3)differenza\n4)moltiplicazione\n0)per uscire\n\n")
        
        scelta = int(input("Fai la tua scelta: "))
        if scelta < 0 or scelta > 4:
            print(f"Hai inserito un valore errato! Ti rimangono {2-cont} tentativi")
            cont +=1
        elif scelta == 1:
            inserimento(lista)
        elif scelta == 2:
            print(somma(lista))
        elif scelta == 3:
            print(differenza(lista))
        elif scelta == 4:
            print(moltiplicazione(lista))
        elif scelta == 0:
            return 0
     
        
         
def inserimento(lista):
    num = int(input("Quanti numeri vuoi inserire?: "))
    i = 0
    while i < num:
        n = 4

        lista.append(n)
        i += 1
    return lista


def somma(lista):
    tot = 0
    for i in range(len(lista)):
        tot += lista[i]
    return tot

def differenza(lista):
    tot = lista[0]
    for i in range(1,len(lista),1):
        tot -= lista[i]
    return tot

def moltiplicazione(lista):
    tot = 1
    for i in range(len(lista)):
        tot *= lista[i]
    return tot


mostraMenu()

