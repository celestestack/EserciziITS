'''Scrivere una funzione che dica se una parola è palindroma 
(“Anna”, “SOS”)'''

def palindroma(stringa):
    n = len(stringa)
    for i in range(n // 2):
        if stringa[i] != stringa[n - 1 - i]:
            return "non palindroma"
    return "palindroma"

