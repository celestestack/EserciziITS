'''Scrivete il programma ‘area.py’, definendo funzioni separate per l’area del quadrato, 
del rettangolo e del cerchio (3.14 * raggio ** 2). Il programma deve includere anche 
un’interfaccia a menu'''

pi = 3.14

def areaQuadrato(lato):
    return lato*lato

def areaRettangolo(lato1, lato2):
    return lato1*lato2

def areaCerchio(raggio):
    return 3.14 * raggio ** 2


def main():
    while True:
        print("\n--- MENU CALCOLO AREE ---")
        print("opzione 1: area del quadrato")
        print("opzione 2: area del rettangolo")
        print("opzione 3: area del cerchio")
        print("opzione 4: esci")

        opzione_scelta = input("scegli un'opzione: ")

        if opzione_scelta == '1':
            lato = float(input("inserire lato del quadrato: "))
            risultato = areaQuadrato(lato)
            print(f"l'area del quadrato è: {risultato}")
        elif opzione_scelta == '2':
            lato1 = float(input("inserire base rettangolo: "))
            lato2 = float(input("inserire altezza rettangolo: "))
            risultato = areaRettangolo(lato1, lato2)
            print(f"l'area del rettangolo è: {risultato}")
        elif opzione_scelta == '3':
            raggio = float(input("inserire raggio del cerchio: "))
            risultato = areaCerchio(raggio)
            print(f"l'area del cerchio è: {risultato}")
        elif opzione_scelta == '4':
            print("arrivederci!")
            break
        else:
            print("opzione non valida. riprova.")



def avvia():
    main()
avvia()