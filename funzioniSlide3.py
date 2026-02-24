'''
Riscrivete il programma ‘area.py’, definendo funzioni separate per l’area del quadrato, del rettangolo e del cerchio (3.14 *
raggio**2). Il programma deve includere anche un’interfaccia a menu
'''

'''
Scrivere una funzione che dica se una parola è palindroma (“Anna”, “SOS”)
'''
def palindroma(stringa):
    for i in range(len(stringa)):
        for j in range(len(stringa)-1,0,-1):
            if stringa[i] != stringa[j]:
                return("Non è palindroma")
    return("E' palindroma")        

print(palindroma("anna"))
'''
Scrivere una funzione che dica se un numero è primo o no
'''

'''
Scrivere una funzione che produce un istogramma esempio Istrogramma([4,2,6]):
****
**
******
'''

'''
Scrivere una funzione che produca una lista dei numeri di Fibonacci fino ad n
'''

'''
Scrivere una funzione che restituisce la media dei numeri passati come lista
'''