def massimo(lista):
    '''
    funzione che individua il massimo senza usare funzione max (incredibile)
    '''
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max
