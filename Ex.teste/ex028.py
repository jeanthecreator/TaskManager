import random
from time import sleep
print("Tente adivinhar um numero de 0 a 5")

#lista = list(range (6))
cria = random.randint(0,5)
#print(cria)
tenta = int(input("Digite Sua tentativa: "))
print("Processando...")
sleep(3)
if tenta == cria:
    print("Voce Acertou!!!")
else:
    print("Não foi dessa vez!!! O Numero era o {}".format(cria))    

