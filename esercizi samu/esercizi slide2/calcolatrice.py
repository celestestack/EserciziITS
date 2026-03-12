'''
Implementare una calcolatrice chiedendo all’utente di inserire i valori e l’operatore
'''

def calcolatrice():
    while True:
        a = input("Inserisci un numero: ")
        b = input("Inserisci un numero: ")
        if(a.isdigit() == True and b.isdigit() == True):
            break
    num1 = int(a)
    num2 = int(b)    
    while True:
        oper = input("Digita + se vuoi sommare, - per sottrarre, * per moltiplicare, / per dividere, e per uscire: ")
        if oper == "e":
            break
        elif(oper == "+"):
            return num1 + num2
        elif(oper == "-"):
            return num1 - num2
        elif(oper == "*"):
            return num1 * num2
        elif(oper == "/"):
            return num1/num2
    
print(calcolatrice())