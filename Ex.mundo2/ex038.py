print("-#\033[0m"*35)
print("Comparação entre numeros")
print('-#'*35)

pri = int(input("Digite um numero inteiro: "))
sec = int(input("Digite outro numero inteiro: "))

if pri == sec:
    print("Os numero são iguais")
elif pri > sec:
    print("O primeiro numero {} é maior que o numero {}".format(pri, sec))
elif sec > pri:
    print("O segundo numero {} é maior que o numero {}".format(sec, pri))
