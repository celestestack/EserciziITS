'''Scrivere una funzione che dica se un numero è primo o no'''


def primo(numero):
    if numero < 2:
        return "non primo"
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return "non primo"
    return "primo"