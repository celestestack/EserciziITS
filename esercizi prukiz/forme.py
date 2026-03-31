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
    
    
#funzione: perimetroTriangolo
#input: lato
#output: perimetro -> lato * 3
def perimetroTriangolo(lato: int):
    if lato > 0:
        return lato * 3
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


def perimCirconferenza(r: float):
    perim = 0
    if r>0:
        perim = 2 * 3.14 * r

    return perim

def menu():
    print("Scegli uno delle seguenti opzioni:")
    print("1) perimetro Quadrato")
    print("2) perimetro Triangolo")
    print("3) perimetro Triangolo Isoscele")
    print("4) perimetro Rettangolo")
    print("5) perimetro Circonferenza")

    scelta = int(input("Inserisci una scelta: "))

    return scelta


valScelta = menu()
if valScelta == 1:
    print(perimetroQuadrato(4))
elif valScelta == 2:
    print(perimetroTriangolo(5))
elif valScelta == 3:
    print(perimTriaIso(4, 6))
elif valScelta == 4:
    print(perimRettangolo(10, 3))
elif valScelta == 5:
    print(perimCirconferenza(2))
else:
    print("Opzione non possibile")



#funzione areaQuadrato
def areaQuadrato(lato: int):
    if lato > 0:
        return lato * lato
    else:
        return 0


#funzione areaTriangolo
def areaTriangolo(lato: int):
    if lato > 0:
        return 0,433(lato **2)
    else:
        return 0
    

#funzione areaRettangolo
def areaRettangolo(lato: int, altezza: int):
    if lato > 0 and altezza > 0:
        return lato * altezza
    else:
        return 0
    

#funzione areaCerchio
def areaCerchio(raggio: int):
    if raggio > 0: 
        return raggio * raggio * 3,14
    else:
        return 0
    


def menu():
    print("Scegli uno delle seguenti opzioni:")
    print("1) area quadrato")
    print("2) area Triangolo")
    print("3) area Rettangolo")
    print("4) area Cerchio")

    scelta = int(input("Inserisci una scelta: "))

    valScelta = menu()
    if valScelta == 1:
        print(areaQuadrato(4))
    elif valScelta == 2:
        print(areaTriangolo(5))
    elif valScelta == 3:
        print(areaRettangolo(10, 3))
    elif valScelta == 4:
        print(areaCerchio(2))
    elif valScelta == 0:
        print()
    else:
        print("Opzione non possibile")








