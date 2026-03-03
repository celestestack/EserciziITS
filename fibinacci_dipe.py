'''Scrivere una funzione che produca una lista dei 
numeri di Fibonacci fino ad n'''

def fibonacci(n):
    if n < 0:
        return "n deve essere non negativo"
    
    risultato = []
    a, b = 0, 1
    
    while a <= n:
        risultato.append(a)
        a, b = b, a + b
    
    return risultato