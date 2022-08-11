import random

print("Tente adivinhar um numero de 0 a 5")

lista = list(range (6))
cria = random.choice(lista)

tenta = int(input("Digite Sua tentativa: "))

if tenta == cria:
    print("Voce Acertou!!!")
else:
    print("Não foi dessa vez!!!")    

