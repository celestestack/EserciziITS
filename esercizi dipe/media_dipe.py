'''
Scrivere una funzione che restituisce la media dei 
numeri passati come lista
'''


def media(lista):    
    if len(lista) == 0:
        return "lista vuota, impossibile calcolare la media"
    
    somma = sum(lista)
    media_calcolata = somma / len(lista)
    
    return media_calcolata