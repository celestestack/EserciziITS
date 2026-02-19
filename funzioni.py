'''Implementare delle funzioni che consentano di trovare il massimo, minimo, contare il numero di elementi su
una lista e ridefinire la funzione range senza usare le funzioni predefinite di python (len, max, min, range).'''


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
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min