iniz = -100
fine = 24
while iniz < fine:
    if iniz % 2 == 0:
        print(iniz)
    iniz += 1


    
for i in range(-6, 24, 2):
    print(i)
   
for i in range(-10, 8, 1):
    if i < 0 and i % 2 == 0:
        print(i)
    if i > 0 and i % 2 == 1:
        print(i)

#chiede all'utente di inserire un numero se viene inserito 0 esce dal while
val = 1

while val != 0:
    val = int(input("Inserisci un numero: "))
    
#chiede all'utente di inserire una stringa se viene inserito "exit" esce dal while
stringa = ""

while stringa != "exit":
    stringa = input("Inserisci una stringa qualsisasi, scrivi exit per uscire: ")
   
#chiede all'utentendi di inserire una stringa, se inserisce una stringa dispari termina
stringa = ""

while len(stringa) % 2 != 1:
    stringa = input("Inserisci una stringa qualsisasi inserisci una stringa dispari per terminare: ")

#inserito un numero stampa i caratteri @ e # n volte
gay = ""
i = 0
n = int(input("Inserisci un numero: "))

while i < n:
    if i % 2 == 0:
        gay += "@"
    else:
        gay += "#"
    i += 1

print(gay)

#stampa la lunghezza totale delle parole inserite con la prima lettera maiuscola
lung = 0
str = "a"

while len(str) != 0:
    if str[0].isupper():
        lung += len(str)
    str = input("Inserisci una stringa, vengono conteggiate solo le parole con la prima lettera maiuscole: ")
print(lung)

#stampa le vocali inserite nella stringa
vocali = "aeiou"
stringa = input("Inserisci una stringa, ti farò uscire le vocali: ")

for i in range(len(stringa)):
    if stringa[i] in vocali:
        print(stringa[i])

#stampa le consonanti inserite nella stringa
stringa = input("Inserisci una stringa, ti farò uscire le consonanti: ")

for i in range(len(stringa)):
    if stringa[i] not in vocali and stringa[i].isdigit() == False: 
            print(stringa[i])

#
disp = ""
stringa = input("Inserisci una stringa, ti faro uscire solo le posizioni pari della parola: ")
for i in range(len(stringa)):
    if i % 2 == 0:
        disp += stringa[i]

print(disp)