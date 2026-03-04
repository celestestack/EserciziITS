volte = int(input("Quante volte vuoi moltiplicare: "))
molt = 1
for i in range(volte):
    num = int(input("Che numero vuoi moltiplicare: "))
    molt *= num
print(molt)