from datetime import date

print("*-"*12)
print("Classificação de atletas")
print("*-"*12)

ano = int(input("Digite o seu ano de nascimento: "))
verifica = date.today().year - ano

print(verifica)

if verifica <= 9:
    print("Atleta tem {} anos, então sua classificação é MIRIM".format(verifica))
elif verifica <= 14:
    print("Atleta tem {} anos, então sua classificação é INFANTIL".format(verifica))
elif verifica <= 19:
    print("Atleta tem {} anos, então sua classificação é JUNIOR".format(verifica))
elif verifica <= 25:
    print("Atleta tem {} anos, então sua classificação é SÊNIOR".format(verifica))
else:
    print("Atleta tem {} anos, então sua classificação é MASTER".format(verifica))
