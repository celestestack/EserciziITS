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
    '''
    funzione che individua il minimo senza usare funzione min (pazzesca)
    '''
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

def lung(lista):
    '''
    funzione che conta gli elementi di una lista 
    '''
    conta = 0
    for i in lista:
        conta += 1
    return conta

def rango(iniz=0, ferma=1, passo=1):
    res = []
    while(iniz < ferma):
        res.append(iniz)
        iniz += passo
    return res



casistita = [79,4289,990,39,755,5]

print(massimo(casistita),minimo(casistita),lung(casistita))
print(rango(0, 3,1))