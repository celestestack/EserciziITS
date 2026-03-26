# creare un ciclo che stampi i numeri da 0 a 10

for i in range(11):
    print(i)

# stampare numeri pari che vann da -7 a 24

for i in range (-7, 25):
    if i%2 == 0:
        print(i)

# stampare i numeri dispari che vanno da -100 a -24

for i in range (-100, -24):
    if i%2 != 0:
        print(i)

# stampare i numeri positivi che vanno da -100 a 2 4

for i in range (-100, 24):
    if i >= 0:
        print(i)

# stampare i numeri dispari positivi che vanno da -100 a 24

for i in range (-100, 24):
    if i >= 0 and i %2 != 0:
        print(i)

# stampare i numeri pari negativi e i dispari positivi che vanno da -10 a 8

for i in range (-100, 8):
    if i < 0 and i %2 == 0:
        print(i)
    if i >= 0 and i %2 != 0:
        print(i)

# richiadere all'utente di inserire una serie di numeri e deve terminare con 0

numero = -1
while numero != 0:
    numero = int(input("inserire un valore. 0 per terminare.   "))
    
# richiadere all'utente di inserire una serie di stringhe e deve terminare con EXIT

stringa = ""
while stringa != "EXIT":
    stringa = input("inserire una stringa. EXIT per terminare.   ")

# creare un programma che: lunghezza stringa inserita pari = continua. altirmenti termina.

stringa = ""
while len(stringa) %2 == 0:
    stringa = input("inserire una stringa.   ")

'''
Creare un programma che chieda all’utente di inserire un numero n e stampi una 
stringa lunga n caratteri dove i caratteri che la compongono saranno i caratteri 
@ e # alternati partendo con un carattere @

Ad esempio se l’utente dice che la stringa dovrà essere lunga 5 caratteri la stringa 
stampata dovrà essere: @#@#@
'''

n = int(input("inserire un valore: "))
stringaF = ""
for i in range(n):
    if i%2 == 0:
        stringaF += "@"
    else:
        stringaF += "#"

print(stringaF)

'''
Scrivere un programma Lunghezze che chiede all'utente di inserire una sequenza di stringhe 
e conclusa dalla stringa vuota, e poi stampa la somma delle lunghezze delle stringhe che 
iniziano con una lettera maiuscola. Per esempio, se si immettono le stringhe "Albero", 
"foglia", "Radici", "Ramo", "fiore" (e poi "" per finire), il programma stampa 16.
'''

tot = 0
stringa = "a"

while len(stringa) != 0:
    stringa = input("inserisci una stringa: ")
    
    if stringa != "" and 65 <= ord(stringa[0]) <= 90:
        tot += len(stringa)

print(tot)

# chiedi all'utente di inserire una stringa e restituisci soltanto le vocali
#con for
stringa = input("inserisci una stringa: ")
vocali = "aeiouAEIOU"
result = ""
for lettera in stringa:
    if lettera in vocali:
        result += lettera
print(result)
#con while
stringa = input("inserisci una stringa: ")
vocali = "aeiouAEIOU"
result = ""
i = 0
while i < len(stringa):
    if stringa[i] in vocali:
        result += stringa[i]
    i += 1
print(result)

# chiedi all'utente di inserire una stringa e restituisci soltanto le consonanti
#con for
stringa = input("inserisci una stringa: ")
vocali = "aeiouAEIOU"
result = ""
for lettera in stringa:
    if lettera not in vocali:
        result += lettera
print(result)

#con while
stringa = input("inserisci una stringa: ")
vocali = "aeiouAEIOU"
result = ""
i = 0
while i < len(stringa):
    if stringa[i] not in vocali:
        result += stringa[i]
    i += 1
print(result)

# chiedi all'utente di inserire una stringa e restituisci soltanto i caratteri in posizione pari
#con for
stringa = input("inserisci una stringa: ")
result = ""
for i in range (len(stringa)):
    if i%2 == 0:
        result += lettera[i]
print(result)
#con while
stringa = input("inserisci una stringa: ")
result = ""
i = 0
while i < len(stringa):
    if i%2 == 0:
        result += stringa[i]
    i += 1
print(result)