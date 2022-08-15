from datetime import date

print("*-"*20)
print("Verificação de Alistamento no Exercito")
print("*-"*20)

anoNasc = int(input("Digite  seu ano de nascimento com 4 digitos: "))

verifica = date.today().year - anoNasc

print(verifica)

if verifica == 18:
    print("Você deve se alistar imediatamente!!")
elif verifica < 18:
    print("Você terá que se alistar em {} Anos".format(18 - verifica))
else:
    print("Você deveria ter se alistado há {} anos atrás!!".format(verifica - 18))
