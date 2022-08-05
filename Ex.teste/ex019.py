import random

n1 = input("Digite nome do primeiro aluno: ")
n2 = input("Digite nome do segundo aluno: ")
n3 = input("Digite nome do terceiro aluno: ")
n4 = input("Digite nome do quarto aluno: ")
lista = [n1, n2, n3, n4]
pe = random.choice(lista)

print("O aluno escolhido foi: {}".format(pe))
