print("~'"*20)
print("Calculo de conversão de base numericas")
print("~'"*20)

num = int(input("Digite o numero que quer converter: "))
esc = int(input(
    "Escolha a base que deseja converter\n[]1.Binaria \n[]2.Octal \n[]3.Hexadecimal\nOpção: "))

if esc == 1:
    print("Convertido para Binario: {}".format(format(num, "b")))
elif esc == 2:
    print("Convertido para Octal {}".format(format(num, "o")))
elif esc == 3:
    print("Convertido para Hex {}".format(format(num, "X")))
else:
    print("Opção invalida!!!")
