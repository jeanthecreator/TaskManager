from random import shuffle

n1 = str(input("Digite o nome do Aluno1: "))
n2 = str(input("Digite o nome do Aluno2: "))
n3 = str(input("Digite o nome do Aluno3: "))
n4 = str(input("Digite o nome do Aluno4: "))

lista = [n1, n2, n3, n4]

shuffle(lista)

print("A entrega dos trabalho será feita na ordem: ")
print(lista)