lista = []

while True:
    num = int(input("Inserisci un numero, 0 per terminare: "))
    if(num != 0):
        lista.append(num)
    else:
        print(lista)
        break