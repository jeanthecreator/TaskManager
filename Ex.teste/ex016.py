import math
num = float(input("Digite um numero com casas decimais: "))
numTru = math.trunc(num)

print("O numero digitado {}, parte inteira {}".format(num, numTru))
