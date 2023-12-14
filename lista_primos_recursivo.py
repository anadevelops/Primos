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


def lista_primos_rec():
    n = int(input())
    primos = []
    anterior = n
    if n > 1:
        for i in range(n + 1):
            if primo(anterior):
                primos.append(anterior)
                anterior = anterior - 1
            else:
                anterior = anterior - 1
                pass
        print(sorted(primos)) #Sorted adicionado para deixar a lista em ordem crescente
    
    else:
        print("O número precisa ser maior que 1")

lista_primos_rec()
