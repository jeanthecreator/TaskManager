ladoA = float(input("Digite o lado A do triangulo: "))
ladoB = float(input("Digite o lado B do triangulo: "))
ladoC = float(input("Digite o lado C do triangulo: "))

modulo = abs(ladoA - ladoB)

if modulo < ladoC < (ladoA + ladoB):
    print("Os segmentos acima podem formar um triangulo")
else:
    print("Os segmentos acima não podem forma um triangulo")