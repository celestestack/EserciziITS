'''Implementare delle funzioni che consentano di trovare il massimo, minimo, 
contare il numero di elementi su una lista e ridefinire la funzione range senza 
usare le funzioni predefinite di python (len, max, min, range).'''


def massimo(lista):
    '''
    funzione che individua il massimo senza usare funzione max (incredibile)
    '''
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

def minimo(lista):
    '''
    funzione che individua il minimo senza usare funzione min (pazzesca)
    '''
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

def conta(lista):
    contaElem = 0
    for i in lista:
        contaElem += 1
    return contaElem

def myRange(start, stop, step = 1):
    risultato = []
    corrente = start
    while corrente < stop:
        risultato.append(corrente)
        corrente += step
    return risultato

print(massimo([1, 2, 3, 4]))
print(minimo([1, 2, 3, 4]))
print(conta([1, 2, 3, 4]))
print(myRange(0, 10))
