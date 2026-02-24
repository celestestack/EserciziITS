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
    print("opzione 1: area del quadrato")
    print("opzione 2: area del rettangolo")
    print("opzione 3: area del cerchio")
    print("opzione 4: esci")

    opzione_scelta = input("scegli un'opzione: ")

    if opzione_scelta == '1':
        lato = int(input("inserire lato del quadrato: "))
        print(areaQuadrato(lato))
    elif opzione_scelta == '2':
        lato1 = int(input("inserire base rettangolo: "))
        lato2 = int(input("inserire altezza rettangolo: "))
        print(areaRettangolo(lato1, lato2))
    elif opzione_scelta == '3':
        raggio = int(input("inserire raggio del cerchio: "))
        print(areaCerchio(raggio))
    else:
        print("exit")






    
