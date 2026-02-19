'''Creare un programma che permetta all’utente di effettuare la divisione 
tra due numeri e mostri a schermo quoziente e resto senza utilizzare 
né l’operatore / né l’operatore %'''

def divisione(n1, n2):
    result = 0
    while n1 >= n2:
        n1 -= n2
        result += 1
    return result, n1


print(divisione(35, 7))