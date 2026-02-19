def stringaFinale():
    num = int(input("Inserire un numero: "))
    stringa = ""
    for i in range(num):
        if(i%2 == 0):
            stringa += "@"
        else:
            stringa += "#"
    return stringa


print(stringaFinale())    