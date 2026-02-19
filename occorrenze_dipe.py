'''Creare una funzione che abbia due parametri: una stringa e un carattere. 
La funzione dovrà scorrere tutte le lettere della stringa utilizzando l'istruzione 
for e restituire il numero di occorrenze del carattere nella stringa.'''

s = "ciaociaociao"

def occorrenze(stringa, carattere):
    conta_carattere = 0
    for lettera in stringa:
        if lettera == carattere:
            conta_carattere += 1
    return conta_carattere


print(occorrenze(s, 'c'))