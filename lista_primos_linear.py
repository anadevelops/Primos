import math

def primo(n):
    if n == 1 or (n % 2 == 0 and n != 2):
        primo = False
    else:
        primo = True
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                primo = False
                break
    return primo


def lista_primos_lin():
    n = int(input())
    primos = []
    if n > 1:
        if n == 2:
            primos.append(n)
        for i in range(n + 1):
            if primo(i):
                primos.append(i)
            else:
                pass
        print(primos)
    
    else:
        print("O número precisa ser maior que 1")

lista_primos_lin()