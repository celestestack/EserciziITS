
#fare un ciclo che stampi i numeri da -3 a 7
inizio = -3
fine = 7

while inizio < fine:
    print(inizio)
    inizio = inizio + 1

#stampare dei numeri pari cha vanno da -7 a 24
contenutoResto = 13 % 2

inizio = -7
fine = 24

while inizio < fine:
    if inizio % 2 == 0:
        print(inizio)
    inizio = inizio + 1

#stampare i numeri dispari cha vanno da -100 a -24
inizio = -7
fine = 24

while inizio < fine:
    if inizio % 2 != 0:
        print(inizio)
    inizio = inizio + 1

#stampare i numeri positivi cha vanno da -100 a 24
inizio = -100
fine = 24

while inizio < fine:
    if inizio > 0:
        print(inizio)
    inizio = inizio + 1

#stampare i numeri dispari positivi cha vanno da -100 a 24
#1, 3, 5, 7, ... 23
inizio = -100
fine = 24

while inizio < fine:
    if inizio > 0:
        if inizio % 2 != 0:
            print(inizio)
    inizio = inizio + 1

#stampare i numeri pari negativi e i dispari positivi cha vanno da -10 a 8
#-10, -8, -6, -4, -2, 1, 3, 5, 7
inizio = -100
fine = 24

while inizio < fine:
    if inizio > 0:
        if inizio % 2 != 0:
            print(inizio)
    else:
        if inizio % 2 == 0:
            print(inizio)

    inizio = inizio + 1

#richiedere all'utente di inserire una serie di numeri e deve terminare con 0 (ZERO)
#SENZA USARE WHILE TRUE
#variabili, condizioni, while
val = 9
while val != 0:
    val = int(input("Inserisci il nuovo numero: "))

#richiedere all'utente di inserire una serie di stringhe e deve terminare con EXIT
val = ""
while val != "EXIT":
    val = input("Inserisci il stringa Exit per uscire: ")

#Creare un programma che chieda all’utente di inserire una stringa di lunghezza pari.
#Se l’utente inserisce una stringa di lunghezza dispari, il programma dovrà terminare.
#ciao
#casa
#pippo (TERMINA)
stringa = ""
while len(stringa) % 2 == 0:
    stringa = input("Inserisci una parola, termina se la lunghezza dispari")




stringa = "prova "
stringa = stringa + "ciao" #prova ciao

#Creare un programma che chieda all’utente di inserire un numero n e stampi una stringa
#lunga n caratteri dove i caratteri che la compongono saranno i caratteri @ e # alternati
#partendo con un carattere @. Ad esempio se l’utente dice che la stringa dovrà essere
#lunga 5 caratteri la stringa stampata dovrà essere: @#@#@ 

stringa = ""
n = int(input("inserisci un val intero: "))

i = 0
while i < n:
    if i % 2 == 0:
        stringa += "#"
    else:
        stringa += "@"
    i += 1

print(stringa)

#Scrivere un programma Lunghezze che chiede all’utente di inserire una sequenza di stringhe e conclusa
#dalla stringa vuota, e poi stampa la somma delle lunghezze delle stringhe che iniziano con una lettera
#maiuscola. Per esempio, se si immettono le stringhe:
#"Albero", "foglia", "Radici", "Ramo", "fiore" (e poi "" per finire), il programma stampa 16.
#Perché considero solo le parole con la lettera iniziale maiuscola come:
#Albero -> 6
#Radici -> 6
#Ramo -> 4
#Totale 16

tot = 0
stringa = "a" #solo per fare un esempio

#1 creare un programma che consenta l'inserimento delle stringhe, viene terminato da un invio (stringa vuolta)
#2 analizzare la stringa, prendere il primo carattere (INDICIZZAZIONE stringa[0])
#3 controllare se il carattere è maiuscolo allora incrementare il totale

#devo far inserire delle stringhe diverse e termino quando la stringa è una stringa vuota "" 
while len(stringa) != 0:
    if stringa[0] >= "A" and stringa[0] <= "Z":
        tot += len(stringa)

    stringa = input("Inserisci la stringa: ")

print(tot)


#creare un programma che chieda all'utente di inserire una stringa e possa restituire soltanto
# le vocali (aiuola = aiuoa, ciao = iao)

parola = input("inserisci stringa: ")
for i in range(0, len(parola), 1):
    if parola[i] == "a" or parola[i] == "e" or parola[i] == "i" or parola[i] == "o" or parola[i] == "u":
        print(parola[i])

#creare un programma che chieda all'utente di inserire una stringa e possa restituire soltanto
# le consonanti

parola = input("inserisci stringa: ")
for i in range(0, len(parola), 1):
    if parola[i] != "a" and parola[i] != "e" and parola[i] != "i" and parola[i] != "o" and parola[i] != "u":
        print(parola[i])


#creare un programma che chieda all'utente di inserire una stringa e visualizzare i caratteri
# della stringa che si trovano  in posizione pari, esempio se inserisco "Fantastico" deve mostrare "Fnatc"

parola = input("inserisci stringa: ")
for i in range(0,len(parola), 1):
    if parola[i] % 2 == 0:



#chiedere all'utente di compiere una serie di operazioni somma differenza moltiplicazione tra diversi elementi di una lista 
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