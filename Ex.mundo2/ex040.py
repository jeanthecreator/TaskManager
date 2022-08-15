print("~*"*7)
print("Media escolar")
print("~*"*7)

av1 = float(input("Digite a nota da sua AV1: "))
av2 = float(input("Digite a nota da sua AV2: "))

media = (av1 + av2)/2

if media <= 4.9:
    print("Sua nota final foi {}. Aluno Reprovado!!".format(media))
elif media >= 5 and media < 6.9:
    print("Sua nota final foi {}. Aluno em recuperação!!".format(media))
else:
    print("Sua nota final foi {}. Aluno Aprovado!!".format(media))
