'''
Creare un programma che chieda all’utente di inserire un numero n e stampi una stringa lunga n
caratteri dove i caratteri che la compongono saranno i caratteri @ e # alternati partendo con un
carattere @
Ad esempio se l’utente dice che la stringa dovrà essere lunga 5 caratteri la stringa stampata dovrà
essere: @#@#@
'''
def stringaFinale():
    num = int(input("Inserire un numero: "))
    stringa = ""
    for i in range(num):
        if(i%2 == 0):
            stringa += "@"
        else:
            stringa += "#"
    return stringa
'''
Creare una funzione che, data una lista di numeri ed un numero da cercare, restituisca il valore
booleano True se tale numero è presente nella lista, False altrimenti
'''

def trovaNum(lista, num):
    for i in lista:
        if i == num:
            return True
    return False
        
#print(stringaFinale())    

lista = [1,9,7,5,2,7,9]
n = 5
print(trovaNum(lista,n))

'''
Creare una funzione che abbia due parametri: una stringa e un carattere. La funzione dovrà scorrere
tutte le lettere della stringa utilizzando l'istruzione for e restituire il numero di occorrenze del
carattere nella stringa.
'''

def occorrenze(str, car):
    count = 0
    for i in str:
        if i == car:
            count += 1
    return count

print(occorrenze("ciaooooo","o"))