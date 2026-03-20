iniz = -100
fine = 24
for iniz in range(fine):
    if iniz % 2 == 0:
        print(iniz)

for i in range(-6, 24, 2):
    print(i)
   
for i in range(-10, 8, 1):
    if i < 0 and i % 2 == 0:
        print(i)
    if i > 0 and i % 2 == 1:
        print(i)

stringa = ""
n = int(input("Inserisci un numero: "))

for i in range(n):
    if i % 2 == 0:
        stringa += "@"
    else:
        stringa += "#"
print(stringa)

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

#stampa le lettere in posizione pari della stringa inserita
disp = ""
stringa = input("Inserisci una stringa, ti faro uscire solo le posizioni pari della parola: ")
for i in range(len(stringa)):
    if i % 2 == 0:
        disp += stringa[i]

print(disp)