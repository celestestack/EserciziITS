'''Creare una funzione che, data una lista di numeri ed un numero da cercare, restituisca il valore
booleano True se tale numero è presente nella lista, False altrimenti'''


listaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 7

def trovaNum(lista, num):
    listaStringata, num = str(lista), str(num)
    if num in listaStringata:
        return True
    else:
        return False
    
print(trovaNum(listaNum, n))


def trovaNum_4(lista, num):
    for i in lista:
        if i == num:
            return True
    return False
    
print(trovaNum_4(listaNum, n))



