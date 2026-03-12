'''
Scrivete un programma che chieda all’utente di indovinare una password, ma che dia al
giocatore solamente 3 possibilità, fallite le quali il programma terminerà, stampando “È troppo
complicato per voi”
'''

import random
import string

def indovinaPass():
    password = ''.join(random.choices(string.ascii_letters + string.digits,k=10))
    print(password)
    for i in range(3):
        tent = input(f"Prova a indovinare la password, hai massimo 3 tentativi, sei al {i+1}° tentativo: ")
        if(tent != password):
            print("AHAHAHHAHA COGLIONE! È troppo complicato per voi")
        else: 
            print("Bastardo! Hai scoperto la password!")
    


print(indovinaPass())