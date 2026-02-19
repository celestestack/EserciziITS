'''Creare un programma che permetta all’utente di effettuare la moltiplicazione 
tra due numeri senza utilizzare l’operatore * ma calcolando il risultato 
attraverso somme ripetute (numeri positivi).'''

def moltiplicazione(n1, n2):
    result = 0
    for i in range(n2):
        result += n1
    return result

print(moltiplicazione(7, 5))