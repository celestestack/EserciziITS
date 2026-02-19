def massimo(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max
