'''Creare un programma che chieda all’utente di inserire un numero n e stampi una 
stringa lunga n caratteri dove i caratteri che la compongono saranno i caratteri 
@ e # alternati partendo con un carattere @

Ad esempio se l’utente dice che la stringa dovrà essere lunga 5 caratteri la stringa 
stampata dovrà essere: @#@#@'''


def stringaFinale(n):
    stringaF = ""
    for i in range(n):
        if i%2 == 0:
            stringaF += "@"
        else:
            stringaF += "#"

    return stringaF

numero = int(input("inserire un valore: "))
print(stringaFinale(numero))