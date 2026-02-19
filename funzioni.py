def massimo(lista):
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