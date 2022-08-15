from random import randint
from time import sleep
from tracemalloc import stop

print("+*"*11)
print("Vamos Jogar Jo Ken Po")
print("+*"*11)

esco = int(input('''Suas opções 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual a sua escolha? '''))

print("JO")
sleep(2)
print("Ken")
sleep(1)
print("PO!!")

rand = randint(1, 3)

if rand == 1:
    alt = "Pedra"
elif rand == 2:
    alt = "Papel"
else:
    alt = "Tesoura"

if esco == 1:
    pl = "Pedra"
elif esco == 2:
    pl = "Papel"
elif esco == 3:
    pl = "Tesoura"
else:
    print("Opção invalida")


if esco == rand:
    resu = " EMPATE"
elif esco == 1 and rand == 3 or esco == 2 and rand == 1 or esco == 3 and rand == 2:
    resu = "JOGADOR GANHOU!!"
else:
    resu = "JOGADOR PERDEU!!"


print("+*"*22)
print("O Computador escolheu {}".format(alt))
print("O Jogador escolheu {}".format(pl))
print("+*"*22)
print(resu)
