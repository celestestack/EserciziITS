vocali = list("aeiou")
conta = 0
voc_trovate = []
print(vocali)
parola = input("Inserisci una parola: ")
for i in range(len(parola)):
    for j in range(len(vocali)):
        if parola[i] == vocali[j]:
            conta += 1
            voc_trovate.append(parola[i])

print(conta, voc_trovate)


conta = 0
lista = [2, 4, -5, 6, 1, 5, 8]
pos_trovati = []
for i in range(len(lista)):
    if lista[i] >= 0:
        conta += 1
        pos_trovati.append(lista[i])
print(pos_trovati)
print(conta)