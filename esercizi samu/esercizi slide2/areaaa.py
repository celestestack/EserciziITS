'''
Riscrivete il programma ‘area.py’, definendo funzioni separate per
l’area del quadrato, del rettangolo e del cerchio (3.14 * raggio**2). Il
programma deve includere anche un’interfaccia a menu
'''

#interfaccia
while True:
    choice = input("Digita 1 per calcolare l'area del quadrato 2 per quella del rettangolo, 3 per l'area del cerchio, qualsiasi altropulsante per uscire:\n")
    if choice == "1":
        while True:
            l = input("Inserisci il lato: ")
            if l.isdigit() == True:
                l = int(l)
                print(l**2)
                break
    elif choice == "2":
        while True:
            a = input("Inserisci l'altezza: ")
            b = input("Inserisci la base: ")
            if(a.isdigit() == True and b.isdigit() == True):
                a, b = int(a), int(b)
                print(a*b)
                break
    elif choice == "3":
        while True:
            r = input("Inserisci il raggio: ")
            if r.isdigit() == True:
                r = int(r)
                print(3.14 * r**2)
                break
    else: break