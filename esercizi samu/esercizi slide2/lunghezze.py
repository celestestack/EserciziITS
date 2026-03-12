'''
* Scrivere un programma Lunghezze che chiede all’utente di inserire
una sequenza di stringhe e conclusa dalla stringa vuota, e poi stampa
la somma delle lunghezze delle stringhe che iniziano con una lettera
maiuscola. Per esempio, se si immettono le stringhe "Albero", "foglia",
"Radici", "Ramo", "fiore" (e poi "" per finire), il programma stampa 16.
'''
lista = []
count = 0
while True:
    parola = input("Inserisci una parola, dai invio per terminare: ")
    if parola == "":
        break
    lista.append(parola)
    if parola[0].isupper():
        count += len(parola)
        
print(lista)
print(count)