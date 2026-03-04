'''
Dati 10 caratteri e un carattere c dire se c è uno dei caratteri inseriti
'''
import random
import string
lista = []
for i in range(10):
    carat = random.choice(string.ascii_lowercase)
    lista.append(carat)
print(lista)
car = input("Inserisci un carattere: ")
#for i in lista:
if car in lista:
    print("Caccona!!! il carattere c'è")
else:
    print("Ops...il carattere da te inserito non è attualmente raggiungibile")