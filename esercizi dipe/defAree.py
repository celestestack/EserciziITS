# creare delle funzioni che consentano di calcolare i perimetri e le aree di quadrati, ciconferenze, 
# triangoli equilateri, rettangoli, chiedendo all'utente di inserire la scelta richiesta fino a 
# quando non decide di uscire dal programma premendo 0

def perimetroQuadrato(lato: int):
  if lato >= 0:
    return lato*4
  else:
    return 0

def areaQuadrato(lato: int):
  if lato >= 0:
    return lato**2
  else:
    return 0

def perimetroTriangoloEq(lato: int):
  if lato >= 0:
    return lato*3
  else:
    return 0

def perimetroTrinagoloIso(lato1: int, lato2: int):
  if lato1 >= 0 and lato2 >= 0:
    return lato1*2 + lato2
  else:
    return 0
  
def areaTriangolo(base: int, altezza: int):
   if base >= 0 and altezza >= 0:
      return (base*altezza)/2
   else:
      return 0

def perimetroRettangolo(base: int, altezza: int):
  if base >= 0 and altezza >= 0:
    return (base + altezza)*2
  else:
    return 0

def areaRettangolo(base: int, altezza: int):
  if base >= 0 and altezza >= 0:
    return base*altezza
  else:
    return 0

def circonferenza(raggio: int):
  if raggio >= 0:
    return 2*3.14*raggio
  else:
    return 0
  
def areaCerchio(raggio: int):
  if raggio >= 0:
    return 3.14*raggio**2
  else:
    return 0

def menu():
    print("scegli una delle seguenti opzioni: ")
    print("1) perimetro quadrato")
    print("2) area quadrato")
    print("3) perimetro triangolo equilatero")
    print("4) area triangolo")
    print("5) perimetro triangolo isoscele")
    print("6) perimetro rettangolo")
    print("7) area rettangolo")
    print("8) circonferenza")
    print("9) area cerchio")
    print("0 per uscire")

    scelta = int(input("inserisci la tua scelta: "))
    return scelta

while True:
    valScelta = menu()

    if valScelta == 1:
        lato = int(input("inserire lato: "))
        print(perimetroQuadrato(lato))
    elif valScelta == 2:
        lato = int(input("inserire lato: "))
        print(areaQuadrato(lato))
    elif valScelta == 3:
        lato = int(input("inserire lato: "))
        print(perimetroTriangoloEq(lato))
    elif valScelta == 4:
        base = int(input("inserire base: "))
        altezza = int(input("inserire altezza: "))
        print(areaTriangolo(base, altezza))
    elif valScelta == 5:
        lato1 = int(input("inserire lato 1: "))
        lato2 = int(input("inserire lato 2: "))
        print(perimetroTrinagoloIso(lato1, lato2))
    elif valScelta == 6:
        base = int(input("inserire base: "))
        altezza = int(input("inserire altezza: "))
        print(perimetroRettangolo(base, altezza))
    elif valScelta == 7:
        base = int(input("inserire base: "))
        altezza = int(input("inserire altezza: "))
        print(areaRettangolo(base, altezza))
    elif valScelta == 8:
        raggio = int(input("inserire raggio: "))
        print(circonferenza(raggio))
    elif valScelta == 9:
        raggio = int(input("inserire raggio: "))
        print(areaCerchio(raggio))
    elif valScelta == 0:
        exit()






