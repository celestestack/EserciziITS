#creare delle funzioni che consentano di calcolare le aree e perimetri di:
#quadrati, circonferenze, triangoli eq., rettangolo
#chiedendo all'utente di inserire la scelta richiesta fino a quando non si 
#preme il valore zero per poter concludere

#funzione: perimetroQuadrato
#input: lato
#output: perimetro -> 4 * lato
def perimetroQuadrato(lato: int):
    if lato > 0:
        return lato * 4
    else:
        return 0

def areaQuadrato(lato: int):
    if lato > 0:
        return lato ** 2
    else:
        return 0
    
    
#funzione: perimetroTriangolo
#input: lato
#output: perimetro -> lato * 3
def perimetroTriangolo(lato: int):
    if lato > 0:
        return lato * 3       
    else:
        return 0

def areaTriangolo(lato: int):
    if lato > 0:
        return 0.433*(lato ** 2)
    else:
        return 0
     
#funzione: perimTriaIso
#input: base, latoOpp
#output: perimetro -> base + latoOpp * 2
def perimTriaIso(base: int, latoOpp: int):
    if base > 0 and latoOpp > 0:
        return base + latoOpp * 2
    else:
        return 0


#funzione perimRettangolo
#input base, altezza
#output: perimetro = base + base + altezza + altezza
def perimRettangolo(base: int, altezza: int):
    perim = 0
    if base > 0 and altezza > 0:
        perim = (base + altezza) * 2

    return perim

def areaRettangolo(base: int, altezza: int):

    if base > 0 and altezza > 0:
        return base * altezza

def perimCirconferenza(r: float):
    perim = 0
    if r>0:
        perim = 2 * 3.14 * r

    return perim

def areaCirconferenza(r: float):
    area = 0
    if r>0:
        area = 3.14 * r ** 2

    return area

def inserimento():
    n1 = int(input("Inserisci il primo lato: "))
    n2 = int(input("Inserisci il secondo lato: "))
        
    return n1, n2

def inserimentoTriQ():
    n1 = int(input("Inserisci il lato/raggio: "))
        
    return n1

def menuPA():
    print("1) Perimetro")
    print("2) Area")
    print("3) Entrambi")

    scelta = int(input("Fai la tua scelta: "))

    return scelta

def menu():
    scelta = -1
    while scelta != 0:
        print("Scegli uno delle seguenti opzioni:")
        print("1) Quadrato")
        print("2) Triangolo")
        print("3) Triangolo Isoscele")
        print("4) Rettangolo")
        print("5) Circonferenza")

        scelta = int(input("Inserisci una scelta: "))


        if scelta == 1:
            lato = inserimentoTriQ()
            sceltaPA = menuPA()
            if sceltaPA == 1:
                print(perimetroQuadrato(lato))
            elif sceltaPA == 2:
                print(areaQuadrato(lato))
            elif sceltaPA == 3:
                print(perimetroQuadrato(lato))
                print(areaQuadrato(lato))
        elif scelta == 2:
            lato = inserimentoTriQ()
            sceltaPA = menuPA()
            if sceltaPA == 1:
                print(perimetroTriangolo(lato))
            elif sceltaPA == 2:
                print(areaTriangolo(lato))
            elif sceltaPA == 3:
                print(perimetroTriangolo(lato))
                print(areaTriangolo(lato))
        elif scelta == 3:
            l1, l2 = inserimento()
            print(perimTriaIso(l1,l2))
        elif scelta == 4:
            l1,l2 = inserimento()
            sceltaPA = menuPA()
            if sceltaPA == 1:
                print(perimRettangolo(l1,l2))
            elif sceltaPA == 2:
                print(areaRettangolo(l1,l2))
            elif sceltaPA == 3:
                print(perimRettangolo(l1,l2))
                print(areaRettangolo(l1,l2))
        elif scelta == 5:
            raggio = inserimentoTriQ()
            sceltaPA = menuPA()
            if menuPA() == 1:
                print(perimCirconferenza(raggio))
            elif menuPA() == 2:
                print(areaCirconferenza(raggio))
            elif menuPA() == 3:
                print(perimCirconferenza(raggio))
                print(areaCirconferenza(raggio))
        elif scelta == 0:
            return 0
        else:
            print("Opzione non possibile")

menu()