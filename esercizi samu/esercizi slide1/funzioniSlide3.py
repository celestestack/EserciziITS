import math
'''
Riscrivete il programma ‘area.py’, definendo funzioni separate per l’area del quadrato, del rettangolo e del cerchio (3.14 *
raggio**2). Il programma deve includere anche un’interfaccia a menu
'''
def areaq(lato):
    return lato * lato
def arear(lato, base):
    return lato*base
def areac(raggio):
    return 3.14 *raggio**2

def areapy():
    flag = 0
    while True:
        sel = int(input("Digita\n0 per uscire\n1 per calcolare l'area del quadrato\n2 per calcolare l'area del rettangolo\n3 per calcolare l'area del cerchio\n"))
        if sel == 0:
            return 0
        if sel == 1:
            q = int(input("Inserisci il lato del quadrato: "))
            print(areaq(q))
        if sel == 2:
            lato = int(input("Inserisci il lato del rettangolo: "))
            base = int(input("Inserisci la base del rettangolo: "))
            print(arear(lato, base))
        if sel == 3:
            r = int(input("Inserisci il raggio del cerchio: "))
            print(areac(r))
        
print(areapy())
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
def isto(lista):
    for i in range(len(lista)):
        print("*"*lista[i])

listas = [1,4,6,3]
print(isto(listas))
'''
Scrivere una funzione che produca una lista dei numeri di Fibonacci fino ad n
'''
def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print("Il numero deve essere positivo")
    fibol = []
    while a <= n:
        fibol.append(a)
        a, b = b, a+b
         
    return fibol

print(fibo(2))
'''
Scrivere una funzione che restituisce la media dei numeri passati come lista
'''
def media(lista):
    #sommare tutti gli elementi della lista e dividerli per la lunghezza della lista
    som = 0
    for i in range(len(lista)):
        som += lista[i]
    return som/len(lista)

cacca = [30,29,29,22]
print(media(cacca))