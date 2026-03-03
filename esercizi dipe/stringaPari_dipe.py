'''Creare un programma che chieda all’utente di inserire una stringa di lunghezza pari. 
Se l’utente inserisce una stringa dispari, il programma dovrà chiedergli di reinserirla 
fino a che non inserisca una stringa di lunghezza pari.'''

def stringaPari(stringaInput):
    lunghezza = len(stringaInput)
    if lunghezza%2 != 0:
        while True:
            strPari = input("inserire una stringa pari!")
            break
    else:
        strPari = stringaInput
    return strPari


print(stringaPari("ciao come va!"))
