print("Analise de numero!!")

dig = int(input("Digite o primeiro numero: "))
dig1 = int(input("Digite o segundo numero: "))
dig2 = int(input("Digite o terceiro numero: "))

num = (dig, dig1, dig2)
arrumado = sorted(num)

print("O Maior numero é {}\nMenor numero é {}".format(arrumado[2],arrumado[0]))

# if dig > dig1 and dig > dig2:
#     print("Maior Numero é: {}".format(dig))
